分析粘贴的构建/校验错误，定位根因并修复，修复后验证通过。

## 执行步骤

1. **分析错误**：识别错误类型（依赖安装失败、TypeScript 类型/配置错误、ESLint 报错、Vite/Webpack 构建错误）
2. **定位根因**：找到真正的根因（不是症状），说明为什么会出现这个错误
3. **制定修复方案**：如有多种修复方式，列出选项并说明取舍
4. **执行修复**：修改相关文件
5. **验证**：运行构建与校验命令确认错误消除

## 常见前端错误处理指引

**npm/pnpm install 失败**
- 检查 Node 版本、lockfile 是否一致
- 清除缓存后重试：`pnpm store prune` 或 `npm cache clean --force`
- 检查是否有私有源、镜像配置问题

**TypeScript 类型错误**
- 从第一个报错开始修，类型错误常有连锁反应
- 检查 tsconfig.json：strict、paths、include/exclude
- 避免用 `as any` 掩盖问题，优先补全类型或使用 unknown + 收窄

**ESLint 报错**
- 区分 error 与 warning，先修阻塞构建的 error
- 规则若与 Prettier 冲突，确认 eslint-config-prettier 已启用
- 必要时在合理处使用 eslint-disable，并注明原因

**Vite/Webpack 构建错误**
- 模块找不到：检查 alias、resolve.extensions、依赖是否安装
- 动态 import 路径：确保路径在构建时可解析
- 环境变量：确保以 VITE_ 前缀暴露给客户端（Vite）

修复完成后，运行：

```bash
pnpm install  # 若修改了依赖
pnpm build
pnpm lint
```

确认无错误输出；若有测试，再运行 `pnpm test`。
