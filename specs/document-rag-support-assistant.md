# Document RAG Support Assistant Spec

## Overview

- Agent name: Document RAG Support Assistant
- Owner: Zachary Levesque
- Workflow file: `RAG_Pipeline___Chatbot.json`
- Status: prototype

## Problem

- User or business problem: answer customer or operator questions using approved internal documents only.
- Why automation alone is not enough: the system must retrieve relevant context, ground the answer, and avoid unsupported claims.

## Inputs

- Trigger: chat trigger and Google Drive ingestion trigger
- Required inputs: user question or new source document
- Optional inputs: follow-up context from the conversation

## Outputs

- Primary output: grounded answer with a short sources section
- Side effects: document ingestion into Pinecone

## Tools and systems

- APIs: OpenAI, Pinecone
- Datastores: Pinecone vector index
- External actions: Google Drive polling and download

## Model responsibility

- What the model decides: answer phrasing and synthesis from retrieved evidence
- What code validates: retrieval path and workflow orchestration
- What must never be decided by the model: unsupported facts not present in retrieved context

## Risks

- Main failure modes: weak retrieval, stale documents, unsupported answers
- Unsafe actions: misinformation given with false confidence
- Data quality risks: poor chunking or outdated source documents

## Guardrails

- Validation rules: every substantive answer must include sources
- Approval step: not required for informational responses, but recommended for policy-sensitive domains
- Retry or fallback strategy: if evidence is missing, state that clearly instead of inferring

## Evaluation

- Success metrics: groundedness, citation accuracy, hallucination rate
- Eval dataset location: `examples/evals/document-rag.yaml`
- Pass threshold: zero unsupported claims on benchmark questions

## Notes

- Prompt version: repository version as of this spec
- Known limitations: no explicit chunk-level logging or document version control yet
