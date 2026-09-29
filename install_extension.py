"""
Install SaidLang VS Code Extension locally.
Copies the extension directly to your user's VS Code extensions directory.
"""

import os
import shutil
import sys

def install_vscode_extension():
    user_home = os.path.expanduser("~")
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vscode-extension")

    if not os.path.exists(src_dir):
        print(f"Error: Extension source folder '{src_dir}' not found.")
        sys.exit(1)

    candidate_ext_dirs = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Antigravity IDE", "resources", "app", "extensions", "saidlang"),
        os.path.join(user_home, ".antigravity-ide", "extensions", "saidlang-0.1.0"),
        os.path.join(user_home, ".vscode", "extensions", "saidlang-0.1.0"),
        os.path.join(user_home, ".vscode-insiders", "extensions", "saidlang-0.1.0"),
        os.path.join(user_home, ".cursor", "extensions", "saidlang-0.1.0"),
    ]

    for target in candidate_ext_dirs:
        parent = os.path.dirname(target)
        if os.path.exists(parent):
            if os.path.exists(target):
                shutil.rmtree(target)
            shutil.copytree(src_dir, target)
            print(f"[SUCCESS] Installed SaidLang extension to: {target}")

    # Update Global User Settings
    appdata = os.environ.get("APPDATA", "")
    settings_files = [
        os.path.join(appdata, "Antigravity IDE", "User", "settings.json"),
        os.path.join(appdata, "Code", "User", "settings.json"),
        os.path.join(appdata, "Cursor", "User", "settings.json"),
    ]

    import json
    for sf in settings_files:
        if os.path.exists(sf):
            try:
                with open(sf, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {}
            fa = data.get("files.associations", {})
            fa["*.said"] = "saidlang"
            data["files.associations"] = fa
            with open(sf, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"[SUCCESS] Registered *.said in Global Settings: {sf}")

    print("\nTip: In any Antigravity / VS Code window, press Ctrl+Shift+P -> 'Developer: Reload Window' to apply globally!")

if __name__ == "__main__":
    install_vscode_extension()
