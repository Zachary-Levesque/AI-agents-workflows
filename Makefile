PYTHON ?= python3

.PHONY: audit audit-json audit-md test

audit:
	$(PYTHON) tools/audit_workflows.py

audit-json:
	$(PYTHON) tools/audit_workflows.py --format json

audit-md:
	$(PYTHON) tools/audit_workflows.py --format markdown --output docs/generated-workflow-audit.md

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'
