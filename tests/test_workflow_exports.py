from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SECRET_PATTERNS = [
    re.compile(r"tvly-dev-[A-Za-z0-9]+"),
    re.compile(r"apify_api_[A-Za-z0-9]+"),
    re.compile(r"zlevesque93@gmail\.com"),
]


class WorkflowExportTests(unittest.TestCase):
    def test_all_workflow_exports_parse(self) -> None:
        workflow_files = sorted(ROOT.glob("*.json"))
        self.assertGreater(len(workflow_files), 0)

        for path in workflow_files:
            with self.subTest(path=path.name):
                data = json.loads(path.read_text())
                self.assertIn("name", data)
                self.assertIn("nodes", data)
                self.assertIsInstance(data["nodes"], list)

    def test_no_raw_secrets_or_personal_email_remain(self) -> None:
        workflow_files = sorted(ROOT.glob("*.json"))
        for path in workflow_files:
            content = path.read_text()
            with self.subTest(path=path.name):
                for pattern in SECRET_PATTERNS:
                    self.assertIsNone(pattern.search(content), f"{path.name} matched {pattern.pattern}")


if __name__ == "__main__":
    unittest.main()
