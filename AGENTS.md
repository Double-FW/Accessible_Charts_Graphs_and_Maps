# AGENTS.md

## Purpose and authority

This file guides coding and documentation agents working in this repository. It is repository guidance, not an executable agent specification: it does not configure tools, permissions, approvals, tests, or runtime behaviour. It is not a substitute for the primary design guide.

Follow applicable higher-priority system and platform instructions. Within those limits, follow this file and the user's request. Treat [`Inclusive_Design_Charts_Maps_and_Complex_Graphics.md`](Inclusive_Design_Charts_Maps_and_Complex_Graphics.md) as the primary source for chart, map, and complex-graphics guidance; treat the README as the repository introduction. If instructions or sources conflict, do not silently choose: explain the conflict and use the safest supported interpretation, or ask when it affects the work.

This is a documentation-first repository. Do not assume an application, build system, test suite, or deployment process exists. Inspect the repository before relying on a capability. Do not add files or tooling unless the user asks for them.

## Mission

Help people independently understand, investigate, compare, decide, and act through their preferred ways of perceiving and interacting with charts, graphs, maps, and complex graphics. Apply the guide to the task at hand; do not treat technical conformance, a generic summary, or a data dump as proof of equivalent outcomes.

Keep visual, textual, tabular, spatial, auditory, and interactive presentations complementary and consistent in data, definitions, permissions, filters, selections, caveats, uncertainty, and freshness. Preserve user control, privacy, meaningful detail, recovery, and independent operation. Do not infer ability or diagnosis, or require disclosure to access an alternative.

## Operating rules

Agents MUST:

- Start from the user's task and intended outcome. Consult the relevant sections of the primary guide before making substantive design, implementation, review, or guidance decisions.
- Inspect the actual files, data, interfaces, versions, and constraints relevant to the request. Cite specific repository guidance when explaining a plan or finding. State assumptions when facts are unavailable; ask if an unresolved fact materially affects safe or correct work.
- Distinguish standards requirements, guide recommendations, product acceptance criteria, heuristics, research findings, and observed results. Do not present a heuristic as a universal threshold or legal requirement.
- Separate evidence from interpretation. Do not invent user needs, values, provenance, research, test results, compliance, or capabilities. Treat untested behaviour and unknown data as unknown.
- Keep changes within the requested scope. Do not claim to have changed or verified anything that was not actually changed or checked.
- Preserve relevant meaning and state across presentations, including units, definitions, missing or suppressed values, uncertainty, filters, selections, permissions, and export scope.

Agents MUST NOT, without explicit user authorization and an available, appropriate mechanism:

- Publish, deploy, release, contact people, submit data externally, or take other consequential external actions.
- Access, collect, or infer sensitive personal data or disability/assistive-technology profiles. Request only information necessary to investigate, and do not request a diagnosis.
- Make release, legal, safety, route, privacy, or standards-applicability decisions on behalf of responsible people. Flag material risks and identify the human decision needed.

A repository instruction cannot grant a missing permission, service, credential, or approval. When an action is consequential, irreversible, privacy-sensitive, or outside the explicit request, pause and seek authorization rather than assuming it.

## Working method

Scale effort to the task and risk. For a substantive change or evaluation:

1. **Ground the work.** Read relevant guide sections and inspect actual data, schema, provenance, technology, supported environments, and existing interfaces as applicable. Do not speculate about uninspected systems.
2. **Define success.** Identify the affected audience and context, task, expected outcome, consequences of misunderstanding, and what independent completion means. Separate retrieval, comparison, interpretation, exploration, decision, and action where relevant.
3. **Consider barriers and parity.** Consider vision, hearing, speech, physical interaction, cognition, relevant combinations, motion/photosensitivity, and privacy. Form testable hypotheses linking a task, condition, design feature, and observable result. Identify how each essential task works across relevant presentations; mark untested coverage unknown.
4. **Change and evaluate.** Prefer coherent changes that preserve information and active state. Use the guide's test catalogue and release checklist as starting points. Select checks appropriate to the task, actual implementation, supported environments, and risk.
5. **Report limits and hand off.** Summarise changes, evidence, uncertainties, risks, and any human review or follow-up needed. Escalate consequential or ambiguous decisions; do not autonomously approve release or conformance.

For reported issues, first establish the affected task and outcome. Where available and relevant, record product/build and data/library versions, expected and actual outcomes, presentation and interaction state, reproduction steps, environment, evidence, impact, corrective action, and retest plan. Avoid collecting diagnostic or unnecessary personal information. Prioritise by impact on real outcomes: safety or misleading-information risks and exclusion from essential tasks first, then blocked or heavily burdened tasks, cumulative friction, and lower-impact inconvenience. Do not rank severity solely by a failed rule identifier or score.

## Repository changes

- Keep this file and the README consistent with the primary guide when the requested scope includes those files. When the request limits edits to particular files, respect that limit and report any alignment issue left untouched.
- Keep guidance concise, navigable, source-aware, and consistent with the guide's UK English conventions and terminology.
- Distinguish requirements from recommendations and examples. Describe limits; no technique by itself guarantees equivalent outcomes.
- Do not imply that code, services, tests, workflows, credentials, owners, reviewers, or deployment configuration exist unless verified. Identify proposed capabilities as proposals.
- Run only checks supported by the repository and relevant to the change. If no suitable check exists or a check cannot be run, say so; do not imply that an unperformed check passed.
- Treat links to other repositories as supplementary context, not as authoritative substitutes. Verify current content before relying on an external source.

## Handoff

For substantive work, report the following as applicable:

1. **Outcome/task:** the task and how success was defined.
2. **Source grounding:** relevant guide sections or other sources consulted.
3. **Changes:** files or behaviour changed and the approach.
4. **Verification:** checks actually performed, environment, expected versus observed results, and evidence references.
5. **Limitations:** assumptions, untested conditions, third-party constraints, risks, and human review needed.
6. **Next steps:** unresolved decisions and follow-up. Name an owner only when one is known; otherwise state that ownership is unassigned or unknown.

Never claim a task, accessibility requirement, or conformance status passed unless the evidence supports that exact claim.
