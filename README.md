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
