# PostToolUse hook: 对 AI 写入/编辑的前端文件自动执行 Prettier
# stdin: JSON，结构为 { "tool_input": { "file_path": "..." } }

$inputJson = $input | Out-String

# 提取 file_path
if ($inputJson -notmatch '"file_path"\s*:\s*"([^"]+)"') { exit 0 }
$filePath = $matches[1] -replace '\\\\', '\'

# 只处理前端相关文件
if ($filePath -notmatch '\.(js|jsx|ts|tsx|json|css|scss|html|vue|md)$') { exit 0 }

# 执行格式化：优先 npx prettier，否则 prettier
$prettierCmd = $null
if (Get-Command npx -ErrorAction SilentlyContinue) {
    & npx --yes prettier --write $filePath 2>$null
    if ($LASTEXITCODE -eq 0) { Write-Host "[prettier] formatted: $filePath" }
} elseif (Get-Command prettier -ErrorAction SilentlyContinue) {
    & prettier --write $filePath
    if ($LASTEXITCODE -eq 0) { Write-Host "[prettier] formatted: $filePath" }
} else {
    Write-Error "[prettier] warning: prettier not found (npx/prettier)"
}
