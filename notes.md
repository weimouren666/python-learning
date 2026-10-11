# 学习笔记

## 2026-10-11

### 今日所学
- Git 基本工作流：`add` → `commit` → `push`
- GitHub 仓库的创建与克隆

### 踩坑记录
- Git 连接 GitHub 报 `CRYPT_E_NO_REVOCATION_CHECK` 错误：
  原因是网络无法访问证书吊销检查服务器，用
  `git -c http.schannelCheckRevoke=false clone ...` 解决。

### 待办
- [ ] 运行第一个 Python 程序 hello.py
