# Canonical Folder Policy v1

Date Established: 2026-06-15
Originating Author: Joseph Kyle Marchand
Business Root: Design Orchard LLC

## Rule

Each real folder has one canonical home.

Every non-canonical cloud location should contain only a shortcut, alias, pointer, or reference.

Exact mirrors are allowed only when there is a manifest and checksum verification.

## Authorities

OneDrive business is the business and system authority.

Dropbox KEJ Studio is the creative payload authority.

GitHub DrMarchand/api is the code composition authority.

Google Drive is collaboration and reference only.

iCloud is device sync only.

OneDrive Personal and OneDrive-drmarchandscom are legacy or bridge layers until reviewed.

## Never Merge From

- .shortcut-targets-by-id
- .Trash
- .tmp
- Other computers
- Google Drive (Not synced)
- Selective Sync Conflict

These are quarantine zones, not trusted sources.

## Migration Rule

Detect first.
Record source and destination.
Checksum if mirrored.
Move only after approval.
Replace duplicate location with shortcut or alias.
Record provenance.
