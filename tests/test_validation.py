import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from evaluate import FIELDS, build_prompt, grade, grade_batch, load_cases
from run_evals import inspect_trace
from validate import markdown_links, private_findings, validate_frontmatter


def response(case):
    exp = case['expected']
    return {'case_id':case['id'], 'verdict':exp['verdict'], 'answer':'Explanation requiring separate prose review.',
            'evidence':[{'source_id':s['source_id'],'locator':s['locator']} for s in case['sources']],
            'effect':exp['effect'], 'outer_n':exp['outer_n'], 'needs_user_input':exp['needs_user_input'],
            'run_new_experiment':exp['run_new_experiment'], 'deliverable':'Replacement text.' if exp['deliverable_required'] else ''}


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases=load_cases()
        self.case=self.cases[0]

    def test_complete_batch(self):
        report=grade_batch(self.cases,{'responses':[response(c) for c in self.cases]})
        self.assertEqual(report['passed'],len(self.cases))

    def test_wrong_scientific_decision_fails(self):
        r=response(self.case); r['verdict']='supported'
        self.assertIn('verdict',grade(self.case,r))

    def test_wrong_statistical_unit_fails(self):
        c=next(c for c in self.cases if c['id']=='outer-unit'); r=response(c); r['outer_n']=3000
        self.assertIn('outer_n',grade(c,r))

    def test_invented_locator_fails(self):
        r=response(self.case); r['evidence'][0]['locator']='nonexistent table'
        self.assertIn('unknown_source_or_locator',grade(self.case,r))

    def test_missing_evidence_fails(self):
        r=response(self.case); r['evidence']=[]
        self.assertIn('missing_required_evidence',grade(self.case,r))

    def test_duplicate_response_fails(self):
        with self.assertRaises(ValueError):
            grade_batch(self.cases,{'responses':[response(self.case)]*len(self.cases)})

    def test_malformed_response_id_fails_cleanly(self):
        r=response(self.case); r['case_id']=['invalid']
        with self.assertRaises(ValueError): grade_batch(self.cases,{'responses':[r]})

    def test_boolean_cannot_pass_as_number(self):
        r=response(self.case); r['effect']=True
        self.assertIn('effect',grade(self.case,r))

    def test_nonfinite_number_fails(self):
        r=response(self.case); r['effect']=float('nan')
        self.assertIn('effect',grade(self.case,r))

    def test_invented_effect_fails(self):
        c=next(c for c in self.cases if c['id']=='missing-evidence'); r=response(c); r['effect']=18
        self.assertIn('effect',grade(c,r))

    def test_empty_requested_deliverable_fails(self):
        c=next(c for c in self.cases if c['id']=='abstract-only'); r=response(c); r['deliverable']=''
        self.assertIn('missing_deliverable',grade(c,r))

    def test_expected_answers_never_enter_prompt(self):
        cases=copy.deepcopy(self.cases); cases[0]['expected']['marker']='HIDDEN_EXPECTATION'
        cases[0]['manual_rubric']='HIDDEN_RUBRIC'
        for arm in ('baseline','skill'):
            prompt=build_prompt(cases,arm)
            self.assertNotIn('HIDDEN_EXPECTATION',prompt)
            self.assertNotIn('HIDDEN_RUBRIC',prompt)
        self.assertNotIn('<skill_file',build_prompt(cases,'baseline'))
        self.assertIn('<skill_file',build_prompt(cases,'skill'))

    def test_real_tool_trace_invalidates_closed_book_run(self):
        usage,tools=inspect_trace(json.dumps({'type':'item.completed','item':{'type':'command_execution'}})+'\n'+json.dumps({'type':'turn.completed','usage':{'input_tokens':12}}))
        self.assertEqual(tools,['command_execution']); self.assertEqual(usage['input_tokens'],12)


class ValidationTests(unittest.TestCase):
    def test_invalid_yaml_frontmatter(self):
        with self.assertRaises(ValueError): validate_frontmatter('no frontmatter')
        with self.assertRaises(ValueError): validate_frontmatter('---\nname: Invalid Name\ndescription: x\n---\n')

    def test_broken_and_escaping_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); page=root/'a.md'; (root/'ok.md').write_text('# OK')
            page.write_text('[ok](ok.md) [missing](absent.md) [outside](../outside.md)')
            self.assertEqual(len(markdown_links(page,root)),2)

    def test_private_paths_are_rejected(self):
        self.assertTrue(private_findings('/'+'Users/example/private/file.txt'))
        self.assertFalse(private_findings('https://github.com/alanrbtx/codex-scientist-skill'))

    def test_schema_and_grader_fields_agree(self):
        root=Path(__file__).resolve().parents[1]
        schema=json.loads((root/'evals/response.schema.json').read_text())
        self.assertEqual(set(schema['required']),FIELDS)
        self.assertEqual(set(schema['properties']),FIELDS)


if __name__=='__main__': unittest.main()
