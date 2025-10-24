import json
from pathlib import Path
from .utils import sanitize_filename, detect_extension

def save_artifact(artifact, output_dir):
    date_folder = artifact["date"].strftime("%Y-%m-%d")
    folder = Path(output_dir) / date_folder
    folder.mkdir(parents=True, exist_ok=True)
    ext = detect_extension(artifact["type"])
    filename = sanitize_filename(artifact["title"])
    if not filename.endswith(ext):
        filename += ext
    path = folder / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(artifact["content"])
    return path

def save_manifest(artifacts, output_dir):
    manifest_path = Path(output_dir) / "manifest.json"
    manifest = [{
        "file": str(a["path"]),
        "title": a["title"],
        "type": a["type"],
        "date": a["date"].isoformat()
    } for a in artifacts]
    with open(manifest_path, "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, indent=2, ensure_ascii=False)
