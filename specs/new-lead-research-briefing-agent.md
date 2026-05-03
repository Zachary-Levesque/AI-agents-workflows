# New Lead Research Briefing Agent Spec

## Overview

- Agent name: New Lead Research Briefing Agent
- Owner: Zachary Levesque
- Workflow file: `New_Lead_Research.json`
- Status: prototype

## Problem

- User or business problem: when a new lead is added, generate an internal briefing that helps the team approach outreach intelligently.
- Why automation alone is not enough: the system must retrieve signal, summarize it clearly, and avoid weak or fabricated claims.

## Inputs

- Trigger: Google Sheets row update
- Required inputs: lead company name
- Optional inputs: industry or territory context if present in the sheet

## Outputs

- Primary output: structured internal briefing
- Side effects: Gmail draft-like send path and sheet status update

## Tools and systems

- APIs: OpenAI, Tavily
- Datastores: Google Sheets
- External actions: Gmail send, sheet update

## Model responsibility

- What the model decides: briefing subject, body, confidence, and review recommendation
- What code validates: review gating and final message assembly
- What must never be decided by the model: whether weak research should be auto-sent without review

## Risks

- Main failure modes: thin sources, overconfident summaries, misleading company descriptions
- Unsafe actions: sending low-quality internal guidance as if it were reliable
- Data quality risks: weak search coverage or noisy source material

## Guardrails

- Validation rules: low-confidence outputs are marked for review instead of sent
- Approval step: built into the workflow through review routing
- Retry or fallback strategy: update the sheet to `Needs review` rather than auto-send

## Evaluation

- Success metrics: briefing usefulness, source trace quality, low-signal review capture rate
- Eval dataset location: create alongside business-specific lead cases
- Pass threshold: zero auto-sends for weak-source cases

## Notes

- Prompt version: repository version as of this spec
- Known limitations: still sends directly on high-confidence cases instead of creating a manual approval inbox queue
