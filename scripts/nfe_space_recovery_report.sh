#!/bin/bash
set -euo pipefail

STAMP="$(date '+%Y%m%d_%H%M%S')"
OUT="reports/space_recovery_$STAMP.txt"

{
echo "=================================================="
echo "NFE SPACE RECOVERY REPORT"
echo "Generated: $(date)"
echo "Mode: READ ONLY"
echo "=================================================="

echo
echo "=== DISK ==="
df -h "$HOME"

echo
echo "=== TOP HOME DIRS ==="
du -sh "$HOME"/* 2>/dev/null | sort -hr | head -40

echo
echo "=== LIBRARY TOP ==="
du -sh "$HOME/Library"/* 2>/dev/null | sort -hr | head -40

echo
echo "=== GROUP CONTAINERS TOP ==="
du -sh "$HOME/Library/Group Containers"/* 2>/dev/null | sort -hr | head -40

echo
echo "=== APPLICATION SUPPORT TOP ==="
du -sh "$HOME/Library/Application Support"/* 2>/dev/null | sort -hr | head -40

echo
echo "=== TRASH NFE ==="
du -sh "$HOME/.Trash"/NFE_* 2>/dev/null || true

echo
echo "=== LARGE FILES OVER 1G, BOUNDED ==="
find "$HOME/Downloads" "$HOME/Documents" "$HOME/Desktop" "$HOME/Pictures" "$HOME/Movies" \
-type f -size +1G -exec du -sh {} \; 2>/dev/null | sort -hr || true

echo
echo "REPORT: $OUT"
} | tee "$OUT"
