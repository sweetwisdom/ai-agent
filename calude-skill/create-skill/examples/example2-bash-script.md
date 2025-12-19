# 示例2：创建带Bash脚本的Git辅助Skill

## 场景描述
用户想创建一个Git操作辅助skill，需要执行实际的git命令，因此需要Bash脚本支持。

## 使用过程

### 用户输入的需求
```
需求：创建一个Git辅助工具skill
功能：
- 快速创建特性分支
- 自动设置分支关联
- 生成标准化的分支命名
输入：特性名称、分支类型（feature/bugfix/hotfix）
输出：创建的分支信息和后续操作建议
实现：需要执行git命令
```

### 系统引导问题与回答

**问题1：Skill基本信息**
- Skill名称：`git-branch-helper`
- Skill描述：智能Git分支管理助手，快速创建标准化命名的特性分支
- 主要用途：简化Git分支创建流程，确保命名规范统一

**问题2：功能详情**
- 核心功能：
  1. 创建符合规范的分支名称
  2. 自动从main/master分支创建
  3. 设置远程跟踪分支
  4. 提供后续操作建议
- 输入要求：
  - 特性名称（如：user-authentication）
  - 分支类型（feature/bugfix/hotfix）
- 输出格式：分支创建结果 + 操作指南

**问题3：实现方式**
- ✅ Markdown + Bash脚本

**问题4：附加选项**
- ✅ 需要用户交互确认
- ✅ 需要示例文件
- ❌ 不需要配置文件
- ✅ 需要错误处理

### 系统生成的需求确认

```
📋 Skill创建需求确认
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Skill名称: git-branch-helper
📝 功能描述: 智能Git分支管理助手，快速创建标准化命名的特性分支

🎯 核心功能:
1. 创建符合规范的分支名称
2. 自动从main/master分支创建
3. 设置远程跟踪分支
4. 提供后续操作建议

📥 输入要求:
- 特性名称（如：user-authentication）
- 分支类型（feature/bugfix/hotfix）

📤 输出格式:
分支创建结果 + 操作指南

🛠️  实现方式:
- 主文件: skill.md
- 脚本: create-branch.sh
- 附加: 示例文件

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 确认无误，开始生成
```

### 生成的文件结构

```
git-branch-helper/
├── skill.md              # 核心skill定义
├── scripts/
│   └── create-branch.sh  # Bash脚本：执行git命令
├── examples/
│   ├── example1.md       # 创建feature分支示例
│   └── example2.md       # 创建bugfix分支示例
└── README.md             # 使用文档
```

### 生成的脚本示例

**create-branch.sh**:
```bash
#!/bin/bash
# Git分支创建辅助脚本

set -e

# 参数检查
if [ $# -lt 2 ]; then
    echo "用法: $0 <分支类型> <特性名称>"
    echo "分支类型: feature, bugfix, hotfix"
    exit 1
fi

BRANCH_TYPE=$1
FEATURE_NAME=$2

# 验证分支类型
if [[ ! "$BRANCH_TYPE" =~ ^(feature|bugfix|hotfix)$ ]]; then
    echo "错误: 分支类型必须是 feature, bugfix 或 hotfix"
    exit 1
fi

# 生成分支名称
BRANCH_NAME="${BRANCH_TYPE}/${FEATURE_NAME}"

# 检查是否在git仓库中
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "错误: 当前目录不是Git仓库"
    exit 1
fi

# 获取默认分支
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# 更新主分支
echo "正在更新 ${DEFAULT_BRANCH}..."
git checkout $DEFAULT_BRANCH
git pull origin $DEFAULT_BRANCH

# 创建新分支
echo "正在创建分支: ${BRANCH_NAME}..."
git checkout -b $BRANCH_NAME

echo "✅ 分支创建成功: ${BRANCH_NAME}"
echo ""
echo "📝 后续步骤:"
echo "1. 进行开发工作"
echo "2. 提交更改: git add . && git commit -m 'your message'"
echo "3. 推送到远程: git push -u origin ${BRANCH_NAME}"
```

## 关键要点

1. **脚本必要性**：需要执行系统命令时使用脚本
2. **错误处理**：脚本包含参数验证和错误检查
3. **用户反馈**：脚本输出清晰的执行状态
4. **安全性**：使用 `set -e` 在错误时停止执行

## skill.md中如何调用脚本

在skill.md的"AI执行指令"部分：
```markdown
### 执行步骤
1. 收集用户输入（分支类型和特性名称）
2. 验证输入有效性
3. 调用脚本: `bash scripts/create-branch.sh [type] [name]`
4. 解析脚本输出
5. 向用户展示结果和后续建议
```

## 预期效果

生成的skill可以：
1. 通过AI收集用户输入
2. 执行Bash脚本完成实际操作
3. 提供友好的反馈和指导
4. 处理各种错误情况
