#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT_DIR"

AI_DIRS=(
  ".ai/manifest"
  ".ai/knowledge"
  ".ai/agents"
  ".ai/research"
  ".ai/planning"
  ".ai/reviews"
  ".ai/decisions"
  ".ai/memory"
  ".ai/tasks"
  ".ai/protocols"
  ".ai/audit"
  ".ai/quality"
  ".ai/handover"
  ".ai/roadmap"
  ".ai/experiments"
  ".ai/benchmarks"
  ".ai/standards"
  ".ai/playbooks"
)

echo "ADM bootstrap: initializing workspace at $ROOT_DIR"

for dir in "${AI_DIRS[@]}"; do
  mkdir -p "$dir"
  touch "$dir/.gitkeep"
  echo "initialized $dir"
done

if [ -d ".git" ]; then
  HOOK_PATH=".git/hooks/pre-commit"
  if [ -f "$HOOK_PATH" ]; then
    BACKUP_PATH=".git/hooks/pre-commit.adm-backup.$(date +%Y%m%d%H%M%S)"
    cp "$HOOK_PATH" "$BACKUP_PATH"
    echo "existing pre-commit hook backed up to $BACKUP_PATH"
  fi

  cat > "$HOOK_PATH" <<'EOF'
#!/usr/bin/env bash
set -e

if [ -f "scripts/check_limits.py" ]; then
  python3 scripts/check_limits.py --path . --max-lines 300 --allow-proposed-exemptions
else
  echo "ADM pre-commit: scripts/check_limits.py not found; skipping line-limit check."
fi
EOF

  chmod +x "$HOOK_PATH"
  echo "installed ADM pre-commit hook"
else
  echo "not a Git repository; skipped pre-commit hook installation"
fi

echo "ADM bootstrap complete"
