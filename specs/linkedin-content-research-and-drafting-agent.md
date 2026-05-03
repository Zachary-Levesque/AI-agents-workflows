# LinkedIn Content Research and Drafting Agent Spec

## Overview

- Agent name: LinkedIn Content Research and Drafting Agent
- Owner: Zachary Levesque
- Workflow file: `LinkedIn_content_creator.json`
- Status: prototype

## Problem

- User or business problem: turn a queued content topic into a credible, source-backed LinkedIn draft for review.
- Why automation alone is not enough: content quality, brand voice, and source interpretation require judgment plus review discipline.

## Inputs

- Trigger: schedule trigger or manual trigger
- Required inputs: topic row from Google Sheets
- Optional inputs: tone and brand style guidance

## Outputs

- Primary output: drafted LinkedIn post with source notes
- Side effects: sheet status update

## Tools and systems

- APIs: OpenAI, Tavily
- Datastores: Google Sheets
- External actions: scheduled content generation

## Model responsibility

- What the model decides: final draft wording, source synthesis, confidence, review recommendation
- What code validates: draft packaging and review status assignment
- What must never be decided by the model: whether generated content is final and safe to publish without review

## Risks

- Main failure modes: repetitive writing, weak source grounding, brand mismatch
- Unsafe actions: treating unreviewed content as publish-ready
- Data quality risks: low-quality or stale source articles

## Guardrails

- Validation rules: content is stored as a review draft, not final content
- Approval step: built into the status model
- Retry or fallback strategy: mark weak drafts as `Needs review`

## Evaluation

- Success metrics: draft quality, instruction adherence, source usefulness, review pass rate
- Eval dataset location: create content-topic cases in `examples/evals/`
- Pass threshold: high editorial acceptability with low repetition

## Notes

- Prompt version: repository version as of this spec
- Known limitations: does not yet track topic overlap across recent posts
