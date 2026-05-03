# Document RAG Support Assistant

## Goal

Answer customer questions from approved internal documents only.

## Systems involved

- Google Drive
- OpenAI embeddings and chat
- Pinecone
- `n8n` chat trigger

## Why it matters

This is the most directly relevant workflow for modern AI application engineering because it touches ingestion, retrieval, grounding, and response quality.

## Current strengths

- separate ingestion and answer paths
- retrieval tool usage
- explicit instruction not to invent unsupported facts

## Recommended next production upgrades

- attach chunk-level source labels to answers
- track document versions
- add a small representative question set with expected answers
- log retrieved evidence for debugging
