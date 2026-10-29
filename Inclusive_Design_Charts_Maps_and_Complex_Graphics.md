---
title: Inclusive Design of Charts, Graphs, Maps and Dynamic Complex Graphics
version: 1.0
date: 2026-10-29
language: en-GB
document_type: Practical design and testing guide
---

# Inclusive Design of Charts, Graphs, Maps and Dynamic Complex Graphics

## Purpose and use

Design graphics so that people can understand the information, investigate the questions that matter to them and act on the results using their preferred ways of perceiving and interacting. Aim for comparable independence, accuracy, effort, timeliness and confidence across experiences.

Comparable does not mean identical. A person may compare values through a table, explore connections through a relationship browser or follow a route through ordered instructions. These experiences succeed when they preserve the relevant information, choices and opportunities for discovery without imposing avoidable extra work.

Use this guide for static charts, statistical graphs, geographical maps, journey maps, service blueprints, process diagrams, networks, dashboards, animated explanations and interactive visualisations. Apply it to internal tools and authoring environments as well as published content.

Follow the numbered design steps, then apply the test catalogue and release checklist. Treat instructions as design requirements for this guide unless explicitly described as an optional enhancement. Technical minimums are distinguished from stronger inclusive practices. Meeting this guide alone does not establish legal compliance or complete standards conformance.

## Core principles

1. **Start with the outcome.** Define what people need to understand or accomplish before choosing a graphic.
2. **Preserve the information advantage.** If the visual makes a trend, relationship, exception or route easy to discover, make that insight available through other presentations too.
3. **Offer complementary ways to work.** Combine overview, explanation, structured detail and accessible interaction according to the task.
4. **Keep every presentation consistent.** Use the same data, definitions, permissions and interaction state for graphics, descriptions, tables and exports.
5. **Make choices available to everyone.** Do not require disability disclosure, a separate account or assistance to use an alternative presentation.
6. **Reduce avoidable effort.** Reachability is insufficient if a user must inspect thousands of points to answer a simple question.
7. **Keep users in control.** Support pausing, revisiting, undoing, changing presentation and returning to a known state.
8. **Design for combinations of needs.** Audio is not a complete alternative for someone who cannot use vision or hearing; voice input is not a complete alternative to manual interaction.
9. **Protect meaning and uncertainty.** Accessible presentation must not simplify away caveats, exclusions, missing data or conditions affecting decisions.
10. **Measure actual outcomes.** Combine technical inspection with evidence from people completing meaningful tasks.

## Step 1 — Define the task and informational outcome

### 1.1 Write an outcome brief

Before drawing anything, record:

- The audience, context of use and likely devices.
- The question the graphic should help answer.
- The decisions or actions that follow.
- Whether users need a headline finding, exact values, relationships, exploration, editing or a combination.
- The meaning of categories, units, dates, geography and filters.
- The consequences of misunderstanding or using outdated information.
- What counts as successful independent completion.

For example: “A user can compare waiting times for three services, identify which meets their chosen threshold, understand the uncertainty and open the relevant booking route.” This is testable. “Users can access the chart” is not sufficiently specific.

### 1.2 Separate retrieval, understanding and action

Test these as different outcomes:

| Outcome | Example question | Evidence needed |
|---|---|---|
| Retrieve | What was the value in June? | Correct value, unit and period |
| Compare | Which service has the shortest wait? | Correct comparison using the same conditions |
| Interpret | Is the increase sustained or temporary? | Reasoning consistent with the data and uncertainty |
| Explore | Which neighbouring areas show a similar pattern? | Ability to investigate relationships, not just receive a preset conclusion |
| Decide | Which route meets my requirements? | Relevant constraints and trade-offs are available |
| Act | Can I select, save, book, annotate or share it? | Equivalent action completes successfully |

Do not replace exploratory access with a single editorial summary. Preserve the user's ability to ask questions that the author did not anticipate.

### 1.3 Decide whether a graphic is necessary

Use a sentence, list or table when it answers the question more directly. Retain a graphic when it adds useful pattern recognition, spatial understanding or explanatory value. A visually impressive display that increases interpretation effort is a poor choice.

**Step output:** a short outcome brief and a list of essential tasks, each with expected answers or acceptable reasoning.

## Step 2 — Map functional needs and barriers

Organise measurement around what people need to perceive, operate and understand. Do not infer functional ability from a diagnosis or require participants to disclose a medical history.

Use the following categories to align with the functional performance approach reflected in Annex I, Section VII of the European Accessibility Act. Multiple impairments is an additional cross-cutting evaluation lens, not a separately named criterion in that section. Include photosensitivity and privacy so that the six broad reporting groups do not omit these concerns. This mapping supports design evaluation; it does not replace applicable legal requirements or establish that a product falls within the Act's scope.

| Reporting group | Functional conditions to evaluate | Example barriers | Required design response |
|---|---|---|---|
| Vision | Without vision; limited vision; without colour perception | Pixel-only data, tiny labels, colour-only categories, lost context when magnified | Structured meaning, scalable presentation, non-colour distinctions and accessible exploration |
| Hearing | Without hearing; limited hearing | Audio-only alerts, sonification-only values, unclear narration | Text equivalents, persistent visual status and user-controlled audio |
| Speech | Without vocal capability | Voice-only queries, spoken confirmation or sound-triggered controls | Keyboard, touch, switch-compatible or other non-vocal operation |
| Physical interaction | Limited manipulation, strength or reach | Drag-only selection, precise targets, simultaneous controls, excessive repeated input | Sequential operation, single-pointer alternatives, generous targets and efficient navigation |
| Cognitive accessibility | Limited cognition, including memory, attention, language and interpretation demands | Unexplained scales, clutter, unstable layouts, hidden state and time pressure | Clear structure, progressive detail, persistent context and recoverable actions |
| Multiple impairments | Relevant combinations across the groups | Audio substituted for vision when neither channel is usable; tiny buttons offered instead of speech | Compatible combinations of alternatives, including structured text usable with braille |
| Cross-cutting: photosensitivity and motion | Exposure to flashing or movement; motion sensitivity is assessed in addition to the explicit photosensitivity criterion | Pulsing warnings, rapid transitions, automatic camera movement | Safe visual behaviour, reduced motion and static or stepwise exploration |
| Cross-cutting: privacy | Private use of accessibility features | Compulsory disclosure, spoken sensitive data, inferred disability profiling | Equal access without disclosure, private output options and restrained data collection |

