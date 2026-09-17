#!/usr/bin/env python3
"""Turkish feasibility report -> single-page HTML artifact (screen reading)."""
import html, re, sys, json

SRC, OUT = sys.argv[1], sys.argv[2]
raw = open(SRC, encoding="utf-8").read().replace("➤", "▶")

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    return t

lines = raw.split("\n"); i, n = 0, len(lines)
body, toc, sec = [], [], 0
open_sec = False

def close():
    global open_sec
    if open_sec: body.append("</section>"); open_sec = False

def is_sep(s): return bool(re.match(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", s)) and "-" in s
def cells(r):
    r = r.strip()
    if r.startswith("|"): r = r[1:]
    if r.endswith("|"): r = r[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", r)]

while i < n:
    s = lines[i].strip()
    if not s: i += 1; continue

    if re.match(r"^-{3,}$", s): i += 1; continue

    m = re.match(r"^(#{1,4})\s+(.*)$", s)
    if m:
        lvl, txt = len(m.group(1)), m.group(2).strip()
        if lvl == 1:
            close(); sec += 1; aid = f"b{sec}"
            num = re.match(r"^(\d+)\.\s*(.*)$", txt)
            label = num.group(2) if num else txt
            kicker = num.group(1) if num else "•"
            if sec == 1:  # the source file's own title block — the masthead already carries it
                label, kicker = "Yöntem, sınırlar ve fiyat düzeltmeleri", "0"
            toc.append((kicker, label, aid))
            body.append(f'<section id="{aid}" class="bolum">')
            body.append(f'<h2 class="bh"><span class="bn">{html.escape(kicker)}</span>'
                        f'<span>{inline(label)}</span></h2>')
            open_sec = True
        else:
            body.append(f"<h{lvl+1} class='h{lvl}'>{inline(txt)}</h{lvl+1}>")
        i += 1; continue

    if "|" in s and i + 1 < n and is_sep(lines[i+1]):
        head = cells(s); nc = len(head); i += 2
        rows = []
        while i < n and "|" in lines[i] and lines[i].strip():
            rows.append(cells(lines[i])); i += 1
        t = [f'<div class="tablo" role="region" tabindex="0" aria-label="Tablo"><table data-cols="{nc}"><thead><tr>']
        t += [f"<th scope='col'>{inline(c)}</th>" for c in head]
        t.append("</tr></thead><tbody>")
        for r in rows:
            r = (r + [""] * nc)[:nc]
            t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        t.append("</tbody></table></div>")
        body.append("".join(t)); continue

    if s.startswith(">"):
        buf = []
        while i < n and lines[i].strip().startswith(">"):
            buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
        inner, sub = [], []
        for b in buf:
            if b.strip().startswith("- "): sub.append(f"<li>{inline(b.strip()[2:])}</li>")
            else:
                if sub: inner.append("<ul>" + "".join(sub) + "</ul>"); sub = []
                if b.strip(): inner.append(f"<p>{inline(b.strip())}</p>")
        if sub: inner.append("<ul>" + "".join(sub) + "</ul>")
        body.append("<blockquote>" + "".join(inner) + "</blockquote>"); continue

    if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
        tag = "ol" if re.match(r"^\d+\.\s+", s) else "ul"
        items = []
        while i < n:
            c = lines[i].strip()
            if not c:
                nxt = lines[i+1].strip() if i + 1 < n else ""
                if re.match(r"^([-*]|\d+\.)\s+", nxt): i += 1; continue
                break
            mm = re.match(r"^(?:[-*]|\d+\.)\s+(.*)$", c)
            if not mm:
                if items: items[-1] = items[-1][:-5] + " " + inline(c) + "</li>"; i += 1; continue
                break
            items.append(f"<li>{inline(mm.group(1))}</li>"); i += 1
        body.append(f"<{tag}>" + "".join(items) + f"</{tag}>"); continue

    buf = []
    while i < n and lines[i].strip() and not re.match(r"^(#{1,4}\s|>|[-*]\s|\d+\.\s|-{3,}$)", lines[i].strip()) \
          and not ("|" in lines[i] and i + 1 < n and is_sep(lines[i+1])):
        buf.append(lines[i].strip()); i += 1
    if buf: body.append("<p>" + inline(" ".join(buf)) + "</p>")
close()

toc_html = "".join(
    f'<li><a href="#{a}" data-t="{html.escape(l.lower())}"><span class="tn">{html.escape(k)}</span>'
    f'<span class="tl">{html.escape(l)}</span></a></li>' for k, l, a in toc)

open(OUT, "w", encoding="utf-8").write(
    TEMPLATE.replace("@@TOC@@", toc_html).replace("@@BODY@@", "".join(body))
) if False else None
print(json.dumps({"sections": len(toc), "body_chars": sum(len(x) for x in body)}))
open(OUT + ".parts.json", "w", encoding="utf-8").write(json.dumps({"toc": toc_html, "body": "".join(body)}))
