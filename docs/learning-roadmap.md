# Learning Roadmap

This roadmap turns the repo into a deliberate training program.

## Phase 1: Clean automation

Goal:
Learn to build workflows that are deterministic and safe before adding complex agent behavior.

Use:

- `Finish_Appointments.json`
- `Weather_Agent.json`
- `Google_Maps_Scraper.json`

Practice:

- trigger design
- API integration
- normalization in code nodes
- logging and error branches

## Phase 2: Extraction agents

Goal:
Use LLMs for structured extraction, then validate the results.

Use:

- `Get_Appointment_and_Schedule.json`
- `Research_assistant.json`

Practice:

- structured outputs
- schema validation
- confidence scoring
- human review routing

## Phase 3: Research and writing agents

Goal:
Combine web retrieval with summarization or content generation while staying grounded.

Use:

- `New_Lead_Research.json`
- `LinkedIn_content_creator.json`

Practice:

- source selection
- anti-hallucination controls
- approval before send or publish
- output quality rubrics

## Phase 4: RAG systems

Goal:
Build an agent that answers from approved knowledge only.

Use:

- `RAG_Pipeline___Chatbot.json`

Practice:

- ingestion pipelines
- chunking strategy
- retrieval evaluation
- answer grounding
- citation formatting

## Phase 5: Production discipline

Apply to every workflow:

- create an agent spec first
- build eval cases
- log failures
- review unsafe actions
- version prompts and important code

## Capstone standard

A strong final version of this repo would include:

- every workflow documented
- at least 3 workflows upgraded with evals and approval steps
- one polished RAG project with citations
- one polished outbound research workflow with validation
- one polished inbound operations workflow with safe automation

That combination is enough to show real agent-building skill, not just tool familiarity.
