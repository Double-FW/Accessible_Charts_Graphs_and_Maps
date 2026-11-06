# Accessible Charts, Graphs and Maps

Practical guidance from **Double FW Ltd** for designing, implementing, evaluating and maintaining accessible charts, graphs, maps and complex graphics. This repository is a human-readable guide and a source of context for people and AI-assisted workflows.

The aim is not merely to make a graphic technically perceivable. Help people independently understand, investigate, compare, decide and act through their preferred ways of perceiving and interacting. Preserve the information advantage of visual presentation—including trends, relationships, exceptions, routes and opportunities for exploration—across complementary presentations.

## Purpose and scope

Use this guidance to:

- Start from people's tasks and intended outcomes, rather than a preferred chart type, framework or compliance checklist.
- Design visual, textual, tabular, spatial, auditory and interactive presentations as complementary ways to work. A generic summary or data dump is not automatically equivalent to exploration or action.
- Keep data, definitions, permissions, filters, selections, caveats, uncertainty and freshness consistent across views and exports.
- Plan implementation and evaluation around independent task completion, meaningful detail, user control, privacy, recovery and real-world consequences.
- Support collaboration among designers, developers, researchers, data specialists and QA teams, as well as grounded, human-reviewed AI assistance.

The guidance applies to static and interactive visualisations, dashboards, wayfinding, networks, process diagrams, journey maps, collaborative canvases, animation and related data experiences. Consider combinations of functional needs without inferring ability or diagnosis, or requiring disclosure to access an alternative.

## Source of truth and repository contents

The primary source is [Inclusive Design of Charts, Graphs, Maps and Dynamic Complex Graphics](Inclusive_Design_Charts_Maps_and_Complex_Graphics.md). It contains practical design and implementation guidance, a test catalogue, worked examples, an evidence-record template and a release checklist. Keep this README and [`AGENTS.md`](AGENTS.md) aligned with that guide.

This is a documentation-first repository. Do not assume it has an application, build system or test suite unless one is added and verified. Recommendations, examples and heuristics in the guide are not automatically legal requirements or guarantees of conformance.

## Principles and approaches

- **Outcome-first:** define the question, decision or action people need to complete before selecting a representation.
- **Complementary parity:** preserve useful facts, relationships, caveats, actions and exploration across presentations; do not assume one generic alternative is sufficient.
- **Consistent state and meaning:** use the same underlying data and keep definitions, permissions, filters, selections and freshness aligned.
- **Agency and privacy:** support independent operation, user choice, recovery and access to detail without unnecessary accounts, disclosure or profiling.
- **Evidence-aware:** ground claims in source material, supplied data, observed behaviour or reproducible tests. Treat unknown or untested behaviour as unknown.
- **Human-centred decisions:** involve disabled people and retain human judgement for consequential interpretation, route and safety information, privacy, standards applicability and release decisions.
- **Clear evidence boundaries:** distinguish standards requirements from guide recommendations, product acceptance criteria, heuristics and research findings. Do not present a heuristic as a universal threshold or legal requirement.

## What the guide covers

- **Tasks and outcomes:** retrieval, comparison, interpretation, exploration, decision and action; task briefs and observable success criteria.
- **Information and data:** representation choice, encodings, scales, units, labels, missing and suppressed values, uncertainty, provenance, freshness and export scope.
- **Charts and maps:** trends, values and relationships; search, locations, routes, boundaries, wayfinding and spatial uncertainty.
- **Complex graphics:** networks, hierarchies, process diagrams, journey maps, collaborative canvases and dynamic or scientific visualisations.
- **Interaction and implementation:** semantic controls, keyboard and pointer/touch alternatives, focus, zoom and reflow, display preferences, updates, motion, failure states and recovery.
- **Testing and maintenance:** automated and manual checks, assistive-technology testing, task-based evaluation with disabled people, evidence, prioritisation and retesting.
- **Human and agent workflows:** source-grounded planning, implementation, review and handoff, with limits and human approval points made explicit.

## Delivery methodology

Use this iterative lifecycle for design, implementation, review and documentation. Scale effort to risk, but do not skip outcome validation for a claimed fix.

