# Pencil Replay Reference

## Input Format

JSONL: each line is a JSON object. The tool extracts from `message.content` items with `type: "tool_use"` and `name` in:

- `mcp__pencil__set_variables`
- `mcp__pencil__batch_design`

Only operations where `input.filePath` matches the target .pen are kept.

## Replay Plan Structure

```json
{
  "filePath": "pencil-new.pen",
  "steps": [
    { "type": "set_variables", "variables": { ... } },
    { "type": "batch_design", "operations": "...", "filePath": "..." }
  ]
}
```

## ID Mapping

- **Within batch**: Use bindings (e.g. `compArea=I(document,...)`, then `I(compArea,...)`)
- **Across batches**: Parent IDs like `KXPe9`, `B3bkG` must be replaced with IDs returned from previous `batch_design` calls
- **Component refs**: `ref("oldId")` → `ref("ComponentName")` where ComponentName comes from the `name` property of reusable components

## Edge Cases

- **Empty document**: Skip `D("xxx")` in the first batch
- **Batch limit**: Pencil allows max 25 operations per `batch_design` call
- **Multiple set_variables**: Use the first one; later ones may override (implementation-dependent)

## Script Usage

From project root:

```bash
# Generate plan
python skills/pencil-replay/scripts/pencil_replay.py input.jsonl -f pencil-new.pen -o plan.json

# Extract to directory (variables.json, batch_00.txt, ...)
python skills/pencil-replay/scripts/pencil_replay.py input.jsonl --output-dir extracted

# Dry run
python skills/pencil-replay/scripts/pencil_replay.py input.jsonl --dry-run
```
