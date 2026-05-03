from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_workflows import (
    build_report,
    collect_reports,
    detect_flags,
    maturity_from_score,
    render_markdown,
)


class AuditWorkflowTests(unittest.TestCase):
    def test_detects_manual_only_and_placeholder_flags(self) -> None:
        data = {
            "name": "Sample Agent",
            "nodes": [
                {"type": "n8n-nodes-base.manualTrigger", "name": "Manual"},
                {"type": "@n8n/n8n-nodes-langchain.agent", "name": "Agent"},
            ],
            "parameters": {"token": "{{TOKEN}}"},
        }
        flags = detect_flags(data)
        self.assertIn("manual-only trigger", flags)
        self.assertIn("agent without structured parser", flags)
        self.assertIn("contains placeholders to reconfigure", flags)

    def test_maturity_bands(self) -> None:
        self.assertEqual(maturity_from_score(90), "production-leaning")
        self.assertEqual(maturity_from_score(75), "advanced prototype")
        self.assertEqual(maturity_from_score(60), "prototype")
        self.assertEqual(maturity_from_score(40), "early prototype")

    def test_build_report_and_markdown_render(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            workflow = {
                "name": "Structured Agent",
                "active": False,
                "nodes": [
                    {"type": "n8n-nodes-base.scheduleTrigger", "name": "Schedule Trigger"},
                    {"type": "@n8n/n8n-nodes-langchain.agent", "name": "Agent"},
                    {
                        "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
                        "name": "Structured Output Parser",
                    },
                ],
            }
            path = root / "workflow.json"
            path.write_text(json.dumps(workflow))

            report = build_report(path)
            self.assertEqual(report.file, "workflow.json")
            self.assertEqual(report.name, "Structured Agent")
            self.assertGreaterEqual(report.score, 50)

            reports = collect_reports(root)
            rendered = render_markdown(reports)
            self.assertIn("| workflow.json |", rendered)
            self.assertIn("Structured Agent", json.dumps([report.__dict__ for report in reports]))


if __name__ == "__main__":
    unittest.main()
