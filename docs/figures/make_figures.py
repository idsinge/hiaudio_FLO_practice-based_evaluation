#!/usr/bin/env python3
"""
Regenerate the figures used in docs/analysis_summary.md.

Every value plotted is computed here from docs/participant_survey_responses.csv —
nothing is copied from the write-up. Running this script should reproduce the
committed SVGs byte-for-byte, so any reader can verify the figures against the data.

    cd docs/figures && python3 make_figures.py

No third-party dependencies; SVG is emitted directly. Figures use an explicit light
background so they stay legible under dark site themes.
"""
import csv, pathlib, re, statistics as st
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
CSV_PATH = HERE.parent / 'participant_survey_responses.csv'

MAP_PATH = HERE.parent / 'response_id_mapping.md'


def load_pid_order():
    """Read PID <-> CSV-row from ../response_id_mapping.md rather than assuming an order.

    CSV rows are reverse-chronological (row 0 is the newest submission), which is the
    opposite of the PDFs' 'Submission N' ordinal. Joining by position yields a clean but
    wrong mirror mapping, so the mapping table is the single source of truth.
    """
    rows = {}
    for line in MAP_PATH.read_text(encoding='utf-8').splitlines():
        m = re.match(r'\|\s*(P0\d)\s*\|[^|]*\|\s*(\d)\s*\|', line)
        if m:
            rows[int(m.group(2))] = m.group(1)
    assert len(rows) == 9, f'expected 9 mapping rows, parsed {len(rows)}'
    return [rows[i] for i in range(9)]

SCALE = {'Strongly disagree': 1, 'Disagree': 2, 'Somewhat disagree': 3,
         'Neither disagree nor agree': 4, 'Somewhat agree': 5, 'Agree': 6,
         'Strongly agree': 7}

ITEMS = ['Q16', 'Q17', 'Q18_1', 'Q18_2', 'Q18_3', 'Q18_4',
         'Q19_1', 'Q19_2', 'Q19_3', 'Q20_1', 'Q20_2', 'Q20_3', 'Q20_4']

LABEL = {
    'Q16': 'Q16  Meets professional standards', 'Q17': 'Q17  Facilitated artistic intentions',
    'Q18_1': 'Q18_1  Clear and understandable', 'Q18_2': 'Q18_2  Low mental effort',
    'Q18_3': 'Q18_3  Easy to use', 'Q18_4': 'Q18_4  Did what I wanted',
    'Q19_1': 'Q19_1  Enjoyable', 'Q19_2': 'Q19_2  Pleasant process', 'Q19_3': 'Q19_3  Had fun',
    'Q20_1': 'Q20_1  Good idea to use', 'Q20_2': 'Q20_2  Would find useful',
    'Q20_3': 'Q20_3  Would plan to use', 'Q20_4': 'Q20_4  Would recommend',
}
BLOCK = dict(Q16='a', Q17='a', Q18_1='b', Q18_2='b', Q18_3='b', Q18_4='b',
             Q19_1='c', Q19_2='c', Q19_3='c', Q20_1='d', Q20_2='d', Q20_3='d', Q20_4='d')
COLOUR = {'a': '#334155', 'b': '#2563eb', 'c': '#0d9488', 'd': '#b45309'}

BG, INK, MUTED, GRID, ACCENT = '#ffffff', '#0f172a', '#64748b', '#e2e8f0', '#dc2626'
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


PID = load_pid_order()


# Each item is identified by text that appears in its own CSV header and in no other.
# Q16/Q17 are single columns, so the question stem identifies them; Q18-Q20 are matrix
# sub-columns sharing a stem, so the statement after ">>" is what distinguishes them.
HEADER_KEY = {
    'Q16': 'meets the necessary standards as a professional audio recording application',
    'Q17': 'facilitated your artistic intentions',
    'Q18_1': 'My interaction with the Hi-Audio platform was clear and understandable',
    'Q18_2': 'Interacting with the Hi-Audio platform did not require a lot of mental effort',
    'Q18_3': 'I found the Hi-Audio platform to be easy to use',
    'Q18_4': 'I found it easy to get the Hi-Audio platform to do what I wanted it to do',
    'Q19_1': 'I found using the Hi-Audio platform to be enjoyable',
    'Q19_2': 'The actual process of using the Hi-Audio platform was pleasant',
    'Q19_3': 'I had fun using the Hi-Audio platform',
    'Q20_1': 'Using the Hi-Audio platform for recording music would be a good idea',
    'Q20_2': 'I would find the Hi-Audio platform useful for recording music',
    'Q20_3': 'I would plan to use the Hi-Audio platform in my next music project',
    'Q20_4': 'I would recommend the Hi-Audio platform to music colleagues',
}


