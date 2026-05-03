# Workflow Audit

This audit focuses on what will actually make these workflows stronger, safer, and more portfolio-worthy.

## Overall repo assessment

Current maturity: early prototype to lower-mid prototype.

Strengths:

- good coverage of practical business use cases
- hands-on use of triggers, sheets, email, search, RAG, and external APIs
- clear signs of experimentation across multiple agent patterns

Weaknesses:

- weak validation and error handling
- several workflows trust model output too much
- missing approval steps for risky actions
- no test or evaluation assets
- shareability and naming were not portfolio-ready

## Workflow-by-workflow findings

### `Get_Appointment_and_Schedule.json`

Priority: very high

Problems:

- hard-coded date bug in the code node overrides extracted dates
- subject-line filter is brittle and easy to miss valid bookings
- uses email snippet rather than a reliably parsed full body
- no conflict check before calendar insertion
- no customer confirmation or exception path

Best next improvements:

- parse full email body
- enforce schema with required and optional fields
- validate date parsing in code
- check calendar conflicts before creating the event
- add manual approval when confidence is low

### `RAG_Pipeline___Chatbot.json`

Priority: very high

Problems:

- no explicit citation output requirement
- no retrieval quality evaluation
- no deduplication or versioning for ingested documents
- no policy for stale or replaced source documents

Best next improvements:

- require answer plus source snippets
- log retrieved chunks for review
- add document version metadata
- build a small eval set of representative customer questions

### `Research_assistant.json`

Priority: very high

Problems:

- workflow itself states it "works but not well"
- multi-step extraction relies on fragile free-form text parsing
- no confidence scoring for contact details
- no deduplication of companies or contacts
- no validation of email or phone formats before writing to Sheets

Best next improvements:

- switch every extraction step to structured JSON output
- validate contact fields in code
- score confidence and route low-confidence results for review
- deduplicate by company domain and contact email

### `New_Lead_Research.json`

Priority: high

Problems:

- assumes search results exist at fixed array positions
- no citation or provenance in final email
- auto-sends research summary without review
- no guard against weak or low-signal search results

Best next improvements:

- check search result count before prompt assembly
- include links or named sources in the summary
- add approval before send
- store research artifacts for later review

### `LinkedIn_content_creator.json`

Priority: high

Problems:

- automatically creates content without editorial review
- no plagiarism or overlap check
- no brand voice evaluation
- no post variation tracking

Best next improvements:

- add draft-review status instead of direct completion
- keep source links with the generated draft
- create a brand voice rubric
- block repeated themes within a recent time window

### `Weather_Agent.json`

Priority: medium

Problems:

- hard-coded location and recipient
- no threshold logic for actual warnings
- no fallback if weather API schema changes

Best next improvements:

- move location and recipient into config
- define alert conditions rather than generic daily email
- add response-shape validation

### `Google_Maps_Scraper.json`

Priority: medium

Problems:

- started as a one-shot export with a secret in the request URL
- no persistence of results
- no deduplication, enrichment, or qualification

Best next improvements:

- move token to credential or env-backed header
- store normalized business records
- add lead-quality scoring

### `Finish_Appointments.json`

Priority: medium

Problems:

- simple condition-based automation, not yet really an agent
- no personalization or feedback loop
- no send logging or retry strategy

Best next improvements:

- add response tracking
- log sent notifications
- branch on service type or customer segment

## Recommended build order

1. Fix `Get_Appointment_and_Schedule.json`
2. Strengthen `RAG_Pipeline___Chatbot.json`
3. Rebuild `Research_assistant.json`
4. Add approval and provenance to `New_Lead_Research.json`
5. Add editorial controls to `LinkedIn_content_creator.json`

## What to build next

To become better at creating successful AI agents, your next workflows should teach:

1. multi-step extraction with validation
2. grounded answering with citations
3. human-in-the-loop approvals
4. fallback and retry design
5. evaluation-driven iteration
