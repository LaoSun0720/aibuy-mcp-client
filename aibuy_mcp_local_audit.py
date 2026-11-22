#!/usr/bin/env python3
"""Encrypted local copy of AIBuy MCP operation IDs.

The server remains the authoritative audit log. This helper only manages the
user's local copy and never talks to the AIBuy server.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import secrets
import sys
from pathlib import Path

from cryptography.fernet import Fernet


ROOT = Path(os.environ.get("AIBUY_MCP_LOCAL_AUDIT_DIR", "~/.config/aibuy-mcp")).expanduser()
KEY_PATH = ROOT / "audit.key"
LOG_PATH = ROOT / "audit.log.enc"


def _secure(path: Path, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        path.chmod(mode)
    except OSError:
        pass


def _fernet() -> Fernet:
    if not KEY_PATH.exists():
        raise SystemExit("本地密钥不存在，请先运行 init")
    return Fernet(KEY_PATH.read_bytes().strip())


def init() -> None:
    ROOT.mkdir(parents=True, exist_ok=True, mode=0o700)
    if not KEY_PATH.exists():
        KEY_PATH.write_bytes(Fernet.generate_key())
    _secure(KEY_PATH)
    if not LOG_PATH.exists():
        LOG_PATH.touch()
    _secure(LOG_PATH)
    print(json.dumps({"directory": str(ROOT), "key": str(KEY_PATH), "log": str(LOG_PATH)}, ensure_ascii=False))


def append(value: str | None) -> None:
    payload = json.loads(value) if value else json.load(sys.stdin)
    if not isinstance(payload, dict):
        raise SystemExit("日志记录必须是 JSON 对象")
    payload.setdefault("savedAt", int(__import__("time").time()))
    token = _fernet().encrypt(json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()).decode()
    with LOG_PATH.open("a", encoding="ascii") as stream:
        stream.write(token + "\n")
    _secure(LOG_PATH)
    print(payload.get("operationId", ""))


def records() -> list[dict]:
    if not LOG_PATH.exists():
        return []
    result = []
    box = _fernet()
    for line in LOG_PATH.read_text(encoding="ascii").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(box.decrypt(line.encode()).decode())
            if isinstance(item, dict):
                result.append(item)
        except Exception:
            continue
    return result


def list_records(limit: int) -> None:
    items = records()
    if limit > 0:
        items = items[-limit:]
    print(json.dumps(items, ensure_ascii=False, indent=2))


def prune(keep: int) -> None:
    items = records()
    if keep < 0:
        raise SystemExit("keep 必须大于等于 0")
    items = items[-keep:] if keep else []
    if not KEY_PATH.exists():
        init()
    box = _fernet()
    with LOG_PATH.open("w", encoding="ascii") as stream:
        for item in items:
            stream.write(box.encrypt(json.dumps(item, ensure_ascii=False, separators=(",", ":")).encode()).decode() + "\n")
    _secure(LOG_PATH)
    print(json.dumps({"kept": len(items), "deletedLocalOnly": True}, ensure_ascii=False))


def export(path: str) -> None:
    target = Path(path).expanduser()
    target.write_text(json.dumps(records(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _secure(target)
    print(str(target))


def main() -> None:
    parser = argparse.ArgumentParser(description="AIBuy MCP 本地加密审计副本")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    add = sub.add_parser("append")
    add.add_argument("record", nargs="?")
    show = sub.add_parser("list")
    show.add_argument("--limit", type=int, default=0)
    cut = sub.add_parser("prune")
    cut.add_argument("--keep", type=int, default=1000)
    out = sub.add_parser("export")
    out.add_argument("path")
    args = parser.parse_args()
    {"init": init, "append": lambda: append(args.record), "list": lambda: list_records(args.limit),
     "prune": lambda: prune(args.keep), "export": lambda: export(args.path)}[args.command]()


if __name__ == "__main__":
    main()