### 2.1 Create a barrier hypothesis for each task

Use this form: “When completing [task] under [functional condition], [design feature] may prevent [outcome]. We will provide [response] and test [observable result].”

Example: “When comparing routes without vision, a list of destinations does not reveal transfers. We will provide ordered route segments and a connection query, then test whether users can identify the same transfer choices.”

### 2.2 Include realistic combinations

Test combinations such as magnification plus keyboard use; screen reader plus reduced motion; speech input plus limited reach; and braille access without reliance on sound. Avoid assuming that one alternative suits every person within a category.

**Step output:** a task-by-functional-condition coverage matrix. Mark untested cells as unknown, not passed. Explain any not-applicable decisions.

## Step 3 — Design comparable presentations together

### 3.1 Build an outcome parity matrix

For each essential task, specify how it works in each presentation before implementation.

| Task | Visual presentation | Structured presentation | Parity check |
|---|---|---|---|
| Identify a trend | Labelled time series | Summary plus chronological values | Same direction, turning points and caveats |
| Compare selected items | Highlighted marks | Comparison table or selected-items list | Same items, units and differences |
| Explore a network | Connected nodes | Searchable nodes and labelled relationships | Same connections, direction and accessible actions |
| Find a service | Markers and spatial filters | Searchable results with attributes | Same eligible results and detail links |
| Change an analysis | Brushing or direct manipulation | Range fields, filters and selection controls | Same query and resulting population |
| Follow a process | Branching diagram | Ordered steps with explicit decision branches | Same conditions, exceptions and destinations |

Do not use one generic “accessible version” column without explaining the actual interaction. Name the interface that will deliver the outcome.

### 3.2 Use layers of information

Provide, in a predictable order:

1. **Identification:** a meaningful heading and a concise identification of the graphic.
2. **Context:** subject, population, geography, period, units and active scope.
3. **Overview:** the main pattern or purpose, including important qualifications.
4. **Exploration:** filters, search, comparisons, relationship queries and detail controls.
5. **Structured detail:** values, locations, steps or connections in navigable text.
6. **Interpretation notes:** definitions, calculation methods, data provenance, freshness and limitations.

Keep essential qualifications visible. Put lengthy supporting detail behind clearly labelled disclosures where useful. Progressive disclosure should reduce initial complexity without hiding the existence of important information.

### 3.3 Avoid alternative-format penalties

Place “View data”, “Read directions” or “Explore connections” beside the graphic, with meaningful labels. Preserve selections and filters when switching views. Do not require a download, specialist software or a support request for ordinary tasks that other users can complete on the page.

A summary does not replace exact data when exact comparison matters. A table does not automatically convey topology, geographical relationships or the overall pattern. Select the combination that preserves the purpose.

**Step output:** paired prototypes and a parity matrix covering both information and actions.

## Step 4 — Select and simplify the representation

### 4.1 Match the form to the question

| Representation | Use it for | Design instructions |
|---|---|---|
| Bar or column chart | Comparing quantities | Use a zero baseline for length comparisons. Prefer horizontal bars for long labels. If a truncated range is necessary, choose a form that does not imply full lengths from zero and explain it. |
| Line chart | Change over ordered time | Distinguish lines beyond colour, explain gaps and label turning points when useful. Do not imply observations where data are missing. |
| Pie or doughnut | A small number of parts of one whole | Label categories and values. Choose bars when differences are small or precise comparison matters. |
| Stacked chart | Composition and totals | Explain absolute versus percentage values. Provide a common-baseline alternative for comparing internal segments. |
| Scatterplot or bubble plot | Relationships and distributions | Explain axes and encodings, expose relevant points and describe clusters without implying causation. Scale bubble area consistently with quantity. |
| Histogram, box plot or density plot | Distribution and variability | Explain bins, quartiles, median and outliers in ordinary language; expose relevant summaries and interval values. |
| Heat map | Patterns across two dimensions | Explain thresholds and missing cells. Provide cell values and a way to locate extremes without identifying colours. |
| Small multiples | Comparing repeated patterns | Use consistent scales for direct comparison and a meaningful reading order. Clearly disclose any unavoidable scale differences. |
| Choropleth or thematic map | Geographical distribution | Choose meaningful rates or quantities, explain region sizes and classification boundaries, and expose regional values. |
| Network, flow or Sankey diagram | Connections, dependencies or movement | Expose named relationships, direction and quantities; support connection and path queries. |
| Journey map or service blueprint | Sequence, roles and hand-offs | Preserve stages, lane meanings, responsibilities, evidence and dependencies in a structured reading order. |

### 4.2 Reduce clutter without removing meaning

Remove decorative depth, shadows, background textures and unnecessary borders. Use only enough gridlines to support reading. Keep numerical labels aligned and format numbers consistently with the chosen locale. Prefer horizontal labels; transpose, wrap or restructure the chart before rotating text.

Use direct labels where they reduce legend matching. When a legend is necessary, keep its order consistent with the display and identify items with text and additional non-colour cues.

