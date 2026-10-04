# Resilient Queue Worker

Small reference worker used to test retry and compatibility behavior on Windows.

The repository keeps release and validation notes in Git history so the source
tree stays small. `src/worker.py` is the example worker. `tools/compatcheck.exe`
is the self-contained Windows compatibility check used by older build agents.
Its small reference source is kept under `tools/source/`.

