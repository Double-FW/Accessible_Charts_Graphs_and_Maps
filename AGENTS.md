# AGENTS.md

## Mission and scope

This repository is a human-readable and agent-consumable practical guide to designing, implementing, evaluating, and maintaining accessible charts, graphs, maps, and complex graphics. Apply its guidance to static and interactive visualisations, dashboards, wayfinding, networks, process diagrams, journey maps, collaborative canvases, animation, and related data experiences.

The goal is not merely to make a graphic technically perceivable. Help people independently understand, investigate, compare, decide, and act through their preferred ways of perceiving and interacting. Preserve the information advantage of a visual presentation—including trends, relationships, exceptions, routes, and opportunities for exploration—across complementary presentations.

The primary source of truth is [`Inclusive_Design_Charts_Maps_and_Complex_Graphics.md`](Inclusive_Design_Charts_Maps_and_Complex_Graphics.md). Keep this file and the README aligned with that guide. This repository is documentation-first; do not assume there is an application, build system, or test suite unless one is added and verified.

## Working principles for people and agents

- Start from the user's task and intended outcome, not a preferred chart type, framework, or compliance checklist.
- Treat visual, textual, tabular, spatial, auditory, and interactive presentations as complementary ways to work. A generic summary or data dump is not automatically equivalent to exploration or action.
- Keep data, definitions, permissions, filters, selections, caveats, uncertainty, and freshness consistent across presentations and exports.
- Design for a range of functional needs and combinations; do not infer ability or diagnosis, or require disclosure to access an alternative.
- Preserve user control, privacy, independent operation, recovery, and access to meaningful detail.
- Distinguish standards requirements from this guide's recommendations, product acceptance criteria, heuristics, and research findings. Do not present a heuristic as a universal threshold or legal requirement.
- Ground claims in source material, supplied data, observed behavior, or reproducible tests. Do not invent user needs, values, evidence, conformance, or test results.
- Treat untested behavior and unknown data as unknown—not as passed, safe, accessible, or not applicable without justification.
- Keep human judgment and disabled people's involvement central, especially for consequential interpretation, route and safety information, privacy, standards applicability, and release decisions.

## Issues and problem framing

When investigating a reported issue, identify the affected task and outcome before proposing a fix. Capture enough context to reproduce and evaluate the problem:

- Graphic or product, version/build, data version, and relevant third-party library/version.
- User task, expected outcome, actual outcome, and whether assistance or abandonment occurred.
- Presentation, interaction state, filters/selections, and failure/loading conditions.
- Relevant functional condition(s) and input method, without requesting diagnosis.
- Browser, operating system, assistive technology, device, viewport, and settings where relevant.
- Reproduction steps, evidence location, impact on information, effort, safety, privacy, or independent completion.
- Proposed owner, corrective action, retest plan, remaining uncertainty, and priority rationale.

Prioritise by impact on real outcomes: critical safety or misleading-information risks and complete exclusion from an essential task first; then blocked or heavily burdened essential tasks, repeated friction and recovery problems, and lower-impact inconvenience. Consider cumulative barriers. Do not rank severity solely by a failed rule identifier or a single accessibility score.

## Delivery methodology

Use this iterative lifecycle for design, implementation, review, and documentation changes. Scale effort to risk, but do not skip outcome validation for a claimed fix.

