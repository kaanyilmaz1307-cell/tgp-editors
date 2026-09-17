# research/tools

## `rapor-md2html.py` — markdown → print-ready HTML → PDF

Purpose-built converter for the feasibility reports in `research/`. It is not a
general markdown engine: it handles exactly the constructs those files use (ATX
headings, GFM pipe tables, blockquotes, bullet/ordered lists, horizontal rules,
bold/italic/code/links) and nothing else. No third-party dependency — the
sandbox has no `markdown`, `reportlab` or `pypdf`.

Tables get a font-size class from their column count, and any table with 9+
columns is moved onto its own **landscape** page via a CSS named page, so the
wide comparison tables stay legible in print.

### Usage

```bash
python3 research/tools/rapor-md2html.py <input.md> <output.html>

/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
  --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=25000 \
  --print-to-pdf=<output.pdf> "file://<absolute path to output.html>"
```

The cover page reads its title, verdict and metadata from constants at the
bottom of the script — edit them there when reusing it for another report.

### Notes

- The cover is `height: 292mm`, not 297mm: at exactly the page height Chromium
  rounds it onto a second page.
- `--no-pdf-header-footer` suppresses Chromium's default header/footer. There
  are no page numbers in the footer as a result; Chromium's print engine does
  not support `@page` margin boxes, and no PDF library is available in this
  environment to stamp them afterwards.
- Output for the Turkish report: 71 pages (66 portrait + 5 landscape), ~2.5 MB.

## `rapor-md2web.py` — markdown → web page (Artifact)

Same converter family, different target: emits an HTML fragment for a Claude
Artifact (no doctype/html/head/body wrapper — the publish skeleton supplies
those) with a sticky table of contents, a section filter, scroll-spy, and
tables in horizontally scrollable containers sized by column count.

```bash
python3 research/tools/rapor-md2web.py <input.md> <parts-prefix>   # writes <prefix>.parts.json
```

The page shell (design tokens, masthead, decision gates, scripts) lives in the
build step that consumes that JSON; `rapor-web.html` is the last rendered
output.

Published page: https://claude.ai/artifact/EnqFkc88oF8CGE6PrfzQjy