Treat limits on numbers of series, categories or gridlines as design heuristics, not universal accessibility thresholds. Split a dense display into meaningful sections, small multiples or filtered views. Preserve access to the complete authorised dataset.

### 4.3 Apply redundant encoding carefully

Use labels, outlines, line styles or point shapes to reinforce colour. Patterns can help when labels alone are insufficient, but dense hatching may obscure small areas and increase visual noise. Start with direct labels and simple distinctions; introduce sparse patterns only where tests show a benefit.

Do not remove a useful redundant cue merely to make the graphic look cleaner. Conversely, do not add every possible cue to every mark.

### 4.4 Preserve statistical meaning

Explain denominators, baselines, aggregation, normalisation and non-linear scales. Distinguish zero, missing, unavailable, suppressed and not applicable. Describe estimates and uncertainty in both visual and structured forms. Do not portray an uncertain ranking as definitive or smooth a time series in a way that conceals variation.

Keep rounding consistent across views. Display the uncertainty relevant to the decision; do not bury it in a footnote when it changes the conclusion.

**Step output:** an annotated design showing what each visual encoding means and how that meaning survives in other presentations.

## Step 5 — Write useful explanations and structured detail

### 5.1 Write concise identification

For a static informative image, provide a short alternative that communicates its purpose in context. For a complex image, identify it and direct users to the associated detailed content. Do not insert the entire dataset into its accessible name.

Example: “Waiting times for three services over twelve months. Summary and monthly values follow.”

Mention the chart type when it helps interpretation. Avoid filenames, “image of” boilerplate and descriptions of decoration. Use an empty image alternative only for genuinely decorative or completely redundant static imagery; do not hide an interactive interface to avoid fixing it.

### 5.2 Write a navigable explanation

Describe the main pattern, important contrasts, exceptions and uncertainty. Explain visual composition where it carries meaning, such as hierarchy, direction, adjacency or a shared baseline. Use headings, lists and tables rather than one long paragraph.

Separate observation from interpretation. “Requests increased from 40 to 60” is an observation; an explanation for the increase requires supporting evidence. Review automatically generated summaries against the actual filtered data, including empty and unusual states.

Keep long explanations available in ordinary page content. A short programmatic description can assist orientation, but it does not replace navigable structured content.

### 5.3 Provide data that people can use

Use semantic tables with a caption and correctly associated row and column headers. Include units, category names, time periods and missing-value meanings. Prefer simple tables over unnecessarily complex merged headers. Provide accessible sorting, filtering, pagination and comparison when the dataset is large.

Do not force sequential reading of thousands of rows. Let users search, narrow a range, select items and compare them. State whether results represent all data, the active filters or only the current map extent. Keep any full-data export consistent with its stated scope and privacy restrictions.

### 5.4 Describe relationships explicitly

Use statements such as “Team A approves requests from Team B”, “Route 3 connects Central Station to the hospital via the library” and “Area North shares a boundary with Area East”. Include direction, conditions and exceptions.

A list of nodes is not a network description. Coordinates alone are not useful route instructions. Raw values alone may not reveal a statistically important trend.

**Step output:** final title, context, summary, structured detail and interpretation notes checked against the same dataset.

## Step 6 — Make presentation adaptable

### 6.1 Design readable text

Choose familiar, clear letterforms with distinguishable characters and numerals. Test actual labels at their final displayed size. Do not assume that all serif fonts are inaccessible, that all sans-serif fonts are accessible or that a specialist font benefits every reader.

Keep prose in ordinary text, use clear headings and avoid long all-capital or italic passages. Use relative sizing, allow wrapping and support user font changes. Avoid fully justified explanatory paragraphs. Select a comfortable line length rather than stretching descriptions across a wide dashboard.

Allow text to grow without clipping labels, buttons or panels. Where text is embedded in a graphic, preserve its meaning in adaptable page content and test whether the enlarged graphic remains legible.

### 6.2 Apply contrast to the information that matters

- Normal-size text: at least 4.5:1 contrast against its background.
- Large-scale text: at least 3:1; the threshold is at least 18 point regular or 14 point bold, approximately 24 or 18.7 CSS pixels respectively.
- Required graphical information and visual identification of controls and states: generally at least 3:1 against relevant adjacent colours, subject to the applicable criterion's exceptions.

Assess actual rendered labels, lines, boundaries and states, including overlap. Decorative gridlines and photographic map tiles do not all need one blanket contrast ratio. Identify the authored information needed for the task and ensure it remains distinguishable. A separate table does not excuse colour-only distinctions in the visual presentation.

### 6.3 Support themes and display overrides

Use semantic styling for text, surfaces, axes, series, focus, selected states and warnings. Check each authored light and dark theme independently. Dark mode is a preference, not an accessibility guarantee.

If providing theme selection, offer clearly labelled system, light and dark options. Expose the current choice, allow keyboard operation and remember an explicit preference where appropriate. In system mode, respond to system changes. Do not require signing in to change presentation.

Test forced colours, increased contrast, colour inversion and reader-style presentation where relevant. Preserve required outlines and state distinctions if backgrounds or shadows disappear. Use system colours and `currentColor` where appropriate. Avoid disabling forced-colour adjustments across the entire interface.

Let users apply their own colour preferences. Do not silently reduce the contrast of the default or authored themes on the assumption that less contrast helps everyone.

### 6.4 Separate page magnification from graphic zoom

Page zoom enlarges controls and text; map or chart zoom changes the data viewport. Support both. Do not disable browser zoom.

Test text resizing to 200%, page zoom to 400% and a viewport equivalent to 320 CSS pixels wide. Reflow headings, filters, descriptions, status and details. Confine necessary two-dimensional panning to the graphic or table; the exception for meaningful two-dimensional layouts is not an exemption for the whole page.

