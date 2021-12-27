import json
import subprocess

from json.decoder import JSONDecodeError
from pathlib import Path


Path(".vscode").mkdir(parents=True, exist_ok=True)

vs_settings = Path(".vscode/settings.json")

venv_path = subprocess.check_output("poetry env info --path".split()).decode("UTF-8")

settings = {}

if vs_settings.is_file():
    with vs_settings.open("r") as f:
        try:
            settings = json.load(f)
        except JSONDecodeError:
            pass

settings["python.defaultInterpreterPath"] = venv_path

with vs_settings.open("w") as f:
    json.dump(settings, f, sort_keys=True, indent=4)

print(settings)
