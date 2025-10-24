<p align="center">
  <img src="https://img.shields.io/badge/version-0.1.0--alpha-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.9%2B-yellow?style=for-the-badge">
</p>

# 🧠 GrokFX – Artifact Extractor  
### *Part of the Dynnovators Grok Export Ecosystem*

GrokFX is a standalone CLI that extracts, reconstructs, and organizes AI-generated artifacts (like code, configs, or docs) from **Grok** conversation exports.  
It reads `<xaiArtifact>` blocks and rebuilds them into real files (`.py`, `.json`, `.md`, etc.), grouped by their creation date and ready for version control.

---

## ✨ Features
- Parses `<xaiArtifact>` blocks from Grok conversations or JSON exports  
- Reconstructs files according to their declared `contentType`  
- Organizes outputs by artifact date (`YYYY-MM-DD` folders)  
- Generates a `manifest.json` with metadata for each export  
- Works seamlessly alongside the [Grok Export Toolkit](https://github.com/hugoamorales/grok_export_toolkit)

---

## ⚙️ Installation
```bash
git clone https://github.com/hugoamorales/grokfx.git
cd grokfx
pip install -e .
```

---

## 💡 Usage
```bash
grokfx extract conversation.txt --out ./artifacts
```

### Example output
```
artifacts/
├── 2025-10-21/
│   ├── config.json
│   └── auth.py
├── 2025-10-24/
│   └── main.py
└── manifest.json
```

---

## 🧭 Roadmap
- [ ] Multi-LLM support (Claude, GPT, Gemini)  
- [ ] Timestamp detection from conversation metadata  
- [ ] Export bundled ZIP with manifest summary  
- [ ] Integration with Dynnovators’ Grok Export Toolkit

---

## 🪞 Credits
Developed with care by **Dynnovators Studio** — creators of the [MAGI Decision Core v5](https://github.com/hugoamorales/magi-decision-core) and the [Grok Export Toolkit](https://github.com/hugoamorales/grok_export_toolkit).  
Licensed under the **MIT License**.

> *“Turning AI conversations into reproducible knowledge artifacts.”*

---

<p align="center">
  <sub>© 2025 Dynnovators Studio | grokfx v0.1.0-alpha</sub>
</p>
