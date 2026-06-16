# Agreement Payment Delivery Spine v1

**Date Established:** 2026-06-15  
**Originating Author:** Joseph Kyle Marchand  
**Business Root:** Design Orchard LLC  
**Publishing Arm:** Design Orchard℠  
**System:** Atlas API

## Purpose

Create a secure and easy system where a client or partner receives:

- contract/agreement form
- full payment breakdown
- copyright explanation
- trademark explanation
- ownership explanation
- signature workflow
- Stripe payment link
- Dropbox project/deliverable link
- HubSpot-linked client/partner/company ID

## Authority Model

HubSpot is the identity ledger.

Stripe is the payment authority.

Adobe Sign is the temporary signature authority.

PandaDoc is the preferred future contract authority.

Dropbox is the deliverable/package link authority.

Atlas API coordinates the workflow.

Notebook records evidence.

Vault stores recoverable snapshots.

## Flow

1. Create or find HubSpot contact/company/deal.
2. Generate agreement packet.
3. Send agreement through Adobe Sign.
4. Capture signature status.
5. Create Stripe Checkout/payment link.
6. Collect payment.
7. Verify Stripe webhook.
8. Update HubSpot deal/contact/company records.
9. Attach Dropbox project/deliverable link.
10. Record evidence in Notebook.
11. Snapshot final package in Vault.

## Required Agreement Sections

- parties
- project scope
- payment breakdown
- deliverables
- timeline
- revision rules
- Dropbox delivery link
- copyright explanation
- trademark explanation
- ownership / license terms
- client responsibilities
- Design Orchard LLC responsibilities
- signature block

## Rule

Payment proof and contract proof must be linked but not confused.

A payment is not the same as a signed agreement.

## Current Contract Provider

Adobe Sign.

## Future Contract Provider

PandaDoc.

The system must keep contract_provider abstract so Adobe Sign can later be replaced by PandaDoc.

Copyright © 2026 Joseph Kyle Marchand and/or Design Orchard LLC.
