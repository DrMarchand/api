#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import csv
import os

HOME = Path.home()
ROOT = Path.cwd()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out = REPORTS / f"authority_registry_{stamp}.csv"

roots = [
    ("library_onedrive", HOME / "Library/CloudStorage/OneDrive-drmarchands com", "institutional_memory"),
    ("laboratory_google", HOME / "Library/CloudStorage/GoogleDrive-Kyle@drmarchandslaboratory.com", "research_and_development"),
    ("lab_icloud", HOME / "Library/Mobile Documents/com~apple~CloudDocs", "active_apple_workbench"),
    ("creative_canvas_dropbox", HOME / "Library/CloudStorage/Dropbox-Kejstudio", "creative_production"),
    ("code_github", HOME / "Developer/NFE/echo-discord-bot", "code_and_registry_authority"),
    ("downloads", HOME / "Downloads", "local_staging"),
    ("desktop", HOME / "Desktop", "local_staging"),
    ("documents", HOME / "Documents", "local_unclassified"),
]

quarantine_terms = [
    ".Trash",
    ".tmp",
    ".shortcut-targets-by-id",
    "Other computers",
    "Google Drive (Not synced)",
    "Selective Sync Conflict",
    "node_modules",
]

def classify_status(path: Path, authority: str) -> str:
    s = str(path)
    if any(term in s for term in quarantine_terms):
        return "graveyard_candidate"
    if authority in ("local_staging", "local_unclassified"):
        return "dumpster_or_review"
    if "bridge" in s.lower() or "migration" in s.lower() or "archive-do-not-edit" in s.lower():
        return "boiler_room"
    return "authority_or_active"

rows = []

for root_id, root_path, authority in roots:
    if not root_path.exists():
        continue

    for dirpath, dirnames, filenames in os.walk(root_path):
        p = Path(dirpath)

        if any(term in str(p) for term in quarantine_terms):
            rows.append({
                "object_name": p.name,
                "path": str(p),
                "root_id": root_id,
                "authority": authority,
                "status": "graveyard_candidate",
                "file_count": len(filenames),
                "path_length": len(str(p)),
                "notes": "quarantine pattern detected",
            })
            dirnames[:] = []
            continue

        try:
            depth = len(p.relative_to(root_path).parts)
        except Exception:
            depth = 0

        if depth > 4:
            dirnames[:] = []
            continue

        rows.append({
            "object_name": p.name,
            "path": str(p),
            "root_id": root_id,
            "authority": authority,
            "status": classify_status(p, authority),
            "file_count": len(filenames),
            "path_length": len(str(p)),
            "notes": "",
        })

with out.open("w", newline="") as f:
    fields = ["object_name", "path", "root_id", "authority", "status", "file_count", "path_length", "notes"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"AUTHORITY REGISTRY: {out}")
print(f"ROWS: {len(rows)}")
