# Security Notes

## Repository policy

This repository is designed to be shareable. Workflow exports should not contain:

- live API tokens
- personal email addresses
- non-placeholder resource identifiers when they are not necessary for review

## Before committing

Run:

```bash
make audit
make test
```

## Current posture

- exported workflows use placeholder credentials and resource IDs
- tests check for common secret patterns in the tracked JSON exports
- CI runs repository validation automatically
