#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import csv

home = Path.home()
reports = Path("reports")
reports.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out = reports / f"lifecycle_classifier_{stamp}.csv"

candidates = []

roots = [
    home,
    home / "Desktop",
    home / "Documents",
    home / "Downloads",
    home / "Library/CloudStorage",
    home / "Library/CloudStorage_OLD",
]

terms = [
    "No Man",
    "No Mans",
    "Graveyard",
    "Deleted",
    "Corrupt",
    "Ghost",
    "Lost and Found",
    "Boiler",
    "Dumpster",
    ".tmp.drive",
]

false_positive_terms = [
    "NativeMessagingHosts",
    "big_brother_graveyard_manifest.py",
    "graveyard_manifest_",
    "no_mans_land_audit_",
]

def classify(path: Path):
    s = str(path)
    name = path.name.lower()

    if any(fp in s for fp in false_positive_terms):
        return "evidence_tooling", "false_positive_or_tooling"

    if "downloads" in s.lower() or ".tmp.drive" in s.lower():
        return "dumpster", "downloads_or_drive_temp_staging"

    if "documents" in s.lower() and not any(x in name for x in ["corrupt", "ghost", "deleted"]):
        return "boiler_room", "documents_working_or_weird"

    if any(x in name for x in ["corrupt", "ghost", "deleted", "broken"]):
        return "no_mans_land", "corrupted_deleted_or_ghost"

    if "lost and found" in s.lower() or "google drive (not synced)" in s.lower():
        return "no_mans_land", "lost_or_not_synced"

    if "no man" in s.lower() or "graveyard" in s.lower():
        return "no_mans_land", "explicit_no_mans_land"

    return "review", "needs_manual_review"

seen = set()

for root in roots:
    if not root.exists():
        continue

    for term in terms:
        try:
            for p in root.rglob(f"*{term}*"):
                sp = str(p)
                if sp in seen:
                    continue
                seen.add(sp)
                status, reason = classify(p)
                candidates.append({
                    "path": sp,
                    "name": p.name,
                    "status": status,
                    "reason": reason,
                    "exists": str(p.exists()).lower(),
                    "is_dir": str(p.is_dir()).lower(),
                    "is_file": str(p.is_file()).lower(),
                })
        except Exception:
            pass

with out.open("w", newline="") as f:
    fields = ["status", "reason", "name", "path", "exists", "is_dir", "is_file"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(candidates)

print(f"LIFECYCLE CLASSIFIER: {out}")
print(f"ROWS: {len(candidates)}")

counts = {}
for r in candidates:
    counts[r["status"]] = counts.get(r["status"], 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
