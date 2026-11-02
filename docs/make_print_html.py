#!/usr/bin/env python3
"""Regenerate docs/analysis_summary_print.html from docs/analysis_summary.md.

`analysis_summary.md` is the single source of truth. The print HTML is a
derived artifact and must never be hand-edited — run this after any change to
the markdown, the same way `docs/figures/make_figures.py` keeps the SVG figures
reproducible from the response CSV:

    python3 docs/make_print_html.py

Standard library only, so it runs wherever python3 does. It handles exactly the
markdown subset `analysis_summary.md` uses: ATX headings, paragraphs, pipe
tables, blockquotes, bullet lists, horizontal rules, images with their figure
captions, and inline bold / italic / code / links.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent
SRC = DOCS / "analysis_summary.md"
OUT = DOCS / "analysis_summary_print.html"

STYLE = """<style>
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
*{box-sizing:border-box}
body{font:11pt/1.55 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;color:#111827;margin:0;padding:0 0 24pt;
     -webkit-print-color-adjust:exact;print-color-adjust:exact}
.wrap{max-width:190mm;margin:0 auto;padding:12mm 6mm}
h1{font-size:20pt;line-height:1.25;margin:0 0 4pt;letter-spacing:-.01em}
h2{font-size:14pt;margin:20pt 0 6pt;padding-bottom:3pt;border-bottom:1.5px solid #111827;break-after:avoid}
h3{font-size:11.5pt;margin:14pt 0 4pt;color:#1f2937;break-after:avoid}
h4{font-size:10.5pt;margin:11pt 0 3pt;color:#374151;break-after:avoid}
p{margin:0 0 7pt;orphans:3;widows:3}
strong{font-weight:700}
code{font:9.5pt ui-monospace,"SF Mono",Menlo,monospace;background:#f1f5f9;padding:.5pt 3pt;border-radius:3px}
ul,ol{margin:0 0 8pt;padding-left:16pt}
li{margin-bottom:3.5pt}
blockquote{margin:7pt 0 9pt;padding:6pt 11pt;border-left:2.5pt solid #94a3b8;background:#f8fafc;
  font-size:10pt;font-style:italic;color:#1f2937;break-inside:avoid}
table{width:100%;border-collapse:collapse;margin:8pt 0 12pt;font-size:9pt;break-inside:avoid;
  font-family:-apple-system,"Helvetica Neue",Helvetica,sans-serif}
th{background:#f1f5f9;text-align:left;padding:4.5pt 6pt;border:.5pt solid #cbd5e1;font-weight:700;font-size:8.5pt}
td{padding:4pt 6pt;border:.5pt solid #cbd5e1;vertical-align:top}
tbody tr:nth-child(even){background:#fafbfc}
hr{border:0;border-top:.5pt solid #d1d5db;margin:14pt 0}
figure{margin:12pt 0 16pt;padding:9pt 10pt 4pt;border:.5pt solid #d8dee7;background:#fcfdfe;
  border-radius:4px;break-inside:avoid}
figure img{width:100%;height:auto;display:block;margin:0 0 6pt;background:#fff}
figcaption{font:8.8pt/1.4 -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#475569}
.fignum{font-weight:700;color:#111827}
.docmeta{font:9pt -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#64748b;
  border-bottom:.5pt solid #d1d5db;padding-bottom:8pt;margin-bottom:14pt}
.banner{background:#fff7ed;border:1pt solid #fdba74;border-radius:4px;padding:7pt 10pt;margin:0 0 14pt;
  font:9pt/1.45 -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#7c2d12}
.noprint{margin:0 0 14pt;padding:9pt 12pt;background:#eef2ff;border:1pt solid #c7d2fe;border-radius:5px;
  font:10pt/1.5 -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#312e81}
@media print{ .noprint{display:none} .wrap{padding:0} }
</style>"""

HOWTO = """<div class="noprint"><strong>To make the PDF:</strong> press <strong>&#8984;P</strong>, then choose
<em>Save as PDF</em> from the PDF menu (bottom-left). Enable &ldquo;Print backgrounds&rdquo; so the figures and
table shading render. This blue box does not print.</div>"""

LICENCE_NOTE = ("""This analysis is licensed CC BY 4.0; the underlying response data it draws on is """
                """separately governed by the repository&rsquo;s research-use licence """
                """(docs/DATA_LICENSE.md). Quoted excerpts are pseudonymised.""")

DRAFT_PREFIX = "<strong>Draft &mdash; not approved, not committed.</strong> "


def banner(md: str) -> str:
    """Build the banner from the markdown's own Status line, never from a hard-coded string.

    The draft warning must not outlive the draft. Hard-coding it meant that approving the
    Markdown and regenerating would emit a page still calling itself unapproved, so the
    status is read from the source document instead: the draft prefix appears only while
    the Status line still says "draft".
    """
    m = re.search(r"^\*\*Status:\*\*\s*(.+)$", md, re.M)
    is_draft = bool(m) and "draft" in m.group(1).lower()
    return '<div class="banner">%s%s</div>' % (DRAFT_PREFIX if is_draft else "", LICENCE_NOTE)

# --- inline ---------------------------------------------------------------

CODE_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
ITAL_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", re.S)


def inline(text: str) -> str:
    """Escape, then apply inline markdown. Code spans are protected first."""
    spans: list[str] = []

    def stash_code(m: re.Match) -> str:
        spans.append("<code>%s</code>" % html.escape(m.group(1)))
        return "\x00%d\x00" % (len(spans) - 1)

    text = CODE_RE.sub(stash_code, text)
    text = html.escape(text, quote=False)
    text = LINK_RE.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), text)
    text = BOLD_RE.sub(lambda m: "<strong>%s</strong>" % m.group(1), text)
    text = ITAL_RE.sub(lambda m: "<em>%s</em>" % m.group(1), text)
    return re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)


# --- block ----------------------------------------------------------------

IMG_RE = re.compile(r"^!\[(.*)\]\((.+)\)$")
CAP_RE = re.compile(r"^\*\*\*(Figure \d+\.)\*\*\s*(.*?)\*$")
ROW_SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            out.append("<hr/>")
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl))
            i += 1
            continue

        # image, optionally followed by a ***Figure N.** caption*
        m = IMG_RE.match(stripped)
        if m:
            alt, src = html.escape(m.group(1), quote=True), m.group(2)
            cap = ""
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n:
                cm = CAP_RE.match(lines[j].strip())
                if cm:
                    cap = '<figcaption><span class="fignum">%s</span> %s</figcaption>' % (
                        inline(cm.group(1)),
                        inline(cm.group(2)),
                    )
                    i = j
            out.append('<figure><img src="%s" alt="%s"/>%s</figure>' % (src, alt, cap))
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and ROW_SEP_RE.match(lines[i + 1].strip()):
            head = cells(stripped)
            i += 2
            body: list[list[str]] = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip()))
                i += 1
            th = "".join("<th>%s</th>" % inline(c) for c in head)
            rows = "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in body
            )
            out.append(
                "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, rows)
            )
            continue

        # blockquote (consecutive "> " lines become one quote, each on its own line)
        if stripped.startswith(">"):
            quoted: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                quoted.append(inline(lines[i].strip().lstrip(">").strip()))
                i += 1
            out.append("<blockquote>%s</blockquote>" % "<br/>".join(quoted))
            continue

        # bullet list
        if stripped.startswith("- "):
            items: list[str] = []
            while i < n and lines[i].strip().startswith("- "):
                items.append("<li>%s</li>" % inline(lines[i].strip()[2:]))
                i += 1
            out.append("<ul>%s</ul>" % "".join(items))
            continue

        # paragraph: consecutive non-blank lines that start no other block.
        # A line ending in two spaces is a markdown hard break.
        para: list[str] = []
        while i < n and lines[i].strip():
            raw = lines[i]
            s = raw.strip()
            if s == "---" or s.startswith(("#", "|", ">", "- ")) or IMG_RE.match(s):
                break
            para.append(inline(s) + ("\x01" if raw.endswith("  ") else ""))
            i += 1
        joined = " ".join(para).replace("\x01 ", "<br/>").rstrip("\x01").replace("\x01", "<br/>")
        # the meta block directly under the title gets its own styling
        cls = ' class="docmeta"' if out and out[-1].startswith("<h1>") else ""
        out.append("<p%s>%s</p>" % (cls, joined))

    return "\n".join(out)


def main() -> int:
    md = SRC.read_text(encoding="utf-8")
    title = md.split("\n", 1)[0].lstrip("# ").strip()
    body = convert(md)
    page = (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"/>\n'
        "<title>%s</title>\n%s</head><body><div class=\"wrap\">\n%s\n%s\n</div></body></html>\n"
        % (html.escape(title), STYLE, HOWTO + "\n" + banner(md), body)
    )
    OUT.write_text(page, encoding="utf-8")
    print("wrote %s (%d bytes) from %s" % (OUT.name, len(page), SRC.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
