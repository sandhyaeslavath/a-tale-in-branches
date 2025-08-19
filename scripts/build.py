#!/usr/bin/env python3
import os, glob, datetime, re
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

chapters = []
for path in sorted(glob.glob(str(CHAPTERS_DIR / "*.md"))):
    raw = Path(path).read_text(encoding="utf-8")

    # extract YAML front matter
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        body_md = m.group(2)
    else:
        meta, body_md = {}, raw

    title = meta.get("title", Path(path).stem)
    author = meta.get("author", "Anonymous")

    # convert markdown → html
    body_html = markdown.markdown(body_md, extensions=["extra", "toc", "sane_lists"])

    # make an anchor from the title
    anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    chapter_html = f'<article id="{anchor}">\n<h2>{title}</h2>\n<p class="meta">by {author}</p>\n{body_html}\n</article>\n'
    chapters.append((title, anchor, chapter_html))

# TOC
toc_items = "\n".join([f'<li><a href="#{a}">{t}</a></li>' for t, a, _ in chapters])
toc_html = f"<ol>\n{toc_items}\n</ol>"

# Merge into template
content_html = "\n".join([h for _, _, h in chapters])
built_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

page = TEMPLATE
page = page.replace("<!-- TOC -->", toc_html)
page = page.replace("<!-- CONTENT -->", content_html)
page = page.replace("<!-- BUILT_AT -->", built_at)

out = DIST / "book.html"
out.write_text(page, encoding="utf-8")
print(f"Built {out.relative_to(ROOT)}")
