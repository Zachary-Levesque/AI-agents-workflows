# Skills Matrix

This matrix makes the learning outcome of the repository explicit.

| Skill area | Evidence in repo |
| --- | --- |
| Workflow orchestration | Multiple `n8n` exports covering triggers, branching, code nodes, and downstream actions |
| LLM integration | OpenAI-backed extraction, summarization, drafting, and chat workflows |
| Structured outputs | `Appointment Intake and Scheduling Agent`, templates, and evaluation guidance |
| Retrieval-augmented generation | `Document RAG Support Assistant` with Pinecone-backed retrieval |
| Prompt engineering | Playbook, workflow audit, and revised prompts in the exports |
| Safety and guardrails | Validation guidance, audit flags, approval recommendations, safer prompt patterns |
| API integration | Tavily, Open-Meteo, Apify, Gmail, Sheets, Drive, Calendar, Pinecone |
| Data normalization | Code-node parsing, spreadsheet writes, lead/contact field extraction |
| Evaluation design | [docs/evaluation-framework.md](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/docs/evaluation-framework.md) and eval templates |
| Tooling and automation | [tools/audit_workflows.py](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/tools/audit_workflows.py:1), `Makefile`, CI |
| Testing discipline | [tests/test_audit_workflows.py](/Users/zacharylevesque/Documents/GitHub/AI-agents-workflows/tests/test_audit_workflows.py:1) |
| Portfolio communication | README, portfolio overview, workflow audit, architecture docs |

## Interview-ready claims

After building and understanding this repo, you can credibly discuss:

- when to use an LLM versus deterministic logic
- how to validate model outputs before real-world actions
- how to structure retrieval systems to reduce hallucinations
- how to evaluate AI workflows with task-specific metrics
- how to package AI agent work so it can be reviewed by engineers