Keep focus visible in scrollable areas. Do not shrink labels until unreadable to avoid scrolling. Support portrait and landscape unless a particular orientation is essential.

**Step output:** tested layouts and colour states, including enlarged text, narrow screens and user overrides.

## Step 7 — Make interaction efficient and predictable

### 7.1 Prefer ordinary controls

Use native buttons, checkboxes, radio groups, select controls and labelled fields for search, filters, series visibility, layers and ranges. Expose names, roles, values and states. Include visible control wording in the accessible name so that speech users can address it.

Reserve interactive semantics for actual actions. Static values do not each need a button or a Tab stop.

### 7.2 Design the keyboard model

1. Provide a logical sequence through the main controls and results.
2. Keep standard button and form behaviour.
3. If a dense component needs internal navigation, define a tested model with a clear entry, movement, selection and exit mechanism.
4. Limit arrow-key handling to the relevant focused component; preserve ordinary page navigation elsewhere.
5. Avoid global single-character shortcuts unless users can disable or remap them, or they operate only when the relevant component has focus.
6. Preserve the focused item's identity after updates. If it disappears, move focus to a predictable nearby control and explain the result where needed.

Do not place hundreds of markers in the page's sequential Tab order. Offer search, grouped navigation or a structured results view. Do not assume that adding `role="application"` makes a complex graphic accessible; prefer document semantics and native controls.

### 7.3 Replace gesture dependencies

| Direct manipulation | Provide an alternative |
|---|---|
| Drag to pan | Direction controls, location search or named region selection |
| Pinch to zoom | Zoom buttons and reset |
| Brush a chart range | Labelled start/end fields and an apply action |
| Lasso points | Attribute filters, checkbox selection or a selection query |
| Drag a node | Select the node and set its position or relationship through controls |
| Drag to reorder | Move up/down or choose position |
| Scrub a timeline | Time field, previous/next step and a labelled slider where suitable |
| Rotate a model | Named view controls and reset orientation |

Keyboard support and single-pointer alternatives are separate requirements. A keyboard-only workaround does not by itself solve a drag-only touch interaction.

Use at least 24 by 24 CSS pixel pointer targets or meet a defined minimum-target exception. Aim for at least 44 by 44 CSS pixels for primary controls as a stronger inclusive practice. Keep enlarged hit areas unambiguous and separated. Allow cancellation, normally by activating on release rather than initial pointer-down.

### 7.4 Make details persistent when needed

Expose important values through labels, structured content or a detail panel, not hover alone. For custom hover/focus content, support dismissal without moving focus when required, allow the pointer to move onto it and keep it available long enough to read. Provide keyboard and touch access.

Use a disclosure or panel for interactive or substantial content. A tooltip should not contain a set of controls that users cannot reach. Keep non-modal panels non-modal. If a genuine modal is necessary, name it, manage focus within it, provide a close action and restore focus on closing.

Do not move focus just because a small preview appears. For an explicitly opened substantial panel, move it only when that supports the user's next task.

### 7.5 Support recovery

Provide clear applied-filter summaries, remove-filter actions, reset and undo where appropriate. Explain errors without clearing entered values. Warn before discarding a substantial selection. Provide an accessible alternative to timed or simultaneous key combinations.

**Step output:** an interaction specification covering keyboard, pointer, touch, speech, focus, error and recovery behaviour.

## Step 8 — Keep dynamic graphics understandable

### 8.1 Use one shared state model

Drive the graphic, summary, result count, table, detail panel and export from the same applied query and dataset version. Include filters, units, date range, selections, map extent and permissions where relevant.

Handle loading, empty, partial, failed, stale and disconnected states explicitly. Label retained old data as stale rather than presenting it as a successful refresh. Cancel or ignore out-of-order responses so that an earlier request cannot overwrite a later selection.

### 8.2 Announce meaningful results

Keep important results persistent on the page. Use a pre-existing status region for concise messages such as “12 locations match these filters”. Do not announce every point, tile, animation frame or collaborator movement. Avoid announcing the same update separately from the map and table.

Status announcements supplement content; they are not the only place to find the new result. Preserve focus during refreshes. Reserve urgent interruption for genuinely urgent information.

### 8.3 Give control over live data

Provide pause or manual refresh when automatic changes interfere with reading or selection. Make clear whether pause freezes the displayed snapshot, stops incoming data or pauses animation only. Keep a timestamp and a “new data available” indication where useful.

When resuming, preserve the user's selected item where possible and explain meaningful changes. Do not silently reorder a row under the pointer or replace the item being read. For decision-critical monitoring, distinguish a frozen snapshot from live status prominently in all presentations.

### 8.4 Design motion as optional explanation

Respect reduced-motion settings in CSS and JavaScript, including canvas and map-library animations. Replace non-essential movement with immediate updates, static before/after views or user-controlled steps. Do not merely slow a long camera sweep; slower motion can still cause discomfort.

For automatically starting movement, blinking or scrolling that lasts more than five seconds and runs alongside other content, provide pause, stop or hide unless essential. Automatically updating information has its own control requirement; do not apply the five-second threshold to every type of update.

Avoid flashing. Where flashing is unavoidable, assess the applicable flash thresholds with a suitable analysis tool. A warning, opt-in or reduced-motion preference does not make unsafe flashing acceptable. Do not ask participants to test suspected hazardous content.

### 8.5 Preserve temporal understanding

For animated explanations and simulations, expose the current time or step, variables, units and changes. Offer previous/next, replay, pause and reset. Provide a textual sequence or comparable query of state over time so users can understand the causal or temporal story without watching motion.

