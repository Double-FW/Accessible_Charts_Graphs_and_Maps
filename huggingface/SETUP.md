# Weekly Accessible Charts, Graphs and Maps updates

Source: https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps

Destination: https://huggingface.co/datasets/GarethFW/Accessible_Charts_Graphs_and_Maps

The destination is fixed in export-config.json. No HF_DATASET_ID variable is needed.
Save a destination-scoped Hugging Face token as repository secret HF_TOKEN, then
create .github/workflows/huggingface-sync.yml from WORKFLOW_TO_COPY.txt in the
setup download. Run it manually once and check the result; weekly runs are
Mondays at 07:23 UTC. Never commit credentials; use the token copy button.

All approved sources are required. New or renamed documents need export-list
review. Proposed tests, methods, examples and release guidance are preserved,
not executed. Export checks do not verify real graphics or user outcomes.
