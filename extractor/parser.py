import re, html
from datetime import datetime

def parse_artifacts(text: str):
    pattern = re.compile(r'<xaiArtifact\s+([^>]+)>(.*?)</xaiArtifact>', re.S)
    artifacts = []
    for match in pattern.finditer(text):
        attrs_raw, inner = match.groups()
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', attrs_raw))
        title = attrs.get("title", "artifact")
        ctype = attrs.get("contentType", "")
        art_id = attrs.get("artifact_id", "unknown")
        date_match = re.search(r'"created_at"\s*:\s*"([^"]+)"', inner)
        if date_match:
            try:
                date = datetime.fromisoformat(date_match.group(1))
            except ValueError:
                date = datetime.now()
        else:
            date = datetime.now()
        code_match = re.search(r'```(?:\w+)?\s*(.*?)\s*```', inner, re.S)
        content = code_match.group(1) if code_match else inner.strip()
        content = html.unescape(content)
        artifacts.append({
            "id": art_id,
            "title": title,
            "type": ctype,
            "date": date,
            "content": content
        })
    return artifacts
