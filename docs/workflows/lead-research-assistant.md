# Lead Research Assistant

## Goal

Turn a broad lead-generation request into a structured list of target companies and contact details.

## Systems involved

- OpenAI
- Tavily
- Google Sheets

## Why it matters

This workflow demonstrates multi-step AI orchestration and highlights the challenges of chaining model output across multiple external lookups.

## Current strengths

- decomposes a complex business task into stages
- combines retrieval, extraction, and persistence
- useful real-world outbound sales use case

## Recommended next production upgrades

- enforce JSON output at every extraction stage
- deduplicate by company and contact
- validate email and phone formats
- add confidence-based review paths
