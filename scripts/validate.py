#!/usr/bin/env python3
"""Offline repository validation. No model calls or network access."""
import json
import re
import subprocess
import sys
from pathlib import Path
import yaml
from evaluate import load_cases

ROOT = Path(__file__).resolve().parents[1]


def validate_frontmatter(text):
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    data = yaml.safe_load(match[1])
    if not isinstance(data, dict) or not isinstance(data.get('name'), str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', data['name']):
        raise ValueError('Invalid skill name')
    if len(data['name']) > 64 or not isinstance(data.get('description'), str) or not 1 <= len(data['description'].strip()) <= 1024:
        raise ValueError('Invalid skill description')
    if set(data) - {'name', 'description', 'license', 'allowed-tools', 'metadata'}:
        raise ValueError('Unknown frontmatter field')
    return data


def markdown_links(path, root):
    text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
    errors = []
    for target in re.findall(r'\]\(([^)]+)\)', text):
        target = target.strip().split(' "')[0].strip('<>')
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            continue
        target = target.split('#')[0]
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            errors.append(f'{path.relative_to(root)}: invalid local link {target}')
    return errors


def private_findings(text):
    patterns = {
        'personal filesystem path': r'/(?:Users|home)/[A-Za-z0-9_.-]+/',
        'internal host': r'\b[a-z0-9.-]+\.vk\.team\b',
        'private key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        'credential assignment': r'(?i)(?:api[_-]?key|password|token)\s*[:=]\s*[\x22\x27]?[A-Za-z0-9_-]{20,}',
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, text)]


def validate(root=ROOT):
    errors = []
    try:
        meta = validate_frontmatter((root / 'researcher/SKILL.md').read_text())
        if meta['name'] != 'researcher':
            errors.append('Skill folder/name mismatch')
        ui = yaml.safe_load((root / 'researcher/agents/openai.yaml').read_text())
        interface = ui['interface']
        if not 25 <= len(interface['short_description']) <= 64 or '$researcher' not in interface['default_prompt']:
            errors.append('Invalid skill UI metadata')
    except (ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        errors.append(str(exc))
    if not re.fullmatch(r'\d+\.\d+\.\d+\n?', (root / 'VERSION').read_text()):
        errors.append('VERSION must be a semantic version')
    candidates = subprocess.check_output(
        ['git', '-C', str(root), 'ls-files', '-z', '--cached', '--others', '--exclude-standard']
    ).decode().split('\0')
    for name in sorted(set(candidates) - {''}):
        file = root / name
        if not file.is_file():
            continue
        try:
            content = file.read_text()
        except UnicodeDecodeError:
            continue
        if file.suffix == '.md':
            errors.extend(markdown_links(file, root))
        for finding in private_findings(content):
            errors.append(f'{file.relative_to(root)}: {finding}')
    load_cases(root / 'evals/cases.json')
    json.loads((root / 'evals/response.schema.json').read_text())
    tracked = subprocess.check_output(['git', '-C', str(root), 'ls-files'], text=True).splitlines()
    if any(Path(p).name == '.DS_Store' or '__pycache__' in p.split('/') for p in tracked):
        errors.append('Tracked platform metadata/cache')
    return errors


if __name__ == '__main__':
    findings = validate()
    for finding in findings:
        print(finding, file=sys.stderr)
    print('Repository validation: ' + ('FAILED' if findings else 'OK'))
    raise SystemExit(bool(findings))
