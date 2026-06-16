# UI and Terminal Safe Authoring Standard v1

Date Established: 2026-06-15
Originating Author: Joseph Kyle Marchand
Business Root: Design Orchard LLC

## Purpose

This standard records a discovered UI and terminal break pattern.

Unicode-heavy symbolic names are valuable for branding and human memory, but they can break when pasted through terminals, heredocs, shell scripts, YAML, JSON, Markdown, GitHub, cPanel, Discord, or automation systems.

## Observed Break Pattern

Examples observed:

- heredoc paste entered continuation mode
- shell showed >....
- emoji rendered as placeholder codes
- symbolic labels were converted into literal placeholder strings
- long decorative names became fragile in paths and config files

## Rule

Machine-readable files must use ASCII-safe IDs.

Human-readable symbolic names may be preserved as display metadata.

## Safe Pattern

Use fields like:

id: workbench_frontend
display_name: DrMarchand's Workbench Front End
symbolic_name: chair DrMarchand's Workbench
symbolic_unicode: retained only in human-facing documentation

Avoid symbolic names as:

- primary IDs
- filenames
- shell paths
- JSON keys
- YAML keys
- environment variable names
- API route names
- database identifiers

## Naming Layers

Machine ID:
Stable, ASCII-safe, lowercase when possible.

Display Name:
Human-readable, brand-safe.

Symbolic Name:
Decorative or branded symbol layer.

## Required Practice

Every major system object should define:

- id
- display_name
- symbolic_name
- role
- authority

## Enforcement

Watchdog should flag symbolic characters in:

- filenames
- config keys
- route names
- environment variable names
- shell scripts
- API identifiers

Copyright 2026 Joseph Kyle Marchand and/or Design Orchard LLC.
