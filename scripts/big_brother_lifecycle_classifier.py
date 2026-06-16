#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import csv

reports = Path("reports")
reports.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out = reports / f"lifecycle_classifier_{stamp}.csv"

sources = []
for pattern in [
    "authority_registry_*.csv",
    "merge_priority_*.csv",
    "merge_plan_*.csv",
    "graveyard_manifest_*.csv",
]:
    sources.extend(sorted(reports.glob(pattern)))

def classify(path: str):
    s = path.lower()

    if "downloads" in s or ".tmp.drive" in s:
        return "dumpster", "downloads_or_drive_temp_staging"

    if "documents" in s and not any(x in s for x in ["corrupt", "ghost", "deleted", "broken", "lost and found"]):
        return "boiler_room", "documents_working_or_weird"

    if "toolbox" in s or "blueprint" in s or "schema" in s or "architecture" in s:
        return "toolbox", "blueprint_layer"

    if any(x in s for x in [
        "corrupt",
        "ghost",
        "deleted",
        "broken",
        "lost and found",
        "google drive (not synced)",
        "no man",
        "graveyard",
        ".trash",
        ".tmp",
        ".shortcut-targets-by-id",
        "other computers",
    ]):
        return "no_mans_land", "ghost_deleted_corrupt_or_lost"

    return "review", "needs_manual_review"

rows = []
seen = set()

for src in sources:
    try:
        with src.open(newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                path = r.get("path") or r.get("canonical_path") or ""
                name = r.get("name") or r.get("object_name") or r.get("basename") or Path(path).name
                if not path or path in seen:
                    continue
                seen.add(path)
                status, reason = classify(path)
                rows.append({
                    "status": status,
                    "reason": reason,
                    "name": name,
                    "path": path,
                    "source_report": str(src),
                })
    except Exception as e:
        rows.append({
            "status": "review",
            "reason": f"source_read_error:{e}",
            "name": src.name,
            "path": str(src),
            "source_report": str(src),
        })

with out.open("w", newline="") as f:
    fields = ["status", "reason", "name", "path", "source_report"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"LIFECYCLE CLASSIFIER: {out}")
print(f"ROWS: {len(rows)}")

counts = {}
for r in rows:
    counts[r["status"]] = counts.get(r["status"], 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