def load():
    """Return {item: [value per respondent, in PID order]} recoded to 1-7.

    Every item is resolved by matching distinctive text inside its own CSV header, and
    each match is asserted unique. Earlier versions selected the 13 rating columns by
    header prefix and then paired them with ITEMS *in order* — which silently mislabels
    every figure if the export ever reorders a matrix block's sub-columns.
    """
    rows = list(csv.reader(open(CSV_PATH, encoding='utf-8')))
    data = rows[1:]
    assert len(data) == 9, f'expected 9 respondents, found {len(data)}'
    header = rows[0]
    col = {}
    for item, key in HEADER_KEY.items():
        hits = [i for i, h in enumerate(header) if key in h]
        assert len(hits) == 1, f'{item}: expected exactly 1 header containing {key!r}, found {len(hits)}'
        col[item] = hits[0]
    assert sorted(col) == sorted(ITEMS), 'HEADER_KEY and ITEMS disagree'
    assert len(set(col.values())) == 13, 'two items resolved to the same column'
    return {n: [SCALE[data[i][col[n]]] for i in range(9)] for n in ITEMS}


def without_p09(values):
    """Drop P09's value, located through the PID mapping rather than by row position."""
    j = PID.index('P09')
    return [v for i, v in enumerate(values) if i != j]


def frame(w, h, title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}">',
            f'<rect width="{w}" height="{h}" fill="{BG}"/>']


