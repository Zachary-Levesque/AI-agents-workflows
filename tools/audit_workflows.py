#!/usr/bin/env python3
"""Repository audit for n8n workflow exports.

The script inspects exported workflows, surfaces common reliability risks,
and assigns a lightweight maturity score so the repo can be reviewed like an
engineering artifact instead of a folder of JSON files.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_GLOB = "*.json"


@dataclass(frozen=True)
class WorkflowReport:
    file: str
    name: str
    active: bool
    node_count: int
    trigger_types: list[str]
    integrations: list[str]
    flags: list[str]
    score: int
    maturity: str


def collect_nodes(data: dict[str, Any]) -> list[dict[str, Any]]:
    return data.get("nodes", [])


def node_types(nodes: list[dict[str, Any]]) -> list[str]:
    return [node.get("type", "") for node in nodes]


def payload_text(data: dict[str, Any]) -> str:
    return json.dumps(data).lower()


def detect_triggers(nodes: list[dict[str, Any]]) -> list[str]:
    triggers: list[str] = []
    for node in nodes:
        node_type = node.get("type", "")
        if "manualTrigger" in node_type:
            triggers.append("manual")
        elif "scheduleTrigger" in node_type:
            triggers.append("scheduled")
        elif "chatTrigger" in node_type:
            triggers.append("chat")
        elif "gmailTrigger" in node_type:
            triggers.append("gmail")
        elif "googleSheetsTrigger" in node_type:
            triggers.append("sheets")
        elif "googleDriveTrigger" in node_type:
            triggers.append("drive")
    return sorted(set(triggers))


def detect_integrations(payload: str) -> list[str]:
    known = {
        "openai": "OpenAI",
        "tavily": "Tavily",
        "pinecone": "Pinecone",
        "googlecalendar": "Google Calendar",
        "googlesheets": "Google Sheets",
        "googledrive": "Google Drive",
        "gmail": "Gmail",
        "open-meteo": "Open-Meteo",
        "apify": "Apify",
    }
    integrations = [label for needle, label in known.items() if needle in payload]
    return sorted(integrations)


def detect_flags(data: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    nodes = collect_nodes(data)
    types = node_types(nodes)
    names = [node.get("name", "") for node in nodes]
    payload = payload_text(data)
    joined_types = "".join(types)

    if "manualTrigger" in joined_types and "scheduleTrigger" not in joined_types and len(detect_triggers(nodes)) == 1:
        flags.append("manual-only trigger")
    if "@n8n/n8n-nodes-langchain.agent" in types and "outputParserStructured" not in joined_types:
        flags.append("agent without structured parser")
    if "gmail" in payload and "manualTrigger" not in joined_types:
        flags.append("email side effect present")
    if "googlesheets" in payload and "operation\":\"append" in payload:
        flags.append("writes to spreadsheet")
    if "googlecalendar" in payload:
        flags.append("calendar side effect present")
    if "{{" in json.dumps(data):
        flags.append("contains placeholders to reconfigure")
    if any(name.lower().startswith("code") for name in names):
        flags.append("custom code node present")
    if "split(/\\n\\s*body:\\s*/i)" in json.dumps(data):
        flags.append("fragile string parsing")
    if any("httpRequest" in value for value in types) and "authorization" not in payload and "token={{" in payload:
        flags.append("token passed in URL")
    if "sources:" not in payload and "pinecone" in payload:
        flags.append("rag answer lacks source requirement")

    return flags


def score_workflow(data: dict[str, Any], flags: list[str]) -> int:
    nodes = collect_nodes(data)
    types = node_types(nodes)
    score = 45

    if len(nodes) >= 5:
        score += 5
    if len(nodes) >= 8:
        score += 5
    if "@n8n/n8n-nodes-langchain.outputParserStructured" in types:
        score += 10
    if "@n8n/n8n-nodes-langchain.vectorStorePinecone" in types:
        score += 10
    if any("trigger" in trigger for trigger in detect_triggers(nodes)):
        score += 0
    if len(detect_triggers(nodes)) > 0:
        score += 5
    if "schedule" in detect_triggers(nodes) or "gmail" in detect_triggers(nodes) or "sheets" in detect_triggers(nodes):
        score += 5

    penalties = {
        "manual-only trigger": 10,
        "agent without structured parser": 12,
        "email side effect present": 4,
        "writes to spreadsheet": 3,
        "calendar side effect present": 4,
        "contains placeholders to reconfigure": 2,
        "custom code node present": 3,
        "fragile string parsing": 8,
        "token passed in URL": 8,
        "rag answer lacks source requirement": 10,
    }
    for flag in flags:
        score -= penalties.get(flag, 0)

    return max(0, min(100, score))


def maturity_from_score(score: int) -> str:
    if score >= 85:
        return "production-leaning"
    if score >= 70:
        return "advanced prototype"
    if score >= 55:
        return "prototype"
    return "early prototype"


def build_report(path: Path) -> WorkflowReport:
    with path.open() as handle:
        data = json.load(handle)

    nodes = collect_nodes(data)
    payload = payload_text(data)
    flags = detect_flags(data)
    score = score_workflow(data, flags)
    return WorkflowReport(
        file=path.name,
        name=data.get("name", "unknown"),
        active=bool(data.get("active", False)),
        node_count=len(nodes),
        trigger_types=detect_triggers(nodes),
        integrations=detect_integrations(payload),
        flags=flags,
        score=score,
        maturity=maturity_from_score(score),
    )


def collect_reports(root: Path = ROOT) -> list[WorkflowReport]:
    return [build_report(path) for path in sorted(root.glob(WORKFLOW_GLOB))]


def print_text_report(reports: list[WorkflowReport]) -> None:
    print("Workflow audit")
    print("==============")
    for report in reports:
        print(f"- {report.file}")
        print(f"  name: {report.name}")
        print(f"  active: {report.active}")
        print(f"  nodes: {report.node_count}")
        print(f"  triggers: {', '.join(report.trigger_types) if report.trigger_types else 'none'}")
        print(f"  integrations: {', '.join(report.integrations) if report.integrations else 'none'}")
        print(f"  score: {report.score}/100 ({report.maturity})")
        print(f"  flags: {', '.join(report.flags) if report.flags else 'none'}")


def render_markdown(reports: list[WorkflowReport]) -> str:
    lines = [
        "# Workflow Audit Report",
        "",
        "| Workflow | Score | Maturity | Triggers | Integrations | Flags |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for report in reports:
        lines.append(
            "| {file} | {score} | {maturity} | {triggers} | {integrations} | {flags} |".format(
                file=report.file,
                score=report.score,
                maturity=report.maturity,
                triggers=", ".join(report.trigger_types) or "none",
                integrations=", ".join(report.integrations) or "none",
                flags=", ".join(report.flags) or "none",
            )
        )
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--format",
        choices=("text", "json", "markdown"),
        default="text",
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional file path to write the report to.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    reports = collect_reports()
    if not reports:
        print("No workflow exports found.")
        return

    if args.format == "json":
        content = json.dumps([asdict(report) for report in reports], indent=2)
    elif args.format == "markdown":
        content = render_markdown(reports)
    else:
        if args.output:
            content = render_markdown(reports)
        else:
            print_text_report(reports)
            return

    if args.output:
        args.output.write_text(content + ("\n" if not content.endswith("\n") else ""))
    else:
        print(content)


if __name__ == "__main__":
    main()
