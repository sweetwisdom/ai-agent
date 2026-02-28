# 前端编码风格规范（JS/TS、React/Vue）

## 命名规则

| 类型       | 规则           | 示例                |
| ---------- | -------------- | ------------------- |
| 变量/函数  | camelCase      | `getUserInfo`        |
| 组件       | PascalCase     | `UserProfile`        |
| 常量       | 全大写下划线   | `API_BASE_URL`       |
| 类型/接口  | PascalCase     | `UserInfo`           |
| 文件名     | kebab-case 或 PascalCase（组件） | `use-auth.ts`、`UserCard.tsx` |
| 目录       | 小写短横线     | `components`、`hooks` |
| 枚举成员   | PascalCase     | `Status.Pending`      |

## 目录约定

- `src/components/` - 可复用 UI 组件
- `src/hooks/` - 自定义 Hooks（React）或 composables（Vue）
- `src/utils/` 或 `src/lib/` - 纯函数与工具
- `src/pages/` 或 `src/views/` - 页面级组件
- `src/types/` - 共享类型定义
- `src/assets/` - 静态资源

## 文件与组件

- 单文件组件：一个文件导出一个组件，组件名与文件名一致（PascalCase 组件时可与文件名一致）
- Props 必须带类型（TypeScript 接口或 type），禁止 `any`
- 优先使用 `const`，需要重新赋值时再用 `let`
- 禁止使用 `any`，必要时用 `unknown` 并做类型收窄

## React 约定

- 函数组件 + Hooks，Hooks 仅在顶层调用，条件/循环中不调用
- 列表渲染必须提供稳定、唯一的 `key`，避免用 index 作为 key（列表会重排时）
- 事件处理函数命名：`handleXxx` 或 `onXxx`（当作为 props 传递时）

## Vue 约定

- 优先 Composition API + `<script setup>`
- 响应式数据明确用 `ref`/`reactive`，注意解构丢失响应式时的处理
- `v-for` 必须带 `key`，且 key 稳定唯一

## 代码风格

- 缩进 2 空格，行宽建议不超过 120 字符
- 字符串优先单引号（与 Prettier/ESLint 一致即可）
- 语句末尾分号按项目统一（通常保留分号）
- 未使用变量及时删除，或按 ESLint 规则用下划线前缀

## 代码质量检查清单

提交前确认：

- [ ] 命名符合规范（camelCase/PascalCase/kebab-case）
- [ ] 无 `any`，类型完整
- [ ] 单文件职责清晰，单文件不宜过长（如超过 300 行考虑拆分）
- [ ] 无深层嵌套（>4 层可考虑提前 return 或拆分）
- [ ] 与项目 ESLint + Prettier 配置一致
