#!/usr/bin/env python3
"""Grade closed-book scientific decision fixtures; never executes model output."""
import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERDICTS = {'supported', 'not_supported', 'unresolved', 'open', 'exploratory', 'blocked', 'not_applicable'}
FIELDS = {'case_id', 'verdict', 'answer', 'evidence', 'effect', 'outer_n', 'needs_user_input', 'run_new_experiment', 'deliverable'}


def load_cases(path=ROOT / 'evals/cases.json'):
    data = json.loads(Path(path).read_text())
    if data.get('version') != 1 or data.get('synthetic') is not True:
        raise ValueError('Expected versioned synthetic fixture corpus')
    cases = data['cases']
    ids = [c['id'] for c in cases]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate case IDs')
    for c in cases:
        sources = c['sources']
        source_ids = [s['source_id'] for s in sources]
        if len(source_ids) != len(set(source_ids)):
            raise ValueError(f"Duplicate source ID in {c['id']}")
        if not set(c['expected']['required_sources']) <= set(source_ids):
            raise ValueError(f"Unknown expected source in {c['id']}")
        if c['expected']['verdict'] not in VERDICTS:
            raise ValueError(f"Invalid verdict in {c['id']}")
        if not c['prompt'] or not c['manual_rubric']:
            raise ValueError(f"Incomplete case {c['id']}")
    return cases


def public_case(case):
    """Only the task and source corpus reach the evaluated model."""
    return {k: case[k] for k in ('id', 'prompt', 'sources')}


def skill_pack():
    paths = [ROOT / 'researcher/SKILL.md', *sorted((ROOT / 'researcher/references').glob('*.md'))]
    return '\n\n'.join(f"<skill_file name=\"{p.relative_to(ROOT)}\">\n{p.read_text()}\n</skill_file>" for p in paths)


def build_prompt(cases, arm):
    if arm not in ('baseline', 'skill'):
        raise ValueError('Unknown arm')
    schema = json.loads((ROOT / 'evals/response.schema.json').read_text())
    preamble = (
        'Complete the following synthetic, closed-book research decision tasks independently. '
        'Use only their supplied sources; these are fictional fixtures, not real literature. '
        'Do not browse, run experiments, read other files, or load installed skills. '
        'Return a JSON object with a responses array containing one response per task. '
        'Each response must follow the supplied schema. Use effect for the requested verified '
        'effect or ratio, outer_n for the requested independent-unit count, and null when '
        'unavailable or irrelevant. Put a requested replacement text in deliverable; otherwise '
        'use an empty string. Source IDs and locators must identify the supplied evidence. '
        'Assess the requested claim or action, not an unasked broader claim. '
        'Provide concise reasoning in answer.\n'
    )
    if arm == 'skill':
        preamble += '\nApply this candidate skill guidance to these tasks:\n' + skill_pack()
    return preamble + '\nResponse schema:\n' + json.dumps(schema) + '\nTasks:\n' + json.dumps([public_case(c) for c in cases], ensure_ascii=False)


def grade(case, result):
    failures = []
    if not isinstance(result, dict) or set(result) != FIELDS:
        return ['response_schema']
    if result['case_id'] != case['id']:
        failures.append('case_id')
    for field in ('answer', 'deliverable'):
        if not isinstance(result[field], str):
            failures.append(field + '_type')
    if not isinstance(result['answer'], str) or not result['answer'].strip():
        failures.append('missing_answer')
    expected = case['expected']
    if result['verdict'] != expected['verdict']:
        failures.append('verdict')
    for field in ('needs_user_input', 'run_new_experiment'):
        if type(result[field]) is not bool or result[field] != expected[field]:
            failures.append(field)
    for field in ('effect', 'outer_n'):
        value, target = result[field], expected[field]
        valid_type = value is None or (type(value) in (int, float) and math.isfinite(value))
        if field == 'outer_n':
            valid_type = value is None or type(value) is int
        matches = value is None if target is None else (valid_type and value is not None and math.isclose(value, target, rel_tol=1e-9, abs_tol=1e-9))
        if not valid_type or not matches:
            failures.append(field)
    known = {(s['source_id'], s['locator']) for s in case['sources']}
    evidence = result['evidence']
    cited = set()
    if not isinstance(evidence, list):
        failures.append('evidence_schema')
    else:
        for item in evidence:
            if not isinstance(item, dict) or set(item) != {'source_id', 'locator'} or not all(isinstance(v, str) for v in item.values()):
                failures.append('evidence_schema')
                continue
            if (item['source_id'], item['locator']) not in known:
                failures.append('unknown_source_or_locator')
            cited.add(item['source_id'])
        if not set(expected['required_sources']) <= cited:
            failures.append('missing_required_evidence')
    if expected['deliverable_required'] and (not isinstance(result['deliverable'], str) or not result['deliverable'].strip()):
        failures.append('missing_deliverable')
    return sorted(set(failures))


def grade_batch(cases, data):
    if not isinstance(data, dict) or set(data) != {'responses'} or not isinstance(data['responses'], list):
        raise ValueError('Expected an object containing only a responses array')
    responses = data['responses']
    ids = [r.get('case_id') if isinstance(r, dict) else None for r in responses]
    if any(not isinstance(i, str) for i in ids) or len(ids) != len(set(ids)) or set(ids) != {c['id'] for c in cases}:
        raise ValueError('Missing, duplicate, or unexpected response IDs')
    mapped = {r['case_id']: r for r in responses}
    details = [{'id': c['id'], 'failures': grade(c, mapped[c['id']]), 'manual_review': 'pending'} for c in cases]
    return {'passed': sum(not c['failures'] for c in details), 'total': len(details), 'cases': details}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prepare = sub.add_parser('prepare')
    prepare.add_argument('--arm', choices=('baseline', 'skill'), required=True)
    prepare.add_argument('--out', type=Path, required=True)
    score = sub.add_parser('grade')
    score.add_argument('responses', type=Path)
    score.add_argument('--out', type=Path)
    args = parser.parse_args()
    cases = load_cases()
    if args.command == 'prepare':
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(build_prompt(cases, args.arm))
        print(f'Prepared {len(cases)} cases ({args.arm}); expected answers excluded')
        return 0
    report = grade_batch(cases, json.loads(args.responses.read_text()))
    report['corpus_sha256'] = hashlib.sha256((ROOT / 'evals/cases.json').read_bytes()).hexdigest()
    report['limitations'] = 'Checks structured decisions, numbers and cited locations. Prose correctness needs manual review. Does not test native skill discovery, actual tool use or independent real-world research.'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] == report['total'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
