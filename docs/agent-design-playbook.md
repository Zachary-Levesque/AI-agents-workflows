# Agent Design Playbook

Successful AI agents are usually not "smart prompts." They are controlled systems.

## Core principle

Treat each agent as a pipeline:

1. Trigger
2. Context collection
3. Model reasoning
4. Validation
5. Action
6. Logging
7. Review

If a workflow skips validation or review, the model is being trusted too early.

## Design rules

1. Narrow the task.
   An agent should do one job well. Split "research, decide, write, send" unless the task is low risk.
2. Keep tools explicit.
   The model should only access the tools needed for the task.
3. Validate before action.
   Never let unvalidated model output directly update calendars, sheets, emails, or CRMs.
4. Prefer structured output.
   Free-form text is hard to test and easy to break.
5. Add deterministic checks.
   Dates, email addresses, URLs, IDs, and enums should be checked outside the model.
6. Add a human checkpoint for irreversible actions.
   Sending, deleting, publishing, or scheduling should usually require approval.
7. Measure performance with evals.
   If you cannot tell whether the workflow improved, you are guessing.

## Minimal agent spec

Every new workflow should answer these questions before build:

- What exact task is this agent responsible for?
- What input starts the workflow?
- What output is considered success?
- What tools does it need?
- What can go wrong?
- What should be rejected?
- What actions require human approval?
- How will we evaluate quality?

## Common failure modes

- prompt too broad
- missing negative instructions
- hidden assumptions in tool outputs
- model output parsed with fragile string splitting
- hard-coded dates, IDs, or recipients
- no retries, fallbacks, or error routing
- automated sending without approval
- no deduplication in lead or content workflows
- retrieval systems answering without citations or source checks

## Improvement ladder

Level 1: Works once

- manual trigger
- single prompt
- happy-path only

Level 2: Repeatable automation

- stable trigger
- structured output
- input validation
- logs and error branch

Level 3: Reliable agent

- eval set
- approval step for risky actions
- retries and fallbacks
- monitoring of failures

Level 4: Production-grade agent

- versioned prompts
- explicit SLAs
- rollback plan
- cost, latency, and quality tracking

## Prompting guidance

Use prompts for judgment, not for state management or schema enforcement alone.

Good uses:

- summarize findings
- classify ambiguous input
- rank options with clear criteria
- extract structured fields from messy text

Bad uses:

- generating IDs
- validating email formats
- deciding whether a field is required when business rules already define that
- performing arithmetic or date math that code can do more reliably

## Practical build pattern for `n8n`

1. Trigger node
2. Filter or router node
3. Context retrieval nodes
4. Model node with structured output
5. Code node for validation and normalization
6. Approval branch if action is risky
7. Action node
8. Logging node
9. Error path

## What separates successful agents from demos

- They are evaluated, not just observed.
- They are constrained, not just prompted.
- They fail safely.
- They keep humans in the loop where risk is real.
- They are built from reusable patterns instead of ad hoc chains.