1. **Gather and ground context.** Read the relevant sections of the primary guide and inspect the actual data, schema, provenance, technology, constraints, supported environments, and existing interfaces. Cite specific repository guidance in plans or review notes. If a necessary fact is unavailable, state the assumption or ask for clarification rather than fabricating it.
2. **Define outcomes and tasks.** Record the audience and context, question(s), decisions/actions, units and definitions, consequences of misunderstanding, and what successful independent completion looks like. Separate retrieval, comparison, interpretation, exploration, decision, and action.
3. **Map barriers and coverage.** Consider vision, hearing, speech, physical interaction, cognition, relevant combinations, motion/photosensitivity, and privacy. Turn each plausible barrier into a testable hypothesis linking task, condition, design feature, response, and observable result. Mark untested coverage as unknown.
4. **Plan parity before implementation.** For each essential task, specify the visual presentation and the specific structured presentation or controls that support it. Record parity for facts, relationships, actions, conditions, uncertainty, and state. Preserve open-ended exploration where it is part of the task.
5. **Choose and design the representation.** Use the simplest useful visual form. Explain encodings, scales, units, missing/suppressed values, uncertainty, boundaries, and statistical caveats. Use redundant cues without relying on colour alone. Remove clutter without discarding meaning.
6. **Implement one coherent experience.** Use a shared data/query/state model for the graphic, summary, controls, structured details, status, and exports. Provide semantic, visible controls and non-drag alternatives. Preserve focus and selection through updates; provide understandable empty, loading, stale, failed, and recovery states.
7. **Verify with multiple methods.** Combine automated checks, manual inspection, assistive-technology testing, and task-based evaluation with disabled people where appropriate. Validate expected answers independently of the rendered presentation. Test important states and realistic edge cases, not only the initial happy path.
8. **Record, prioritise, and maintain.** Link evidence to tasks, versions, states, environments, and functional conditions. Report independent completion, accuracy, parity, effort, time, confidence, recovery, comfort, and coverage separately. Assign owners and retest after changes to data, content, interaction, libraries, or outputs.
9. **Human review and handoff.** Summarise what changed, evidence collected, unresolved risks, unknowns, and follow-up work. Escalate consequential or ambiguous decisions; do not autonomously approve a release based only on generated code or automated scans.

## Implementation techniques

### Information and presentation

- Provide a meaningful heading and context, concise overview, interactive exploration, navigable structured detail, and interpretation notes as appropriate.
- Supply exact values and useful ways to search, filter, select, compare, and inspect details where task demands require them; do not force sequential reading of very large datasets.
- Keep tables semantic, with captions, associated row/column headers, units, period, and explicit missing-value meanings.
- Describe relationships and direction explicitly for networks, routes, hierarchies, and processes; a node list or colour description alone is not enough.
- Keep descriptions, summaries, values, and exports driven by the same data and active state. Distinguish observation from interpretation and identify evidence for causal claims.
- Preserve data provenance, freshness, scope, limitations, and uncertainty. Distinguish zero, missing, unavailable, suppressed, and not applicable.

### Interaction and semantics

- Prefer native, labelled controls for search, filters, layer/series visibility, ranges, selection, and view changes. Expose appropriate names, roles, values, and states; do not make static marks unnecessary Tab stops.
- Define a predictable keyboard path and component navigation model. Keep focus visible and stable, and restore it predictably when content changes or a selected item disappears.
- Offer single-pointer alternatives to drag, pinch, lasso, rotate, scrub, and drag-to-reorder actions; keyboard access alone does not solve a touch/pointer gesture dependency.
- Do not expose essential information only on hover. Support relevant pointer, keyboard, touch, and assistive-technology use for details and controls.
- Keep status messages concise and persistent results available in page content. Avoid announcing every point or update. Preserve a user's reading/selection context during refreshes.
- Provide pause, stop, reset, undo, and recovery where appropriate. Respect reduced-motion settings in CSS and scripted/canvas/map behavior; avoid unsafe flashing and audio autoplay.
- For maps, provide a searchable list with equivalent eligible places, attributes, and actions; support manual location entry and explain location, route, boundary, and freshness uncertainty.
- For networks and diagrams, expose named nodes, relationships, direction, conditions, paths, and dependencies through structured navigation and queries.
- Ensure useful headings, summaries, controls, and structured results remain available when a renderer, map tile provider, script, embed, or export fails.

### Adaptation and privacy

- Test readable labels and controls at their actual rendered size; permit text growth, page zoom, and reflow. Do not disable browser zoom. Keep necessary two-dimensional panning confined to the spatial content.
- Evaluate text and required graphical/control information against applicable contrast criteria in authored themes and relevant states. Check focus, selection, and boundaries, not only default colors.
- Support user overrides such as forced colors and reduced motion where applicable. Do not presume dark mode or a particular palette is universally accessible.
- Separate page magnification from chart/map data zoom and make both understandable and controllable.
- Do not require accounts, disability disclosure, voice, geolocation, or assistive-technology profiling to access essential alternatives. Ask for geolocation after an explicit user action; provide manual entry where relevant.

## Testing and evidence

