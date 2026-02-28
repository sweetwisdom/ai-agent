---
name: tdd-workflow
description: 前端 TDD 工作流指南。当编写新功能、修复 Bug、重构或添加组件/工具函数测试时使用；确保先写测试再实现，覆盖边界与错误场景。
---

# 前端测试驱动开发 (TDD) 工作流

此 skill 确保前端项目的功能开发遵循 TDD：先写测试，再实现代码。

## 何时使用

- 编写新特性或组件
- 修复 Bug
- 重构现有代码
- 添加或修改工具函数、Hooks、工具类

## 核心原则

### 1. 测试先行 (Tests BEFORE Code)

先写测试用例，再实现代码使测试通过。

### 2. 覆盖率与场景

- 工具函数：正常输入、空值、边界、异常
- 组件：渲染、用户交互、条件分支
- Hooks：返回值、依赖变化、清理逻辑
- 边界与错误路径必须覆盖

### 3. 测试类型

- **单元测试**：纯函数、工具、部分 Hooks 逻辑
- **组件测试**：渲染、事件、条件显示（Vitest + React Testing Library / Vue Test Utils）
- **E2E**：关键用户路径（Playwright/Cypress，按项目配置）

## 工作流步骤

### 1. 定义需求

明确功能与验收条件（输入、输出、边界）。

### 2. 写测试（应失败）

```ts
// 示例：工具函数
import { describe, it, expect } from 'vitest'
import { myUtil } from './myUtil'

describe('myUtil', () => {
  it('should return expected when given valid input', () => {
    expect(myUtil('a')).toBe('expected')
  })
  it('should handle empty string', () => {
    expect(myUtil('')).toBe('')
  })
})
```

### 3. 实现代码

用最小实现使测试通过。

### 4. 运行测试

```bash
pnpm test
# 或 npm run test
```

### 5. 重构

在测试保持通过的前提下整理代码、去重、改进命名。

## 前端注意点

- 组件测试：测行为与输出，避免依赖实现细节（如内部 state 结构）
- 异步：使用 `async/await` 或 `waitFor` 处理异步更新
- Mock：API、路由、定时器按需 mock，保持测试稳定
- 快照：慎用，仅对结构稳定的 UI 使用，避免无意义变更

## 验收

- 新功能/修复有对应测试
- `pnpm test` 通过
- 边界与错误场景有覆盖
