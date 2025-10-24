import re

def sanitize_filename(name: str) -> str:
    return re.sub(r'[^\w\-.]', '_', name.strip())

def detect_extension(content_type: str) -> str:
    mapping = {
        "text/x-python": ".py",
        "text/python": ".py",
        "application/json": ".json",
        "text/markdown": ".md",
        "text/plain": ".txt",
        "text/html": ".html",
        "application/xml": ".xml",
    }
    return mapping.get(content_type.lower(), ".txt")
