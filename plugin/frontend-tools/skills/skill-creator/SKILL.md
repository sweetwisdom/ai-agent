---
name: skill-creator
description: 创建有效技能的指南。当用户想要创建新技能（或更新现有技能）以扩展 Claude 的能力时使用此技能，包括专业知识、工作流程或工具集成。
---

# 技能创建器

此技能提供创建有效技能的指导。与 cpp-qt-tools 插件中的 skill-creator 结构一致；若需 init_skill.py、package_skill.py 等脚本，可参考 `plugins/cpp-qt-tools/skills/skill-creator/`。

## 关于技能

技能是模块化、自包含的包，通过提供专业知识、工作流程和工具来扩展 Claude 的能力。可将它们视为特定领域或任务的「入职指南」。

### 技能提供什么

1. 专业工作流程 - 特定领域的多步骤程序
2. 工具集成 - 处理特定文件格式或 API 的说明
3. 领域专业知识 - 公司特定知识、模式、业务逻辑
4. 捆绑资源 - 脚本、参考资料、资产

## 技能结构

```
skill-name/
├── SKILL.md（必需）
│   ├── YAML 前置元数据：name、description（必需）
│   └── Markdown 说明（必需）
└── 可选：scripts/、references/、assets/
```

- **name** 与 **description**：Claude 据此判断何时使用技能，description 中写清「做什么、何时触发」。
- 正文保持精简，将详细示例与参考放入 references/，需要时再加载。

## 创建流程（简要）

1. 通过具体示例理解技能用途与触发场景
2. 规划可复用内容（脚本、参考资料、资产）
3. 初始化目录与 SKILL.md 模板（可用 cpp-qt-tools 的 init_skill.py）
4. 编写 SKILL.md 与资源，确保描述清晰、示例简洁
5. 打包与验证（可用 cpp-qt-tools 的 package_skill.py）
6. 根据使用反馈迭代

## 原则

- **简洁**：只写 Claude 尚不知道且对执行任务有用的内容
- **渐进披露**：元数据常驻，正文在触发时加载，大块资料放 references/ 按需读取
- **自由度适中**：按任务脆弱程度选择「纯说明 / 伪代码+参数 / 固定脚本」

用户说「帮我写一个 xxx 技能」或「如何创建 skill」时，按上述流程引导并协助产出 SKILL.md 与必要资源。
