# Pencil Replay Examples

## Example 1: Basic restore

**Input**: User says "用 pencil 恢复 input.jsonl 中 pencil-new.pen 的操作"

**Output**:
1. Run `python skills/pencil-replay/scripts/pencil_replay.py input.jsonl -f pencil-new.pen -o plan.json`
2. Read plan.json, call `mcp_pencil_set_variables` with variables from first step
3. Call `mcp_pencil_batch_design` for each batch_design step in order

## Example 2: Extract only

**Input**: User says "从 input.jsonl 提取 pencil 操作到 extracted 目录"

**Output**:
```bash
python skills/pencil-replay/scripts/pencil_replay.py input.jsonl --output-dir extracted
```
Produces `extracted/variables.json` and `extracted/batch_00.txt`, `batch_01.txt`, etc.

## Example 3: Multiple .pen files in log

**Input**: JSONL contains ops for both `design-a.pen` and `design-b.pen`

**Output**: Use `-f design-a.pen` to filter; only ops for that file are extracted.
