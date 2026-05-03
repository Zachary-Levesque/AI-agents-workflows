# Evaluation Framework

If you want to become strong at building AI agents, this is the skill to learn fastest.

## Goal

Measure whether a workflow is:

- correct
- reliable
- safe
- useful
- efficient

## Metrics by workflow type

Extraction workflows:

- field accuracy
- missing-field rate
- invalid-format rate
- false positive rate

Research workflows:

- factual accuracy
- citation quality
- deduplication quality
- coverage of target facts

RAG workflows:

- answer groundedness
- retrieval relevance
- citation accuracy
- hallucination rate

Content workflows:

- instruction adherence
- tone fit
- originality
- approval pass rate

Action workflows:

- action correctness
- unsafe-action rate
- approval bypass rate
- rollback success

## Eval set design

Each workflow should have at least 10 to 20 cases across:

- normal cases
- edge cases
- malformed inputs
- adversarial inputs
- missing-context cases

Example for appointment extraction:

- explicit date and time
- vague date like "next Friday morning"
- no vehicle mentioned
- spam email with similar keywords
- multiple dates in one message

## Scoring method

Use a simple rubric:

- `pass`: output is fully correct and safe
- `partial`: useful but needs human correction
- `fail`: wrong, unsafe, or unusable

Track reasons for failure, not just counts.

## What to log after each run

- workflow name
- input case ID
- model version
- prompt version
- raw output
- normalized output
- expected output
- pass or fail
- failure reason

## Review cadence

- After every major prompt change
- After adding a new tool or integration
- Before enabling auto-send or auto-write behavior
- Monthly for active production workflows

## Fast rule

Do not trust a workflow in production until it passes the eval set you designed for it.
