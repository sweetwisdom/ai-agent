---
name: pencil-replay
description: Restores .pen design files from Pencil conversation logs (JSONL). Extracts set_variables and batch_design operations, generates replay plans, and executes via Pencil MCP. Use when the user provides a JSONL file and asks to restore, replay, or recover a Pencil design, or when working with Pencil dialogue records.
---

# Pencil 文件恢复

从 Pencil 对话记录 (JSONL) 还原 .pen 设计文件。

## Quick Start

1. **Parse the JSONL**: Run `python .cursor/skills/pencil-replay/scripts/pencil_replay.py <input.jsonl> -f <target.pen> -o plan.json`
2. **Execute via MCP**: Call `mcp_pencil_set_variables` then `mcp_pencil_batch_design` in order (≤25 ops per batch)

## Workflow

```
Task Progress:
- [ ] Step 1: Parse JSONL and extract Pencil ops
- [ ] Step 2: Call mcp_pencil_set_variables
- [ ] Step 3: Call mcp_pencil_batch_design (batches of ≤25)
- [ ] Step 4: Handle ID mapping for cross-batch refs
```

**Step 1: Parse**

```bash
python .cursor/skills/pencil-replay/scripts/pencil_replay.py input.jsonl -f pencil-new.pen -o plan.json --output-dir extracted
```

Extracts `mcp__pencil__set_variables` and `mcp__pencil__batch_design` where `input.filePath` matches the target .pen.

**Step 2–3: Execute**

- `mcp_pencil_set_variables(filePath, variables)` — use first step's variables from plan
- `mcp_pencil_batch_design(filePath, operations)` — run each batch in order

**Step 4: ID mapping**

- Replace parent node IDs (e.g. `KXPe9`, `B3bkG`) with IDs returned from previous batches
- Replace `ref("oldId")` with `ref("ComponentName")` when referencing reusable components by name

## Rules

- Skip `D("xxx")` when document is empty
- Max 25 operations per `batch_design` call
- Use bindings (e.g. `compArea`) within same batch; IDs across batches

## Additional Resources

- For detailed API and edge cases, see [reference.md](reference.md)
- For usage examples, see [examples.md](examples.md)
