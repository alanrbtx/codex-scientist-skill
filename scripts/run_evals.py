#!/usr/bin/env python3
"""Explicit, bounded Codex CLI evals. Not run by ordinary skill invocation."""
import argparse
import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path
from evaluate import ROOT, build_prompt, grade_batch, load_cases, skill_pack


def inspect_trace(text):
    usage = None
    unexpected = []
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get('type') == 'turn.completed':
            usage = event.get('usage')
        if event.get('type') == 'item.completed':
            kind = event.get('item', {}).get('type')
            if kind not in ('agent_message', 'reasoning'):
                unexpected.append(kind)
    return usage, unexpected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Authorize model calls using existing Codex login')
    parser.add_argument('--models', nargs='+', default=['gpt-6-astra', 'gpt-6.1-sol'])
    parser.add_argument('--arms', nargs='+', choices=['baseline', 'skill'], default=['baseline', 'skill'])
    parser.add_argument('--effort', choices=['low', 'medium', 'high', 'xhigh', 'max'], default='medium')
    parser.add_argument('--timeout-seconds', type=int, default=240)
    parser.add_argument('--max-calls', type=int, default=4)
    parser.add_argument('--out', type=Path, required=True, help='New output directory; never overwritten')
    args = parser.parse_args()
    if args.timeout_seconds <= 0 or args.max_calls <= 0:
        parser.error('Budgets must be positive')
    pairs = [(m, a) for m in dict.fromkeys(args.models) for a in dict.fromkeys(args.arms)]
    if len(pairs) > args.max_calls:
        parser.error(f'{len(pairs)} calls exceed --max-calls={args.max_calls}')
    if not args.execute:
        print(json.dumps({'planned_calls':len(pairs), 'models':args.models, 'arms':args.arms, 'timeout_seconds_per_call':args.timeout_seconds, 'note':'Add --execute to make model calls.'}, indent=2))
        return 0
    args.out.mkdir(parents=True, exist_ok=False)
    out = args.out.resolve()
    version = subprocess.check_output(['codex', '--version'], text=True).strip()
    features = subprocess.check_output(['codex', 'features', 'list'], text=True)
    if 'skip_host_skill_discovery' not in features:
        raise SystemExit('This CLI cannot isolate host skill discovery; no eval was run.')
    cases = load_cases()
    response_schema = json.loads((ROOT / 'evals/response.schema.json').read_text())
    schema = {'type':'object', 'additionalProperties':False, 'required':['responses'], 'properties':{'responses':{'type':'array', 'items':response_schema}}}
    schema_path = out / 'batch.schema.json'
    schema_path.write_text(json.dumps(schema))
    report = {'backend':'codex-cli', 'cli_version':version, 'effort':args.effort, 'corpus_sha256':hashlib.sha256((ROOT/'evals/cases.json').read_bytes()).hexdigest(), 'skill_sha256':hashlib.sha256(skill_pack().encode()).hexdigest(), 'runs':[], 'limitations':'One batch per arm. Deterministic fixture checks, not native discovery or real-world scientific quality. Manual prose review required. Costs are not estimated.'}
    for index, (model, arm) in enumerate(pairs):
        stem = f'{index:02d}-{model}-{arm}'
        if not all(c.isalnum() or c in '.-_' for c in stem):
            raise SystemExit('Invalid model name for artifact path')
        prompt = build_prompt(cases, arm)
        (out / f'{stem}.prompt.txt').write_text(prompt)
        answer = out / f'{stem}.responses.json'
        with tempfile.TemporaryDirectory(prefix='case-', dir=out) as tmp:
            command = ['codex', '--no-daemon', '-a', 'never', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check', '--sandbox', 'read-only', '--enable', 'skip_host_skill_discovery', '--disable', 'skill_search', '--disable', 'multi_agent', '--disable', 'shell_tool', '--disable', 'unified_exec', '-c', 'project_doc_max_bytes=0', '-c', 'web_search="disabled"', '-c', f'model_reasoning_effort="{args.effort}"', '-m', model, '--json', '--output-schema', str(schema_path), '-C', tmp, '-o', str(answer), '-']
            start = time.monotonic()
            item = {'model':model, 'arm':arm, 'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest()}
            try:
                proc = subprocess.run(command, input=prompt, text=True, capture_output=True, timeout=args.timeout_seconds)
                (out / f'{stem}.trace.jsonl').write_text(proc.stdout)
                (out / f'{stem}.stderr.txt').write_text(proc.stderr)
                item['exit_code'] = proc.returncode
                item['usage'], item['unexpected_tool_items'] = inspect_trace(proc.stdout)
                if proc.returncode:
                    item['status'] = 'backend_error'
                elif item['unexpected_tool_items']:
                    item['status'] = 'invalid_tool_use'
                else:
                    try:
                        item['grade'] = grade_batch(cases, json.loads(answer.read_text()))
                        item['status'] = 'graded'
                    except (ValueError, OSError) as exc:
                        item['status'] = 'invalid_output'
                        item['reason'] = type(exc).__name__
            except subprocess.TimeoutExpired:
                item['status'] = 'timeout'
            item['seconds'] = round(time.monotonic()-start,3)
            report['runs'].append(item)
            (out / 'report.json').write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(item),flush=True)
            if item['status'] != 'graded':
                print('Stopped on backend, isolation, or output failure; no model substitution or automatic retry.',flush=True)
                return 2
    return 0 if all(r['grade']['passed']==r['grade']['total'] for r in report['runs']) else 1


if __name__ == '__main__':
    raise SystemExit(main())
