# 学习笔记

## 2026-11-01

### 今日所学
- 仓库整理：study 文件夹按知识点拆成 5 类（变量/条件/循环/实战/列表）
- 第一次独立完成 `add → commit → push` 全流程（commit cd2f817）
- 给电脑正式安装了 Git 2.56（之前用的都是 WorkBuddy 内置版）

### 知识点速记
- for + range：`range(1, 100, 7)` 从 1 到 99 步长 7
- 嵌套循环：99 乘法表内循环 `range(1, i+1)` 才是三角形
- while True + break：猜数字游戏的标准写法
- 列表：下标从 0 开始；`scores[-1]` 是最后一个；切片含头不含尾

### 踩坑记录
- （接上）HTTPS 连 GitHub 报证书错误 → 改用 SSH 443 端口，一劳永逸
- VS 的 `.vs` 缓存文件夹不要上传，已写进 `.gitignore`

## 2026-10-15

### 第 1 周实战：个人健康卡片
- 综合运用：input 转型（int/float）、BMI 公式、if/elif 分支、f-string
- 成果：`study/04_实战/shizhan1.py`

## 2026-10-13

### 条件判断
- if / elif / else 写成绩等级判定
- 真值测试：空字符串是 False（kongmingzi.py）

## 2026-10-11

### 今日所学
- Git 基本工作流：`add` → `commit` → `push`
- GitHub 仓库的创建与克隆、SSH 免密配置
- 把云端课程代码同步到 GitHub

### 踩坑记录
- Git 连接 GitHub 报 `CRYPT_E_NO_REVOCATION_CHECK` 错误：
  HTTPS 连接被网络环境干扰，改用 SSH（443 端口）解决，
  配置在 `~/.ssh/config`，密钥为 ed25519。

### 课程进度（来自云端辅导课）
- 第一课「变量与数据类型」已完成
- 第 1 周实战「个人信息卡片生成器」已完成

### 待办
- [ ] 完成班级成绩小统计作业
