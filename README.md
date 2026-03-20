# Openable Local Path Skill

Portable utility skill for generating no-space alias paths that open reliably in Codex App local links.

## What Ships

- installable skill: [`openable-local-path`](./openable-local-path)
- bundled helper scripts: [`openable-local-path/scripts/`](./openable-local-path/scripts)

## Install / Use

- `Codex App`: install the skill from this repo path `openable-local-path`
- GitHub install target:
  - repo: `<owner>/openable-local-path-skill`
  - path: `openable-local-path`
- Restart `Codex App` after installation so the new skill is discovered.

## Coverage

- whitespace-safe alias generation for local files and folders
- component-by-component symlink creation without moving the real target
- collision-aware fallback behavior when an alias cannot be created safely

## Trigger Examples

- `Give me a clickable local path for this file.`
- `Repair this local link that breaks because of spaces.`
- `Create a stable openable alias path in Codex App.`

## Non-Trigger Examples

- `Return a remote URL.`
- `Rename the real file on disk.`
- `Use the raw path only inside a shell command.`

## Privacy Boundary

This public repository keeps the workflow generic and reusable.

- The helper uses generic host-relative paths and does not encode personal directory names.
- The public package preserves the low-risk symlink strategy without private path assumptions.

## Repository Layout

- `openable-local-path/`: installable `Codex App` skill
- `openable-local-path/scripts/`: bundled public scripts
- `CHANGELOG.md`: release history
- `LICENSE`: `MIT`

Chinese:

- [README.zh-CN.md](./README.zh-CN.md)
