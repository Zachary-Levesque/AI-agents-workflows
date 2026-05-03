# Contributing

## Repository standard

Any new workflow or major revision should include:

- a clear problem statement
- a workflow spec based on `templates/agent-spec-template.md`
- at least one evaluation file in `examples/evals/`
- documentation of risks and guardrails

## Local checks

Run:

```bash
make audit
make test
```

## Principles

- prefer deterministic validation around model output
- do not commit secrets or live credentials
- document side effects and approval requirements
- keep workflows shareable and reviewable
