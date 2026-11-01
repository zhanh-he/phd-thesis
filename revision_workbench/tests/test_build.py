#!/usr/bin/env python3
"""Dependency-free tests for reusable builds and conservative source binding."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('workbench_build', Path(__file__).resolve().parents[1] / 'build.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def dataset(text='before\nExact original sentence.\nafter\n', document_id='test-manuscript-a'):
    return {'schemaVersion': 1, 'documentId': document_id,
            'manuscript': {'title': 'Synthetic manuscript', 'extension': {'unknown': [1, 2]}},
            'reviewers': [{'id': 'reviewer-C', 'displayName': 'Reviewer C'}, {'id': 'reviewer-A', 'displayName': 'Reviewer A'}],
            'comments': [{'id': 'same-comment-id', 'reviewer': 'reviewer-C', 'candidateVersion': 'proposal-1',
                          'locations': [{'file': 'paper.tex', 'lineStart': 2, 'lineEnd': 2,
                                         'quote': 'Exact original sentence.', 'before': 'before\n', 'after': '\nafter\n',
                                         'sourceSha256': digest(text), 'extension': {'arbitrary': True}}],
                          'extension': {'future': 'retained'}}],
            'sources': {'paper.tex': {'text': text, 'sha256': digest(text), 'future': 'original snapshot extension'}},
            'extension': {'futureMajor': {'unknown': True}}}


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def prepare(self, data, current_text=None):
        if current_text is not None:
            (self.root / 'paper.tex').write_text(current_text)
        return builder.prepare_data(data, self.root)

    def loc(self, data):
        return data['comments'][0]['locations'][0]

    def test_verified_range_preserves_original_and_unknown_fields(self):
        data = dataset()
        original = copy.deepcopy(data)
        prepared = self.prepare(data, data['sources']['paper.tex']['text'])
        loc = self.loc(prepared)
        self.assertEqual(loc['binding']['status'], 'verified')
        self.assertFalse(loc['binding']['reviewRequired'])
        self.assertEqual((loc['binding']['lineStart'], loc['binding']['lineEnd']), (2, 2))
        self.assertEqual(prepared['sources'], original['sources'])
        self.assertEqual(prepared['extension'], original['extension'])
        self.assertEqual(loc['extension'], self.loc(original)['extension'])
        self.assertEqual(data, original, 'HTML preparation must not mutate input')

    def test_changed_source_unique_quote_relocates_without_overwriting_original(self):
        data = dataset()
        prepared = self.prepare(data, 'new paragraph\n\n' + data['sources']['paper.tex']['text'])
        loc = self.loc(prepared)
        self.assertEqual(loc['binding']['status'], 'relocated')
        self.assertEqual(loc['binding']['lineStart'], 4)
        self.assertTrue(loc['binding']['reviewRequired'])
        self.assertEqual(loc['lineStart'], 2)
        self.assertEqual(loc['sourceSha256'], self.loc(data)['sourceSha256'])
        self.assertEqual(prepared['comments'][0]['candidateVersion'], 'proposal-1')
        self.assertNotEqual(prepared['currentSources']['paper.tex']['sha256'], prepared['sources']['paper.tex']['sha256'])

    def test_source_binding_version_changes_with_source_not_proposal_identity(self):
        data = dataset()
        first = self.prepare(data, data['sources']['paper.tex']['text'])
        second = self.prepare(data, 'preamble\n' + data['sources']['paper.tex']['text'])
        self.assertNotEqual(first['comments'][0]['sourceBindingVersion'], second['comments'][0]['sourceBindingVersion'])
        self.assertEqual(first['comments'][0]['candidateVersion'], second['comments'][0]['candidateVersion'])

    def test_duplicate_quotes_require_unique_exact_context(self):
        data = dataset()
        current = 'other\nExact original sentence.\nother\n' + data['sources']['paper.tex']['text']
        binding = self.loc(self.prepare(data, current))['binding']
        self.assertEqual(binding['status'], 'relocated')
        self.assertEqual(binding['matchedBy'], 'unique-exact-quote-and-context')
        self.assertEqual(binding['lineStart'], 5)

    def test_ambiguous_quote_never_chooses_nearest_line(self):
        data = dataset()
        text = data['sources']['paper.tex']['text']
        binding = self.loc(self.prepare(data, text + text))['binding']
        self.assertEqual(binding['status'], 'needs_relocation')
        self.assertNotIn('lineStart', binding)
        self.assertTrue(binding['reviewRequired'])

    def test_same_hash_original_range_disambiguates_known_unchanged_source(self):
        text = 'before\nExact original sentence.\nafter\n\nExact original sentence.\n'
        binding = self.loc(self.prepare(dataset(text), text))['binding']
        self.assertEqual(binding['status'], 'verified')
        self.assertEqual(binding['lineStart'], 2)

    def test_missing_quote_retains_original_location_and_snapshot(self):
        data = dataset()
        prepared = self.prepare(data, 'A rewritten paper with no original sentence.\n')
        self.assertEqual(self.loc(prepared)['binding']['status'], 'needs_relocation')
        self.assertEqual(self.loc(prepared)['quote'], 'Exact original sentence.')
        self.assertEqual(self.loc(prepared)['lineStart'], 2)
        self.assertEqual(prepared['sources'], data['sources'])

    def test_missing_file_is_visible_not_rebound(self):
        self.assertEqual(self.loc(self.prepare(dataset()))['binding']['status'], 'needs_relocation')

    def test_inconsistent_original_snapshot_hash_is_not_accepted(self):
        data = dataset()
        data['sources']['paper.tex']['text'] = 'tampered snapshot'
        binding = self.loc(self.prepare(data, 'before\nExact original sentence.\nafter\n'))['binding']
        self.assertEqual(binding['status'], 'needs_relocation')
        self.assertIn('快照', binding['reason'])

    def test_missing_original_hash_is_not_claimed_verified(self):
        data = dataset()
        self.loc(data).pop('sourceSha256')
        data['sources']['paper.tex'].pop('sha256')
        binding = self.loc(self.prepare(data, data['sources']['paper.tex']['text']))['binding']
        self.assertEqual(binding['status'], 'needs_relocation')
        self.assertIn('哈希', binding['reason'])

    def test_path_traversal_and_symlink_escape_are_not_read(self):
        for relative in ('../outside.tex', '/tmp/outside.tex', 'folder\\outside.tex'):
            data = dataset()
            self.loc(data)['file'] = relative
            prepared = self.prepare(data)
            self.assertEqual(self.loc(prepared)['binding']['status'], 'needs_relocation')
            self.assertEqual(prepared['currentSources'], {})
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / 'outside.tex'; target.write_text('secret')
            (self.root / 'paper.tex').symlink_to(target)
            self.assertEqual(self.prepare(dataset())['currentSources'], {})

    def test_future_binding_extensions_survive_rebuild_without_stale_safety_fields(self):
        data = dataset()
        self.loc(data)['binding'] = {'future': {'color': 'blue'}, 'status': 'verified', 'lineStart': 999, 'lineEnd': 999}
        data['currentSources'] = {'paper.tex': {'future': 'preserved', 'text': 'stale', 'sha256': 'stale'}}
        prepared = self.prepare(data, 'missing quote')
        binding = self.loc(prepared)['binding']
        self.assertEqual(binding['future'], {'color': 'blue'})
        self.assertEqual(binding['status'], 'needs_relocation')
        self.assertNotIn('lineStart', binding)
        self.assertEqual(prepared['currentSources']['paper.tex']['future'], 'preserved')
        self.assertEqual(prepared['currentSources']['paper.tex']['text'], 'missing quote')

    def test_second_manuscript_custom_reviewer_count_order_and_identity(self):
        a, b = dataset(document_id='manuscript-a'), dataset(document_id='manuscript-b')
        b['reviewers'].append({'id': 'reviewer-B', 'displayName': 'Reviewer B'})
        b['comments'].append({'id': 'another-comment', 'reviewer': 'reviewer-A', 'candidateVersion': 'proposal-2', 'locations': []})
        prepared = self.prepare(b, b['sources']['paper.tex']['text'])
        self.assertEqual(prepared['documentId'], 'manuscript-b')
        self.assertEqual([r['id'] for r in prepared['reviewers']], ['reviewer-C', 'reviewer-A', 'reviewer-B'])
        self.assertEqual([c['reviewer'] for c in prepared['comments']], ['reviewer-C', 'reviewer-A'])
        self.assertEqual([c['id'] for c in a['comments']], ['same-comment-id'])

    def test_placeholder_duplicate_ids_and_unknown_reviewers_are_rejected(self):
        cases = []
        a = dataset(); a['documentId'] = builder.PLACEHOLDER_DOCUMENT_ID; cases.append(a)
        a = dataset(); a['comments'].append(copy.deepcopy(a['comments'][0])); cases.append(a)
        a = dataset(); a['comments'][0]['reviewer'] = 'missing'; cases.append(a)
        a = dataset(); a['reviewers'].append(copy.deepcopy(a['reviewers'][0])); cases.append(a)
        a = dataset(); a['documentId'] = 'bad\nidentity'; cases.append(a)
        for item in cases:
            with self.assertRaises(ValueError):
                builder.prepare_data(item, self.root)

    def test_future_schema_payload_retained_without_downgrade_or_binding(self):
        future = {'schemaVersion': 3, 'documentId': 'future-project', 'futureData': {'deep': [1, {'raw': '<script>'}]}}
        prepared = builder.prepare_data(future, self.root)
        self.assertEqual(prepared, future)
        self.assertNotIn('currentSources', prepared)

    def test_temp_output_self_contained_and_original_json_unchanged(self):
        data = dataset()
        (self.root / 'paper.tex').write_text(data['sources']['paper.tex']['text'])
        data['extension']['inert'] = "</script><script>throw Error('never')</script>"
        source = self.root / 'manuscript.json'; source.write_text(json.dumps(data))
        before = source.read_bytes()
        output = self.root / 'output' / 'review.html'
        prepared = builder.build(source, output, self.root)
        html = output.read_text()
        self.assertIn('id="workbench-data"', html)
        self.assertNotIn('/* WORKBENCH_DATA */', html)
        self.assertNotIn("</script><script>throw Error('never')</script>", html)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(self.loc(prepared)['binding']['status'], 'verified')


if __name__ == '__main__':
    unittest.main()
