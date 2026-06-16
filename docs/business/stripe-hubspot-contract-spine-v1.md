# Stripe + HubSpot Contract Spine v1

**Date Established:** 2026-06-15  
**Originating Author:** Joseph Kyle Marchand  
**Business Root:** Design Orchard LLC  
**System:** Atlas API  
**Laboratory:** DrMarchand's Laboratory

## Purpose

This document establishes the transaction spine for Design Orchard LLC.

The system connects agreements, contracts, payments, partners, clients, and company identity records through Stripe and HubSpot.

## Authority Model

Stripe is the payment authority.

HubSpot is the relationship and identity ledger.

Atlas API is the routing and orchestration layer.

Asana is the command/task layer.

Notebook is the knowledge and evidence archive.

Vault is the backup and recovery layer.

## Flow

1. Agreement or contract draft is created.
2. Partner/client/company identity is created or found in HubSpot.
3. Atlas creates a transaction record.
4. Atlas creates a Stripe Checkout Session or invoice/payment flow.
5. Stripe collects payment.
6. Stripe sends webhook event.
7. Atlas verifies the webhook.
8. Atlas updates HubSpot contact/company/deal records.
9. Atlas creates or updates Asana execution tasks.
10. Atlas writes evidence summary to Notebook.
11. Atlas creates backup/export reference for Vault.

## Required IDs

- design_orchard_company_id
- client_company_id
- partner_company_id
- hubspot_contact_id
- hubspot_company_id
- hubspot_deal_id
- agreement_id
- contract_id
- stripe_customer_id
- stripe_checkout_session_id
- stripe_payment_intent_id
- asana_task_gid
- github_commit_sha
- notebook_record_id
- vault_snapshot_id

## Stripe Role

Stripe handles:

- checkout
- payment status
- customer payment records
- invoices when enabled
- payment webhook events
- payment proof

Stripe does not replace signed contracts.

## HubSpot Role

HubSpot handles:

- contacts
- companies
- deals
- partner/client identity
- relationship history
- payment-linked CRM records
- company IDs

## Contract Rule

A payment should not be treated as a full signed agreement unless the user has separately accepted the agreement terms through an approved agreement flow.

Payment proof and contract proof must be linked, but not confused.

## Evidence Rule

Every completed paid agreement should produce:

- Stripe event ID
- Stripe checkout/session/payment ID
- HubSpot contact/company/deal ID
- agreement version
- timestamp
- business root
- responsible DBA/project
- storage/archive location
- Asana execution task when fulfillment is required

## Security Rule

Never commit:

- Stripe secret keys
- Stripe webhook secrets
- HubSpot private app tokens
- client contracts containing sensitive private information
- raw payment data
- bank data
- card data

Copyright © 2026 Joseph Kyle Marchand and/or Design Orchard LLC.