For coordinated dashboards, explain which chart controls the others and show active selections globally. Give users a clear way to undo cross-filtering.

**Step output:** a state-transition specification and test fixtures for successful, empty, stale, failed and rapidly changing data.

## Step 9 — Apply the method to maps and complex diagrams

### 9.1 Location and service maps

Provide a searchable list containing the same eligible locations and actions as the map. Include names, addresses, relevant attributes and distances with their calculation basis. State whether results are constrained to the visible map area. Prefer an explicit “Search this area” action when continuous viewport-based updates would be disruptive.

Label markers uniquely. Give clusters meaningful names and counts, and let users inspect their contents without precision zooming. Keep filters and selection consistent between list and map.

Request geolocation after an explicit action and provide manual address or place entry. Handle denial, ambiguity and inaccurate location. Keep ordinary page scrolling possible when an embedded map captures gestures.

### 9.2 Routes and indoor wayfinding

Provide ordered directions including decision points, distances, landmarks and relevant conditions. Combine street or place names with direction; do not rely exclusively on left/right, compass points or visual landmarks.

Expose route features such as steps, gradients, surfaces, widths, crossings, lifts, doors and entrances when relevant and known. Distinguish verified, reported, inferred and unknown information. “Unknown” must not become “accessible” or “not accessible” through a default value.

Allow users to express functional requirements such as avoiding steps or limiting walking distance. Explain trade-offs: a step-free route may be longer or have a steeper gradient. Avoid implying that one “accessible route” meets every need.

For buildings, include floor, entrance, lift connections and destination names. Update directions when the floor or route changes. Expose closures and freshness, provide a correction route and avoid presenting unverified live positioning as certainty.

### 9.3 Geographical analysis and boundaries

Provide region values and meaningful spatial queries: within, adjacent to, connected to, upstream/downstream or within a chosen distance. Define boundary inclusion rules where they affect eligibility. Explain whether classifications represent counts, rates or another measure.

Keep legends, thresholds and active layers synchronised. Preserve relevant spatial understanding rather than reducing a thematic map to a list of colour names. Where free spatial exploration is central, prototype a structured spatial browser or additional tactile/audio presentation with users.

### 9.4 Networks, process maps and hierarchies

Give nodes stable names and identifiers. Expose incoming and outgoing connections, relationship labels, direction, weight and conditions. Provide parent/child navigation for hierarchies and identify cycles or multiple parents where present.

Support questions such as “What depends on this?”, “What happens next?” and “Which paths connect these items?” without requiring visual tracing. Preserve selection while exploring neighbours and provide a route back to the overview.

For decision trees, state the decision, available answers and destination for each answer. For flow diagrams, retain quantities and explain any apparent imbalance or unrepresented flows.

### 9.5 Journey maps, blueprints and collaborative canvases

Break large canvases into named stages and purposeful views. Provide a structured account of the actor, action, channel, evidence, difficulty, responsibility and hand-off for each stage where relevant.

Allow people to read, contribute, comment, review and resolve issues through accessible controls. A read-only transcript is not comparable when others can edit. Tie comments to stable item identifiers rather than coordinates alone. Avoid forcing the viewport to follow another collaborator. Summarise changes on request or through restrained notifications.

### 9.6 Dense scientific, 3D and simulation graphics

Expose parameters, states, measurements, coordinate systems and relationships outside the rendering surface. Offer named viewpoints, explicit selection and reset. Explain occlusion and hidden layers where they affect interpretation.

When a data table cannot preserve the intended investigation, provide task-specific queries or alternative analytical views. Treat unresolved equivalence as a design gap requiring research, not as solved because a description exists.

**Step output:** domain-specific tasks and alternatives that preserve both overview and investigation.

## Step 10 — Implement robust semantics and delivery

### 10.1 Choose a coherent rendering model

Use a static image model for an atomic graphic and a structured interaction model when individual objects must be operated. Do not put controls inside an SVG exposed as a single `role="img"` and assume its descendants remain independently accessible.

For canvas and WebGL, provide the meaningful data, controls, state and results through accessible page structure. Painted objects do not acquire semantics from their visual appearance. For interactive SVG, verify the actual accessibility tree, naming, focus and reading order in supported environments.

Prefer visible HTML controls around the graphic. Keep decorative internal objects out of the accessibility tree. Generate unique identifiers for labels and descriptions.

### 10.2 Manage hiding deliberately

| Intention | Implementation approach | Verify |
|---|---|---|
| Collapse content for everyone | Use an appropriate hidden/display mechanism and update disclosure state | Hidden controls cannot retain focus; expanded content is reachable |
| Add a short screen-reader clarification | Use a tested visually hidden text technique | Content remains programmatically available and does not create invisible focus stops |
| Hide a redundant decorative object from assistive technology | Use appropriate empty alternatives or `aria-hidden` | No unique information or interactive descendants are lost |
| Make background content unavailable during a modal | Use a tested modal/inert model | Background is not operable and focus returns correctly |

Never put `aria-hidden="true"` on a focusable control or an ancestor of active controls. It does not remove keyboard focusability. A child cannot override an ancestor's hidden accessibility state with `aria-hidden="false"`.

Hidden text can contribute to an accessible name or description when directly referenced under accessible-name computation rules. Do not assume that all hidden references are ignored. Equally, do not rely on this mechanism for navigable explanations, tables or interactive detail: keep those available as structured content and test actual output.

### 10.3 Keep access when enhancements fail

Load essential headings, summaries and task controls independently where practical. Keep useful structured results available if tiles, fonts, scripts or third-party embeds fail. Explain unavailable functionality and offer a meaningful recovery path.

