#!/usr/bin/env python3

import os
import sys
import re
import shutil

# Helper function to add resource_path if missing
RESOURCE_PATH_FUNCTION = '''
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller bundle """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
'''

def inject_resource_path_function(content):
    if "def resource_path(" not in content:
        return RESOURCE_PATH_FUNCTION.strip() + "\n\n" + content
    return content

def replace_asset_paths(content):
    # Regex to find "./assets/..." inside double quotes
    pattern = r'"(\./assets/[^"]+)"'

    def replacement(match):
        asset_path = match.group(1)
        new_text = f'resource_path("{asset_path[2:]}")'  # remove leading ./
        return new_text

    return re.sub(pattern, replacement, content)

def backup_config_file(config_path):
    backup_path = config_path + ".bak"
    shutil.copyfile(config_path, backup_path)
    print(f"🛡️  Backup created: {backup_path}")

def process_config_file(config_path):
    print(f"🔧 Processing {config_path}")

    if not os.path.exists(config_path):
        print(f"⚠️  Warning: {config_path} not found, skipping.")
        return

    # Create a backup before modifying
    backup_config_file(config_path)

    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = inject_resource_path_function(content)
    content = replace_asset_paths(content)

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Finished {config_path}")

def main():
    base_dir = "."
    found = False

    for entry in os.listdir(base_dir):
        entry_path = os.path.join(base_dir, entry)
        if os.path.isdir(entry_path):
            config_path = os.path.join(entry_path, "config.py")
            assets_path = os.path.join(entry_path, "assets")
            if os.path.isfile(config_path) and os.path.isdir(assets_path):
                process_config_file(config_path)
                found = True

    if not found:
        print(f"❌ No matching folders with config.py and assets/ found. Exiting.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
