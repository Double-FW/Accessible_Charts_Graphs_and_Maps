# Accessible Charts, Graphs and Maps

Practical guidance from **Double FW Ltd** for designing, building and testing charts, graphs, maps and other complex graphics so that people can understand, explore and use them independently.

The repository is both a human-readable design resource and a source of context for AI-assisted work. It helps teams preserve the information, choices and opportunities for discovery a visual presentation offers—across complementary visual, textual, structured and interactive presentations.

## Purpose

A graphic can make a trend, relationship, exception or route easy to see. An accessible experience should make those insights and actions available through other ways of working, too. The aim is comparable independence, accuracy, effort, timeliness and confidence—not necessarily identical presentation or interaction.

Use this guidance to:

- Define what people need to understand, decide or accomplish before choosing a chart or map.
- Design equivalent, complementary presentations and keep their content and state consistent.
- Plan implementation, accessibility testing and user evaluation around meaningful tasks.
- Help developers, designers, researchers, data specialists and QA teams collaborate around observable outcomes.
- Give AI coding assistants and agents a source-grounded framework for planning, implementation, review and test generation, with human oversight.

It applies to static and interactive charts, statistical graphs, geographical maps, indoor wayfinding, dashboards, process diagrams, networks, journey maps, service blueprints, animations and other dynamic or complex graphics. A sentence, list or table may be a better solution than a graphic when it answers the question more directly.

## Repository contents and reading order

The main resource is [Inclusive Design of Charts, Graphs, Maps and Dynamic Complex Graphics](Inclusive_Design_Charts_Maps_and_Complex_Graphics.md). It is a practical design and testing guide: define outcomes and barriers, design comparable presentations, implement and maintain the experience, then test and evaluate it.

The guide includes design steps, patterns for charts and maps, interaction and implementation considerations, a test catalogue, worked examples, an evidence-record template and a release checklist. The repository currently contains this guide and its MIT license; it does not include separate chart-specific and map-specific best-practice documents.

## Knowledge and practices the guide supports

The guide brings together practical knowledge about:

- **Tasks and outcomes:** retrieval, comparison, interpretation, exploration, decision and action; task briefs and testable success criteria.
- **Functional needs and barriers:** vision, hearing, speech, physical interaction, cognition, relevant combinations, motion sensitivity and privacy—without inferring ability from diagnosis.
- **Information parity:** meaningful summaries, exact values, relationships, caveats, uncertainty and actions across visual and structured presentations.
- **Charts and data:** representation choice, visual encoding, colour-independent cues, scales, missing values, uncertainty, labels, structured data and export scope.
- **Maps and spatial information:** location search, markers, clusters, routes, indoor wayfinding, boundaries, geography, freshness and uncertainty.
- **Complex graphics:** networks, hierarchies, process diagrams, journey maps, collaborative canvases and scientific or dynamic visualisations.
- **Interaction and implementation:** semantic controls, keyboard and pointer alternatives, focus, zoom and reflow, display preferences, dynamic updates, motion, failure states and recovery.
- **Evidence and maintenance:** automated and manual checks, assistive-technology testing, evaluation with disabled people, outcome measures, prioritisation and retesting.

The guide distinguishes technical checks from evidence that people can successfully complete meaningful tasks. Automated tools can identify some defects and regressions; they cannot establish that an explanation preserves an insight, route directions are useful, or an alternative supports independent exploration.

## A practical process

Use the guide as an iterative lifecycle, adapting the depth to the task and risk:

1. **Define the outcome.** Record audience and context, the questions and decisions the graphic supports, data meaning and what successful independent completion looks like.
2. **Identify barriers.** Consider perception, understanding and interaction needs, including realistic combinations and privacy. Turn likely barriers into hypotheses to test.
3. **Plan presentations together.** For every essential task, specify how it works visually and through structured information or alternative controls. Record parity for facts, relationships, actions and state.
4. **Choose and design the representation.** Use the simplest useful form; preserve statistical meaning, uncertainty, relationships and the ability to explore beyond a preset summary when exploration matters.
5. **Implement and synchronise.** Keep descriptions, graphic, controls, structured details and exports connected to the same data, filters, selections and permissions. Include loading, empty, stale, failure and recovery states.
6. **Test and evaluate.** Combine automated checks, manual inspection, assistive-technology testing and realistic task evaluation with disabled people. Compare expected outcomes, not just whether a control exists.
7. **Record, improve and maintain.** Link findings to tasks, states, environments and evidence. Prioritise barriers by their impact on outcomes; retest after changes to data, content, libraries or interaction.

Treat untested behaviour as unknown, not as passed. Involve disabled people in understanding needs and shaping designs as well as evaluating implemented experiences.

## Outcomes and deliverables

Applying the guidance can produce practical artifacts for a project, such as:

- An outcome brief and essential-task list.
- A task-by-functional-condition coverage matrix and barrier hypotheses.
- An outcome-parity matrix and paired presentation prototypes.
- An annotated design and interaction/state specification.
- A purposeful test dataset, expected answers and reproducible test cases.
- Evidence records covering technical results and observed task outcomes.
- A prioritised remediation plan, release decision and maintenance/retest triggers.

