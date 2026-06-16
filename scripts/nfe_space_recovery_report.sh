#!/bin/bash
set -euo pipefail

STAMP="$(date '+%Y%m%d_%H%M%S')"
OUT="reports/space_recovery_$STAMP.txt"

{
echo "=================================================="
echo "NFE SPACE RECOVERY REPORT"
echo "Generated: $(date)"
echo "Mode: READ ONLY / BOUNDED"
echo "=================================================="

echo
echo "=== DISK ==="
df -h "$HOME"

echo
echo "=== SAFE HOME TOP DIRS ==="
for p in "$HOME/Desktop" "$HOME/Documents" "$HOME/Downloads" "$HOME/Pictures" "$HOME/Movies" "$HOME/Music" "$HOME/Developer"; do
  [ -e "$p" ] && du -sh "$p" 2>/dev/null || true
done | sort -hr

echo
echo "=== LIBRARY TOP BOUNDED ==="
for p in \
"$HOME/Library/Group Containers" \
"$HOME/Library/Application Support" \
"$HOME/Library/CloudStorage" \
"$HOME/Library/Mobile Documents" \
"$HOME/Library/Messages" \
"$HOME/Library/Containers" \
"$HOME/Library/Metadata" \
"$HOME/Library/Mail" \
"$HOME/Library/Photos" \
"$HOME/Library/Caches" \
"$HOME/Library/Logs" \
"$HOME/Library/CloudStorage_OLD"
do
  [ -e "$p" ] && du -sh "$p" 2>/dev/null || true
done | sort -hr

echo
echo "=== GROUP CONTAINERS TOP ==="
du -sh "$HOME/Library/Group Containers"/* 2>/dev/null | sort -hr | head -30

echo
echo "=== APPLICATION SUPPORT TOP ==="
du -sh "$HOME/Library/Application Support"/* 2>/dev/null | sort -hr | head -30

echo
echo "=== CLOUD STORAGE TOP LEVEL ONLY ==="
du -sh "$HOME/Library/CloudStorage"/* 2>/dev/null | sort -hr | head -30

echo
echo "=== TRASH NFE ==="
du -sh "$HOME/.Trash"/NFE_* 2>/dev/null || true

echo
echo "=== LARGE LOCAL FILES OVER 1G ==="
find "$HOME/Downloads" "$HOME/Documents" "$HOME/Desktop" "$HOME/Pictures" "$HOME/Movies" \
-xdev -type f -size +1G -exec du -sh {} \; 2>/dev/null | sort -hr || true

echo
echo "REPORT: $OUT"
} | tee "$OUT"
