FONTS='/tmp/claude-0/-home-user-acompagnement/add46904-4241-51c5-837a-9d7b561d32e5/scratchpad/fonts/'
CSS = """
@font-face{font-family:Figtree;src:url(file://__F__figtree/package/files/figtree-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:Figtree;src:url(file://__F__figtree/package/files/figtree-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:Figtree;src:url(file://__F__figtree/package/files/figtree-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:Figtree;src:url(file://__F__figtree/package/files/figtree-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:Figtree;src:url(file://__F__figtree/package/files/figtree-latin-800-normal.woff2);font-weight:800}
@font-face{font-family:Playfair;src:url(file://__F__playfair-display/package/files/playfair-display-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:Playfair;src:url(file://__F__playfair-display/package/files/playfair-display-latin-600-italic.woff2);font-weight:600;font-style:italic}
@page{size:A4;margin:0}
:root{--ch:#6E100F;--ch2:#8E1B1A;--bl:#FDF2F0;--wm:#F5F0ED;--ink:#1a1a1a;--mute:#6b6260;--gold:#C9A46A}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:Figtree,sans-serif;color:var(--ink);font-size:10.8pt;line-height:1.55}
.page{width:210mm;height:297mm;padding:22mm 20mm 20mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.foot{position:absolute;bottom:10mm;left:20mm;right:20mm;display:flex;justify-content:space-between;font-size:8pt;color:#a09693;letter-spacing:.6px;text-transform:uppercase}
.brand{font-family:Playfair;font-weight:600;color:var(--ch);letter-spacing:.5px;text-transform:none;font-size:10pt}
h1,h2,h3{margin:0}
.kicker{font-size:8.5pt;font-weight:800;letter-spacing:2.2px;text-transform:uppercase;color:var(--ch);margin-bottom:6px}
h2{font-family:Playfair;font-weight:600;font-size:25pt;line-height:1.15;color:var(--ink);margin-bottom:14px}
h2 em{color:var(--ch);font-style:italic}
h3{font-size:12.5pt;font-weight:800;margin:14px 0 6px;color:var(--ink)}
p{margin:0 0 9px}
.lead{font-size:12pt;color:#3d3533}
.rule{width:46px;height:3px;background:var(--ch);border-radius:3px;margin:4px 0 16px}
.box{background:var(--bl);border-radius:14px;padding:14px 16px;margin:12px 0}
.box.dark{background:var(--ch);color:#fff}
.box.dark h3{color:#fff}
.box.line{background:#fff;border:1.5px solid #ecd9d5}
.tip{display:flex;gap:10px;align-items:flex-start}
.tip b.ic{flex:0 0 26px;height:26px;border-radius:50%;background:var(--ch);color:#fff;display:flex;align-items:center;justify-content:center;font-size:10pt}
ul.ch{list-style:none;padding:0;margin:6px 0}
ul.ch li{padding-left:20px;position:relative;margin:5px 0}
ul.ch li:before{content:'';position:absolute;left:2px;top:6px;width:9px;height:9px;border-radius:50%;background:var(--ch)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.card{border:1.5px solid #ecd9d5;border-radius:14px;padding:12px 14px;background:#fff}
.card .n{font-family:Playfair;font-size:20pt;color:var(--ch);line-height:1}
.day{border-radius:14px;padding:10px 14px;background:var(--wm);margin-bottom:9px;display:grid;grid-template-columns:62px 1fr;gap:12px;align-items:start}
.day .d{background:var(--ch);color:#fff;border-radius:10px;text-align:center;padding:6px 0}
.day .d small{display:block;font-size:7pt;letter-spacing:1.5px;font-weight:700;opacity:.8}
.day .d b{font-family:Playfair;font-size:18pt;line-height:1}
.day h4{margin:0 0 3px;font-size:11pt;font-weight:800}
.day p{margin:0;font-size:9.8pt;color:#3d3533}
.day .act{margin-top:4px;font-size:9.4pt;color:var(--ch);font-weight:700}
table{width:100%;border-collapse:collapse;font-size:8.6pt}
th{background:var(--ch);color:#fff;font-weight:700;padding:6px 4px;text-align:center}
td{border:1px solid #ecd9d5;height:9.6mm;padding:3px;text-align:center;color:#999}
td:first-child{font-weight:800;color:var(--ch);background:var(--bl)}
.cover{background:var(--ch);color:#fff;padding:0;display:flex;flex-direction:column;justify-content:space-between}
.cover .top{padding:20mm 20mm 0;display:flex;justify-content:space-between;align-items:center;font-size:9pt;letter-spacing:3px;text-transform:uppercase;font-weight:700;opacity:.9}
.cover .art{display:flex;justify-content:center}
.cover .ttl{padding:0 20mm}
.cover h1{font-family:Playfair;font-weight:600;font-size:44pt;line-height:1.05;margin-bottom:12px}
.cover h1 em{color:#F3C9C2}
.cover .sub{font-size:13pt;opacity:.9;max-width:140mm}
.cover .bot{padding:0 20mm 18mm;display:flex;justify-content:space-between;align-items:flex-end}
.pill{display:inline-block;border:1.5px solid rgba(255,255,255,.6);border-radius:30px;padding:6px 14px;font-size:9pt;font-weight:700;letter-spacing:1.2px;text-transform:uppercase}
.logo{font-family:Playfair;font-size:22pt}
.back{background:var(--wm);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.small{font-size:8.4pt;color:var(--mute)}
.recipe{display:grid;grid-template-columns:1fr 1.35fr;gap:16px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px dashed #e3cfca}
.recipe:last-child{border-bottom:none}
.recipe .meta{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 8px}
.recipe .meta span{background:var(--bl);color:var(--ch);font-size:8pt;font-weight:700;border-radius:20px;padding:3px 9px}
.recipe h3{margin:0;font-family:Playfair;font-weight:600;font-size:15pt}
.recipe ol{margin:4px 0 0;padding-left:18px;font-size:9.6pt}
.recipe ol li{margin-bottom:3px}
.recipe ul{margin:4px 0 0;padding-left:16px;font-size:9.6pt}
.recipe .why{font-size:8.8pt;color:var(--mute);font-style:italic;margin-top:6px}
.toc a{display:flex;justify-content:space-between;border-bottom:1px dotted #d8c4bf;padding:7px 0;color:var(--ink);text-decoration:none;font-weight:600}
.toc a span:last-child{color:var(--ch);font-weight:800}
""".replace("__F__", FONTS)

