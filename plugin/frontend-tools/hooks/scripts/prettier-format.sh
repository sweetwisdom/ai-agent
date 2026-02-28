#!/bin/bash
# PostToolUse hook: 对 AI 写入/编辑的前端文件自动执行 Prettier
# stdin: JSON，结构为 { "tool_input": { "file_path": "..." } }

input=$(cat)

# 用 sed 提取 file_path
file_path=$(echo "$input" | sed -n 's/.*"file_path":"\([^"]*\)".*/\1/p')

# 路径为空则跳过
[ -z "$file_path" ] && exit 0

# Windows 反斜杠转正斜杠
file_path="${file_path//\\//}"

# 只处理前端相关文件
case "$file_path" in
    *.js|*.jsx|*.ts|*.tsx|*.json|*.css|*.scss|*.html|*.vue|*.md) ;;
    *) exit 0 ;;
esac

# 执行格式化：优先 npx prettier，否则 prettier
if command -v npx &>/dev/null; then
    npx --yes prettier --write "$file_path" 2>/dev/null && echo "[prettier] formatted: $file_path" || true
elif command -v prettier &>/dev/null; then
    prettier --write "$file_path" && echo "[prettier] formatted: $file_path" || true
else
    echo "[prettier] warning: prettier not found (npx/prettier)" >&2
fi
