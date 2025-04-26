#!/bin/bash

# Exit on any error
set -e

# Check for branch name
if [ -z "$1" ]; then
  echo "Usage: $0 <branch-name>"
  exit 1
fi

BRANCH="$1"
TARGET_DIR="../$BRANCH"

echo "📦 Exporting branch: $BRANCH"
mkdir -p "$TARGET_DIR"

# Step 1: Create the patch file
echo "📝 Generating patch..."
git diff main.."$BRANCH" > "$TARGET_DIR/changes.patch"

# Step 2: Generate Markdown summary
echo "📄 Generating Markdown diff..."
awk '
  /^diff --git a\// {
    if (in_diff) { print "```"; in_diff=0 }
    sub(/^diff --git a\//, "### File: ");
    sub(/ b\/.*$/, "");
    print ""; print;
    next;
  }
  /^index / { next }                 # Skip index lines
  /^--- / { next }                   # Skip old file path
  /^\+\+\+ / { next }                # Skip new file path
  /^@@ / {
    if (!in_diff) { print "```diff"; in_diff=1 }
    match($0, /\+([0-9]+)/, m);
    new_line_num = m[1];
    print $0;
    next;
  }
  /^\+[^\+]/ {
    printf("+ %4d | %s\n", new_line_num, substr($0, 2));
    new_line_num++;
    next;
  }
  /^-[^-]/ {
    printf("-      | %s\n", substr($0, 2));
    next;
  }
  END {
    if (in_diff) print "```";
  }
' "$TARGET_DIR/changes.patch" > "$TARGET_DIR/changes.md"

# Step 3: Copy added and modified files
echo "📁 Copying added and modified files to $TARGET_DIR"
git diff --name-status main.."$BRANCH" | grep -E '^[AM]' | cut -f2 | \
  xargs -I{} cp --parents {} "$TARGET_DIR"

echo "✅ Export complete!"
echo "• Patch:    $TARGET_DIR/changes.patch"
echo "• Markdown: $TARGET_DIR/changes.md"
echo "• Files:    Added/modified files copied to $TARGET_DIR"