1. **Gather and ground context.** Read relevant guide sections and inspect actual data, schema, provenance, technology, constraints, supported environments and existing interfaces. Cite specific repository guidance in plans or review notes. State assumptions or ask when necessary facts are missing.
2. **Define tasks and outcomes.** Record audience and context, questions, decisions or actions, units and definitions, consequences of misunderstanding, and what successful independent completion looks like. Separate retrieval, comparison, interpretation, exploration, decision and action.
3. **Map barriers and coverage.** Consider vision, hearing, speech, physical interaction, cognition, relevant combinations, motion/photosensitivity and privacy. Turn plausible barriers into testable hypotheses linking task, condition, design feature, response and observable result. Mark untested coverage as unknown.
4. **Plan parity before implementation.** For every essential task, specify the visual presentation and the structured presentations or controls that support it. Record parity for facts, relationships, actions, filters, selections, caveats, uncertainty and exports.
5. **Choose and design the representation.** Use the simplest useful visual form. Explain encodings, scales, units, missing or suppressed values, uncertainty, boundaries and statistical caveats. Use a summary as an entry point, not a substitute for meaningful exploration when the task requires it.
6. **Implement one coherent experience.** Use a shared data/query/state model for the graphic, summary, controls, structured details, status and exports. Provide semantic, visible controls and non-gesture alternatives.
7. **Verify with multiple methods.** Combine automated checks, manual inspection, assistive-technology testing and task-based evaluation with disabled people where appropriate. Validate expected outcomes and recovery, not just individual rules.
8. **Record, prioritise and maintain.** Link evidence to tasks, versions, states, environments and relevant functional conditions. Report independent completion, accuracy, parity, effort, time, confidence and recovery. Prioritise by real impact and retest after changes.
9. **Human review and handoff.** Summarise changes, evidence, unresolved risks, unknowns and follow-up work. Escalate consequential or ambiguous decisions; do not autonomously approve release or claim conformance.

## Practical implementation techniques

### Information and presentation

- Provide meaningful heading and context, a concise overview, interactive exploration, navigable structured detail and interpretation notes as appropriate.
- Provide exact values and useful ways to search, filter, select, compare and inspect details where task demands require them; do not force sequential reading of very large datasets.
- Use semantic tables with captions, associated row and column headers, units, periods and explicit missing-value meanings.
- Describe relationships and direction explicitly for networks, routes, hierarchies and processes; a node list or colour description alone is not enough.
- Keep descriptions, summaries, values and exports driven by the same data and active state. Distinguish observation from interpretation and identify evidence for causal claims.
- Preserve provenance, freshness, scope, limitations and uncertainty. Distinguish zero, missing, unavailable, suppressed and not applicable.

### Interaction and semantics

- Prefer native, labelled controls for search, filters, layer or series visibility, ranges, selection and view changes. Expose appropriate names, roles, values and states; do not make static marks behave like controls without an understandable interaction model.
- Define a predictable keyboard path and component navigation model. Keep focus visible and stable, and restore it predictably when content changes or a selected item disappears.
- Offer single-pointer alternatives to drag, pinch, lasso, rotate, scrub and drag-to-reorder actions. Keyboard access alone does not solve a touch/pointer gesture dependency.
- Do not expose essential information only on hover. Support relevant pointer, keyboard, touch and assistive-technology use for details and controls.
- Keep status messages concise and persistent results available in page content. Avoid announcing every point or update, and preserve reading and selection context during refreshes.
- Provide pause, stop, reset, undo and recovery where appropriate. Respect reduced-motion settings in CSS and scripted, canvas or map behaviour; avoid unsafe flashing and audio autoplay.
- For maps, provide a searchable list with equivalent eligible places, attributes and actions; support manual location entry and explain location, route, boundary and freshness uncertainty.
- For networks and diagrams, expose named nodes, relationships, direction, conditions, paths and dependencies through structured navigation and queries.
- Keep useful headings, summaries, controls and structured results available when a renderer, map tile provider, script, embed or export fails.

### Adaptation and privacy

- Test readable labels and controls at their actual rendered size; permit text growth, page zoom and reflow. Do not disable browser zoom. Confine necessary two-dimensional panning to the relevant graphic where possible.
- Evaluate text and required graphical or control information against applicable contrast criteria in authored themes and relevant states. Check focus, selection and boundaries, not only default colours.
- Support user overrides such as forced colours and reduced motion where applicable. Do not presume dark mode or a particular palette is universally accessible.
- Separate page magnification from chart or map data zoom, and make both understandable and controllable.
- Do not require accounts, disability disclosure, voice, geolocation or assistive-technology profiling to access essential alternatives. Ask for geolocation after an explicit user action and provide a non-location alternative.

## Testing, evidence and prioritisation

For each essential task, define expected facts, acceptable reasoning, actions and recovery before testing. Build fixtures for ordinary data and meaningful edge cases, including long labels, negative and zero values, missing or suppressed data, dense relationships, boundary cases, stale data and failed or empty states.

Select tests by product risk and relevant states. Check correctness and parity of values, units, filters, totals, relationships, caveats and exports; colour independence, contrast, resizing, zoom/reflow, themes and forced colours; keyboard, focus, pointer/touch alternatives and representative screen-reader tasks; motion, updates and announcements; map, route and diagram outcomes; permissions, denial and recovery; and user understanding, independent completion, effort, confidence and mistake correction.

Automated tools can detect some deterministic defects and regressions. They cannot establish meaningful information parity, comprehensible interpretation, spatial usefulness or practical task completion. Combine methods and record what was actually tested, the environment, expected versus observed results, evidence, limitations and unknowns. Do not claim a task or accessibility requirement passed unless evidence supports that exact claim.

