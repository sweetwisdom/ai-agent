#!/usr/bin/env python3
"""
Pencil 文件恢复 - 从 JSONL 提取 set_variables 和 batch_design 操作。

用法: python scripts/pencil_replay.py <input.jsonl> -f <target.pen> -o plan.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

PENCIL_TOOLS = {"mcp__pencil__set_variables", "mcp__pencil__batch_design"}
BATCH_LIMIT = 25


def parse_jsonl(path: Path) -> list:
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return records


def extract_pencil_ops(records: list, file_path: Optional[str] = None) -> list:
    ops = []
    for i, rec in enumerate(records):
        for item in rec.get("message", {}).get("content", []) or []:
            if not isinstance(item, dict) or item.get("type") != "tool_use":
                continue
            name = item.get("name", "")
            if name not in PENCIL_TOOLS:
                continue
            inp = item.get("input", {}) or {}
            rec_fp = inp.get("filePath")
            if file_path and rec_fp and rec_fp != file_path:
                continue
            ops.append({"line": i + 1, "name": name, "input": inp})
    return ops


def get_pen_path(ops: list) -> Optional[str]:
    for op in ops:
        fp = op.get("input", {}).get("filePath")
        if fp and ".pen" in fp:
            return fp
    return None


def build_replay_plan(ops: list, max_per_batch: int = BATCH_LIMIT) -> dict:
    plan = {"filePath": get_pen_path(ops), "steps": []}
    for op in ops:
        if op["name"] == "mcp__pencil__set_variables":
            plan["steps"].append({"type": "set_variables", "variables": op["input"].get("variables", {})})
            continue
        if op["name"] == "mcp__pencil__batch_design":
            raw = (op["input"].get("operations") or "").strip()
            if not raw:
                continue
            lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]
            for i in range(0, len(lines), max_per_batch):
                chunk = lines[i : i + max_per_batch]
                if i == 0 and chunk and chunk[0].startswith('D("'):
                    chunk = chunk[1:]
                if chunk:
                    plan["steps"].append({
                        "type": "batch_design",
                        "operations": "\n".join(chunk),
                        "filePath": op["input"].get("filePath"),
                    })
    return plan


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("-f", "--file-path", help="目标 .pen 路径")
    p.add_argument("-o", "--output", type=Path)
    p.add_argument("--output-dir", type=Path)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--max-ops", type=int, default=BATCH_LIMIT)
    args = p.parse_args()

    if not args.input.exists():
        print(f"错误: 文件不存在 {args.input}", file=sys.stderr)
        sys.exit(1)

    records = parse_jsonl(args.input)
    ops = extract_pencil_ops(records, args.file_path)
    if not ops:
        print("未找到 Pencil 操作", file=sys.stderr)
        sys.exit(1)

    file_path = args.file_path or get_pen_path(ops)
    plan = build_replay_plan(ops, args.max_ops)
    plan["filePath"] = file_path

    print(f"提取 {len(ops)} 条操作, 目标: {file_path}")
    print(f"恢复计划: {len(plan['steps'])} 步")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        print(f"已写入 {args.output}")

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for i, step in enumerate(plan["steps"]):
            if step["type"] == "set_variables":
                with open(args.output_dir / "variables.json", "w", encoding="utf-8") as f:
                    json.dump(step["variables"], f, ensure_ascii=False, indent=2)
            elif step["type"] == "batch_design":
                with open(args.output_dir / f"batch_{i:02d}.txt", "w", encoding="utf-8") as f:
                    f.write(step["operations"])
        print(f"已写入 {args.output_dir}")

    if not args.dry_run:
        print("\n执行: mcp_pencil_set_variables → mcp_pencil_batch_design (每批 ≤25 条)")


if __name__ == "__main__":
    main()
