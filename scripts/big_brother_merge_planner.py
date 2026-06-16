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
out = REPORTS / f"merge_plan_{stamp}.csv"

roots = [
    HOME / "Library/CloudStorage/OneDrive-drmarchands com",
    HOME / "Library/CloudStorage/Dropbox-Kejstudio",
    HOME / "Library/CloudStorage/Dropbox-Personal",
    HOME / "Library/CloudStorage/OneDrive-drmarchandscom",
    HOME / "Library/CloudStorage/OneDrive-Personal",
    HOME / "Documents",
    HOME / "Downloads",
    HOME / "Desktop",
]

quarantine_terms = [
    ".shortcut-targets-by-id",
    ".Trash",
    ".tmp",
    "Other computers",
    "Google Drive (Not synced)",
    "Selective Sync Conflict",
    "node_modules",
]

def is_quarantine(path: Path) -> bool:
    s = str(path)
    return any(term in s for term in quarantine_terms)

def authority_for(path: Path) -> str:
    s = str(path)
    if "OneDrive-drmarchands com" in s:
        return "business_system_authority"
    if "Dropbox-Kejstudio" in s:
        return "creative_payload_authority"
    if "OneDrive-drmarchandscom" in s:
        return "landing_bridge_shortcut_layer"
    if "OneDrive-Personal" in s:
        return "legacy_personal_review"
    if "Dropbox-Personal" in s:
        return "legacy_personal_review"
    if "/Documents" in s or "/Downloads" in s or "/Desktop" in s:
        return "local_unclassified"
    return "unknown"

records = []

for root in roots:
    if not root.exists():
        continue
    for dirpath, dirnames, filenames in os.walk(root):
        p = Path(dirpath)

        if is_quarantine(p):
            dirnames[:] = []
            continue

        depth = len(p.relative_to(root).parts) if p != root else 0
        if depth > 6:
            dirnames[:] = []
            continue

        size_hint = 0
        file_count = len(filenames)

        records.append({
            "basename": p.name,
            "path": str(p),
            "authority": authority_for(p),
            "depth": depth,
            "file_count": file_count,
            "path_length": len(str(p)),
            "quarantine": "false",
            "recommended_action": "review",
        })

by_name = {}
for r in records:
    by_name.setdefault(r["basename"].lower(), []).append(r)

rows = []
for name, items in by_name.items():
    if len(items) < 2:
        continue

    authorities = sorted(set(i["authority"] for i in items))
    for i in items:
        action = "candidate_duplicate_review"
        if i["authority"] in ("landing_bridge_shortcut_layer", "legacy_personal_review", "local_unclassified"):
            action = "possible_replace_with_alias_after_verification"
        if i["path_length"] > 220:
            action = "pirate_flag_long_path_review"

        row = dict(i)
        row["duplicate_group_count"] = len(items)
        row["authorities_seen"] = ";".join(authorities)
        row["recommended_action"] = action
        rows.append(row)

with out.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "basename",
        "path",
        "authority",
        "depth",
        "file_count",
        "path_length",
        "quarantine",
        "duplicate_group_count",
        "authorities_seen",
        "recommended_action",
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f"MERGE PLAN CSV: {out}")
print(f"DUPLICATE CANDIDATES: {len(rows)}")
