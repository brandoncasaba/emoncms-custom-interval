import json
from pathlib import Path
import shutil
import subprocess

UPSTREAM = Path(".upstream/home-assistant-core")
SOURCE = UPSTREAM / "homeassistant/components/emoncms"
DEST = Path("custom_components/emoncms")

shutil.rmtree(DEST, ignore_errors=True)
shutil.copytree(SOURCE, DEST)

coordinator = DEST / "coordinator.py"
text = coordinator.read_text()

old = "update_interval=timedelta(seconds=60)"
new = "update_interval=timedelta(seconds=20)"

if old not in text:
    raise RuntimeError(
        "The upstream coordinator interval changed. "
        "Review the integration manually before syncing."
    )

coordinator.write_text(text.replace(old, new, 1))

# Required for a custom override and HACS versioning.
manifest = DEST / "manifest.json"
manifest_text = manifest.read_text()
manifest_data = json.loads(manifest_text)
if "version" not in manifest_data:
    name_line = f'  "name": {json.dumps(manifest_data["name"])},\n'
    if name_line not in manifest_text:
        raise RuntimeError("Unable to place the custom integration version.")

    version_line = '  "version": "1.0.0",\n'
    manifest.write_text(manifest_text.replace(name_line, name_line + version_line, 1))