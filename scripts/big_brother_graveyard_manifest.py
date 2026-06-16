#!/usr/bin/env python3
from pathlib import Path
import csv
from datetime import datetime

latest = sorted(Path("reports").glob("authority_registry_*.csv"))[-1]
rows = list(csv.DictReader(latest.open()))

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out = Path("reports") / f"graveyard_manifest_{stamp}.csv"

grave = [r for r in rows if r["status"] == "graveyard_candidate"]

with out.open("w", newline="") as f:
    fields = [
        "path",
        "root_id",
        "authority",
        "file_count",
        "path_length",
        "reason",
        "recommended_action",
    ]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()

    for r in grave:
        path = r["path"]
        reason = "quarantine_pattern"
        action = "review_before_remove"

        if path.endswith(".tmp.driveupload") or path.endswith(".tmp.drivedownload"):
            action = "remove_if_empty_or_stale"
        if ".Trash" in path:
            action = "cloud_trash_review"
        if ".shortcut-targets-by-id" in path:
            action = "do_not_scan_deep_google_shortcut_index"
        if "Other computers" in path:
            action = "google_drive_other_computers_review"
        if "Google Drive (Not synced)" in path:
            action = "migration_graveyard_review"

        w.writerow({
            "path": path,
            "root_id": r["root_id"],
            "authority": r["authority"],
            "file_count": r["file_count"],
            "path_length": r["path_length"],
            "reason": reason,
            "recommended_action": action,
        })

print(f"GRAVEYARD MANIFEST: {out}")
print(f"CANDIDATES: {len(grave)}")
for r in grave:
    print(r["path"])
