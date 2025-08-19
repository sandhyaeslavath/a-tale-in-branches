# A Tale in Branches

Each Git branch represents a chapter. Merging chapters into `main` rebuilds a single **book** at `dist/book.html`.

## How it works
- One branch per chapter: `chapter/01-intro`, `chapter/02-forest`, …
- Each chapter is a Markdown file in `chapters/` with YAML front matter.
- A Python script merges all chapters → `dist/book.html`.
- GitHub Actions rebuilds automatically on merges to `main`.

## Conventions
- Chapter file name: `NN-title.md` (NN = 2-digit order).
- Front matter:
```yaml
---
title: "Chapter X — Title"
author: "Your Name"
---

### `template.html`
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>A Tale in Branches</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root { --fg:#111; --bg:#fff; --muted:#666; --accent:#4b7bec; }
    body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.7 system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
    header { padding:2rem 1rem; border-bottom:1px solid #eee; }
    h1 { margin:.2rem 0; font-size:2rem; }
    .meta { color:var(--muted); }
    main { max-width: 820px; margin: 2rem auto; padding: 0 1rem; }
    nav#toc { background:#fafafa; border:1px solid #eee; padding:1rem; border-radius:12px; }
    nav#toc h2 { margin-top:0; font-size:1.1rem; }
    article { margin:2rem 0; }
    article h2 { border-bottom: 1px solid #eee; padding-bottom:.4rem; }
    footer { margin:3rem 0; color:var(--muted); text-align:center; }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    code, pre { background:#f6f8fa; border-radius:6px; padding:.2rem .4rem; }
  </style>
</head>
<body>
  <header>
    <h1>A Tale in Branches</h1>
    <div class="meta">A collaborative story written via Git branches.</div>
  </header>
  <main>
    <nav id="toc">
      <h2>Table of Contents</h2>
      <!-- TOC -->
    </nav>

    <!-- CONTENT -->

    <footer>
      Built with ❤️ by contributors. Last updated: <!-- BUILT_AT -->
    </footer>
  </main>
</body>
</html>
