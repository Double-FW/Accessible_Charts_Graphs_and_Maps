"""Export the approved Accessible Charts Graphs and Maps Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from charts_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

GUIDE = 'Inclusive_Design_Charts_Maps_and_Complex_Graphics.md'
CONTEXT = ['AGENTS.md', 'README.md', GUIDE]
CONTEXT_HEADINGS = ['Purpose and use', 'Core principles', 'Step 2 — Map functional needs and barriers',
                    'Step 11 — Test technical access and comparable outcomes',
                    'Step 12 — Measure, prioritise and maintain', 'Release checklist']
class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.load(match[1], Loader=UniqueKeyLoader) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    context = {title:body for _,title,body,*_ in sections(texts[GUIDE]) if title in CONTEXT_HEADINGS}
    if set(context) != set(CONTEXT_HEADINGS):
        raise ValueError('Required scope, functional needs, testing or release context changed; review extraction.')
    test_ids = re.findall(r'^\| (T[0-9]{2})\b', texts[GUIDE], re.M)
    if test_ids != [f'T{i:02}' for i in range(1,32)]:
        raise ValueError('Test catalogue identities changed or duplicated; review export mapping.')
    warnings = [
        'This is practical source design/testing guidance, not an implemented chart library, completed evaluation, approved release or verified equivalent user outcomes.',
        'T01–T31 are proposed tests with complementary automated, manual, assistive-technology and user methods; export does not execute them.',
        'Standards thresholds and EAA framing retain source applicability and qualifications; export does not reverify legal scope or current external standards.',
        'Worked examples and evidence/release templates remain illustrative. Missing values, uncertainty, privacy and state-parity principles are not converted into actual product findings.'
    ]
    for path,text in texts.items():
        if metadata(text).get('license', 'MIT') != 'MIT': raise ValueError('Review changed source licence: ' + path)
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'source_document_intro': sections(texts[path])[0][2],
            'source_context_sections_json': json.dumps(context,ensure_ascii=False,sort_keys=True) if path == GUIDE else '{}',
            'proposed_test_ids': re.findall(r'^\| (T[0-9]{2})\b',body,re.M) if path == GUIDE else [],
            'interpretation_notice': 'Guidance and proposed tests, not observed results. Keep task, functional condition, information/state parity, uncertainty, permissions, privacy, actual methods and human review together. Conformance or data availability alone does not establish comparable independent outcomes.',
            'review_status': 'faithful_extraction_checked_not_graphic_product_or_audience_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = 'advisory_agent_guidance' if path == 'AGENTS.md' else 'orientation' if path == 'README.md' else 'practical_design_and_testing_guidance'
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, ('illustrative_worked_examples_not_results' if path == GUIDE and title == 'Worked examples' else 'proposed_release_checklist_not_approval' if path == GUIDE and title == 'Release checklist' else 'proposed_test_catalogue_and_methods_not_executed' if path == GUIDE and title.startswith('Step 11') else kind + '_section')))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False, 'proposed_test_ids': test_ids, 'graphic_tests_executed': False, 'user_outcomes_verified': False, 'release_approval_claimed': False})
    card = f'''---
pretty_name: Double FW Accessible Charts Graphs and Maps
language:
- en
license: mit
tags:
- accessibility
- charts
- maps
- data-visualisation
- inclusive-design
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Accessible Charts, Graphs and Maps

Practical guidance on independent understanding, investigation, comparison, decisions
and action through charts, maps, complex diagrams and dynamic graphics. Covers complementary
presentations, shared data/state, functional needs, statistical meaning, interaction, semantics,
privacy, testing and comparable outcomes. This is a text knowledge corpus, not a graphic/data
library, implemented interface, validated user study or compliance certificate.

## Source and versions

Source: https://github.com/{SOURCE}

Checkout: `{sha}` ({date}); export format {cfg['dataset_version']}. Original guide version,
date, metadata, qualifications and source text remain unchanged. Export does not make the
guidance newly peer-reviewed or reverify external standards, legal scope or linked resources.
No linked repository content is automatically imported.

## Dataset views

- `knowledge_chunks`: {len(chunks)} exact H1/H2 Markdown sections from three source documents.
- `documents`: {len(docs)} complete Markdown source documents.

These views overlap; do not concatenate them as independent training examples or evidence.
No synthetic Q&A, actual participant observations, chart fixtures, benchmark or model training
is supplied. `train` is a dataset loading convention. Worked examples and proposed test outcomes
remain illustrative guidance rather than labels of successful product behaviour.

## Retrieval context and traceability

Sections preserve nested headings, tables, fenced evidence templates, caveats and exceptions
without rewriting the source. Every row carries exact source path/commit URL, line range,
text/document hashes, heading path, JSON-encoded metadata, opening context and required context
paths. `source_context_sections_json` attaches complete purpose, principles, functional-needs,
testing, measurement and release sections to guide rows. `proposed_test_ids` records original
T01–T31 identities where the exact catalogue appears; rows retain methods and expected outcomes.
Context pointers and source agent guidance are not implemented runtime enforcement or authority.

## Interpretation and outcome boundaries

Keep visual, textual, tabular, spatial, auditory and interactive routes consistent in data,
units, definitions, caveats, uncertainty, suppressed/missing values, freshness, permissions,
filters, selections and export scope. Alternative formats should preserve meaningful exploration
and action, not merely supply a data dump or editorial summary. Comparable independence,
accuracy, effort, time and confidence require actual scoped evidence.

The functional-needs framing, including combined needs, photosensitivity/motion and privacy,
is design guidance and does not determine legal applicability or diagnose individuals. Preserve
standards requirements, guide recommendations, acceptance criteria, heuristics, findings and
unknowns as distinct. Do not turn conditional thresholds or source recommendations into universal
legal duties, infer ability from diagnosis, or require disclosure for an alternative presentation.

The source proposes 31 tests spanning information parity, keyboard/pointer, AT, display, motion,
live updates, spatial tasks, exports, recovery and privacy. Their methods are complementary;
automation does not replace manual review or user outcomes. These tests are not executed by the
exporter. Worked examples are design scenarios; release checkboxes and an evidence template do
not establish completed testing, configured owners, legal approval or real release readiness.
No production service, route decision, geolocation access, external publication or personal-data
collection is authorised or performed by retaining those source instructions.

## Licence and limits

The root MIT LICENSE is copied unchanged, including copyright (c) 2026 Double FW. Source
attribution, links and qualifications remain intact. Third-party material retains its own terms;
links do not relicense their targets and external full text is not fetched. Extraction checks do
not independently validate legal facts, research, rights, numerical design thresholds, real
interface accessibility or audience equivalence. See record_schema.json, provenance.json and
validation_report.json for the precise snapshot and limited checks.

## Updates

GitHub is the authoring source. Manual runs and Mondays at 07:23 UTC are configured;
GitHub may delay schedules or disable them after public-repository inactivity. All three
Markdown documents and LICENSE are required. New/renamed sources need export-list review.
Missing required sources, changed licence text, changed test/context mapping or failed checks
stop publication. Source-authoring documents are not rewritten.

Seven destination files are managed: README.md, LICENSE, documents.jsonl,
knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json.
Other raw files and .gitattributes remain; unmanaged copies are not kept in sync. Visibility
stays unchanged. Historical versions/downloads are not recalled. Destination: `{target}`.
First authenticated publication remains to be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Authenticate for a private dataset and pin a revision for reproducible use.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