def fig_q16(num):
    w, h, L, R, base = 940, 200, 60, 60, 118
    x = lambda v: L + (v - 1) / 6 * (w - L - R)
    counts = {v: [PID[i] for i in range(9) if num['Q16'][i] == v] for v in sorted(set(num['Q16']))}
    o = frame(w, h, 'Distribution of the nine Q16 ratings across the 1 to 7 response scale')
    o.append(f'<line x1="{L}" y1="{base}" x2="{w-R}" y2="{base}" stroke="{GRID}"/>')
    for v in range(1, 8):
        o.append(f'<line x1="{x(v):.1f}" y1="{base-6}" x2="{x(v):.1f}" y2="{base+6}" stroke="{GRID}"/>')
        o.append(f'<text x="{x(v):.1f}" y="{base+24}" text-anchor="middle" font-family="{SANS}" font-size="12" fill="{MUTED}">{v}</text>')
    for lbl, v in (('Strongly disagree', 1), ('Neither', 4), ('Strongly agree', 7)):
        o.append(f'<text x="{x(v):.1f}" y="{base+40}" text-anchor="middle" font-family="{SANS}" font-size="10" fill="{MUTED}">{lbl}</text>')
    o.append(f'<line x1="{x(4):.1f}" y1="{base-100}" x2="{x(4):.1f}" y2="{base+6}" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    for v, pids in counts.items():
        for k, p in enumerate(pids):
            cy = base - 20 - k * 22
            o.append(f'<circle cx="{x(v):.1f}" cy="{cy}" r="9.5" fill="#2563eb"/>')
            o.append(f'<text x="{x(v):.1f}" y="{cy+3.5}" text-anchor="middle" font-family="{SANS}" font-size="9.5" font-weight="600" fill="#fff">{p}</text>')
    o.append(f'<text x="{x(7):.1f}" y="{base-20}" text-anchor="middle" font-family="{SANS}" font-size="11" font-style="italic" fill="#94a3b8">none</text>')
    o.append('</svg>')
    return '\n'.join(o)


def fig_items(num):
    L, R, T, rowh, w = 250, 66, 40, 25, 940
    h = T + rowh * len(ITEMS) + 50
    x = lambda v: L + (v - 1) / 6 * (w - L - R)
    o = frame(w, h, 'Mean rating for each of the thirteen items at n=9 and n=8, against the 4.0 scale midpoint')
    for v in range(1, 8):
        o.append(f'<line x1="{x(v):.1f}" y1="{T-8}" x2="{x(v):.1f}" y2="{T+rowh*len(ITEMS)}" stroke="{GRID}"/>')
        o.append(f'<text x="{x(v):.1f}" y="{T-16}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="{MUTED}">{v}</text>')
    o.append(f'<line x1="{x(4):.1f}" y1="{T-8}" x2="{x(4):.1f}" y2="{T+rowh*len(ITEMS)+6}" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{x(4):.1f}" y="{T+rowh*len(ITEMS)+24}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="{ACCENT}">midpoint 4.0</text>')
    for i, n in enumerate(ITEMS):
        y = T + rowh * i + rowh / 2
        m9, m8 = st.mean(num[n]), st.mean(without_p09(num[n]))
        c = COLOUR[BLOCK[n]]
        o.append(f'<text x="{L-12}" y="{y+4}" text-anchor="end" font-family="{SANS}" font-size="12" fill="{INK}">{LABEL[n]}</text>')
        o.append(f'<line x1="{x(min(m9,m8)):.1f}" y1="{y}" x2="{x(max(m9,m8)):.1f}" y2="{y}" stroke="{c}" stroke-width="1.5" opacity="0.45"/>')
        o.append(f'<circle cx="{x(m8):.1f}" cy="{y}" r="4" fill="{BG}" stroke="{c}" stroke-width="1.8"/>')
        o.append(f'<circle cx="{x(m9):.1f}" cy="{y}" r="5" fill="{c}"/>')
        o.append(f'<text x="{x(m9)+13:.1f}" y="{y+4}" font-family="{SANS}" font-size="11" fill="#334155">{m9:.2f}</text>')
    o.append('</svg>')
    return '\n'.join(o)


def fig_respondents(num):
    w, h, L, R, base = 940, 198, 60, 60, 106
    x = lambda v: L + (v - 1) / 6 * (w - L - R)
    means = sorted((st.mean([num[n][i] for n in ITEMS]), PID[i]) for i in range(9))
    o = frame(w, h, 'Mean rating across all thirteen items for each of the nine respondents')
    o.append(f'<line x1="{L}" y1="{base}" x2="{w-R}" y2="{base}" stroke="{GRID}"/>')
    for v in range(1, 8):
        o.append(f'<line x1="{x(v):.1f}" y1="{base-6}" x2="{x(v):.1f}" y2="{base+6}" stroke="{GRID}"/>')
        o.append(f'<text x="{x(v):.1f}" y="{base+24}" text-anchor="middle" font-family="{SANS}" font-size="12" fill="{MUTED}">{v}</text>')
    o.append(f'<line x1="{x(4):.1f}" y1="{base-80}" x2="{x(4):.1f}" y2="{base+6}" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{x(4):.1f}" y="{base-86}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="{ACCENT}">midpoint</text>')
    # Stack any marker whose centre is within one diameter of an already-placed marker
    # on the same row. Exact ties are not the only overlap: adjacent means a tenth of a
    # point apart also collide at r=9.5, which is what put P04 on top of P06/P07.
    placed, seen, labels, last_row = [], {}, [], [1]
    for m, p in means:
        row = 0
        while any(abs(x(m) - px) < 20 and r == row for px, r in placed):
            row += 1
        placed.append((x(m), row))
        cy = base - 22 - row * 22
        o.append(f'<circle cx="{x(m):.1f}" cy="{cy}" r="9.5" fill="#0d9488"/>')
        o.append(f'<text x="{x(m):.1f}" y="{cy+3.5}" text-anchor="middle" font-family="{SANS}" font-size="9.5" font-weight="600" fill="#fff">{p}</text>')
        # One value label per distinct mean, wherever its marker ended up stacked.
        k = round(m, 2)
        seen[k] = seen.get(k, 0) + 1
        if seen[k] == 1:
            # Stagger onto a second row when the previous label would overlap this one.
            row = 0
            if labels and x(m) - labels[-1] < 34:
                row = 1 - last_row[0]
            last_row[0] = row
            labels.append(x(m))
            o.append(f'<text x="{x(m):.1f}" y="{base+42+row*15}" text-anchor="middle" font-family="{SANS}" font-size="10" fill="#475569">{m:.2f}</text>')
    o.append('</svg>')
    return '\n'.join(o)


def main():
    num = load()
    import xml.etree.ElementTree as ET
    for name, svg in (('fig1_q16_distribution.svg', fig_q16(num)),
                      ('fig2_item_means.svg', fig_items(num)),
                      ('fig3_respondent_means.svg', fig_respondents(num))):
        ET.fromstring(svg)          # fail loudly rather than emit malformed XML
        (HERE / name).write_text(svg + '\n', encoding='utf-8')
        print('wrote', name, '(XML valid)')
    print('\nvalues plotted (verify against docs/analysis_summary.md):')
    for n in ITEMS:
        print(f'  {n:6} n=9 {st.mean(num[n]):.2f}   n=8 {st.mean(without_p09(num[n])):.2f}')
    print('  Q16 distribution:', dict(sorted(Counter(num['Q16']).items())))
    print('  respondent means:', {PID[i]: round(st.mean([num[n][i] for n in ITEMS]), 2) for i in range(9)})


if __name__ == '__main__':
    main()
