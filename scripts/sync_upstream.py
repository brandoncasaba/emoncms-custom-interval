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
if '"version"' not in manifest_text:
    manifest_text = manifest_text.rstrip()[:-1] + ',\n  "version": "1.0.0"\n}\n'
    manifest.write_text(manifest_text)