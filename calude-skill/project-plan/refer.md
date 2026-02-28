## 参考资料（References）

- [相关文档 1](link)
- [相关讨论 2](link)

````

## 新项目 README 模板（New Project README Template）

对于新项目，优先生成以下 README 结构：

```markdown
# [项目名称]

**创建日期**：YYYY-MM-DD

> 一句话描述项目的核心价值

## 目录
- [简介](#简介)
- [核心功能](#核心功能)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [开发指南](#开发指南)
- [测试](#测试)
- [部署](#部署)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 简介

[2-3 段详细描述项目背景、目标、解决的问题]

## 核心功能

- ✅ 功能 1：[描述]
- ✅ 功能 2：[描述]
- 🚧 功能 3：[开发中]
- 📋 功能 4：[计划中]

## 技术栈

### 后端
- [技术 1]：[版本] - [用途]
- [技术 2]：[版本] - [用途]

### 前端
- [技术 1]：[版本] - [用途]
- [技术 2]：[版本] - [用途]

### 基础设施
- [工具 1]：[用途]
- [工具 2]：[用途]

## 项目结构

````

project-root/
├── src/ # 源代码
│ ├── components/ # 组件
│ ├── services/ # 业务逻辑
│ └── utils/ # 工具函数
├── tests/ # 测试文件
├── docs/ # 文档
└── config/ # 配置文件

````

## 快速开始

### 前置要求

- Node.js >= 16.0
- npm >= 8.0
- [其他依赖]

### 安装

```bash
# 克隆项目
git clone [repository-url]

# 安装依赖
npm install

# 配置环境变量
cp .env.example .env
````

### 运行

```bash
# 开发模式
npm run dev

# 生产构建
npm run build

# 启动生产服务
npm start
```

## 配置说明

[环境变量、配置文件的详细说明]

## 开发指南

### 代码规范

- [规范 1]
- [规范 2]

### 分支策略

- `main`：生产分支
- `develop`：开发分支
- `feature/*`：功能分支

### 提交规范

```
feat: 新功能
fix: Bug 修复
docs: 文档更新
style: 代码格式
refactor: 重构
test: 测试
chore: 构建/工具
```

## 测试

```bash
# 运行所有测试
npm test

# 运行单元测试
npm run test:unit

# 运行集成测试
npm run test:integration

# 生成覆盖率报告
npm run test:coverage
```

## 部署

[部署流程和说明]

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交变更 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

[许可证类型]

````

## 最佳实践（Best Practices）

1. **主动确认需求**：在开始详细规划前，必须与用户确认需求理解
2. **务必具体**：使用确切的文件路径、函数名、变量名
3. **考虑边缘情况**：思考错误场景、空值（null values）、空状态
4. **最小化变更**：优先考虑扩展现有代码而非重写
5. **保持模式**：遵循现有的项目规范（Conventions）
6. **支持测试**：构建易于测试的变更结构
7. **增量思维**：每一步都应该是可验证的
8. **记录决策**：解释"为什么"做，而不仅仅是"做了什么"
9. **文档优先**：所有规划必须输出为 Markdown 文件
10. **索引维护**：更新项目文档后，同步更新 `docs/README.md` 索引
11. **互动优先**：模糊的需求必须先确认，不要假设用户意图

## 规划重构时的注意事项（When Planning Refactors）

1. 识别代码异味（Code Smells）和技术债（Technical Debt）
2. 列出需要的具体改进
3. 保留现有功能
4. 尽可能创建向下兼容的变更
5. 如有必要，规划渐进式迁移
6. **输出重构方案文档**到 `docs/architecture/REFACTOR_[功能名].md`

## 需检查的负面信号（Red Flags to Check）

- 过大的函数（>50 行）
- 过深的嵌套（>4 层）
- 重复代码
- 缺失错误处理
- 硬编码（Hardcoded）数值
- 缺失测试
- 性能瓶颈
- 文档缺失或过时

## 输出清单（Output Checklist）

在完成规划后，确保：

### 需求确认阶段
- [ ] 已向用户展示需求理解
- [ ] 已标注不确定的点并提问
- [ ] 已收到用户明确确认
- [ ] 已记录用户的选择和偏好

### 文档输出阶段
- [ ] 已生成完整的实施方案文档
- [ ] 文档已保存到正确的目录（`docs/[分类]/[文件名].md`）
- [ ] 文档包含创建日期和目录
- [ ] 新项目已生成 README.md
- [ ] 架构图使用 mermaid 格式
- [ ] 已更新 `docs/changelog/CHANGELOG.md`
- [ ] 如需要，已更新 `docs/README.md` 索引

### 规划质量检查
- [ ] **确认没有编写任何实现代码**
- [ ] **确认没有创建测试文件**
- [ ] 所有步骤都有明确的文件路径
- [ ] 所有依赖关系都已标注
- [ ] 风险评估已完成
- [ ] 验收标准清晰可验证

## 互动确认要点（Interaction Key Points）

### 何时需要确认
- 🔴 **必须确认**：需求模糊、技术选型、功能范围不明确、优先级需要明确
- 🟢 **可以直接规划**：需求非常明确且具体、只有一种合理实现方式、标准功能

### 提问技巧
1. **使用多选题**：比开放式问题更容易回答
2. **提供上下文**：解释每个选项的优缺点
3. **分优先级**：区分必须回答和可选问题（可提供默认值）

### 确认后的行动
- ✅ **收到确认**：立即开始详细规划，记录确认的选择
- ❌ **未收到确认**：不进行详细规划，等待用户回复

## 文档索引维护（Documentation Index Maintenance）

当创建新文档时，更新 `docs/README.md`：

```markdown
# 项目文档索引

## 变更日志
- [CHANGELOG.md](changelog/CHANGELOG.md) - 项目变更历史

## 架构设计
- [系统架构](architecture/SYSTEM_ARCHITECTURE.md)
- [用户认证架构](architecture/USER_AUTH_ARCHITECTURE.md)

## 功能文档
- [用户认证](features/USER_AUTH_FEATURE.md)
- [数据导出](features/DATA_EXPORT_FEATURE.md)

## Bug 修复
- [登录 500 错误](bugfix/BUGFIX_LOGIN_500.md)
- [V1.2.3 Bug 修复](bugfix/BUGFIX_V1.2.3.md)

## 性能优化
- [数据库查询优化](performance/PERFORMANCE_DB_QUERY.md)

## 需求文档
- [Todo 应用需求](requirements/REQUIREMENTS_TODO_APP.md)
````

**记住**：

- 一个优秀的方案是具体、可操作的，并且兼顾正常流程（Happy Path）与边缘情况
- 最佳方案应当能支撑起充满信心的增量实现
- **所有规划文档必须输出到文件系统，不能只在对话中展示**
- **新项目必须先生成 README，再进行详细规划**
- **规划阶段绝不编写实现代码或测试，保持纯粹的设计与思考**
