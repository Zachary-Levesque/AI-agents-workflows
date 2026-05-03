# Appointment Intake and Scheduling Agent Spec

## Overview

- Agent name: Appointment Intake and Scheduling Agent
- Owner: Zachary Levesque
- Workflow file: `Get_Appointment_and_Schedule.json`
- Status: prototype

## Problem

- User or business problem: convert inbound service-booking email into a usable appointment record with minimal manual admin work.
- Why automation alone is not enough: the request arrives as natural language and must be interpreted safely before calendar and sheet writes occur.

## Inputs

- Trigger: Gmail trigger
- Required inputs: sender, message snippet or body, booking intent, requested date or time
- Optional inputs: vehicle type, service type

## Outputs

- Primary output: structured booking object
- Side effects: Google Calendar event and Google Sheets row

## Tools and systems

- APIs: OpenAI
- Datastores: Google Sheets
- External actions: Gmail intake, Calendar write

## Model responsibility

- What the model decides: extract customer name, service, date, vehicle, and email from the request
- What code validates: date parsing and normalization
- What must never be decided by the model: whether an invalid date should still be scheduled

## Risks

- Main failure modes: ambiguous dates, incomplete requests, false-positive booking detection
- Unsafe actions: wrong calendar event creation
- Data quality risks: snippet-only extraction misses key details

## Guardrails

- Validation rules: invalid dates fail the workflow
- Approval step: recommended when extraction confidence is low
- Retry or fallback strategy: route invalid or ambiguous bookings to manual review

## Evaluation

- Success metrics: extraction accuracy, invalid-date rejection rate, scheduling correctness
- Eval dataset location: `examples/evals/appointment-intake.yaml`
- Pass threshold: 90 percent of happy-path cases, zero unsafe scheduling on invalid cases

## Notes

- Prompt version: repository version as of this spec
- Known limitations: does not yet perform calendar conflict checks or full-body parsing
