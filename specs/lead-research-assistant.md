# Lead Research Assistant Spec

## Overview

- Agent name: Lead Research Assistant
- Owner: Zachary Levesque
- Workflow file: `Research_assistant.json`
- Status: prototype

## Problem

- User or business problem: turn a vague lead-generation request into structured candidate companies and likely contacts.
- Why automation alone is not enough: the task requires decomposing language, retrieving evidence, extracting entities, and validating contact quality.

## Inputs

- Trigger: chat trigger
- Required inputs: industry, location, target role intent
- Optional inputs: size filters, niche context

## Outputs

- Primary output: structured lead rows with company and contact data
- Side effects: appends rows to Google Sheets

## Tools and systems

- APIs: OpenAI, Tavily
- Datastores: Google Sheets
- External actions: web retrieval and spreadsheet write

## Model responsibility

- What the model decides: structured request interpretation, company-name extraction, contact extraction
- What code validates: JSON parsing, deduplication, email validation, write gating
- What must never be decided by the model: whether fake or low-confidence contact data is acceptable

## Risks

- Main failure modes: weak search evidence, duplicate companies, fabricated contact data
- Unsafe actions: writing bad prospect data into operational sheets
- Data quality risks: missing or invalid email addresses, low-confidence names

## Guardrails

- Validation rules: only contacts that pass normalization and confidence checks are written
- Approval step: recommended for low-confidence or high-value lead lists
- Retry or fallback strategy: invalid contacts are skipped instead of persisted

## Evaluation

- Success metrics: valid-email rate, company relevance, duplication rate, contact precision
- Eval dataset location: `examples/evals/lead-research.yaml`
- Pass threshold: at least 80 percent valid contacts with low fabrication rate

## Notes

- Prompt version: repository version as of this spec
- Known limitations: does not yet enrich against a dedicated contact data provider
