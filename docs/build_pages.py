#!/usr/bin/env python3
"""Build the public GitHub Pages site from its markdown sources.

    python3 docs/build_pages.py

Writes three pages. All three are derived files: never hand-edit them, rebuild them.

  index.html          landing page at the repository root, linking the two documents
  docs/memo.html      the practice-based evaluation memo exactly as its author delivered it,
                      including her amendment of 9 November 2026 (see MEMO_AMENDMENT).
                      Source: docs/output.md, the Pandoc conversion of the original .docx,
                      which this script reads and never modifies. The script only lays the
                      text out (the conversion's bold heading lines become headings, its raw
                      <img> tags become figures, Pandoc's direction/underline tags are
                      dropped) and adds the site header and footer around it.
  docs/analysis.html  the participant survey analysis. Source: docs/analysis_summary.md.

Standard library only, so it runs wherever python3 does. It handles the markdown subset the
two sources use: ATX headings, paragraphs with hard breaks, pipe tables, blockquotes, bullet
lists, horizontal rules, images with figure captions, and inline bold / italic / code / links.

On the analysis page, single question references (Q16, Q18_1, ...) get a hover/focus pop-up
with the question's wording, read from the analysis's own "Appendix: Survey questions" table.
Memo section references (§5.2) get one with that section's title, read from the memo itself.
References to the analysis's own sections are links in the markdown, so they get none, and
ranges (Q1–Q15, §4–§8) get none either. The pop-ups never print.

On every page, clicking a figure opens it enlarged in a native <dialog> (Esc, the close button or a
click outside closes it; clicking a large image toggles its full size). Without JavaScript the
figure's link simply opens the image file.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

DOCS = Path(__file__).resolve().parent
ROOT = DOCS.parent
ANALYSIS_SRC = DOCS / "analysis_summary.md"
MEMO_SRC = DOCS / "output.md"
ANALYSIS_OUT = DOCS / "analysis.html"
MEMO_OUT = DOCS / "memo.html"
INDEX_OUT = ROOT / "index.html"

REPO_URL = "https://github.com/idsinge/hiaudio_FLO_practice-based_evaluation"
MEMO_PDF = "docs/Practice-Based%20Evaluation%20of%20the%20Hi-AUDiO%20platform%20by%20FLO%20Lab%20.pdf"
# The author's amendment to the memo as delivered: Nela Brown changed "two" to "three" onboarding
# sessions in section 3 of her PDF; docs/output.md carries the same change, made at her request.
# Stated on the memo page and the landing page.
MEMO_AMENDMENT = "amended by the author, 9 November 2026 (§3)"
# The title printed at the head of every page of the original PDF; docs/output.md has none.
MEMO_TITLE = "Practice-Based Evaluation: Hi-AUDiO"
SITE_NAME = "Hi-Audio practice-based evaluation"

STYLE = """<style>
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
*{box-sizing:border-box}
body{font:11pt/1.55 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;color:#111827;margin:0;padding:0 0 24pt;
     background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.wrap{max-width:190mm;margin:0 auto;padding:10mm 6mm}
h1{font-size:20pt;line-height:1.25;margin:0 0 4pt;letter-spacing:-.01em}
h2{font-size:14pt;margin:20pt 0 6pt;padding-bottom:3pt;border-bottom:1.5px solid #111827;break-after:avoid}
h3{font-size:11.5pt;margin:14pt 0 4pt;color:#1f2937;break-after:avoid}
h4{font-size:10.5pt;margin:11pt 0 3pt;color:#374151;break-after:avoid}
p{margin:0 0 7pt;orphans:3;widows:3}
a{color:#1d4ed8}
.section-link{color:#475569;margin-inline-start:.35em;text-decoration:none}
.section-link:hover,.section-link:focus-visible{color:#1d4ed8;text-decoration:underline}
.section-link:focus-visible{outline:2px solid currentColor;outline-offset:2px}
strong{font-weight:700}
code{font:9.5pt ui-monospace,"SF Mono",Menlo,monospace;background:#f1f5f9;padding:.5pt 3pt;border-radius:3px}
ul,ol{margin:0 0 8pt;padding-left:16pt}
li{margin-bottom:3.5pt}
blockquote{margin:7pt 0 9pt;padding:6pt 11pt;border-left:2.5pt solid #94a3b8;background:#f8fafc;
  font-size:10pt;font-style:italic;color:#1f2937;break-inside:avoid}
.tablewrap{overflow-x:auto;margin:8pt 0 12pt}
table{width:100%;border-collapse:collapse;font-size:9pt;break-inside:avoid;
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
.note{border-radius:4px;padding:7pt 10pt;margin:0 0 14pt;font:9pt/1.45 -apple-system,"Helvetica Neue",Helvetica,sans-serif}
.note{background:#f8fafc;border:1pt solid #cbd5e1;color:#334155}
nav.site{display:flex;flex-wrap:wrap;gap:4pt 14pt;align-items:baseline;padding:8pt 0 9pt;margin:0 0 14pt;
  border-bottom:.5pt solid #d1d5db;font:10pt -apple-system,"Helvetica Neue",Helvetica,sans-serif}
nav.site a{color:#334155;text-decoration:none}
nav.site a:hover{text-decoration:underline}
nav.site a.home{font-weight:700;color:#111827;margin-right:auto}
nav.site a[aria-current]{color:#111827;font-weight:600}
@media (max-width:600px){ nav.site a.home{flex-basis:100%} }
footer.site{margin-top:28pt;padding-top:10pt;border-top:.5pt solid #d1d5db;
  font:8.5pt/1.45 -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#475569}
footer.site img{width:200px;max-width:60%;height:auto;display:block;margin:0 0 8pt}
.lead{font-size:12pt;margin:6pt 0 16pt}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:12pt;margin:0 0 16pt}
.card{display:block;border:1pt solid #cbd5e1;border-radius:6px;padding:12pt 14pt;color:inherit;text-decoration:none;background:#fcfdfe}
.card:hover,.card:focus{border-color:#1d4ed8;box-shadow:0 1px 6px rgba(29,78,216,.15)}
.card h2{border:0;margin:0 0 3pt;padding:0;font-size:14pt}
.card .by{font:9pt -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#64748b;margin:0 0 7pt}
.card .go{font:10pt -apple-system,"Helvetica Neue",Helvetica,sans-serif;color:#1d4ed8;font-weight:600}
.badge{font:8pt -apple-system,"Helvetica Neue",Helvetica,sans-serif;background:#fff7ed;color:#9a3412;
  border:1pt solid #fdba74;border-radius:3px;padding:0 4pt;vertical-align:middle}
.small{font-size:10pt;color:#334155}
.tip{position:relative;border-bottom:1px dotted #64748b;cursor:help}
.tip:hover::after,.tip:focus::after{content:attr(data-tip);position:absolute;left:0;top:calc(100% + 4px);z-index:20;
  width:max-content;max-width:min(24rem,80vw);padding:6pt 8pt;background:#111827;color:#f9fafb;border-radius:4px;
  font:9pt/1.4 -apple-system,"Helvetica Neue",Helvetica,sans-serif;font-weight:400;font-style:normal;
  white-space:normal;text-align:left;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.tip:focus{outline:1px solid #94a3b8;outline-offset:1px}
@media (hover:none){ .tip{cursor:pointer} }
main p,main li{overflow-wrap:anywhere}
figure a.zoom{display:block;cursor:zoom-in}
dialog.zoom-view{padding:0;margin:0;border:0;background:transparent;width:100vw;height:100vh;max-width:100vw;max-height:100vh}
dialog.zoom-view[open]{display:flex;overflow:auto}
dialog.zoom-view::backdrop{background:rgba(15,23,42,.88)}
dialog.zoom-view img{margin:auto;width:96vw;height:auto;max-height:94vh;object-fit:contain;background:#fff;cursor:zoom-in}
dialog.zoom-view.actual img{width:auto;max-width:none;max-height:none;cursor:zoom-out}
dialog.zoom-view .close{position:fixed;top:10px;right:14px;z-index:2;border:0;border-radius:50%;width:40px;height:40px;
  background:rgba(17,24,39,.75);color:#fff;font:26px/40px -apple-system,"Helvetica Neue",Helvetica,sans-serif;cursor:pointer}
@media print{ dialog.zoom-view{display:none !important} }
/* On screen: one column for text, tables and figures alike, sized for comfortable reading,
   with a larger type scale. Print keeps the A4 sizes above. */
@media screen{
  body{font-size:1.125rem;line-height:1.6}
  .wrap{max-width:52rem;padding:1.5rem 1.25rem 2rem}
  h1{font-size:1.9rem} h2{font-size:1.4rem} h3{font-size:1.15rem} h4{font-size:1.05rem}
  code{font-size:.85em} blockquote{font-size:.95em}
  table{font-size:.9rem} th{font-size:.85rem} figcaption{font-size:.85rem}
  .docmeta,.note{font-size:.85rem}
  nav.site{font-size:.95rem} footer.site{font-size:.8rem}
  .lead{font-size:1.15em} .small{font-size:.95rem}
  .card h2{font-size:1.3rem} .card .by{font-size:.85rem} .card .go{font-size:.95rem} .badge{font-size:.7rem}
  .tip:hover::after,.tip:focus::after{font-size:.85rem}
}
@media screen and (min-width:60rem){ .wrap{max-width:min(90vw,68rem)} }
@media print{ nav.site,.section-link{display:none} .wrap{padding:0} .tablewrap{overflow:visible}
  .tip{border-bottom:none} .tip::after{content:none !important} a{color:inherit} }
</style>"""

# Funding acknowledgement and the Horizon Europe disclaimer, word for word as in README.md.
FUNDING = (
    "The Hi-Audio platform is developed as part of the project <em>Hybrid and Interpretable Deep "
    "Neural Audio Machines</em>, funded by the European Research Council (ERC) under the European "
    "Union&rsquo;s Horizon Europe research and innovation programme (grant agreement No. 101052978)."
)
DISCLAIMER = (
    "Funded by the European Union. Views and opinions expressed are however those of the author(s) "
    "only and do not necessarily reflect those of the European Union or the European Research Council "
    "Executive Agency. Neither the European Union nor the granting authority can be held responsible for them."
)


def is_draft(md: str) -> bool:
    m = re.search(r"^\*\*Status:\*\*\s*(.+)$", md, re.M)
    return bool(m) and "draft" in m.group(1).lower()


# --- inline ---------------------------------------------------------------

CODE_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
ITAL_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", re.S)
URL_RE = re.compile(r'(?<![\w/"=])(https?://[^\s<>"]*[^\s<>".,;:!?)\]])')


def inline(text: str) -> str:
    """Escape, then apply inline markdown. Code spans are protected first."""
    spans: list[str] = []

    def stash_code(m: re.Match) -> str:
        spans.append("<code>%s</code>" % html.escape(m.group(1)))
        return "\x00%d\x00" % (len(spans) - 1)

    text = CODE_RE.sub(stash_code, text)
    text = html.escape(text, quote=False)
    text = LINK_RE.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), text)
    # bare web addresses become links too (outside existing links), e.g. DOIs in reference lists
    text = "".join(part if part.startswith("<a ") else URL_RE.sub(r'<a href="\1">\1</a>', part)
                   for part in re.split(r"(<a [^>]*>.*?</a>)", text))
    text = BOLD_RE.sub(lambda m: "<strong>%s</strong>" % m.group(1), text)
    text = ITAL_RE.sub(lambda m: "<em>%s</em>" % m.group(1), text)
    return re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)


# --- block ----------------------------------------------------------------

def slug(text: str) -> str:
    """Heading id, built the way GitHub and GitHub Pages (kramdown, GFM input) build theirs,
    so links written for the markdown also work in this HTML."""
    t = text.strip().lower()
    t = "".join(c for c in t if c in " -_" or unicodedata.category(c)[0] in "LNM")
    return t.replace(" ", "-")


IMG_RE = re.compile(r"^!\[(.*)\]\((.+)\)$")
CAP_RE = re.compile(r"^\*\*\*(Fig(?:ure)? [A-Z]?\d+\.)\*\*\s*(.*?)\*$")
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
            title = m.group(2)
            fragment = slug(title)
            content = inline(title)
            if lvl > 1:
                label = html.escape(f"Link to {title}", quote=True)
                content += f' <a class="section-link" href="#{fragment}" aria-label="{label}">#</a>'
            out.append(f'<h{lvl} id="{fragment}">{content}</h{lvl}>')
            i += 1
            continue

        # image, optionally followed by a ***Figure N.** / ***Fig BN.** caption*
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
            out.append('<figure><a class="zoom" href="%s" title="Enlarge"><img src="%s" alt="%s"/></a>%s</figure>'
                       % (src, src, alt, cap))
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
                '<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                % (th, rows)
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
        cls = ' class="docmeta"' if out and out[-1].startswith("<h1") else ""
        out.append("<p%s>%s</p>" % (cls, joined))

    return "\n".join(out)


# --- the memo: layout only, never a change of wording ----------------------

FIG_BLOCK_RE = re.compile(r'<img src="([^"]+)"[^>]*/>\n\n(Fig [A-Z]?\d+\.(?:[^\n]|\n(?!\n))*)')


def memo_markdown(raw: str) -> str:
    """Turn the Pandoc conversion of the memo into the markdown subset convert() handles.

    Every word stays as converted: this only drops Pandoc's direction and underline tags,
    joins each raw <img> tag with its "Fig Bn." caption, promotes the bold heading lines to
    headings, and gathers the header fields into one block under the PDF's own title.
    """
    t = raw.replace("\r\n", "\n")
    t = re.sub(r'<span dir="rtl">(.*?)</span>', r"\1", t, flags=re.S)
    t = re.sub(r"<u>(.*?)</u>", r"\1", t, flags=re.S)

    def figure(m: re.Match) -> str:
        caption = " ".join(m.group(2).split())
        num, text = re.match(r"(Fig [A-Z]?\d+\.)\s*(.*)", caption).groups()
        return "![%s](%s)\n\n***%s** %s*" % (text, m.group(1), num, text)

    t = FIG_BLOCK_RE.sub(figure, t)

    head, sep, rest = t.partition("\n**Summary**\n")
    fields = [ln for ln in head.split("\n") if ln.strip()]
    for k in range(len(fields) - 1):
        if fields[k + 1].startswith("**") and not fields[k].endswith("  "):
            fields[k] += "  "
    out = ["# " + MEMO_TITLE, "", "\n".join(fields), "", "## Summary"]

    after_appendix = False
    for line in rest.split("\n"):
        m = re.fullmatch(r"\*\*(.+?)\*\*", line.strip())
        if m:
            h = m.group(1)
            if re.fullmatch(r"\d+\.\s.+|Appendix [A-Z]", h):
                out.append("## " + h)
                after_appendix = h.startswith("Appendix")
                continue
            if re.fullmatch(r"\d+\.\d+\s.+", h) or after_appendix:
                out.append("### " + h)
                after_appendix = False
                continue
        if line.strip():
            after_appendix = False
        out.append(line)
    return "\n".join(out)


def memo_map(memo_md: str) -> dict[str, str]:
    """Memo section number -> title, from the memo's own numbered headings."""
    return {
        m.group(1): m.group(2)
        for m in re.finditer(r"^#{2,3}\s+(\d+(?:\.\d+)?)\.?\s+(.+?)\s*$", memo_md, re.M)
    }


# --- pop-ups ---------------------------------------------------------------

APPENDIX_HEADING = "## Appendix: Survey questions"
APPENDIX_ID = slug(APPENDIX_HEADING[3:])
RANGE_RE = re.compile(
    r"Q\d{1,2}(?:_\d)?\s?[–-]\s?Q?\d{1,2}(?:_\d)?(?![\w])"
    r"|§\s?\d+(?:\.\d+)?\s?[–-]\s?§?\d+(?:\.\d+)?"
)
REF_RE = re.compile(r"(?<![\w])(?P<q>Q\d{1,2}(?:_\d)?)(?![\w])|§\s?(?P<s>\d+(?:\.\d+)?)")
NO_TIP_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "a", "code"}


def question_map(md: str) -> dict[str, str]:
    """Question id -> wording, from the analysis's own appendix table, so the pop-ups
    and the appendix can never disagree."""
    i = md.find("\n" + APPENDIX_HEADING + "\n")
    if i < 0:
        return {}
    return {
        m.group(1): m.group(2)
        for m in re.finditer(r"^\|\s*(Q\d{1,2}(?:_\d)?)\s*\|\s*(.+?)\s*\|", md[i:], re.M)
    }


def tip(label: str, shown: str) -> str:
    return '<span class="tip" tabindex="0" data-tip="%s">%s</span>' % (
        html.escape(label, quote=True),
        shown,
    )


def add_tips(body: str, qmap: dict[str, str], smap: dict[str, str]) -> str:
    """Pop-ups for single question references (their wording) and memo section
    references (their title).

    Every plain § reference in the analysis is to the memo: references to the analysis's
    own sections are links, and text inside links is skipped, as is text in headings,
    code and the appendix itself. Ranges are left plain.
    """
    if not (qmap or smap):
        return body
    cut = body.find('<h2 id="%s">' % APPENDIX_ID)
    head, tail = (body, "") if cut < 0 else (body[:cut], body[cut:])
    out: list[str] = []
    depth = 0
    for part in re.split(r"(<[^>]+>)", head):
        if part.startswith("<"):
            m = re.match(r"</?([A-Za-z0-9]+)", part)
            if m and m.group(1).lower() in NO_TIP_TAGS:
                depth += -1 if part.startswith("</") else 1
            out.append(part)
            continue
        if depth or not ("Q" in part or "§" in part):
            out.append(part)
            continue
        kept: list[str] = []

        def keep(m: re.Match) -> str:
            kept.append(m.group(0))
            return "\x02%d\x02" % (len(kept) - 1)

        def pop(m: re.Match) -> str:
            q, s = m.group("q"), m.group("s")
            if q and q in qmap:
                return tip("%s. %s" % (q, html.unescape(qmap[q])), q)
            if s and s in smap:
                return tip("Memo §%s — %s" % (s, smap[s]), m.group(0))
            return m.group(0)

        text = REF_RE.sub(pop, RANGE_RE.sub(keep, part))
        out.append(re.sub("\x02(\\d+)\x02", lambda m: kept[int(m.group(1))], text))
    return "".join(out) + tail


# --- pages -----------------------------------------------------------------

ZOOM = """<dialog id="zoom" class="zoom-view" aria-label="Enlarged figure">
<form method="dialog"><button class="close" aria-label="Close">&times;</button></form><img alt=""/></dialog>
<script>
(function () {
  var d = document.getElementById("zoom");
  if (!d || typeof d.showModal !== "function") return;  /* no dialog support: the link opens the image */
  var big = d.querySelector("img");
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a.zoom");
    if (!a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    var img = a.querySelector("img");
    d.classList.remove("actual");
    big.src = a.getAttribute("href");
    big.alt = img ? img.alt : "";
    d.showModal();
  });
  big.addEventListener("click", function (e) {      /* toggle full size, when the image is larger than the screen */
    e.stopPropagation();
    if (d.classList.contains("actual") || big.naturalWidth > window.innerWidth) d.classList.toggle("actual");
  });
  d.addEventListener("click", function (e) { if (e.target === d) d.close(); });   /* click outside the image */
  d.addEventListener("close", function () { big.removeAttribute("src"); });
})();
</script>
"""


def page(title: str, body: str, root: str, current: str, description: str = "") -> str:
    """Wrap a body in the shared site chrome. `root` is the relative path to the repository
    root ("" or "../"); `current` names the page for the navigation bar."""

    def link(key: str, href: str, label: str) -> str:
        cur = ' aria-current="page"' if key == current else ""
        return '<a href="%s"%s>%s</a>' % (href, cur, label)

    nav = '<nav class="site">%s%s%s%s</nav>' % (
        '<a class="home" href="%sindex.html">%s</a>' % (root, SITE_NAME),
        link("memo", root + "docs/memo.html", "Memo"),
        link("analysis", root + "docs/analysis.html", "Survey analysis"),
        '<a href="%s">GitHub repository</a>' % REPO_URL,
    )
    footer = (
        '<footer class="site"><img src="%simages/ERC_logo.png" '
        'alt="Emblem of the European Union and logo of the European Research Council"/>'
        "<p>%s</p><p>%s</p>"
        '<p>Survey questions, response data, licences and citation details: '
        '<a href="%s">GitHub repository</a>.</p></footer>' % (root, FUNDING, DISCLAIMER, REPO_URL)
    )
    meta = '<meta name="description" content="%s"/>\n' % html.escape(description, quote=True) if description else ""
    return (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1"/>\n%s'
        "<title>%s</title>\n%s</head><body><div class=\"wrap\">\n%s\n"
        '<main class="%s">\n%s\n</main>\n%s\n</div>\n%s</body></html>\n'
        % (meta, html.escape(title), STYLE, nav, current, body, footer, ZOOM)
    )


def build_analysis(md: str, smap: dict[str, str]) -> str:
    title = md.split("\n", 1)[0].lstrip("# ").strip()
    body = add_tips(convert(md), question_map(md), smap)
    return page(title, body, "../", "analysis",
                "Participant survey analysis of the practice-based evaluation of the Hi-Audio platform.")


def build_memo(memo_md: str, memo_raw: str) -> str:
    date = re.search(r"\*\*Document Date:\*\*\s*(.+?)\s*$", memo_raw, re.M).group(1)
    note = (
        '<div class="note">The practice-based evaluation memo by Nela Brown (FLO Lab), dated %s, '
        'reproduced as delivered; %s: the onboarding sentence now says &ldquo;three separate two-hour '
        'sessions&rdquo;, previously &ldquo;two&rdquo;. <a href="../%s">PDF</a> &middot; licensed CC BY 4.0.</div>'
        % (html.escape(date), html.escape(MEMO_AMENDMENT), MEMO_PDF)
    )
    return page("%s — memo by Nela Brown, %s" % (MEMO_TITLE, date), note + "\n" + convert(memo_md),
                "../", "memo", "Practice-based evaluation of the Hi-Audio platform by FLO Lab (memo, %s)." % date)


def build_index(analysis_md: str, memo_raw: str) -> str:
    date = re.search(r"\*\*Document Date:\*\*\s*(.+?)\s*$", memo_raw, re.M).group(1)
    authors = re.search(r"^\*\*Authors:\*\*\s*(.+?)\s*$", analysis_md, re.M).group(1)
    authors = re.sub(r"\s*\([^)]*\)", "", authors)
    year = re.search(r"^\*\*Prepared:\*\*\s*(20\d\d)", analysis_md, re.M).group(1)
    badge = ' <span class="badge">Draft</span>' if is_draft(analysis_md) else ""
    body = """<h1>Practice-Based Evaluation of the Hi-Audio Platform</h1>
<p class="lead">In February and March 2026, nine performers from the Female Laptop Orchestra (FLO) used the
Hi-Audio web platform (<a href="https://hiaudio.fr">hiaudio.fr</a>) to record the source tracks of a collaborative
composition, which was then mixed offline for the Radiophrenia 2026 festival broadcast. Two documents report on that evaluation.</p>
<div class="cards">
<a class="card" href="docs/memo.html"><h2>Practice-based evaluation memo</h2>
<p class="by">Nela Brown, FLO Lab &middot; %s</p>
<p>The evaluator&rsquo;s account of the recording project: platform strengths, workflow challenges, design
implications and fit for professional creative work. Reproduced as delivered; %s.</p>
<span class="go">Read the memo &rarr;</span></a>
<a class="card" href="docs/analysis.html"><h2>Participant survey analysis%s</h2>
<p class="by">%s &middot; %s</p>
<p>Descriptive results from a follow-up questionnaire answered by nine FLO performers, compared section by
section with the memo&rsquo;s findings.</p>
<span class="go">Read the analysis &rarr;</span></a>
</div>
<p class="small">The memo is also available as a <a href="%s">PDF</a>. The survey questions,
the pseudonymised response data, licences and citation details are in the
<a href="%s">GitHub repository</a>.</p>""" % (
        html.escape(date), html.escape(MEMO_AMENDMENT), badge, html.escape(authors), year, MEMO_PDF, REPO_URL)
    return page("Practice-based evaluation of the Hi-Audio platform — FLO Lab", body, "", "index",
                "Practice-based evaluation of the Hi-Audio platform by the Female Laptop Orchestra (FLO), "
                "with the evaluation memo and the participant survey analysis.")


def main() -> int:
    analysis_md = ANALYSIS_SRC.read_text(encoding="utf-8")
    memo_raw = MEMO_SRC.read_text(encoding="utf-8")
    memo_md = memo_markdown(memo_raw)
    for path, text in (
        (MEMO_OUT, build_memo(memo_md, memo_raw)),
        (ANALYSIS_OUT, build_analysis(analysis_md, memo_map(memo_md))),
        (INDEX_OUT, build_index(analysis_md, memo_raw)),
    ):
        path.write_text(text, encoding="utf-8")
        print("wrote %s (%d bytes)" % (path.relative_to(ROOT), len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
