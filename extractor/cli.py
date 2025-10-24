#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────
#  Dynnovators presents:
#  GrokFX – Artifact Extractor v0.1.0-alpha
#  © 2025 Dynnovators Studio — MIT License
#  Website: https://dynnovators.com
#  Contact: hello@dynnovators.com
#  Grok™ is a registered trademark of xAI Corp.
#  This is an independent, open-source utility
#  not affiliated with or endorsed by xAI.
# ─────────────────────────────────────────────────────────────
#  File: cli.py
#  Version: 0.1.0-alpha
#  Author: Dynnovators Studio — AI Systems Division
#  Assistant: Lyra Magilla
# ─────────────────────────────────────────────────────────────

"""
Extracts and reconstructs <xaiArtifact> objects from Grok conversations
into actual files (e.g., Python, JSON, Markdown). Each artifact is stored
in a date-based folder and registered in a manifest.json for easy tracking.

Usage:
    python3 -m extractor.cli extract conversation.txt --out ./artifacts
"""

import typer
from pathlib import Path
from datetime import datetime
from .parser import parse_artifacts
from .saver import save_artifact, save_manifest
import sys

__version__ = "0.1.0-alpha"

BANNER = f"""
──────────────────────────────────────────────
Dynnovators presents:
GrokFX – Artifact Extractor v{__version__}
© 2025 Dynnovators Studio
https://dynnovators.com | hello@dynnovators.com
──────────────────────────────────────────────
Grok™ is a registered trademark of xAI Corp.
This is an independent, open-source utility.
──────────────────────────────────────────────
"""

HELP_TEXT = f"""{BANNER}
USAGE:
    grokfx extract <conversation_file.txt|.json> [--out ./output_folder]

DESCRIPTION:
    GrokFX parses <xaiArtifact> blocks from Grok conversation exports,
    reconstructing code, configs, and documents as real files grouped
    by their creation date. Generates a manifest.json for traceability.

EXAMPLES:
    grokfx extract prod-grok-session.txt
    grokfx extract conversation.json --out ./my_artifacts

VERSION:
    {__version__}
"""

app = typer.Typer(help="GrokFX – Extracts artifacts from Grok conversations")


@app.command()
def extract(input_file: Path, out: Path = Path("./artifacts_export")):
    """
    Extracts and reconstructs artifacts from a Grok conversation export.
    """
    try:
        typer.echo(BANNER)
        if not input_file.exists():
            typer.echo(f"❌ Error: File not found → {input_file}")
            raise typer.Exit(code=1)

        typer.echo(f"📂 Loading: {input_file}")
        text = input_file.read_text(encoding="utf-8")

        typer.echo("🔍 Parsing conversation...")
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
        typer.echo("──────────────────────────────────────────────")

    except Exception as e:
        typer.echo(f"❌ Unexpected error: {e}")
        raise typer.Exit(code=1)


def main():
    """
    CLI entrypoint for GrokFX.
    """
    if len(sys.argv) == 1 or sys.argv[1] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)
    app()


if __name__ == "__main__":
    main()
