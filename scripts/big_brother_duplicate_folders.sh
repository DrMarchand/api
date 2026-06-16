#!/bin/bash
set -euo pipefail

STAMP="$(date '+%Y%m%d_%H%M%S')"
OUT="reports/duplicate_folder_audit_$STAMP.txt"

ROOTS=(
"$HOME/Library/CloudStorage"
"$HOME/Documents"
"$HOME/Desktop"
"$HOME/Downloads"
)

{
echo "=================================================="
echo "BIG BROTHER DUPLICATE FOLDER AUDIT"
echo "Generated: $(date)"
echo "Mode: READ ONLY / BOUNDED"
echo "=================================================="

echo
echo "=== TOP LEVEL CLOUD ROOTS ==="
find "$HOME/Library/CloudStorage" -maxdepth 2 -type d -print 2>/dev/null | sort

echo
echo "=== DUPLICATE FOLDER BASENAMES MAXDEPTH 6 ==="
for r in "${ROOTS[@]}"; do
  [ -d "$r" ] || continue
  find "$r" -maxdepth 6 \
    -path "*/.shortcut-targets-by-id/*" -prune -o \
    -path "*/node_modules/*" -prune -o \
    -type d -print 2>/dev/null
done | awk -F/ '{print $NF}' | sort | uniq -c | sort -nr | head -100

echo
echo "=== CLOUD LOOP / CONFLICT PATHS MAXDEPTH 8 ==="
for r in "${ROOTS[@]}"; do
  [ -d "$r" ] || continue
  find "$r" -maxdepth 8 \
    -path "*/.shortcut-targets-by-id/*" -prune -o \
    -type d \( \
      -iname "*Selective Sync Conflict*" -o \
      -iname "*Google Drive (Not synced)*" -o \
      -iname "*Other computers*" -o \
      -iname "*Dropbox*" -o \
      -iname "*OneDrive*" \
    \) -print 2>/dev/null
done | head -300

echo
echo "=== LONG PATHS OVER 220 CHARS MAXDEPTH 8 ==="
for r in "${ROOTS[@]}"; do
  [ -d "$r" ] || continue
  find "$r" -maxdepth 8 \
    -path "*/.shortcut-targets-by-id/*" -prune -o \
    -print 2>/dev/null | awk 'length($0) > 220 { print length($0), $0 }'
done | sort -nr | head -300

echo
echo "REPORT: $OUT"
} | tee "$OUT"
