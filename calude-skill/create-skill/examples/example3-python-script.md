# 示例3：创建带Python脚本的数据分析Skill

## 场景描述
用户想创建一个数据分析skill，需要进行复杂的数据处理和统计计算，因此需要Python脚本支持。

## 使用过程

### 用户输入的需求
```
需求：创建一个项目代码统计分析skill
功能：
- 统计项目代码行数
- 分析编程语言分布
- 计算代码复杂度
- 生成可视化报告
输入：项目目录路径
输出：详细的统计报告（Markdown格式）
实现：需要Python处理复杂逻辑
```

### 系统引导问题与回答

**问题1：Skill基本信息**
- Skill名称：`code-stats-analyzer`
- Skill描述：项目代码统计分析器，提供代码行数、语言分布、复杂度等详细报告
- 主要用途：快速了解项目规模和代码结构特征

**问题2：功能详情**
- 核心功能：
  1. 统计各类文件的代码行数
  2. 分析编程语言使用比例
  3. 识别最大/最复杂的文件
  4. 生成Markdown格式报告
  5. 排除node_modules、.git等无关目录
- 输入要求：
  - 项目根目录路径
  - 可选：要分析的文件扩展名
- 输出格式：结构化的Markdown统计报告

**问题3：实现方式**
- ✅ Markdown + Python脚本

**问题4：附加选项**
- ✅ 需要用户交互确认
- ✅ 需要示例文件
- ❌ 不需要配置文件
- ✅ 需要错误处理

### 系统生成的需求确认

```
📋 Skill创建需求确认
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Skill名称: code-stats-analyzer
📝 功能描述: 项目代码统计分析器，提供代码行数、语言分布、复杂度等详细报告

🎯 核心功能:
1. 统计各类文件的代码行数
2. 分析编程语言使用比例
3. 识别最大/最复杂的文件
4. 生成Markdown格式报告
5. 排除node_modules、.git等无关目录

📥 输入要求:
- 项目根目录路径
- 可选：要分析的文件扩展名

📤 输出格式:
结构化的Markdown统计报告

🛠️  实现方式:
- 主文件: skill.md
- 脚本: analyze.py
- 附加: 示例文件

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 确认无误，开始生成
```

### 生成的文件结构

```
code-stats-analyzer/
├── skill.md              # 核心skill定义
├── scripts/
│   └── analyze.py        # Python脚本：代码分析逻辑
├── examples/
│   ├── example-output.md # 示例输出报告
│   └── usage.md          # 使用示例
└── README.md             # 使用文档
```

### 生成的脚本示例

