#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  bash clean_tex.sh [--dry-run]

Options:
  -n, --dry-run   Only print files/dirs that would be removed
  -h, --help      Show this help
EOF
}

dry_run=0
case "${1:-}" in
  -n|--dry-run) dry_run=1 ;;
  -h|--help) usage; exit 0 ;;
  "") ;;
  *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
esac

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

remove_paths() {
  local kind="$1"
  shift
  local count=0
  while IFS= read -r -d '' path; do
    count=$((count + 1))
    if [[ $dry_run -eq 1 ]]; then
      printf '[dry-run] %s %s\n' "$kind" "$path"
    else
      printf '%s %s\n' "$kind" "$path"
      rm -rf -- "$path"
    fi
  done
  printf 'Total %s: %d\n' "$kind" "$count"
}

temp_file_expr=(
  -name '*.aux'
  -o -name '*.bbl'
  -o -name '*.bcf'
  -o -name '*.blg'
  -o -name '*.brf'
  -o -name '*.fdb_latexmk'
  -o -name '*.fls'
  -o -name '*.idx'
  -o -name '*.ilg'
  -o -name '*.ind'
  -o -name '*.loa'
  -o -name '*.lof'
  -o -name '*.lol'
  -o -name '*.lot'
  -o -name '*.log'
  -o -name '*.nav'
  -o -name '*.out'
  -o -name '*.run.xml'
  -o -name '*.snm'
  -o -name '*.synctex.gz'
  -o -name '*.synctex.gz(busy)'
  -o -name '*.toc'
  -o -name '*.vrb'
  -o -name '*.xdv'
  -o -name '*-blx.bib'
  -o -name 'texput.log'
)

remove_paths "file" < <(
  find . -type f \( "${temp_file_expr[@]}" \) -print0
)

build_dir_candidates=(
  '_minted*'
  '%OUTDIR%'
)

for pattern in "${build_dir_candidates[@]}"; do
  while IFS= read -r -d '' dir; do
    # Only remove directories that look like build artifacts (no sources/assets inside).
    if find "$dir" -type f \( \
      -name '*.tex' -o -name '*.bib' -o -name '*.bst' -o -name '*.cls' -o -name '*.sty' \
      -o -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' -o -name '*.pdf' -o -name '*.eps' \
    \) -print -quit | grep -q .; then
      continue
    fi
    remove_paths "dir" < <(printf '%s\0' "$dir")
  done < <(find . -type d -name "$pattern" -prune -print0 2>/dev/null || true)
done