For each essential task, define expected facts, acceptable reasoning, actions, and recovery before testing. Build fixtures covering ordinary data and meaningful edge cases such as long labels, negative/zero values, ties, missing/suppressed values, uncertainty, dense/overlapping marks, large results, no results, delayed/out-of-order updates, stale data, and failures.

Use the guide's test catalogue and release checklist as a starting point. Select tests by product risk and relevant states, including:

- Correctness and parity of values, units, filters, totals, relationships, caveats, and exports.
- Colour independence, contrast, text resizing, zoom/reflow, text spacing, themes, and forced-colour behavior.
- Keyboard, focus, pointer/touch alternatives, target operation, names/structure, and representative screen-reader tasks.
- Motion/reduced-motion, live updates, announcements, audio independence, and combinations of needs.
- Map/route and diagram outcomes, permission/location denial, empty/stale/failed states, and recovery.
- User understanding, independent completion, effort, confidence, and ability to correct mistakes.

Automated tools can detect some deterministic defects and regressions; they cannot establish meaningful information parity, comprehensible interpretation, spatial usefulness, or practical task completion. A passing scan, simulator, sample session, or code review is not proof of accessibility or conformance. Record methods, versions, environment, outcomes, limitations, and untested conditions. Protect participant privacy and minimise research data.

## Documentation and contribution approach

This repository currently contains a README, the primary Markdown guide, and a license. Keep additions concise, navigable, source-aware, and consistent with the guide's UK English conventions and inclusive language. Preserve stable test identifiers, definitions, and evidence limits when editing existing content. Use Markdown headings in logical order, descriptive link text, clear tables, and fenced examples where they improve usability.

When adding or changing guidance:

- State the issue or user outcome addressed, affected scope, rationale, and evidence/source basis.
- Distinguish mandatory requirements from recommendations, examples, and optional enhancements.
- Provide actionable methods for both people and agents, with observable acceptance/evaluation criteria where possible.
- Do not imply that a technique guarantees equivalent outcomes; describe how to validate it and its limits.
- Check cross-references, repository links, spelling, and consistency among `AGENTS.md`, `README.md`, and the main guide.
- If a change creates or assumes code, tooling, or a test suite not present in the repository, clearly identify it as proposed rather than existing. Run only checks supported by the repository and report what was and was not run.

## Related public Double-FW repositories

Use these repositories as complementary resources when their scope helps answer a delivery question. They do not replace this repository's chart/map-specific guidance; inspect the current content and cite the relevant source before relying on it.

- [The Little Book of Accessibility](https://github.com/Double-FW/The-Little-Book-of-Accessibility) — broader accessibility and inclusive-design knowledge, including source-aware AI/RAG workflows.
- [QA Accessibility Testing](https://github.com/Double-FW/QA_Accessibility_Testing) — manual and automated accessibility QA and test-management approaches.
- [Task Analysis for Comparative Accessibility Evaluation of Internal Systems](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems) — task analysis methods useful for defining observable tasks and comparing outcomes.
- [Cognitive UX Design](https://github.com/Double-FW/Cognitive-UX-Design) — guidance and tools for understandable, controllable, inclusive experiences and evidence-aware workflows.
- [Accessible Digital and Printed Documents](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents) — useful when charts, data tables, or findings are delivered in documents, print, or hybrid formats.
- [Global Accessibility Regulatory Requirements](https://github.com/Double-FW/Global_Accessiblity_Regulatory_Requirements) — consult for jurisdiction-specific regulatory routing; it is not legal advice and does not determine conformance for a product.
- [Accessible Chatbots](https://github.com/Double-FW/Accessible-Chatbots) — relevant when an assistant or conversational workflow is part of the interface or delivery process.

Repository availability and content can change. Verify current scope and guidance in each linked project before use.

## Agent handoff format

When reporting work, include:

1. **Outcome/task:** who needs to do what and how success was defined.
2. **Source grounding:** relevant guide sections and any complementary repository material used.
3. **Changes:** files/behaviors changed and the design/implementation approach.
4. **Verification:** checks actually performed, environment, expected versus observed results, and evidence references.
5. **Limitations:** untested conditions, assumptions, third-party constraints, remaining risks, and human/user review needed.
6. **Next steps:** owners, retest triggers, and unresolved decisions.

Never claim a task or accessibility requirement passed unless the evidence supports that exact claim.
