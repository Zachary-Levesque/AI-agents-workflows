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

This repository is useful if you want to:

- learn how AI agents work in real workflows
- see examples of AI connected to business tools
- study how prompts, structured outputs, and validation fit together
- understand how RAG, research agents, and action-taking agents are built
- use the workflows as templates for your own projects

It is also useful as a portfolio project because it demonstrates practical AI engineering rather than theory alone.

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

### 5. Adapt the workflow for your use case

These workflows are best used as starting points.

You can adapt them by:

- changing prompts
- replacing tools or APIs
- adjusting validation rules
- adding approval steps
- changing the final output destination

## Important note

This repository is meant to be practical and shareable.

Because of that:

- credentials are redacted
- resource IDs use placeholders
- workflows may require configuration before they can run in your environment
