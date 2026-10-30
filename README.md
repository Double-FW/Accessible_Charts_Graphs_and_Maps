# Accessible Charts, Graphs and Maps

Practical guidance from **Double FW Ltd** for designing, building and testing charts, graphs, maps and complex graphics that people can understand, explore and use independently.

The aim is to preserve the information, choices and opportunities for discovery that a visual presentation provides. Users should be able to retrieve values, recognise patterns, investigate relationships and act on findings through presentations and interactions that meet their needs.

## Who this guidance is for

- Designers and researchers planning inclusive visualisations and user journeys.
- Developers implementing charts, maps, dashboards and accessible alternatives.
- Content authors and data specialists explaining findings, context and uncertainty.
- QA and accessibility practitioners evaluating technical behaviour and task completion.
- AI coding and review agents using the guidance as context for implementation and remediation.

It applies to public services, customer experiences and internal systems.

## Scope

Use the guidance for static and interactive charts, statistical graphs, geographical maps, indoor wayfinding, dashboards, process diagrams, networks, journey maps, service blueprints and dynamic complex graphics.

The material combines WCAG 2.2 Level A and AA considerations with broader inclusive design practices. Enhanced and Level AAA practices should remain distinguishable from the A/AA baseline. Following the guidance alone does not establish complete standards conformance or legal compliance.

## Reading order

The guidance is organised around three complementary resources:

| Resource | Purpose |
| --- | --- |
| **Inclusive Design of Charts, Graphs, Maps and Dynamic Complex Graphics** | An outcome-led design and evaluation approach: define tasks, identify barriers, plan comparable presentations and evaluate independent use. |
| **Charts and Graphs Accessibility Best Practices** | Implementation guidance for chart explanations, structured data, visual encodings, controls, dynamic updates and accessible exports. |
| **Maps Accessibility Best Practices** | Guidance for map alternatives, locations, routes, markers, clusters, search, indoor navigation, embedded maps and testing. |

Start with the inclusive design guide to establish the intended outcomes, then apply the chart or map guidance to the implementation. Use both for experiences that combine geographical and statistical information.

## Core principles

1. **Start with the user's question.** Define what someone needs to understand, decide or accomplish before selecting a visual format or library.
2. **Preserve equivalent purpose.** Make essential information and actions available without requiring visual inspection or operation of the graphic.
3. **Provide complementary presentations.** Combine concise identification, context, an overview, structured detail and accessible exploration according to the task.
4. **Keep presentations synchronised.** Graphics, descriptions, tables, lists, directions and exports must reflect the same data, filters, selections and permissions.
5. **Avoid reliance on one sensory or input method.** Support alternatives to colour, position, hover, sound, dragging, pinching and precise pointer movement.
6. **Reduce avoidable effort.** A large table is insufficient if users must inspect thousands of rows to discover a relationship that the graphic makes immediately apparent.
7. **Preserve meaning and uncertainty.** Explain units, scales, missing values, sources, dates, assumptions and limitations consistently across presentations.
8. **Test meaningful outcomes.** Evaluate what people can understand and do, alongside technical checks.

Comparable experiences need not look or behave identically. They should support comparable independence, accuracy, effort, timeliness and confidence.

## Getting started

1. Write a short brief identifying the audience, context, essential questions, decisions and actions.
2. Identify barriers across vision, hearing, speech, physical interaction and cognition, including combinations of needs, motion sensitivity and privacy.
3. For each essential task, specify how it will work through the visual presentation and through structured content or alternative controls.
4. Choose the simplest useful representation. A sentence, list or table may answer the question more directly than a graphic.
5. Implement accessible content and interaction together, using native HTML controls where practical.
6. Verify technical behaviour, data consistency and task completion; resolve known barriers before evaluative user testing.
7. Evaluate realistic tasks with disabled people and use the findings to improve comprehension, efficiency and confidence.

Involve disabled people in understanding needs and shaping designs as well as evaluating the implemented experience.

## What to test

Combine automated checks, manual inspection, assistive technology testing and research with disabled users.

- **Information:** equivalent findings, values, relationships, caveats and actions across presentations.
- **Keyboard and focus:** logical navigation, visible focus, usable controls and no traps.
- **Assistive technology:** useful names, roles and states; navigable explanations; proportionate status announcements.
- **Visual presentation:** contrast, non-colour distinctions, zoom, text spacing, narrow viewports and forced colours.
- **Pointer and touch:** alternatives to dragging and complex gestures, usable targets and unobstructed page scrolling.
- **State and integration:** synchronised filters and selections; loading, empty, error and provider-failure states.
- **Real tasks:** independent retrieval, comparison, interpretation, exploration, decision-making and action.

Record the environment, expected outcome, observed result and any remaining limitation. Treat untested behaviour as unknown.

Automation can detect some structural defects and regressions. It cannot establish whether a description preserves meaning, directions are accurate or an alternative supports comparable exploration.

## Using the guidance with AI

Supply the relevant guidance alongside the task, dataset, interface constraints and acceptance criteria. Ask the agent to identify applicable requirements, implement complementary presentations and report the checks performed and remaining uncertainties.

For example:

> Build a chart comparing monthly service waiting times. Provide a visible summary, structured values and keyboard-operable filters. Keep all presentations synchronised, preserve missing values and uncertainty, and explain which outcomes require manual or user testing.

Review generated code and descriptions against the actual data and rendered experience. An agent's assertion of accessibility is not evidence that the essential tasks work.

## Contributing

Suggestions, corrections and practical examples can be proposed through this repository's available contribution channels. Describe the affected guidance, the barrier or ambiguity, the proposed change and supporting evidence. For implementation examples, include relevant browser and assistive technology details and reproducible steps.

Distinguish standards requirements from recommendations, design heuristics and findings that depend on a particular context.

## About

Developed by **Double FW Ltd** to support accessibility and inclusive design across human and AI-assisted delivery.

Explore more resources through the [Double FW GitHub organisation](https://github.com/Double-FW).
