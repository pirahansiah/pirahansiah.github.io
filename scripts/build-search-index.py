#!/usr/bin/env python3
import os, json, re

base = "/Volumes/4tb/2026-6/pirahansiah.github.io/contents/pkm"
index = []

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, "r", errors="replace") as fh:
                content = fh.read()
            title = f.replace(".md", "")
            m = re.search(r"^title:\s*(.+)", content, re.MULTILINE)
            if m:
                title = m.group(1).strip().strip('"')
            body = re.sub(r"^---.*?---", "", content, flags=re.DOTALL).strip()
            body = re.sub(r"[#*>\[\]()!`~]", " ", body)
            body = re.sub(r"\s+", " ", body).strip()
            rel = os.path.relpath(path, "/Volumes/4tb/2026-6/pirahansiah.github.io")
            url = "/" + rel.replace(".md", "")
            index.append({"title": title, "url": url, "body": body[:500]})
        except Exception:
            pass

out = "/Volumes/4tb/2026-6/pirahansiah.github.io/assets/search-index.json"
with open(out, "w") as f:
    json.dump(index, f)
print(f"Indexed {len(index)} files")
