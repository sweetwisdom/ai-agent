---
description: 从插件模板初始化新的前端项目脚手架
---

请帮我初始化一个新的前端项目（React/Vue + TypeScript + Vite）。

用法：`/setup` 或 `/setup --framework react --pm pnpm`（可选参数）

示例：`/setup`（交互式选择框架与包管理器）

## 执行步骤

**第零步：获取项目名称与选项**

询问用户：
> "请输入项目名称（英文，小写短横线，如 `my-app`）："

可选：若未通过参数指定，再询问：
- 框架：React 或 Vue（默认 React）
- 包管理器：npm 或 pnpm（默认 pnpm）

**第一步：复制模板文件**

从 `${CLAUDE_PLUGIN_ROOT}/templates/` 复制以下文件到当前工作目录：
- `package.json`、`tsconfig.json`、`tsconfig.node.json`、`vite.config.ts`
- `.prettierrc`、`.eslintrc.cjs`、`.mcp.json`、`.gitignore`
- `index.html`、`src/` 目录（含 main.tsx、App.tsx、index.css、vite-env.d.ts）
- `CLAUDE.md.template` 仅作参考，不复制；CLAUDE.md 在第五步根据实际项目生成

**第二步：替换项目名称**

在复制后的文件中，将 `package.json` 的 `name` 字段替换为实际项目名（如用户输入的 `my-app`）。目录保持 `src/`，无需重命名。

**第三步：初始化 .gitignore**

检查是否存在 `.gitignore`：
- 若不存在，使用模板中的 `.gitignore`（含 node_modules、dist、.env.local、coverage 等）
- 若存在，将模板中未包含的条目合并进去

**第四步：将 AI 工具链复制到项目**

将插件内容复制到项目的 `.claude/` 目录：

1. 复制 slash commands：将 `${CLAUDE_PLUGIN_ROOT}/commands/` 下所有文件复制到 `.claude/commands/`。若目标文件已存在，询问用户是否覆盖。

2. 复制 agents：将 `${CLAUDE_PLUGIN_ROOT}/agents/` 下所有文件复制到 `.claude/agents/`。若目标文件已存在，询问用户是否覆盖。

3. 复制编码规范：将 `${CLAUDE_PLUGIN_ROOT}/rules/` 下所有文件复制到 `.claude/rules/`。

4. 复制 hooks 脚本：将 `${CLAUDE_PLUGIN_ROOT}/hooks/` 下所有文件复制到 `.claude/hooks/`。

5. 写入 hooks 配置到 `.claude/settings.json`：
   - 若文件不存在，创建并写入：
     ```json
     {
       "hooks": {
         "PostToolUse": [
           {
             "matcher": "Write|Edit",
             "hooks": [
               {
                 "type": "command",
                 "command": "bash \".claude/hooks/scripts/prettier-format.sh\" 2>/dev/null || powershell -ExecutionPolicy Bypass -File \".claude/hooks/scripts/prettier-format.ps1\" 2>/dev/null || true",
                 "timeout": 10
               }
             ]
           }
         ]
       }
     }
     ```
   - 若文件已存在，将上述 `hooks` 字段合并进去，不覆盖其他已有配置。

**第五步：扫描并生成 CLAUDE.md**

根据实际 `package.json`、目录结构生成 `CLAUDE.md`，内容包括：
- 构建命令：`pnpm build` 或 `npm run build`
- 启动命令：`pnpm dev` 或 `npm run dev`
- 测试命令：`pnpm test` 或 `npm run test`
- 校验命令：`pnpm lint` 或 `npm run lint`
- 目录结构说明（src、components、hooks、utils 等）
- 推断出的禁止修改区域

生成后，在对话中列出需要人工确认的项目：

```
✅ 已自动填充：
  - 项目名称：<name>
  - 框架：React / Vue
  - 包管理器：pnpm / npm
  - 构建/启动/测试命令

⚠️  需要人工确认：
  - [ ] 是否启用 E2E（Playwright/Cypress）
  - [ ] 是否使用 CSS 方案（Tailwind/CSS Modules/SCSS）

❌ 未能自动推断（请手动补充）：
  - [ ] 状态管理：Zustand / Pinia / Redux
  - [ ] 特殊设计决策
```

**第六步：完成插件脱离，移交项目管理**

告知用户：

```
✅ setup 完成！以下文件已写入项目：

  .claude/
  ├── commands/        ← slash commands（可直接编辑迭代）
  ├── agents/          ← AI agents（可直接编辑迭代）
  ├── rules/           ← 编码规范（可直接编辑迭代）
  ├── hooks/scripts/   ← Prettier 自动格式化脚本
  ├── settings.json    ← hooks 配置
  └── CLAUDE.md        ← 项目上下文（需在项目根目录单独生成）

后续步骤：

1. 安装依赖并验证：
     pnpm install && pnpm build && pnpm lint

2. 将 .claude/ 与 CLAUDE.md 提交到 git，团队成员拉取后即生效：
     git add .claude/ CLAUDE.md
     git commit -m "chore: 初始化 AI 工具链配置"

3. 卸载插件（可选）：claude plugin uninstall frontend-tools --scope project

4. 后续对 commands/agents/rules 的修改直接编辑 .claude/ 下的文件，像普通代码一样提 PR、code review、迭代。
```
