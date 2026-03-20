#!/usr/bin/env python3
import argparse
import json
import os
import pathlib
import re
import sys


def sanitize(name: str) -> str:
    return re.sub(r"\s+", "_", name.strip())


def is_same_target(alias_path: pathlib.Path, target_path: pathlib.Path) -> bool:
    try:
        return alias_path.resolve(strict=True) == target_path.resolve(strict=True)
    except FileNotFoundError:
        return False


def ensure_openable_path(target: pathlib.Path) -> pathlib.Path:
    if not target.is_absolute():
        raise ValueError("path must be absolute")
    if not target.exists():
        raise FileNotFoundError(f"target does not exist: {target}")

    alias_cursor = pathlib.Path("/")
    actual_cursor = pathlib.Path("/")

    for component in target.parts[1:]:
        actual_child = actual_cursor / component

        if re.search(r"\s", component):
            alias_name = sanitize(component)
            alias_child = alias_cursor / alias_name

            if alias_child.exists() or alias_child.is_symlink():
                if not is_same_target(alias_child, actual_child):
                    raise RuntimeError(
                        f"alias collision: {alias_child} already exists and does not point to {actual_child}"
                    )
            else:
                os.symlink(component, alias_child)

            alias_cursor = alias_child
        else:
            alias_cursor = alias_cursor / component

        actual_cursor = actual_child

    return alias_cursor


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ensure a no-space alias path for a local file or directory."
    )
    parser.add_argument("path", help="Absolute path to a local file or directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    target = pathlib.Path(args.path).expanduser()

    try:
        alias = ensure_openable_path(target)
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}))
        else:
            print(str(exc), file=sys.stderr)
        return 1

    if args.json:
        print(
            json.dumps(
                {
                    "ok": True,
                    "target": str(target),
                    "openable_path": str(alias),
                    "changed": str(alias) != str(target),
                }
            )
        )
    else:
        print(str(alias))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
