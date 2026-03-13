#!/bin/bash
# ============================================================
# Divi Docs Screenshot Cleanup
# Run from the root of your divi-docs repo:
#   chmod +x cleanup_screenshots.sh && ./cleanup_screenshots.sh
# ============================================================

set -e

SCREENSHOTS_DIR="docs/assets/screenshots/modules"
MODULES_DIR="docs/modules"

# Verify we're in the right directory
if [ ! -f "mkdocs.yml" ]; then
    echo "ERROR: Run this from the root of the divi-docs repo."
    exit 1
fi

echo "=== DIVI DOCS SCREENSHOT CLEANUP ==="
echo ""

# Step 1: Delete all PNG screenshots (keep .gitkeep files)
echo "Step 1: Removing all scraped screenshots..."
count=$(find "$SCREENSHOTS_DIR" -name "*.png" -type f | wc -l | tr -d ' ')
find "$SCREENSHOTS_DIR" -name "*.png" -type f -delete
echo "  Deleted $count PNG files"

# Step 2: Comment out active image lines in markdown files
echo ""
echo "Step 2: Commenting out image references in markdown files..."
modified=0
for md in "$MODULES_DIR"/*.md; do
    if grep -q '^!\[' "$md" 2>/dev/null; then
        # macOS sed needs '' after -i for in-place with no backup
        sed -i '' 's|^\(!\[.*screenshots.*\)$|<!-- TODO: Replace with proper screenshot -->\
<!-- \1 -->|' "$md"
        ((modified++))
    fi
done
echo "  Updated $modified markdown files"

# Step 3: Comment out orphaned caption lines (*Caption text*)
echo ""
echo "Step 3: Cleaning up orphaned captions..."
for md in "$MODULES_DIR"/*.md; do
    awk '
    prev_was_commented_img && /^\*.*\*$/ {
        print "<!-- " $0 " -->"
        prev_was_commented_img = 0
        next
    }
    /^<!-- !\[/ { prev_was_commented_img = 1 }
    !/^<!-- !\[/ { prev_was_commented_img = 0 }
    { print }
    ' "$md" > "${md}.tmp" && mv "${md}.tmp" "$md"
done
echo "  Done"

# Step 4: Verify
echo ""
echo "Step 4: Verifying..."
remaining_pngs=$(find "$SCREENSHOTS_DIR" -name "*.png" -type f | wc -l | tr -d ' ')
remaining_active=$(grep -rl '^!\[.*screenshots' "$MODULES_DIR"/ --include="*.md" 2>/dev/null | wc -l | tr -d ' ')
echo "  Remaining PNG files: $remaining_pngs"
echo "  Remaining active image refs: $remaining_active"

echo ""
echo "=== CLEANUP COMPLETE ==="
echo ""
echo "Next steps:"
echo "  git add -A"
echo "  git commit -m 'fix: remove all incorrect scraped screenshots'"
echo "  git push"
