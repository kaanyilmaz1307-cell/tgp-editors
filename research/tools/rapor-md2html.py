#!/usr/bin/env python3
"""Markdown -> print-ready HTML for the Turkish feasibility report.

Deliberately a purpose-built converter, not a general one: it handles exactly the
constructs used in the source file (ATX headings, GFM pipe tables, blockquotes,
bullet/ordered lists, hr, bold/italic/code/links) and nothing else. Tables get a
size class from their column count so wide ones stay legible in print.
"""
import html, re, sys, datetime

SRC, OUT = sys.argv[1], sys.argv[2]
raw = open(SRC, encoding="utf-8").read()

# Glyphs that DejaVu may not carry, swapped for ones it does.
raw = raw.replace("➤", "▶")

# ---------- inline ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    return t

lines = raw.split("\n")
out, toc = [], []
i, n = 0, len(lines)
sec = 0

def is_table_sep(s):
    return bool(re.match(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", s)) and "-" in s

def cells(row):
    r = row.strip()
    if r.startswith("|"): r = r[1:]
    if r.endswith("|"): r = r[:-1]
    # split on | not preceded by a backslash
    return [c.strip() for c in re.split(r"(?<!\\)\|", r)]

while i < n:
    ln = lines[i]
    s = ln.strip()

    if not s:
        i += 1; continue

    # horizontal rule / section break
    if re.match(r"^-{3,}$", s):
        out.append('<hr class="rule">'); i += 1; continue

    # headings
    m = re.match(r"^(#{1,4})\s+(.*)$", s)
    if m:
        lvl, txt = len(m.group(1)), m.group(2).strip()
        if lvl == 1:
            sec += 1
            aid = f"s{sec}"
            toc.append((txt, aid))
            out.append(f'<h1 id="{aid}">{inline(txt)}</h1>')
        else:
            out.append(f"<h{lvl}>{inline(txt)}</h{lvl}>")
        i += 1; continue

    # table
    if "|" in s and i + 1 < n and is_table_sep(lines[i + 1]):
        head = cells(s)
        ncol = len(head)
        cls = ("t-xs" if ncol >= 12 else "t-s" if ncol >= 9
               else "t-m" if ncol >= 6 else "t-l")
        wide = ' wrap-wide' if ncol >= 9 else ''
        body = []
        i += 2
        while i < n and "|" in lines[i] and lines[i].strip():
            body.append(cells(lines[i])); i += 1
        t = [f'<div class="tw{wide}"><table class="{cls}"><thead><tr>']
        t += [f"<th>{inline(c)}</th>" for c in head]
        t.append("</tr></thead><tbody>")
        for r in body:
            r = (r + [""] * ncol)[:ncol]
            t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        t.append("</tbody></table></div>")
        out.append("".join(t)); continue

    # blockquote (may span several lines)
    if s.startswith(">"):
        buf = []
        while i < n and lines[i].strip().startswith(">"):
            buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
        inner, sub = [], []
        for b in buf:
            if b.strip().startswith("- "):
                sub.append(f"<li>{inline(b.strip()[2:])}</li>")
            else:
                if sub: inner.append("<ul>" + "".join(sub) + "</ul>"); sub = []
                if b.strip(): inner.append(f"<p>{inline(b.strip())}</p>")
        if sub: inner.append("<ul>" + "".join(sub) + "</ul>")
        out.append('<blockquote>' + "".join(inner) + "</blockquote>"); continue

    # lists
    if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
        ordered = bool(re.match(r"^\d+\.\s+", s))
        tag = "ol" if ordered else "ul"
        items = []
        while i < n:
            c = lines[i].strip()
            if not c: 
                # a blank line ends the list unless the next line continues it
                if i + 1 < n and (re.match(r"^[-*]\s+", lines[i+1].strip())
                                  or re.match(r"^\d+\.\s+", lines[i+1].strip())):
                    i += 1; continue
                break
            mm = re.match(r"^(?:[-*]|\d+\.)\s+(.*)$", c)
            if not mm:
                if items:  # continuation line of the previous item
                    items[-1] = items[-1][:-5] + " " + inline(c) + "</li>"
                    i += 1; continue
                break
            items.append(f"<li>{inline(mm.group(1))}</li>")
            i += 1
        out.append(f"<{tag}>" + "".join(items) + f"</{tag}>"); continue

    # paragraph
    buf = []
    while i < n and lines[i].strip() and not re.match(r"^(#{1,4}\s|>|[-*]\s|\d+\.\s|-{3,}$)", lines[i].strip()) \
          and not ("|" in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
        buf.append(lines[i].strip()); i += 1
    if buf:
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

# ---------- assemble ----------
today = datetime.date.today().strftime("%d.%m.%Y")
_num = re.compile(r"^\d+\.\s*")
_items = []
for k, (t, a) in enumerate(toc):
    label = html.escape(_num.sub("", t))
    _items.append('<li><span class="tn">' + str(k + 1) + '</span><a href="#' + a + '">' + label + '</a></li>')
toc_html = "".join(_items)

CSS = """
@page { size: A4 portrait; margin: 15mm 14mm 16mm 14mm; }
@page cover { margin: 0; }
@page land { size: A4 landscape; margin: 12mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 9.6pt; line-height: 1.5;
       color: #1b1b19; margin: 0; }
.cover { page: cover; height: 292mm; overflow: hidden; padding: 28mm 24mm 17mm 24mm; display: flex;
         flex-direction: column; background: #12110f; color: #f5f1ea;
         break-after: page; }
.cover .kicker { font-family: "DejaVu Sans", sans-serif; font-size: 8.5pt; letter-spacing: .22em;
                 text-transform: uppercase; color: #c9a227; margin-bottom: 12mm; }
.cover h1 { font-size: 27pt; line-height: 1.16; margin: 0 0 8mm 0; font-weight: normal;
            border: 0; padding: 0; color: #f5f1ea; }
.cover .sub { font-size: 11.5pt; line-height: 1.45; color: #bdb6ab; max-width: 130mm; margin-bottom: auto; }
.cover .verdict { font-family: "DejaVu Sans", sans-serif; display: inline-block; align-self: flex-start;
                  border: 1.4pt solid #c9a227; color: #c9a227; padding: 3.5mm 7mm; font-size: 12.5pt;
                  letter-spacing: .08em; margin: 10mm 0 8mm 0; }
.cover .meta { font-family: "DejaVu Sans", sans-serif; font-size: 8.2pt; line-height: 1.7; color: #8e877d;
               border-top: .5pt solid #3a352f; padding-top: 5mm; }
.cover .meta b { color: #d6cfc4; font-weight: normal; }
.toc { break-after: page; }
.toc h2 { font-family: "DejaVu Sans", sans-serif; font-size: 13pt; letter-spacing: .05em;
          text-transform: uppercase; color: #6b6459; border-bottom: .8pt solid #d8d2c8;
          padding-bottom: 3mm; margin: 0 0 7mm 0; }
.toc ol { list-style: none; padding: 0; margin: 0; column-count: 2; column-gap: 12mm; }
.toc li { margin: 0 0 2.4mm 0; font-size: 9.2pt; break-inside: avoid; display: flex; gap: 3mm; }
.toc .tn { font-family: "DejaVu Sans", sans-serif; color: #b0a89c; min-width: 6mm; text-align: right; }
.toc a { color: #1b1b19; text-decoration: none; }
h1 { font-family: "DejaVu Sans", sans-serif; font-size: 16pt; line-height: 1.22; margin: 0 0 5mm 0;
     padding-bottom: 2.5mm; border-bottom: 1.6pt solid #12110f; break-before: page; break-after: avoid; }
h2 { font-family: "DejaVu Sans", sans-serif; font-size: 11.6pt; margin: 7mm 0 2.5mm 0;
     break-after: avoid; color: #12110f; }
h3 { font-family: "DejaVu Sans", sans-serif; font-size: 10pt; margin: 5.5mm 0 2mm 0;
     break-after: avoid; color: #3a352f; }
p { margin: 0 0 2.6mm 0; orphans: 2; widows: 2; }
ul, ol { margin: 0 0 3mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.2mm; }
a { color: #1b1b19; text-decoration: none; border-bottom: .4pt solid #c5bdb1; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: .86em; background: #f2efe9;
       padding: 0 .5mm; border-radius: 1px; }
strong { font-weight: bold; }
blockquote { margin: 3mm 0; padding: 3mm 4mm; background: #f7f4ee; border-left: 2pt solid #c9a227;
             break-inside: avoid; }
blockquote p { margin: 0 0 1.5mm 0; }
blockquote p:last-child { margin-bottom: 0; }
hr.rule { border: 0; border-top: .5pt solid #ddd7cd; margin: 6mm 0; }
h1 + hr.rule, hr.rule + h1 { display: none; }
.tw { margin: 0 0 4mm 0; break-inside: auto; }
.tw.wrap-wide { page: land; break-before: page; break-after: page; }
table { width: 100%; border-collapse: collapse; font-family: "DejaVu Sans", sans-serif; }
th, td { border: .4pt solid #cfc8bc; padding: 1.1mm 1.5mm; text-align: left; vertical-align: top;
         line-height: 1.34; }
th { background: #12110f; color: #f5f1ea; font-weight: normal; }
tbody tr:nth-child(even) td { background: #f7f4ee; }
table.t-l { font-size: 8.4pt; }
table.t-m { font-size: 7.6pt; }
table.t-s { font-size: 6.9pt; }
table.t-xs { font-size: 6.2pt; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
"""

doc = f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<title>İspanya/Fransa Premium Şal Girişimi — Fizibilite Raporu</title>
<style>{CSS}</style></head><body>
<section class="cover">
  <div class="kicker">E-Ticaret Girişim Fizibilite Raporu</div>
  <h1>Türkiye → İspanya → Fransa<br>Premium Kadın Şal / Fular<br>DTC Girişimi</h1>
  <div class="sub">Türkiye'den tedarik edilen kadın şallarını İspanya'da, ardından Fransa'da
  premium bir Avrupa aksesuar markası olarak konumlandırıp Meta + Google Ads ile
  2026 Q4'e kârlı şekilde ölçekleme fizibilitesi.</div>
  <div class="verdict">KARAR: ÖNCE TEST ET</div>
  <div class="meta">
    <b>Hazırlanan:</b> Kaan Yılmaz &nbsp;·&nbsp; <b>Tarih:</b> {today}<br>
    <b>Kapsam:</b> 26 bölüm · pazar analizi · birim ekonomisi · rakip fiyat taraması ·
    Meta &amp; Google modelleri · Q4 stratejisi · uyum · test planı<br>
    <b>Test bütçesi:</b> €5.000 sert tavan &nbsp;·&nbsp;
    <b>Baraj:</b> link CTR × CVR ≥ %0,053 · AOV ≥ €65 · CAC &lt; €30
  </div>
</section>
<section class="toc"><h2>İçindekiler</h2><ol>{toc_html}</ol></section>
{''.join(out)}
</body></html>"""

open(OUT, "w", encoding="utf-8").write(doc)
print(f"sections={len(toc)} html_bytes={len(doc):,}")
