# Create Skill - Claude Skills 创建器

> 🎯 将你的想法快速转换为符合Claude Code官方规范的标准Skills

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/create-skill)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 目录

- [简介](#简介)
- [核心特性](#核心特性)
- [快速开始](#快速开始)
- [使用指南](#使用指南)
- [示例参考](#示例参考)
- [文件结构](#文件结构)
- [最佳实践](#最佳实践)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)

## 🎯 简介

**Create Skill** 是一个智能的Claude Code skill生成器，它能够通过交互式问答引导，帮助你快速创建符合官方规范的高质量skills。无论你是想创建简单的提示词skill，还是需要配套脚本的复杂skill，这个工具都能满足你的需求。

### 为什么需要这个工具？

- ✅ **标准化**：确保生成的skill符合Claude Code官方规范
- ✅ **高效**：通过引导式问答快速收集需求，无需手动编写模板
- ✅ **完整性**：自动生成必要的文档、示例和脚本框架
- ✅ **灵活性**：支持多种实现方式（纯Markdown、Bash脚本、Python脚本）
- ✅ **可靠性**：内置二次确认机制，避免生成错误的skill

## ✨ 核心特性

### 1. 交互式需求收集
通过结构化的问题引导，帮助你理清skill的设计思路：
- Skill基本信息（名称、描述、用途）
- 功能详情（核心功能、输入输出）
- 实现方式选择
- 附加选项配置

### 2. 智能模板选择
根据你的需求自动选择最合适的实现方式：
- **纯Markdown**：适合大多数基于提示词的场景
- **Markdown + Bash**：需要执行系统命令
- **Markdown + Python**：需要复杂逻辑处理
- **自定义组合**：灵活搭配多种方式

### 3. 二次确认机制
生成前展示完整的需求摘要，确保准确理解：
```
📋 Skill创建需求确认
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Skill名称: your-skill-name
📝 功能描述: ...
🎯 核心功能: ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. 完整文件生成
一次生成所有必要的文件：
- `skill.md` - 核心skill定义文件
- `scripts/` - 配套的Bash/Python脚本（如需要）
- `examples/` - 使用示例文件
- `README.md` - 详细的使用文档

## 🚀 快速开始

### 安装

#### 方式1：复制到Claude Code skills目录（推荐）
```bash
# 复制整个create-skill目录到Claude Code的skills目录
cp -r create-skill ~/.claude/skills/

# 或者在Windows上
xcopy /E /I create-skill %USERPROFILE%\.claude\skills\create-skill
```

#### 方式2：在当前项目中使用
```bash
# 直接在当前目录使用（适合临时使用）
# 确保create-skill目录在你的工作目录中
```

### 第一次使用

1. **启动Claude Code**

2. **调用skill**
   ```
   使用create-skill创建一个新的skill
   ```

3. **回答引导问题**
   - Skill名称（使用小写字母+连字符，如：my-awesome-skill）
   - 功能描述（简明扼要地说明skill的作用）
   - 核心功能列表
   - 输入输出要求
   - 实现方式选择

4. **确认并生成**
   - 查看生成的需求摘要
   - 确认无误后开始生成
   - 获得完整的skill文件

## 📖 使用指南

### 详细使用流程

#### 阶段1：准备工作

在开始创建skill之前，建议你先思考以下问题：

1. **明确目标**
   - 这个skill要解决什么具体问题？
   - 谁会使用这个skill？在什么场景下使用？

2. **功能范围**
   - 核心功能是什么？（2-5个主要功能点）
   - 不包含哪些功能？（避免功能蔓延）

3. **输入输出**
   - 需要用户提供什么信息？
   - 期望输出什么样的结果？

#### 阶段2：创建skill

1. **启动创建流程**
   ```
   我想创建一个skill，功能是[简要描述]
   ```

2. **回答基本信息问题**
   - **Skill名称**：遵循命名规范
     - ✅ 正确：`code-review-skill`, `git-helper`, `data-analyzer`
     - ❌ 错误：`CodeReview`, `git_helper`, `data analyzer`

   - **功能描述**：20-50字，清晰说明用途
     - ✅ 正确：智能代码审查助手，提供质量、性能和安全建议
     - ❌ 错误：审查代码（太简短）

   - **主要用途**：说明使用场景
     - 例如：帮助开发者在提交代码前发现潜在问题

3. **回答功能详情问题**
   - **核心功能**：具体列出功能点
     ```
     1. 检查代码风格和命名规范
     2. 识别常见的性能问题
     3. 检测安全漏洞
     4. 提供改进建议
     ```

   - **输入要求**：明确输入格式
     ```
     - 代码文件路径或代码片段
     - 可选：编程语言类型
     - 可选：检查严格程度（高/中/低）
     ```

   - **输出格式**：定义输出结构
     ```
     Markdown格式的审查报告，包含：
     - 问题列表（按严重程度分类）
     - 每个问题的详细说明
     - 具体的修复建议
     - 整体代码质量评分
     ```

4. **选择实现方式**

   根据功能需求选择合适的实现方式：

   | 实现方式 | 适用场景 | 示例 |
   |---------|---------|------|
   | **纯Markdown** | 基于提示词的分析、生成、建议任务 | 代码审查、文档生成、架构建议 |
   | **Markdown + Bash** | 需要执行git、文件操作等系统命令 | Git辅助、文件批处理、环境检查 |
   | **Markdown + Python** | 需要复杂数据处理、统计计算 | 代码统计、日志分析、数据转换 |
   | **自定义组合** | 特殊需求 | 根据具体情况灵活组合 |

5. **配置附加选项**
   - ✅ 用户交互确认：让用户在执行前确认操作
   - ✅ 示例文件：提供使用示例（强烈推荐）
   - ✅ 配置文件：需要复杂配置时使用
   - ✅ 错误处理：说明异常情况的处理方式

6. **确认需求摘要**

   仔细检查生成的需求摘要，确保：
   - ✅ Skill名称符合规范
   - ✅ 功能描述准确清晰
   - ✅ 核心功能完整无遗漏
   - ✅ 输入输出定义明确
   - ✅ 实现方式选择恰当

   如有问题，选择"需要修改"并说明具体内容。

7. **生成并验证**

   skill生成后，系统会显示：
   ```
   ✅ Skill创建成功！

   📁 生成的文件：
   ├── skill.md              [核心skill定义]
   ├── scripts/              [脚本文件（如有）]
   ├── examples/             [使用示例]
   └── README.md             [使用文档]
   ```

#### 阶段3：安装使用

1. **移动到Claude Code目录**
   ```bash
   # Linux/Mac
   mv your-skill-name ~/.claude/skills/

   # Windows
   move your-skill-name %USERPROFILE%\.claude\skills\
   ```

2. **测试skill**
   ```
   使用[skill名称]处理[测试任务]
   ```

3. **根据需要调整**
   - 打开 `skill.md` 调整提示词
   - 修改脚本逻辑（如有）
   - 更新示例和文档

## 💡 示例参考

### 示例1：简单的代码审查Skill
适用场景：纯提示词驱动的代码质量检查

**特点**：
- 纯Markdown实现
- 无需额外脚本
- 交互式反馈

查看完整示例：[example1-simple-skill.md](examples/example1-simple-skill.md)

### 示例2：Git分支管理Skill
适用场景：需要执行Git命令的自动化操作

**特点**：
- Markdown + Bash脚本
- 自动化Git操作
- 标准化命名规范

查看完整示例：[example2-bash-script.md](examples/example2-bash-script.md)

### 示例3：代码统计分析Skill
适用场景：需要复杂数据处理和统计计算

**特点**：
- Markdown + Python脚本
- 深度数据分析
- 生成可视化报告

查看完整示例：[example3-python-script.md](examples/example3-python-script.md)

## 📁 文件结构

```
create-skill/
├── skill.md                           # 核心skill定义文件
│                                      # 包含完整的AI执行指令
├── examples/                          # 示例目录
│   ├── example1-simple-skill.md      # 示例1：简单skill
│   ├── example2-bash-script.md       # 示例2：Bash脚本skill
│   └── example3-python-script.md     # 示例3：Python脚本skill
└── README.md                          # 本文件：使用文档
```

## 🎨 最佳实践

### 命名规范

**Skill名称**
- ✅ 使用小写字母
- ✅ 使用连字符分隔单词
- ✅ 简洁且具有描述性
- ✅ 可以使用前缀分类

```
# 好的命名
code-review-skill
git-branch-helper
data-analyzer
security-audit-tool

# 不好的命名
CodeReview          # 大写字母
git_helper          # 下划线
data analyzer       # 空格
analyzer            # 不够描述性
```

### 提示词设计

**skill.md中的AI执行指令应该**：
1. **明确具体**：清楚说明每个步骤要做什么
2. **结构化**：使用标题、列表组织内容
3. **包含示例**：展示期望的输入输出格式
4. **错误处理**：说明异常情况如何处理
5. **用户友好**：提供清晰的反馈和指导

**示例**：
```markdown
### 执行步骤
1. 读取用户提供的代码文件
2. 进行以下维度的检查：
   - 代码风格（命名规范、缩进格式）
   - 潜在bug（空指针、边界条件）
   - 性能问题（低效算法、重复计算）
   - 安全隐患（SQL注入、XSS）
3. 为每个问题生成：
   - 问题描述
   - 严重程度（高/中/低）
   - 具体位置（文件名:行号）
   - 修复建议
4. 生成总结和评分
```

### 脚本开发

**Bash脚本**：
- 使用 `set -e` 在错误时退出
- 充分的参数验证
- 清晰的错误消息
- 友好的输出格式

**Python脚本**：
- 使用类组织复杂逻辑
- 完善的异常处理
- 使用标准库避免依赖
- 添加详细的文档字符串

### 文档撰写

**README.md应该包含**：
- 清晰的功能说明
- 详细的使用步骤
- 丰富的示例
- 常见问题解答
- 更新日志

**示例文件应该**：
- 覆盖常见使用场景
- 展示实际的输入输出
- 包含解释性说明

## ❓ 常见问题

### Q1: 我应该选择哪种实现方式？

**A**: 遵循以下原则：
- **首选纯Markdown**：如果功能可以通过提示词实现，就不要用脚本
- **Bash脚本**：需要执行系统命令（git、文件操作、进程管理）
- **Python脚本**：需要复杂数据处理、统计计算、API调用

大多数情况下（约70%），纯Markdown就足够了。

### Q2: Skill名称有什么要求？

**A**:
- 必须是小写字母
- 使用连字符（-）分隔单词
- 避免使用下划线、空格或大写字母
- 长度建议在2-4个单词之间
- 应该具有描述性，让人一看就知道功能

### Q3: 如何测试生成的skill？

**A**:
1. 将skill移动到 `~/.claude/skills/` 目录
2. 重启Claude Code（如果已经在运行）
3. 使用简单的测试用例调用skill
4. 检查输出是否符合预期
5. 根据需要调整 `skill.md` 中的提示词

### Q4: 生成的skill可以修改吗？

**A**: 当然可以！生成的文件只是起点：
- 修改 `skill.md` 调整AI行为
- 修改脚本实现具体逻辑
- 添加更多示例和文档
- 根据使用反馈持续优化

### Q5: 如何处理skill之间的依赖？

**A**:
- 在 `skill.md` 的"注意事项"部分说明依赖的其他skills
- 在README中列出必需的依赖
- 如果依赖外部工具，提供安装说明
- 考虑在脚本中检查依赖是否存在

### Q6: skill生成失败怎么办？

**A**:
1. 检查需求描述是否清晰完整
2. 确认输入的信息格式正确
3. 查看错误提示，针对性修改
4. 如果多次失败，尝试简化功能范围
5. 查看示例文件获取参考

### Q7: 可以为团队创建共享的skills吗？

**A**:
可以！建议做法：
1. 将skill代码提交到Git仓库
2. 团队成员clone到本地
3. 创建符号链接到 `.claude/skills/` 目录
4. 通过PR的方式协作改进

```bash
# 创建符号链接
ln -s /path/to/team-skills/my-skill ~/.claude/skills/my-skill
```

### Q8: 如何让skill支持多语言？

**A**:
- 在 `skill.md` 的AI指令中添加语言检测逻辑
- 根据用户输入的语言选择相应的提示词
- 在示例中展示不同语言的用法
- 考虑使用配置文件存储多语言文本

## 🤝 贡献指南

欢迎贡献！如果你有改进建议或发现了问题：

### 报告问题
1. 检查是否已有类似的issue
2. 创建新issue，详细描述问题
3. 提供复现步骤和环境信息

### 提交改进
1. Fork本仓库
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 提交改动：`git commit -m "Add some feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建Pull Request

### 添加示例
欢迎提交更多有用的示例！示例应该：
- 覆盖实际的使用场景
- 包含完整的代码和说明
- 遵循现有的格式规范

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 感谢Claude Code团队提供的出色工具
- 感谢所有贡献者的支持

## 📞 联系方式

- Issue Tracker: [GitHub Issues](https://github.com/yourusername/create-skill/issues)
- 讨论区: [GitHub Discussions](https://github.com/yourusername/create-skill/discussions)

---

**Happy Skill Creating!** 🎉

如果这个工具对你有帮助，请给个 ⭐ Star 支持一下！
