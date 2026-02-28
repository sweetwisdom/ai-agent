# Git 工作流规范

## Commit 消息格式

```
<type>: <description>

<optional body>
```

### 类型说明

| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | Bug 修复 |
| refactor | 重构（不改变功能） |
| docs | 文档更新 |
| test | 测试相关 |
| chore | 构建/工具变更 |
| perf | 性能优化 |
| ci | CI/CD 配置 |
| style | 代码风格（不影响逻辑） |

### 示例

```
feat: 新增用户设置持久化

fix: 修复列表在空数据时报错

perf: 路由级懒加载减少首屏 bundle
```

## Pull Request 工作流

1. 分析完整的 commit 历史（不仅是最新 commit）
2. 使用 `git diff [base-branch]...HEAD` 查看所有变更
3. 编写 PR 摘要，包含：变更概述、测试/自测说明
4. 新分支推送时使用 `-u` 标志

## 分支管理

- `main`：主分支，稳定版本
- `develop`：开发分支
- `feature/*`：功能分支
- `fix/*`：修复分支

## 提交前检查

- [ ] 代码已通过构建：`pnpm build`
- [ ] 已通过校验：`pnpm lint`
- [ ] 有测试时通过测试：`pnpm test`
- [ ] 无调试代码残留
- [ ] Commit 消息符合规范
