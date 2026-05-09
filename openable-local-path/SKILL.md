---
name: openable-local-path
description: Use when you need to return, open, or reference a local filesystem path in the Codex app, especially for clickable links to files or folders. Ensure a no-space alias path exists before returning the link so local Markdown file references open reliably instead of rendering blank due to path whitespace.
---

# Openable Local Path

## Overview

This skill makes local file references safer in the Codex app by ensuring that
the returned path has no whitespace in any linked path segment. It creates
low-risk sibling symlink aliases with underscores when needed, then uses the
alias path as the primary user-facing link.

## When To Use

Use this skill whenever the task needs a clickable local file or folder path,
including:

- returning a local `.md`, `.pdf`, image, or source-file link in the final answer
- giving the user a path to open inside the Codex app
- repairing a previously blank or unreliable local link caused by spaces in the path
- preparing a stable local path for repeated future references

Do not use this skill for:

- remote URLs
- paths that are only being mentioned in shell commands, logs, or code samples
- cases where the user explicitly wants the raw original path only

## Workflow

1. Start from the real absolute target path.
2. Run the helper script on that target:

```bash
python3 $CODEX_HOME/skills/openable-local-path/scripts/ensure_openable_path.py "<absolute-path>"
```

3. If the script succeeds, use the returned alias path as the primary link.
4. If the script reports a name collision, do not overwrite anything. Fall back
   to the raw absolute path on its own line and mention the collision briefly.
5. When the alias path differs from the original path, prefer the alias in
   Markdown links and keep the raw absolute path available in plain text only if
   it adds value.

## Output Rules

- Default behavior: never use a whitespace-containing path as the primary local
  Markdown link if an alias can be created safely.
- Prefer one clean alias path over explanations about why the link might fail.
- Keep the alias stable. Reuse an existing matching alias instead of creating a
  new variant.
- Only create sibling symlinks that replace whitespace with underscores. Do not
  rename, move, or copy the real file or folder.

## Notes

- The helper script operates component-by-component, so it can produce a fully
  openable path even when multiple directories or the filename itself contain
  spaces.
- Existing valid aliases are reused.
- Conflicting pre-existing names are treated as a stop condition for alias
  creation, not as something to overwrite.


## Validation And Checkpoints

- Before final handoff, validate the requested artifact or decision against this skill's output contract and report the verification result explicitly.
- Before any local mutation, pass the recoverability gate: create a rollback point when the change is reversible, and request confirmation when backup cannot cover the risk.
- Use an explicit checkpoint when required input is missing, tool evidence conflicts, or repeated attempts fail; wait for approval or route to the named owner instead of guessing.
- For multi-session work, update a progress or HANDOFF artifact with current state, verified result, and next executable step.
- For L1/default-triggered work, if the path fails or becomes ambiguous, stop the default route, state the failure, and provide recovery options instead of expanding scope silently.
