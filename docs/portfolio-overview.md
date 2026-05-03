# Portfolio Overview

This repository demonstrates applied AI agent engineering using `n8n`, LLMs, retrieval, external APIs, and operational automations.

## What this project proves

It shows ability to:

- design task-specific AI agents instead of generic chatbots
- combine model reasoning with deterministic business logic
- integrate external systems such as Gmail, Google Sheets, Google Calendar, Google Drive, Pinecone, Tavily, Open-Meteo, and Apify
- evaluate agents for correctness, safety, and reliability
- document architecture, guardrails, and failure modes
- build supporting tooling and tests around agent workflows

## Reviewer summary

This is not a prompt collection. It is a small AI systems lab centered on production-style workflow design.

Evidence included in the repo:

- portfolio-quality repository documentation
- workflow audit and maturity scoring
- evaluation framework and templates
- examples of extraction, retrieval, research, and action agents
- CI and tests for local repository tooling

## Flagship projects

### Appointment Intake and Scheduling Agent

Capabilities:

- parses inbound customer messages
- extracts structured fields
- normalizes dates
- creates downstream operational records

Skills demonstrated:

- structured output design
- human-facing workflow automation
- validation before side effects
- calendar and sheet integration

### Document RAG Support Assistant

Capabilities:

- ingests source documents from Google Drive
- stores embeddings in Pinecone
- answers user questions from retrieved knowledge only

Skills demonstrated:

- retrieval-augmented generation
- prompt grounding
- ingestion pipeline design
- knowledge-source discipline

### Lead Research Assistant

Capabilities:

- decomposes a lead-research request
- gathers search evidence
- extracts company and contact information
- prepares data for downstream enrichment

Skills demonstrated:

- multi-step agent workflow design
- retrieval plus extraction chaining
- data normalization concerns
- operational AI for GTM workflows

## Why this is relevant to big tech

The work here maps to problems large companies actually care about:

- safe use of LLMs around operational systems
- workflow orchestration around non-deterministic components
- grounding, evaluation, and observability
- turning prototypes into repeatable systems

## Limits

This repository does not claim that every exported workflow is production-ready as-is. Instead, it demonstrates the correct engineering discipline for taking agent workflows from prototype to reliable systems.
