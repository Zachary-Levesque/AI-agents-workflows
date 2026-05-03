# AI Agents Workflows Lab

This repository is a collection of practical AI agent workflows built in `n8n`.

It is designed for people who want to explore how AI agents can automate real tasks such as:

- handling appointment requests
- researching leads
- drafting LinkedIn content
- sending weather alerts
- answering questions from documents with RAG

## What this repository is

This project is a hands-on lab of AI-powered workflows.

Each workflow shows how large language models can be combined with tools like Gmail, Google Sheets, Google Calendar, Google Drive, Tavily, Pinecone, and external APIs to complete useful tasks.

Rather than being a chatbot demo, this repository focuses on real automations and agent workflows that connect to business tools and perform structured work.

## Why it is useful

- Helps companies **automate repetitive, time-consuming workflows**:
  - appointment scheduling, lead research, reporting, and notifications
  - reduces manual work and operational costs

- Enables **faster and more consistent decision-making**:
  - structured outputs and validation reduce human error
  - workflows run reliably at scale

- Bridges the gap between AI and real business systems:
  - integrates directly with tools like Gmail, Google Sheets, CRM-like data, and APIs
  - shows how AI can move from “chat” → to **taking real actions**

- Demonstrates how to build **production-ready AI agents**:
  - combines LLMs with tools, memory (RAG), and external data
  - includes evaluation, structure, and workflow design patterns

## What it includes

### Workflow exports

The root of the repository contains exported `n8n` workflows such as:

- `Appointment Intake and Scheduling Agent`
- `Lead Research Assistant`
- `New Lead Research Briefing Agent`
- `LinkedIn Content Research and Drafting Agent`
- `Document RAG Support Assistant`
- `Daily Weather Alert Agent`
- `Google Maps Lead Collection Agent`
- `Service Completion Notification Agent`

These workflows cover several common AI agent patterns:

- extraction from unstructured text
- research and summarization
- retrieval-augmented generation
- content drafting
- operational automations with downstream actions

### Documentation

The `docs/` folder explains the project in more detail.

It includes:

- portfolio and architecture overviews
- a workflow audit
- an AI agent design playbook
- an evaluation framework
- learning and reviewer notes

### Specs and templates

The repository also includes:

- `specs/` for detailed agent specifications
- `templates/` for reusable planning and evaluation templates
- `examples/evals/` for sample evaluation cases

### Tooling

The `tools/` and `tests/` folders provide lightweight engineering support for the repo, including:

- a workflow audit script
- tests for repository tooling
- CI configuration for validation

## How to use this repository

### 1. Explore the workflows

Start by reading the workflow names in the root folder and the supporting docs in `docs/`.

If you want a quick overview, begin with:

- `docs/portfolio-overview.md`
- `docs/workflow-audit.md`
- `docs/skills-matrix.md`

### 2. Import a workflow into `n8n`

To try a workflow:

1. Open your `n8n` instance.
2. Import one of the `.json` workflow files from this repository.
3. Review the nodes and connections.

### 3. Reconnect credentials

The workflows in this repository use placeholder credentials and placeholder resource IDs so the repository can be shared safely.

Before running a workflow, you will need to:

- connect your own accounts
- replace placeholder email addresses
- replace placeholder spreadsheet, drive, or other resource IDs
- update any required API credentials

### 4. Test before enabling automation

Before turning on any live trigger:

- test with sample data
- verify outputs carefully
- confirm email, calendar, or sheet actions behave the way you expect
- review any risky workflow before using it with real data