def cherry_svg(size=230, c1='#F3C9C2', moon=True):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="100" r="96" fill="rgba(255,255,255,.06)"/>
<path d="M70 128 Q78 70 108 40" stroke="#9FBF8F" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M128 126 Q126 78 108 40" stroke="#9FBF8F" stroke-width="5" fill="none" stroke-linecap="round"/>
<ellipse cx="128" cy="40" rx="24" ry="10" fill="#9FBF8F" transform="rotate(-18 128 40)"/>
<circle cx="66" cy="142" r="30" fill="{c1}"/>
<circle cx="56" cy="132" r="7" fill="rgba(255,255,255,.55)"/>
{'<mask id="m"><rect width="200" height="200" fill="#fff"/><circle cx="142" cy="128" r="28" fill="#000"/></mask><circle cx="130" cy="140" r="30" fill="'+c1+'" mask="url(#m)"/>' if moon else '<circle cx="132" cy="140" r="30" fill="'+c1+'"/>'}
<path d="M168 92 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3z" fill="{c1}"/>
<circle cx="40" cy="70" r="2.2" fill="{c1}"/><circle cx="160" cy="58" r="1.8" fill="{c1}"/>
</svg>'''

def foot(title, n):
    return f'<div class="foot"><span class="brand">Nasely</span><span>{title}</span><span>{n}</span></div>'

def doc(title, pages):
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

COVER_CSS = """
.cv2{background:var(--ch);color:#fff;padding:14mm;display:block}
.cv2 .frame{position:absolute;inset:14mm;border:1px solid rgba(255,255,255,.35);border-radius:2px;padding:14mm 14mm 12mm;display:flex;flex-direction:column;justify-content:space-between}
.cv2 .row{display:flex;justify-content:space-between;align-items:center;font-size:8.5pt;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:rgba(255,255,255,.8)}
.cv2 .big{font-family:Playfair;font-weight:600;font-size:170pt;line-height:1;color:transparent;-webkit-text-stroke:1.2px rgba(243,201,194,.9);margin:0 0 9mm -2mm;height:62mm}
.cv2 .lbl{font-size:9pt;letter-spacing:3px;text-transform:uppercase;color:#F3C9C2;font-weight:700;margin-bottom:6mm}
.cv2 h1{font-family:Playfair;font-weight:600;font-size:40pt;line-height:1.05;margin:0 0 6mm}
.cv2 h1 em{color:#F3C9C2}
.cv2 .sub{font-size:12pt;line-height:1.55;color:rgba(255,255,255,.88);max-width:125mm;margin:0}
.cv2 .sep{width:40mm;height:1px;background:rgba(255,255,255,.5);margin:8mm 0}
.cv2 .logo{font-family:Playfair;font-size:20pt;letter-spacing:.5px}
.bk2{background:var(--wm);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.bk2 .mono{font-family:Playfair;font-size:54pt;color:var(--ch);line-height:1;margin-bottom:6mm}
.bk2 .line{width:30mm;height:1px;background:var(--ch);opacity:.4;margin:0 auto 10mm}
"""
CSS = CSS + COVER_CSS

def cover2(big, label, title_html, sub, kind):
    return f'''<div class="page cv2"><div class="frame">
<div class="row"><span>Nasely</span><span>{kind}</span></div>
<div><div class="big">{big}</div><div class="lbl">{label}</div><h1>{title_html}</h1><div class="sep"></div><p class="sub">{sub}</p></div>
<div class="row"><span class="logo" style="letter-spacing:.5px;text-transform:none;font-weight:600;color:#fff">Nasely</span><span>Extrait de cerise griotte</span></div>
</div></div>'''

def back2(title_html, lead, legal):
    return f'''<div class="page bk2"><div class="mono">N</div><div class="line"></div>
<h2 style="font-size:30pt">{title_html}</h2><p class="lead" style="max-width:125mm">{lead}</p>
<p style="font-weight:800;color:var(--ch);margin-top:10px">nasely.fr</p>
<p class="small" style="max-width:140mm;margin-top:30mm">{legal}</p></div>'''
