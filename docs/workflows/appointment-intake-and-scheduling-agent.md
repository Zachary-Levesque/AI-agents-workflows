# Appointment Intake and Scheduling Agent

## Goal

Convert inbound service-booking messages into structured operational records and calendar events.

## Systems involved

- Gmail
- OpenAI
- Google Calendar
- Google Sheets

## Why it matters

This is a strong example of an AI workflow that must combine language understanding with safe real-world actions.

## Current strengths

- uses structured output parsing
- includes downstream normalization logic
- connects extraction to action

## Recommended next production upgrades

- parse full message body rather than only snippet data
- add low-confidence routing
- check calendar conflicts before insertion
- store decision logs for review