Name embedded frames, test entry and exit, and provide essential alternatives outside them. Evaluate the exact installed library version and configuration; an accessibility claim is not evidence that the delivered experience works.

### 10.4 Offer multimodal enhancements without new dependencies

Sonification, narration, haptics and tactile output can add valuable ways to recognise patterns. Explain their encoding and provide user control. Avoid audio autoplay; support pause, replay, speed and volume where relevant. Keep equivalent text and values available without sound, and test interference with screen-reader speech.

Where narrated video is used, provide appropriate captions and access to important visual information. Ensure tactile or braille users can access the structured content rather than being forced into an audio-only path.

### 10.5 Preserve information in exports

Export the current scope explicitly: title, units, period, filters, selection, timestamp, interpretation notes and data limitations. Include a summary and structured data when required by the task. Do not offer only an image when users need values or relationships.

Test documents, spreadsheets, presentations and PDFs independently for reading order, headings, alternatives and table structure. Check print and greyscale output. A CSV can support reuse, but it is not a replacement for an understandable on-page experience.

**Step output:** an implementation checked in real browsers, assistive technologies, failure states and output formats.

## Step 11 — Test technical access and comparable outcomes

### 11.1 Build a purposeful test dataset

Include ordinary data and edge cases: long labels, negative and zero values, ties, missing and suppressed values, uncertainty, overlapping points, dense clusters, very large results, no results and inconsistent network responses. Include an item that disappears after filtering and a live update that changes order.

Create expected answers independently of the rendered graphic. Verify visual and structured results against these answers rather than merely comparing two outputs that might share the same calculation error.

### 11.2 Use four complementary methods

1. **Automated checks:** inspect semantics, deterministic interaction, state consistency and known technical rules.
2. **Manual inspection:** evaluate visual encoding, keyboard behaviour, enlargement, content and dynamic states.
3. **Assistive-technology testing:** check the actual experience using representative supported combinations.
4. **User evaluation:** assess understanding, independent completion, effort, confidence and recovery with people who have relevant functional needs.

Automation cannot establish that an explanation conveys the same insight, that a route description is useful or that a dense interface is practical to operate.

### 11.3 Recommended test catalogue

Run the relevant tests for each essential task and each materially different state. “Pass” means the expected outcome was observed, not merely that the control exists.

| ID | Procedure | Expected result | Method and functional coverage |
|---|---|---|---|
| T01 Purpose and context | Ask users to identify subject, units, period, population and active filters before answering a task. | Users understand the scope without guessing from colour or position. | Content review and user test; cognitive, vision |
| T02 Informational parity | Complete the same retrieval, comparison and interpretation tasks through the visual and structured presentations. | Same relevant facts, caveats and correct conclusions are available. | Manual and user test; all applicable groups |
| T03 Independent exploration | Ask an unprompted follow-up question about a trend, relationship or exception using the alternative presentation. | Users can investigate beyond the author's summary. | User test; vision, cognitive, multiple |
| T04 Data integrity | Compare values, filters, totals, units and summaries to independent fixtures after each change. | All views and exports represent the intended state and dataset. | Automated plus content review; all |
| T05 Colour independence | Inspect greyscale and altered-colour presentations; identify categories, selected states and warnings. | Meaning remains visible through labels or other cues. | Manual; vision |
| T06 Contrast | Measure rendered text and required graphics against adjacent colours in each authored theme and state. | Applicable ratios are met; overlaps and focus remain distinguishable. | Tool-assisted manual; vision |
| T07 Text resize | Enlarge text to 200%; inspect labels, controls and panels. | No loss of information or functionality. | Manual; vision |
| T08 Zoom and reflow | Test 400% page zoom, approximately 320 CSS pixel width and both orientations. Navigate contained scrolling. | Supporting content reflows; necessary spatial scrolling is operable; focus is visible. | Manual; vision, physical |
| T09 Text spacing | Apply line height 1.5 times font size, paragraph spacing 2 times, letter spacing 0.12 times and word spacing 0.16 times, where applicable to the writing system. | No clipped, overlapping or missing content or controls. | Assisted manual; vision, cognitive |
| T10 Keyboard completion | Put the pointer aside. Complete search, filtering, selection, comparison, drill-down, reset and export using keyboard only. | Every essential function is usable with no trap or impractical sequence. | Manual with automated regression; physical, vision |
| T11 Focus persistence | Open and close panels; filter away a focused item; refresh, paginate and enter/exit full screen. | Focus remains visible, follows a predictable path and is not lost or entirely obscured. | Manual and browser tests; vision, physical |
| T12 Pointer alternatives | Complete drag, pinch, rotate, lasso and reorder tasks using a single pointer without dragging. | Equivalent functions are available through straightforward controls. | Manual; physical |
| T13 Target and cancellation | Measure effective targets and spacing; try imprecise input and release outside the target. | Applicable size rules are met; accidental activation can be avoided or reversed. | Assisted manual; physical |
| T14 Hover, focus and touch | Open each tooltip or detail through pointer, keyboard and touch; move onto it and dismiss it. | Required content is available and remains readable; interactive detail is operable. | Manual; vision, physical, cognitive |
| T15 Names and structure | Inspect the accessibility tree and navigate headings, tables, lists and controls with a screen reader. | Meaningful names, relationships, roles and states; no excessive decorative noise. | Automated inspection plus assistive technology; vision |
| T16 Screen-reader tasks | Complete representative tasks using a desktop screen reader and relevant mobile combination. | Efficient navigation, understandable detail and actionable results. | Assistive technology and user test; vision |
| T17 Speech and switch | Use visible-label speech commands and sequential switch navigation; also complete voice functions without speaking. | Controls can be identified and operated without precision or mandatory vocal input. | Assistive technology and user test; physical, speech |
| T18 Display modes | Change light/dark/system mode, forced colours, contrast preferences and relevant reader settings. | Required meaning, focus and selected states survive; explicit choice is honoured. | Manual; vision, cognitive |
| T19 Reduced motion | Enable reduced motion before loading and change it during use. Trigger transitions and map movement. | Non-essential CSS and scripted motion is removed or replaced without losing information. | Automated plus manual; motion sensitivity, cognitive |
| T20 Flash safety | Inspect assets and transitions; analyse potentially flashing content before participant exposure. | Content stays within applicable flash thresholds; unsafe effects are removed. | Specialist/tool-assisted; photosensitivity |
| T21 Live updates | Read an item during streaming; pause, resume, change filters rapidly and delay responses. | Stable reading and selection; clear snapshot status; no obsolete response overwrites. | Automated plus manual; vision, cognitive, physical |
| T22 Announcements | Listen while searching, filtering, loading and receiving errors or updates. | Concise relevant messages; no repeated interruption; results remain available in page content. | Assistive technology; vision, cognitive |
| T23 Sound independence | Mute sound and complete every task; test audio clarity, controls and screen-reader coexistence separately. | No information or action depends solely on hearing; audio can be controlled. | Manual and user test; hearing, multiple |
| T24 Combined needs | Complete tasks with relevant combinations, including non-audio structured access where vision and hearing are unavailable. | Alternatives remain compatible; no task forces an unusable sensory or input channel. | User and assistive-technology test; multiple |
| T25 Geographic outcomes | Find a location, compare routes, identify a transfer or boundary and change floor using each presentation. | Same relevant spatial facts and choices, with freshness and unknowns visible. | Content and user test; all relevant groups |
| T26 Diagram outcomes | Trace a dependency, follow a branch, inspect a connection and return to the overview without visual tracing. | Relationships and conditions are accurate and navigable. | Manual and user test; vision, cognitive |
| T27 Editing and collaboration | Add, edit, move, comment, undo and resolve through accessible controls; introduce a concurrent edit. | Comparable contribution, conflict recovery and change awareness. | Manual and user test; physical, vision, cognitive |
| T28 Failure and performance | Block the rendering provider, deny location, simulate slow loading and test empty/stale/error states. | Useful content or a meaningful recovery route remains; no misleading successful state. | Automated plus manual; all |
| T29 Export parity | Export a filtered or selected view, then inspect the file independently. | Correct scope and information; usable document structure and alternatives. | File-specific checks plus manual; all |
| T30 Privacy | Use alternatives without disclosure; inspect location requests, stored preferences and analytics fields. | No unnecessary diagnosis or assistive-technology profiling; private output is possible. | Design and implementation review; all |
| T31 Understanding and recovery | Ask users to explain a conclusion, change their approach and recover from an intentional error. | Correct reasoning, visible state and recovery without moderator rescue. | User test; cognitive and all applicable groups |