Prioritise critical safety or misleading-information risks and complete exclusion from an essential task first. Then address blocked or heavily burdened essential tasks, repeated friction and recovery problems, and lower-impact inconvenience. Consider cumulative barriers; do not rank severity solely by a failed rule identifier or a single accessibility score.

## Investigating reported issues

Identify the affected task and outcome before proposing a fix. Capture enough context to reproduce and evaluate the problem:

- Graphic or product version/build, data version and relevant third-party library/version.
- User task, expected and actual outcomes, and whether assistance or abandonment occurred.
- Presentation and interaction state, filters/selections, and failure or loading conditions.
- Relevant functional condition(s) and input method, without requesting a diagnosis.
- Browser, operating system, assistive technology, device, viewport and settings where relevant.
- Reproduction steps, evidence location, and impact on information, effort, safety, privacy or independent completion.
- Proposed owner, corrective action, retest plan, remaining uncertainty and priority rationale.

## Useful project deliverables

Depending on risk and scope, applying the guide can produce an outcome brief and essential-task list; barrier hypotheses and a task-by-condition coverage matrix; a presentation-parity matrix and paired prototypes; an annotated design and interaction/state specification; purposeful test data with expected answers; reproducible cases and evidence records; and a prioritised remediation plan with release decisions and retest triggers.

Evaluate meaningful outcomes separately, including independent completion, accuracy, information parity, effort, time, confidence, recovery, comfort and coverage. Do not compress these into a single score that hides different outcomes or uncertainty.

## Using this repository with AI agents

The guide can inform AI skills, system instructions, retrieval-augmented generation (RAG), coding agents and human-led design or QA workflows. Agents should read relevant source sections, inspect actual data and interfaces, cite repository guidance, separate requirements from recommendations and project criteria, and ask for human decisions when facts or consequences are unresolved.

A grounded agent workflow should plan outcomes, task coverage and parity before implementation; update related views and controls coherently from shared data and state; verify with tests that are actually run; and report evidence, assumptions, unknowns and handoff needs. Do not fabricate values, user needs, source claims, test results or conformance. Do not treat generated code or automated scans as proof of accessibility, simulate disabled people's participation, infer diagnoses, or autonomously approve consequential decisions.

### Agent handoff format

1. **Outcome/task:** who needs to do what and how success was defined.
2. **Source grounding:** relevant guide sections and complementary repository material used.
3. **Changes:** files or behaviours changed and the approach.
4. **Verification:** checks actually performed, environment, expected versus observed results and evidence references.
5. **Limitations:** untested conditions, assumptions, third-party constraints, remaining risks and human/user review needed.
6. **Next steps:** owners, retest triggers and unresolved decisions.

## Related public Double-FW repositories

These complementary repositories can help with adjacent parts of delivery. They do not replace this chart- and map-specific guide; check each project's current content and scope before relying on it.

- [The Little Book of Accessibility](https://github.com/Double-FW/The-Little-Book-of-Accessibility) — broader accessibility and inclusive-design knowledge, including source-aware AI/RAG workflows.
- [QA Accessibility Testing](https://github.com/Double-FW/QA_Accessibility_Testing) — manual and automated accessibility QA and test-management approaches.
- [Task Analysis for Comparative Accessibility Evaluation of Internal Systems](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems) — task analysis and comparative evaluation methods.
- [Cognitive UX Design](https://github.com/Double-FW/Cognitive-UX-Design) — guidance and tools for understandable, controllable, inclusive experiences and evidence-aware workflows.
- [Accessible Digital and Printed Documents](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents) — accessible document design for digital, print and hybrid formats.
- [Global Accessibility Regulatory Requirements](https://github.com/Double-FW/Global_Accessiblity_Regulatory_Requirements) — jurisdiction-specific regulatory routing; not legal advice or a substitute for an authoritative assessment.
- [Accessible Chatbots](https://github.com/Double-FW/Accessible-Chatbots) — relevant when an assistant or conversational workflow is part of the interface or delivery process.

See the [Double-FW organisation](https://github.com/Double-FW) for other public resources. Repository availability and content can change; verify the current scope and guidance in each linked project.

## Contributing

Suggestions, corrections and practical examples are welcome through this repository's contribution channels. Describe the affected guidance, user outcome or barrier, proposed change and source/evidence basis. Keep additions concise, navigable, source-aware and consistent with the guide's UK English conventions. Distinguish requirements from recommendations and examples, include actionable evaluation criteria where possible, and explain limits rather than implying a technique guarantees equivalent outcomes. Check links and consistency across `AGENTS.md`, this README and the primary guide.

Run only checks supported by the repository and report what was actually done. If a change proposes or assumes code, tooling or tests not present here, identify them as proposed rather than existing.

## About

Developed by **Double FW Ltd** to support accessible, inclusive design and delivery across human and AI-assisted work. The repository is available under the [MIT License](LICENSE).