**analyze.py**:
```python
#!/usr/bin/env python3
"""
项目代码统计分析器
分析项目中的代码文件，生成统计报告
"""

import os
import sys
from pathlib import Path
from collections import defaultdict
import argparse

# 要排除的目录
EXCLUDE_DIRS = {
    'node_modules', '.git', '__pycache__', 'venv', '.venv',
    'dist', 'build', '.next', '.cache', 'coverage'
}

# 语言到文件扩展名的映射
LANGUAGE_MAP = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.jsx': 'JavaScript (JSX)',
    '.tsx': 'TypeScript (TSX)',
    '.java': 'Java',
    '.cpp': 'C++',
    '.c': 'C',
    '.h': 'C/C++ Header',
    '.go': 'Go',
    '.rs': 'Rust',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.md': 'Markdown',
    '.html': 'HTML',
    '.css': 'CSS',
    '.scss': 'SCSS',
}

class CodeAnalyzer:
    def __init__(self, root_path):
        self.root_path = Path(root_path).resolve()
        self.stats = {
            'total_files': 0,
            'total_lines': 0,
            'language_stats': defaultdict(lambda: {'files': 0, 'lines': 0}),
            'largest_files': []
        }

    def should_exclude(self, path):
        """检查路径是否应该被排除"""
        parts = path.parts
        return any(excluded in parts for excluded in EXCLUDE_DIRS)

    def count_lines(self, file_path):
        """计算文件行数"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for line in f if line.strip())
        except Exception as e:
            print(f"警告: 无法读取文件 {file_path}: {e}", file=sys.stderr)
            return 0

    def analyze(self):
        """执行分析"""
        print(f"正在分析项目: {self.root_path}")

        for file_path in self.root_path.rglob('*'):
            # 跳过目录和排除的路径
            if not file_path.is_file() or self.should_exclude(file_path):
                continue

            # 获取文件扩展名
            ext = file_path.suffix.lower()
            if ext not in LANGUAGE_MAP:
                continue

            # 统计行数
            line_count = self.count_lines(file_path)
            if line_count == 0:
                continue

            # 更新统计
            language = LANGUAGE_MAP[ext]
            self.stats['total_files'] += 1
            self.stats['total_lines'] += line_count
            self.stats['language_stats'][language]['files'] += 1
            self.stats['language_stats'][language]['lines'] += line_count

            # 记录大文件
            relative_path = file_path.relative_to(self.root_path)
            self.stats['largest_files'].append({
                'path': str(relative_path),
                'lines': line_count,
                'language': language
            })

        # 排序最大文件
        self.stats['largest_files'].sort(key=lambda x: x['lines'], reverse=True)
        self.stats['largest_files'] = self.stats['largest_files'][:10]

    def generate_report(self):
        """生成Markdown报告"""
        report = []
        report.append("# 📊 项目代码统计报告\n")
        report.append(f"**项目路径**: `{self.root_path}`\n")
        report.append("---\n")

        # 总览
        report.append("## 📈 总览\n")
        report.append(f"- **总文件数**: {self.stats['total_files']}")
        report.append(f"- **总代码行数**: {self.stats['total_lines']:,}\n")

        # 语言分布
        report.append("## 🌐 编程语言分布\n")
        report.append("| 语言 | 文件数 | 代码行数 | 占比 |")
        report.append("|------|--------|----------|------|")

        sorted_langs = sorted(
            self.stats['language_stats'].items(),
            key=lambda x: x[1]['lines'],
            reverse=True
        )

        for language, data in sorted_langs:
            percentage = (data['lines'] / self.stats['total_lines'] * 100) if self.stats['total_lines'] > 0 else 0
            report.append(
                f"| {language} | {data['files']} | {data['lines']:,} | {percentage:.1f}% |"
            )

        report.append("")

        # 最大的文件
        report.append("## 📁 代码行数最多的文件 (Top 10)\n")
        report.append("| 文件路径 | 代码行数 | 语言 |")
        report.append("|----------|----------|------|")

        for file_info in self.stats['largest_files']:
            report.append(
                f"| `{file_info['path']}` | {file_info['lines']:,} | {file_info['language']} |"
            )

        report.append("")
        report.append("---")
        report.append("*报告生成时间: " +
                     __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "*")

        return '\n'.join(report)

def main():
    parser = argparse.ArgumentParser(description='项目代码统计分析器')
    parser.add_argument('path', help='项目根目录路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')

    args = parser.parse_args()

    # 验证路径
    if not os.path.isdir(args.path):
        print(f"错误: 路径不存在或不是目录: {args.path}", file=sys.stderr)
        sys.exit(1)

    # 执行分析
    analyzer = CodeAnalyzer(args.path)
    analyzer.analyze()

    # 生成报告
    report = analyzer.generate_report()

    # 输出或保存
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ 报告已保存到: {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()
```

## 关键要点

1. **Python适用场景**：
   - 需要复杂数据处理
   - 需要文件系统遍历
   - 需要统计和计算
   - 需要生成格式化输出

2. **脚本设计原则**：
   - 使用类组织代码逻辑
   - 完善的错误处理
   - 清晰的进度反馈
   - 支持命令行参数
   - 输出格式化的结果

3. **skill.md与脚本交互**：
```markdown
### 执行步骤
1. 询问用户项目路径
2. 确认要分析的内容
3. 调用Python脚本: `python scripts/analyze.py [path] -o report.md`
4. 读取生成的报告
5. 向用户展示分析结果
6. 提供优化建议
```

4. **依赖管理**：
   - 使用Python标准库（避免外部依赖）
   - 如需第三方库，在README中说明安装方法

## 预期效果

生成的skill可以：
1. 接收用户输入的项目路径
2. 执行Python脚本进行深度分析
3. 生成专业的统计报告
4. 提供基于数据的改进建议
5. 处理各种边界情况和错误

## 使用示例

```bash
# 分析当前项目
python scripts/analyze.py . -o stats.md

# 分析指定项目
python scripts/analyze.py /path/to/project
```

## 输出示例

```markdown
# 📊 项目代码统计报告

**项目路径**: `/home/user/my-project`

---

## 📈 总览

- **总文件数**: 156
- **总代码行数**: 23,458

## 🌐 编程语言分布

| 语言 | 文件数 | 代码行数 | 占比 |
|------|--------|----------|------|
| TypeScript | 89 | 15,234 | 64.9% |
| JavaScript | 32 | 4,567 | 19.5% |
| CSS | 18 | 2,345 | 10.0% |
| Python | 12 | 987 | 4.2% |
| Markdown | 5 | 325 | 1.4% |

## 📁 代码行数最多的文件 (Top 10)

| 文件路径 | 代码行数 | 语言 |
|----------|----------|------|
| `src/components/Dashboard.tsx` | 1,234 | TypeScript |
| `src/utils/dataProcessor.ts` | 987 | TypeScript |
...
```