Text-spacing figures above are override test conditions, not compulsory default typography. Test CSS-supported text appropriately; do not treat an image of text as adaptable merely because surrounding text passes.

### 11.4 Build useful automation

Run an accessibility rules engine on initial, expanded, filtered, modal, empty and error states. Add deterministic tests for accessible names, disclosure states, keyboard actions, focus restoration, request ordering and synchronisation between presentations. Check that hidden panels contain no active focus stops.

Use visual regression for clipping and unintended layout changes, but review semantic and numerical assertions separately. Automated contrast checks often miss canvas, complex SVG, gradients and overlaps; retain manual assessment. A clean scan is evidence of the checks performed, not evidence of complete accessibility.

### 11.5 Select environments deliberately

Record operating system, browser, assistive technology, device, input method, viewport and relevant settings. Include representative desktop screen-reader, mobile screen-reader, magnification, speech input, switch and braille combinations according to the audience and risk.

Use actual supported combinations rather than assuming that one browser or one screen reader represents all users. A simulator is a design aid, not evidence of lived usability. Recruit people with relevant functional needs for consequential decisions and novel interactions.

### 11.6 Run fair comparative user sessions

Give neutral tasks, such as “Which two areas meet these conditions, and how certain are you?” Avoid instructions that reveal the answer or tell users which interface to choose.

Allow familiar assistive technologies, practice, breaks and preferred communication. Counterbalance presentation order or use equivalent datasets to reduce learning effects. Distinguish moderator help with research logistics from help needed to overcome the interface. Record the latter as assisted completion.

Do not compare every participant against a sighted mouse user's speed as the universal standard. Look for avoidable interaction burden, loss of information and blocked independence within each task and functional context.

**Step output:** reproducible evidence linked to tasks, functional conditions, interface states and product versions.

## Step 12 — Measure, prioritise and maintain

### 12.1 Measure outcomes separately

| Measure | Record | Interpret carefully |
|---|---|---|
| Independent completion | Completed without interface-related assistance, assisted, failed or abandoned | Never count assisted completion as independent success |
| Accuracy | Correct values, reasoning, selected route or resulting action | Score against predefined answers or justified interpretation criteria |
| Information parity | Required facts and relationships available in each presentation | A missing essential fact is not offset by many available minor facts |
| Effort | Interactions, repeated navigation, retries and reported effort | Investigate avoidable burden rather than setting an arbitrary universal click limit |
| Time | Time to understand and complete, including delays and recovery | Compare appropriate conditions and report variation, not just an overall mean |
| Confidence | User confidence alongside observed correctness | High confidence in a wrong answer indicates a serious design problem |
| Recoverability | Ability to correct input, undo and regain context | Note whether help or restarting was necessary |
| Comfort and satisfaction | Reported strain, disorientation, clarity and control | Do not infer satisfaction from task completion alone |
| Coverage | Tasks, states and functional conditions actually tested | Untested conditions remain unknown |