Evaluate meaningful outcomes separately, including independent completion, accuracy, information parity, effort, time, confidence, recovery, comfort and test coverage. Do not compress results into a single accessibility percentage that could hide exclusion from an essential task.

## Using this repository to develop AI skills and agentic processes

This guidance can serve as domain knowledge for AI skills, system instructions, retrieval-augmented generation (RAG), coding agents and human-led design or QA workflows. The guide is reference material—not a prebuilt executable agent, formal skill package or guarantee of accessible output. Provide the relevant sections to the model for the task at hand, along with project-specific context.

### Suggested agent workflow

1. **Gather context:** request the graphic or map purpose, intended users and environment, data schema and provenance, constraints, existing controls, supported technologies and acceptance criteria. Flag missing information instead of inventing it.
2. **Ground recommendations:** find the relevant guide sections and map each proposed requirement to the source guidance. Separate guide recommendations, applicable standards requirements, project decisions and assumptions; do not present them as interchangeable.
3. **Plan before coding:** produce an outcome brief, task list, barrier hypotheses and parity matrix. Ask for human decisions where data meaning, risk, policy or user research is unresolved.
4. **Implement coherently:** update the visual view and its summary, structured detail, controls and relevant exports from shared data and state. Preserve values, relationships, uncertainty, permissions and recovery paths.
5. **Verify with evidence:** create tests for expected values, state synchronization, keyboard operation, names and states, focus, zoom/reflow, dynamic and failure states. Distinguish tests actually run from tests merely proposed.
6. **Report limits and hand off:** summarize changed behavior, evidence, remaining risks, unknowns and follow-up tasks. Recommend review with assistive technologies and disabled users where appropriate.

### Example task for an AI coding agent

> Build a dashboard chart comparing monthly waiting times for three services. First identify the essential user tasks and any missing assumptions. Provide a concise visible summary, exact structured values and keyboard-operable filters. Keep the chart, summary, table and export synchronized; preserve missing values, units and uncertainty. Add tests for expected values, filters, keyboard use and empty/error states. Cite the applicable sections of this repository, report which tests you ran, and list what still needs human or user evaluation.

### Guardrails for AI-assisted work

- Ground decisions in the actual dataset and repository guidance; do not fabricate findings, values, user needs or test evidence.
- Treat a text summary or data table as a complement, not automatically a replacement for visual relationships or user-led exploration.
- Do not claim conformance or accessibility from generated code, a passing automated scan or this guide alone.
- Do not substitute simulation for disabled people's participation or infer diagnoses from behavior.
- Keep human review for consequential interpretation, data accuracy, route and safety information, privacy, standards applicability and release decisions.
- Make uncertainty explicit. Record untested combinations, unsupported technologies and third-party limitations as open questions.

Teams building formal AI skills can turn the workflow into reusable task instructions and checklists, while keeping source references, project-specific acceptance criteria and human approval points visible. Generated tests and code remain hypotheses until executed and reviewed in the actual experience.

## Complementary public Double-FW repositories

These public repositories cover adjacent parts of an inclusive delivery workflow and can be used alongside this guide:

- [The Little Book of Accessibility](https://github.com/Double-FW/The-Little-Book-of-Accessibility) — broader accessibility and inclusive-design knowledge, structured with AI agents, RAG and skills in mind.
- [QA Accessibility Testing](https://github.com/Double-FW/QA_Accessibility_Testing) — manual and automated accessibility QA, testing and AI-assisted test management.
- [Accessible Chatbots](https://github.com/Double-FW/Accessible-Chatbots) — prompt templates and RAG guidance for inclusive chatbot experiences.
- [Cognitive UX Design](https://github.com/Double-FW/Cognitive-UX-Design) — guidance and tools for understandable, controllable and inclusive experiences, including source-aware agent workflows.
- [Task Analysis for Comparative Accessibility Evaluation of Internal Systems](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems) — task analysis to support comparative evaluation of user outcomes.
- [Accessible Digital and Printed Documents](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents) — accessible document design across digital, print and hybrid formats, useful when graphics are also published in documents.
- [Global Accessibility Regulatory Requirements](https://github.com/Double-FW/Global_Accessiblity_Regulatory_Requirements) — regulatory routing and knowledge; use it for jurisdiction-specific context and do not treat this practical guide as legal advice.

See the [Double-FW organisation](https://github.com/Double-FW) for other publicly available resources. Repository scope and content can change; consult each repository directly for its current guidance.

## Contributing

Suggestions, corrections and practical examples are welcome through this repository's contribution channels. Describe the affected guidance, the barrier or ambiguity, the proposed change and any evidence or context that supports it. Distinguish standards requirements from recommendations, design heuristics and findings that depend on context.

## About

Developed by **Double FW Ltd** to support accessible, inclusive design and delivery across human and AI-assisted work. The repository is available under the [MIT License](LICENSE).
