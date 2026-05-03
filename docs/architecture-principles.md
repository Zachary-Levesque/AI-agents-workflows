# Architecture Principles

This repository follows a simple architecture model for AI agents:

## 1. Separate reasoning from execution

The model should interpret, summarize, classify, or extract.

Deterministic code or workflow logic should:

- validate structure
- normalize formats
- branch on policy
- execute external actions

## 2. Make side effects explicit

Sending email, updating sheets, creating events, publishing content, and storing embeddings are side effects. Side effects must be visible in the workflow and should be reviewable.

## 3. Prefer grounded systems

When a workflow depends on external facts, the system should retrieve approved context first. RAG is preferable to relying on model priors for business-specific answers.

## 4. Fail safely

If key data is missing or ambiguous, the workflow should stop, route for review, or ask for clarification. Silent failure and unsafe automation are not acceptable defaults.

## 5. Build for iteration

Every workflow should be documented, auditable, and measurable so it can be improved over time.

## Reference architecture

1. Trigger
2. Filter or route
3. Context collection
4. LLM step with narrow responsibility
5. Validation or normalization
6. Approval step when needed
7. Action
8. Logging and evaluation