Report results by task and functional condition, including relevant combinations. Do not add overlapping category counts as though they represent different people. With small samples, report participant counts and observed barriers rather than implying population-wide statistical certainty.

Do not compress everything into a single accessibility percentage. An average can conceal complete exclusion from a critical task.

### 12.2 Set acceptance criteria before testing

For each essential task, define the required information, actions, accuracy and acceptable burden. As a release policy, require no known unresolved blocker to independent completion in the tested scope, no critical loss of meaning between presentations and no unsafe flashing.

Set any time or effort thresholds from task risk, research and reasonable expectations. They are product acceptance thresholds, not universal accessibility standards. Passing a small study does not prove that all users will succeed.

### 12.3 Prioritise by impact

| Priority | Impact | Response |
|---|---|---|
| Critical | Safety risk, misleading consequential information or complete exclusion from an essential task | Prevent release of the affected experience until resolved or replace it with a demonstrably effective route |
| High | Essential task requires assistance, loses important information or incurs severe avoidable effort | Assign an owner and fix before acceptance of that task |
| Medium | Task succeeds but repeated friction, confusion or weak recovery remains | Schedule remediation and retest affected outcomes |
| Low | Limited inconvenience without meaningful loss of outcome | Improve through normal maintenance and monitor cumulative impact |

Record repeated smaller barriers together: several modest problems may cumulatively prevent completion. Severity is contextual; do not assign it solely from a failed rule identifier.

### 12.4 Keep a compact evidence record

Use this template for each finding:

```text
Finding ID:
Product/build and data version:
Task and expected outcome:
Functional condition(s):
Presentation and interface state:
Environment and settings:
Steps to reproduce:
Observed outcome and assistance required:
Information, effort or safety impact:
Technical check result, where applicable:
Evidence location:
Priority and rationale:
Owner and corrective action:
Retest result and date:
Remaining uncertainty:
```

Keep research participation voluntary and minimise personal data. Record functional test conditions rather than diagnostic details. Restrict access to recordings and sensitive findings, define retention and deletion periods, and avoid logging personal queries, precise locations or disability inferences unnecessarily.

### 12.5 Maintain the experience

Assign responsibility for data accuracy, explanations, interaction, accessibility evidence and third-party changes. Retest affected tasks after changes to data structure, aggregation, wording, rendering libraries, theme tokens, controls, exports or provider configuration.

Monitor feedback by task and barrier, not only by page. Keep a visible way to report incorrect data or access problems. Treat support requests as evidence for improving the product, not as the primary alternative experience.

## Worked examples

### Example A — Comparing services on a dashboard

1. Define the task: compare waiting times for a selected period and identify services below a chosen threshold.
2. Provide a labelled chart, a concise trend explanation and a table with the same services, dates, values and uncertainty.
3. Offer period fields, service checkboxes and a threshold input; these perform the same query as direct chart selection.
4. Keep selected services in a persistent comparison panel. Explain whether a value is estimated or missing.
5. Update all presentations together and announce one concise result summary.
6. Test whether users can independently identify qualifying services and explain uncertainty using keyboard, magnification and non-visual access.

The table alone is insufficient if it omits uncertainty or makes users manually derive a comparison the chart performs automatically. Add the same comparison calculation and explanation.

### Example B — Finding a suitable route

1. Define the destination and functional route constraints, such as avoiding steps and limiting distance.
2. Offer location search independently of geolocation.
3. Present route choices with distance, relevant conditions, known closures and verification date.
4. Supply ordered directions, named connections and accessible controls for changing the start, destination or constraints.
5. Keep route changes consistent across visual and textual presentations.
6. Test a closure, an unknown lift status and a longer alternative route. Confirm users can recognise uncertainty and choose appropriately.

A route labelled “accessible” without the conditions behind that claim does not provide enough information for an individual decision.

### Example C — Exploring a live dependency network

1. Define tasks: locate a service, identify its dependencies and assess which services a failure affects.
2. Offer a visual network plus a searchable node list and incoming/outgoing relationship panels.
3. Provide a dependency query and explicit path exploration; do not require tracing lines visually.
4. Keep selection stable during updates, provide a frozen snapshot mode and identify its time.
5. Offer structured editing and undo if users can change relationships visually.
6. Test that the same affected services and relationship conditions are discoverable in each presentation, including cycles and missing data.

## Release checklist

- [ ] Essential questions, decisions and actions are documented.
- [ ] Functional coverage includes vision, hearing, speech, physical interaction, cognition and relevant combinations.
- [ ] Photosensitivity, motion sensitivity and privacy have been assessed.
- [ ] Each presentation preserves the required information, uncertainty and actions.
- [ ] Users can investigate beyond a preset summary when exploration is part of the task.
- [ ] Visual encoding is understandable without colour alone and remains legible in supported conditions.
- [ ] Titles, descriptions, values and relationships are available in navigable structured content.
- [ ] Keyboard, single-pointer and relevant assistive-technology tasks work efficiently.
- [ ] Focus, hidden content, panels and dynamic updates behave predictably.
- [ ] Page enlargement, reflow, themes, forced colours and reduced motion have been tested.
- [ ] Maps and diagrams preserve their spatial, temporal and relational meaning.
- [ ] Empty, stale, failed, delayed and conflicting states are understandable and recoverable.
- [ ] Exports retain the intended scope and are independently usable.
- [ ] Outcome tests record independent completion, accuracy, effort and confidence.
- [ ] Known blockers are resolved; remaining uncertainties and untested conditions are explicit.
- [ ] Owners, retest triggers and a user feedback route are in place.
