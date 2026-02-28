# frontend-tools — 面向前端开发的 Claude 插件

面向前端（React/Vue、TypeScript、npm/pnpm、ESLint/Prettier）的 AI 工具集：代码规范、项目脚手架、代码审查、构建/校验错误修复。

## 安装

```bash
# 若已配置插件市场
/plugin install frontend-tools
```

或从本仓库将 `plugins/frontend-tools` 复制到本地插件目录后安装。

## 快速开始：/setup

在空目录或已有前端项目中执行：

```
/setup
```

可选参数（或由 AI 交互询问）：

- 框架：React / Vue（默认 React）
- 包管理器：npm / pnpm（默认 pnpm）

`/setup` 会：

- 从模板生成 `package.json`、`tsconfig.json`、`vite.config.ts`、`.prettierrc`、`.eslintrc.cjs`、`.mcp.json`、`.gitignore`、`index.html`、`src/` 骨架
- 将 commands、agents、rules、hooks 复制到项目 `.claude/`，并写入 PostToolUse 格式化 hook
- 根据项目生成 `CLAUDE.md`（构建/启动/测试命令、目录说明）

完成后执行 `pnpm install && pnpm build && pnpm lint` 验证。

## 斜杠命令 (commands)

| 命令 | 说明 |
|------|------|
| `/setup` | 从模板初始化前端项目并接入 AI 工具链 |
| `/plan` | 先输出结构化计划（影响范围、步骤、风险、验收），等用户确认后再实现 |
| `/review` | 对指定前端代码做审查（a11y、性能、React/Vue、安全、代码质量），输出严重程度 + 位置 + 建议 |
| `/fix-build` | 根据粘贴的构建/校验错误定位根因并修复，验收：`pnpm build`、`pnpm lint` |

## Agents

| Agent | 用途 |
|-------|------|
| **code-reviewer** | 前端代码审查：a11y、性能、React/Vue 实践、安全、代码质量；输出带严重程度与优先建议 |
| **build-error-resolver** | 修复 npm/TypeScript/ESLint/Vite 等构建与校验错误，最小改动、不架构变更 |

## Rules（编码规范）

- **coding-style.md** - JS/TS 命名、目录约定、React/Vue 约定、禁止 any、单文件职责
- **git-workflow.md** - Commit 格式、PR 流程、分支、提交前检查
- **testing.md** - 单元/组件/E2E（Vitest、Playwright/Cypress）、覆盖率与提交前检查
- **performance.md** - 包体、懒加载、资源优化、Core Web Vitals

## Hooks

- **PostToolUse**：当 AI 调用 `Write` 或 `Edit` 后，对涉及的前端文件（.js/.jsx/.ts/.tsx/.json/.css/.scss/.html/.vue/.md）自动执行 Prettier 格式化。
- 脚本：`hooks/scripts/prettier-format.sh`（Linux/macOS）、`prettier-format.ps1`（Windows），跨平台优先 bash 再回退 PowerShell。

## Templates

`/setup` 使用的模板位于 `templates/`：

- `package.json`、`tsconfig.json`、`tsconfig.node.json`、`vite.config.ts`
- `.prettierrc`、`.eslintrc.cjs`、`.mcp.json`、`.gitignore`
- `index.html`、`src/main.tsx`、`src/App.tsx`、`src/index.css`、`src/vite-env.d.ts`
- `CLAUDE.md.template`（由 setup 根据实际项目生成 CLAUDE.md）

## Skills（可选）

- **tdd** - 前端 TDD 工作流：先写测试再实现，Vitest/Jest 组件与工具函数测试
- **skill-creator** - 创建自定义技能的指南与流程（与 cpp-qt-tools 的 skill-creator 对齐，可引用其脚本）

## 与 cpp-qt-tools 的对应关系

| cpp-qt-tools | frontend-tools |
|--------------|----------------|
| C++/Qt、CMake、clang-format | React/Vue、TS、npm/pnpm、Prettier/ESLint |
| /setup → CMake + Qt 模板 | /setup → Vite + package.json + tsconfig 等 |
| /fix-build → 编译错误 | /fix-build → npm/ts/eslint/vite 错误 |
| code-reviewer → 内存/线程/Qt | code-reviewer → a11y/性能/React-Vue/安全 |
| build-error-resolver → CMake/MSVC | build-error-resolver → TypeScript/ESLint/Vite |
| PostToolUse → clang-format | PostToolUse → Prettier |

整体保持同一套插件形态（commands + agents + rules + hooks + templates + skills），仅将领域从 C++/Qt 换为前端开发。
