import typer
from pathlib import Path
from .parser import parse_artifacts
from .saver import save_artifact, save_manifest

app = typer.Typer(help="GrokFX – Extracts artifacts from Grok conversations")

@app.command()
def extract(input_file: Path, out: Path = Path("./artifacts_export")):
    """Extract artifacts from Grok conversation file."""
    text = input_file.read_text(encoding="utf-8")
    typer.echo(f"🔍 Parsing {input_file.name}...")
    artifacts = parse_artifacts(text)
    typer.echo(f"✅ Found {len(artifacts)} artifact(s).")
    saved = []
    for art in artifacts:
        path = save_artifact(art, out)
        art["path"] = path
        saved.append(art)
        typer.echo(f"📝 Saved: {path}")
    save_manifest(saved, out)
    typer.echo(f"\n📦 Export complete → {out.resolve()}")

if __name__ == "__main__":
    app()
