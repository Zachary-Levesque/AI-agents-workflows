# AI Agents Workflows Lab

This repository is now structured as an `n8n`-based AI agent lab instead of a loose collection of workflow exports.

It serves 3 purposes:

1. Portfolio: show practical agent workflows you have built.
2. Training system: give you a repeatable way to design, test, and improve agents.
3. Upgrade path: turn simple automations into reliable, production-ready agents.

## What is in this repo

- `*.json`: exported `n8n` workflows.
- `docs/`: playbooks, audits, and learning material.
- `templates/`: reusable specs, eval cases, and workflow docs.
- `tools/`: small local utilities to inspect workflow quality.

## Current workflows

1. `Finish_Appointments.json`
   Sends completion emails after a service is marked finished.
2. `Get_Appointment_and_Schedule.json`
   Extracts booking details from inbound email and creates a calendar event.
3. `Google_Maps_Scraper.json`
   Collects business details from Google Maps search results.
4. `LinkedIn_content_creator.json`
   Pulls web research and drafts LinkedIn content.
5. `New_Lead_Research.json`
   Researches a lead and emails a summary.
6. `RAG_Pipeline___Chatbot.json`
   Ingests documents into Pinecone and answers questions from retrieved context.
7. `Research_assistant.json`
   Searches for companies and contact information for outbound lead generation.
8. `Weather_Agent.json`
   Fetches weather data and sends a daily report.

## What was missing before

The original repo had useful workflow ideas, but it was not yet a complete project for learning how to build successful AI agents. The main gaps were:

- no evaluation framework
- no build standard for new agents
- no portfolio-quality documentation
- no security redaction for shareable exports
- no workflow audit showing what is weak and how to improve it
- no roadmap from beginner automations to stronger agent systems

Those gaps are now addressed in this repository structure.

## Start here

Read these in order:

1. [docs/learning-roadmap.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/learning-roadmap.md)
2. [docs/agent-design-playbook.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/agent-design-playbook.md)
3. [docs/workflow-audit.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/workflow-audit.md)
4. [docs/evaluation-framework.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/evaluation-framework.md)
5. [docs/portfolio-overview.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/portfolio-overview.md)
6. [docs/skills-matrix.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/skills-matrix.md)

Then use:

- [templates/agent-spec-template.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/templates/agent-spec-template.md)
- [templates/eval-cases-template.yaml](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/templates/eval-cases-template.yaml)
- [templates/workflow-readme-template.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/templates/workflow-readme-template.md)

## How to improve any workflow in this repo

Use the same cycle every time:

1. Define the task precisely.
2. Define the required inputs, outputs, tools, and failure modes.
3. Add deterministic guardrails before and after the model step.
4. Create eval cases for normal, edge, and adversarial inputs.
5. Run the workflow against the eval set.
6. Record failures and fix the workflow, prompt, or control logic.
7. Repeat until the workflow is reliable enough for the intended use.

## Standard for a strong agent project

A workflow in this repo should eventually have:

- a clear problem statement
- explicit trigger, input, output, and ownership
- documented dependencies and credentials
- a prompt that is narrow and testable
- validation and error handling
- a human approval step for high-risk actions
- eval cases with expected outputs
- notes on observed failure modes
- a short README explaining how to run it

## Highest-priority upgrades

If your goal is to gain real skill and produce stronger portfolio work, improve these first:

1. `Get_Appointment_and_Schedule.json`
   Good example of extraction plus action, but it has brittle parsing and a hard-coded date bug.
2. `RAG_Pipeline___Chatbot.json`
   Best base for learning retrieval, grounding, and answer evaluation.
3. `Research_assistant.json`
   High upside, but it needs validation, deduplication, and confidence checks.
4. `New_Lead_Research.json`
   Useful business workflow, but it currently trusts search output too much.

## Security note

The workflow exports in this repo were redacted so the repository is safer to share. Before importing and running them, you should reconnect your own credentials and replace placeholder resource IDs.

## Local tooling

Run the workflow audit helper:

```bash
python3 tools/audit_workflows.py
```

This prints a compact inventory of the exported workflows and flags common risks such as hard-coded secrets, manual-only triggers, or missing chat triggers.

You can also run:

```bash
make audit
make test
```

## Engineering signals

This repo includes the kinds of artifacts strong engineering teams expect:

- automated workflow auditing
- unit tests for local tooling
- CI via GitHub Actions
- security checks for shareable exports
- evaluation templates and architecture documentation
