#!/bin/bash
set -euo pipefail

STAMP="$(date '+%Y%m%d_%H%M%S')"
OUT="reports/no_mans_land_audit_$STAMP.txt"

{
echo "=================================================="
echo "BIG BROTHER NO MAN'S LAND AUDIT"
echo "Generated: $(date)"
echo "Mode: READ ONLY"
echo "=================================================="

echo
echo "=== LIKELY NO MAN'S LAND PATHS ==="
find "$HOME" -maxdepth 5 \( \
  -iname "*No Man*" -o \
  -iname "*Graveyard*" -o \
  -iname "*Deleted*" -o \
  -iname "*Corrupt*" -o \
  -iname "*Ghost*" \
\) -print 2>/dev/null

echo
echo "=== BROKEN SYMLINKS ==="
find "$HOME" -type l ! -exec test -e {} \; -print 2>/dev/null | head -300

echo
echo "=== DRIVE TEMP GHOSTS ==="
find "$HOME/Desktop" "$HOME/Documents" "$HOME/Downloads" \
  -name ".tmp.drive*" -print 2>/dev/null

echo
echo "=== ZERO BYTE FILES IN DESKTOP DOCUMENTS DOWNLOADS ==="
find "$HOME/Desktop" "$HOME/Documents" "$HOME/Downloads" \
  -type f -size 0 -print 2>/dev/null | head -300

echo
echo "REPORT: $OUT"
} | tee "$OUT"
