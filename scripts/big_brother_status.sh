#!/bin/bash
set -euo pipefail

STAMP="$(date '+%Y%m%d_%H%M%S')"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_DIR="$ROOT/reports"
OUT="$REPORT_DIR/big_brother_status_$STAMP.txt"

mkdir -p "$REPORT_DIR"

{
echo "=================================================="
echo "BIG BROTHER STATUS REPORT"
echo "Generated: $(date)"
echo "Host: $(hostname)"
echo "Mode: READ ONLY"
echo "=================================================="

echo
echo "=== DISK ==="
df -h "$HOME" || true

echo
echo "=== MEMORY / LOAD ==="
uptime || true

echo
echo "=== GIT ==="
git status --short || true
git log --oneline --decorate -5 || true

echo
echo "=== CLOUD MOUNTS ==="
find "$HOME/Library/CloudStorage" -maxdepth 1 -type d -print 2>/dev/null | sort || true

echo
echo "=== ICLOUD ==="
ls -ld "$HOME/Library/Mobile Documents/com~apple~CloudDocs" 2>/dev/null || echo "iCloud path not found"

echo
echo "=== REPO IMPORTANT FILES ==="
for f in \
  index.js \
  package.json \
  docs/architecture/titan-architecture-v1.md \
  docs/architecture/big-brother-v1.md \
  registry/nodes/big-brother.yaml \
  docs/legal/COPYRIGHT_STRATEGY.md \
  docs/provenance/ESTABLISHMENT_LOG.md
do
  if [ -e "$f" ]; then
    echo "FOUND: $f"
  else
    echo "MISSING: $f"
  fi
done

echo
echo "=== POSSIBLE SECRET FILES - FILENAMES ONLY ==="
find . -maxdepth 4 -type f \( \
  -iname "*.env" -o \
  -iname "*secret*" -o \
  -iname "*token*" -o \
  -iname "service_account.json" -o \
  -iname "*.key" -o \
  -iname "*.pem" \
\) -print 2>/dev/null || true

echo
echo "=================================================="
echo "REPORT: $OUT"
echo "=================================================="
} | tee "$OUT"
