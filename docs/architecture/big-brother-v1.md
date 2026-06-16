# Big Brother v1

Date Established: 2026-06-15
Originating Author: Joseph Kyle Marchand
Business Root: Design Orchard LLC

## Purpose

Big Brother is the visibility and telemetry layer.

Big Brother gives Watchdog the light it needs to observe the system.

Big Brother observes. It does not execute.

## Responsibilities

- observe storage health
- observe Git repository state
- observe cloud mount availability
- observe API health endpoints
- observe local system pressure
- observe NFE registry drift
- report findings to Workbench
- provide signals to Watchdog

## Authority Limits

Big Brother cannot:

- delete files
- move files
- change permissions
- push code
- alter contracts
- alter payments
- expose secrets

## Signal Flow

Big Brother observes.
Watchdog evaluates.
Lionheart authorizes.
Echo communicates.
Workbench displays.
Notebook archives.

Copyright 2026 Joseph Kyle Marchand and/or Design Orchard LLC.
