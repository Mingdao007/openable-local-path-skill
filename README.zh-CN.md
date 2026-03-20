# Openable Local Path Skill

用于生成无空格别名路径、提升 Codex App 本地链接可点击稳定性的可移植工具 skill。

## 提供内容

- 可安装 skill: [`openable-local-path`](./openable-local-path)
- 辅助脚本: [`openable-local-path/scripts/`](./openable-local-path/scripts)

## 安装 / 使用

- `Codex App`：从本仓库路径 `openable-local-path` 安装
- GitHub 安装目标：
  - repo：`<owner>/openable-local-path-skill`
  - path：`openable-local-path`
- 安装后重启 `Codex App`，让新 skill 被发现。

## 覆盖范围

- 支持为本地文件和目录生成无空格别名路径
- 逐级创建 sibling symlink，而不移动真实目标
- 当别名冲突时提供安全回退行为

## 触发示例

- `Give me a clickable local path for this file.`
- `Repair this local link that breaks because of spaces.`
- `Create a stable openable alias path in Codex App.`

## 不触发示例

- `Return a remote URL.`
- `Rename the real file on disk.`
- `Use the raw path only inside a shell command.`

## 隐私边界

这个公开仓库只保留可复用、可公开的工作流部分。

- The helper uses generic host-relative paths and does not encode personal directory names.
- The public package preserves the low-risk symlink strategy without private path assumptions.

## 仓库结构

- `openable-local-path/`: installable `Codex App` skill
- `openable-local-path/scripts/`: bundled public scripts
- `CHANGELOG.md`: release history
- `LICENSE`: `MIT`

English:

- [README.md](./README.md)
