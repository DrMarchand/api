# Notebook, Vault, and Workbench Infrastructure v1

**Date Established:** 2026-06-15  
**Originating Author:** Joseph Kyle Marchand  
**Business Root:** Design Orchard LLC  
**System Context:** DrMarchand's Laboratory inside Atlas

## 📒 DrMarchand's ⚛︎ Notebook™

The Notebook is the primary knowledge archive.

It stores:

- research notes
- architecture notes
- system decisions
- evidence summaries
- operating knowledge
- documentation records

The Notebook answers:

> What do we know?

## 🔐 DrMarchand's ⚛ VAULT™

The Vault is the time-machine backup and recovery layer.

It stores:

- historical snapshots
- recovery archives
- backup states
- prior versions
- disaster recovery evidence

The Vault answers:

> What did we know or have at a specific point in time?

## ☸ Workbench™

The Workbench is split into front end and back end roles.

### 🪑 DrMarchand's ☸ Workbench™

Front End.

This is the human-facing operator control surface.

It displays:

- dashboard status
- tasks
- reports
- system health
- approvals
- evidence links
- architecture state

### ⑁ DrMarchand's ☸ Workbench™

Back End.

This is the automation and API coordination layer.

It handles:

- connectors
- API routing
- automation jobs
- task synchronization
- registry updates
- audit processing
- signal routing

## Relationship to Atlas

Atlas contains the Laboratory infrastructure.

The Laboratory produces work.

Workbench displays and coordinates work.

Notebook records knowledge.

Vault preserves recoverable history.

Atomic Notebook preserves permanent evidence.

## Evidence Policy

Major infrastructure changes require:

- Git commit
- changelog entry
- provenance note
- registry update
- archive reference when appropriate

Copyright © 2026 Joseph Kyle Marchand and/or Design Orchard LLC.
