# Openable Local Path Skill

可移植的本地路径 utility skill，用于生成无空格 alias path，让 Codex App 中的本地链接更可靠打开。

## 适合谁

| 适合使用 | 不适合使用 |
| --- | --- |
| 需要在 Codex App 中返回可点击的本地文件或文件夹链接 | 需要 remote URL |
| 需要不移动真实文件的 whitespace-safe alias path | 想重命名或移动真实文件 |
| 需要带 collision check 的逐组件 symlink 创建 | 只在 shell command 里使用 raw path |

## 为什么需要它

- Codex App 本地链接可能因为路径段含空格而失败。
- alias path 可以避免移动真实目标。
- collision check 让 symlink 创建保持可恢复。

## 包含内容

| Component | 作用 |
| --- | --- |
| [`openable-local-path`](./openable-local-path) | 可安装的 Codex App skill package |
| [`openable-local-path/scripts`](./openable-local-path/scripts) | 随包发布的 helper scripts |
| [`openable-local-path/test-prompts.json`](./openable-local-path/test-prompts.json) | trigger / non-trigger 示例 |
| [`CHANGELOG.md`](./CHANGELOG.md) | release history |
| [`LICENSE`](./LICENSE) | license |

## 安装 / 使用

### Codex App

- 从本 repo 的这个路径安装 skill：`openable-local-path`
- GitHub install target:
  - repo: `Mingdao007/openable-local-path-skill`
  - path: `openable-local-path`
- 安装后重启 `Codex App`，让新 skill 被重新发现。

## 工作流

```mermaid
flowchart LR
    A["本地路径请求"] --> B["空格/路径检查"]
    B --> C["创建 alias"]
    C --> D["格式化链接"]
    D --> E["可打开输出"]
```

## 覆盖范围

- 为本地文件和文件夹生成 whitespace-safe alias
- 逐组件创建 symlink，不移动真实目标
- 当 alias 无法安全创建时提供 collision-aware fallback

## 预期结果 / 验证

| 检查项 | 预期结果 |
| --- | --- |
| 安装路径 | `openable-local-path` |
| GitHub target | `Mingdao007/openable-local-path-skill`，path 为 `openable-local-path` |
| Skill 入口 | 存在 `openable-local-path/SKILL.md` |
| 触发样例 | `openable-local-path/test-prompts.json` |
| 隐私检查 | 公开包不包含私人本机路径或 live user state |

## 触发示例

- `Give me a clickable local path for this file.`
- `Repair this local link that breaks because of spaces.`
- `Create a stable openable alias path in Codex App.`

## 不应触发

- `Return a remote URL.`
- `Rename the real file on disk.`
- `Use the raw path only inside a shell command.`

## 隐私边界

这个公开仓库只保留通用、可复用的 workflow。

- helper 使用通用 host-relative path，不写入个人目录名。
- 公开包保留低风险 symlink 策略，不带 private path assumptions。

## 仓库结构

| 路径 | 作用 |
| --- | --- |
| [`openable-local-path`](./openable-local-path) | 可安装的 Codex App skill package |
| [`openable-local-path/scripts`](./openable-local-path/scripts) | 随包发布的 helper scripts |
| [`openable-local-path/test-prompts.json`](./openable-local-path/test-prompts.json) | trigger / non-trigger 示例 |
| [`CHANGELOG.md`](./CHANGELOG.md) | release history |
| [`LICENSE`](./LICENSE) | license |

English:

- [README.md](./README.md)
