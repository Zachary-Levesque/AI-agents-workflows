#!/usr/bin/env python3
"""Quick repository audit for n8n workflow exports."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def detect_flags(data: dict) -> list[str]:
    flags: list[str] = []
    nodes = data.get("nodes", [])
    node_types = [node.get("type", "") for node in nodes]
    node_names = [node.get("name", "") for node in nodes]
    payload = json.dumps(data)

    if "manualTrigger" in "".join(node_types) and "scheduleTrigger" not in "".join(node_types):
        flags.append("manual-only trigger")
    if "@n8n/n8n-nodes-langchain.agent" in node_types and "outputParserStructured" not in "".join(node_types):
        flags.append("agent without structured parser")
    if "gmail" in payload.lower() and "manualTrigger" not in "".join(node_types):
        flags.append("email side effect present")
    if "{{" in payload:
        flags.append("contains placeholders to reconfigure")
    if "works but not well" in data.get("name", "").lower():
        flags.append("workflow self-identifies as weak")
    if any(name.lower().startswith("code") for name in node_names):
        flags.append("custom code node present")

    return flags


def main() -> None:
    workflow_files = sorted(ROOT.glob("*.json"))
    if not workflow_files:
        print("No workflow exports found.")
        return

    print("Workflow audit")
    print("==============")
    for path in workflow_files:
        with path.open() as f:
            data = json.load(f)

        nodes = data.get("nodes", [])
        active = data.get("active", False)
        flags = detect_flags(data)

        print(f"- {path.name}")
        print(f"  name: {data.get('name', 'unknown')}")
        print(f"  active: {active}")
        print(f"  nodes: {len(nodes)}")
        print(f"  flags: {', '.join(flags) if flags else 'none'}")


if __name__ == "__main__":
    main()
