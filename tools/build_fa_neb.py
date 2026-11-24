import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_site import *

# =========================== FRANCISC'ANDREA ================================
css = """    .logo { position: relative; overflow: hidden; }
    .logo img { position: absolute; max-width: none; }
    .marks { row-gap: var(--s-block); }
    .marks > .main { --c: 3 / 11; display: flex; flex-direction: column; align-items: center; gap: var(--s-block); }
    .marks > .var { display: flex; flex-direction: column; align-items: center; gap: var(--s-block); }
    .marks > .var:nth-of-type(2) { --c: 1 / 7; } .marks > .var:nth-of-type(3) { --c: 7 / 13; }
    .marks p { max-width: 528px; }
    .marks .main p { text-align: center; }
    .swatches { column-gap: var(--gutter); }
    .swatches > div { display: flex; flex-direction: column; gap: var(--s-text); }
    .swatches > div:not(:last-child) .chip { margin-right: calc(-1 * var(--gutter)); }
    .swatches .chip { aspect-ratio: auto; height: calc(100vw * 512 / 1440); min-height: 160px; }
    .swatches p { font-family: var(--serif-mono); font-size: 14px; line-height: 1.2; }
    .fa-spec { background: #ece1d5; color: #20201a; font-family: "Roboto Mono", monospace; }
    .fa-spec .corm { font-family: "Cormorant Upright", serif; }
    @media (max-width: 768px) {
      .marks > .main, .marks > .var { --m: 1 / -1; }
      .swatches > div { --m: span 2 !important; } .swatches .chip { margin-right: 0 !important; }
    }"""
sw = [("#ece1d5", "1 / 4", "Light neutral"), ("#a5a598", "4 / 6", "Light neutral"), ("#20201a", "6 / 9", "Dark"), ("#4b3f1b", "9 / 11", "Dark earth"), ("#4e1003", "11 / 12", "Wine"), ("#bd850a", "12 / 13", "Dry yellow")]
swatches = "\n".join(f'      <div style="--c: {c}"><div class="chip" style="background:{h}"></div><p>{n}<br>{h.upper()}</p></div>' for h, c, n in sw)
spec_fa = f'''    <div class="spec g fa-spec">
      <div class="rule"></div>
      <p class="caps c1 row1">Type specimen</p><p class="caps c2 row1">Cormorant Upright — display</p><p class="caps c3 row1">Roboto Mono — text</p>
      <p class="corm big row2" style="font-size:calc(var(--fs-display) * 1.857); line-height:.9; letter-spacing:-.01em; font-weight:600">Diseño floral</p>
      <div class="c3 row2" style="display:flex; flex-direction:column; gap:12px; --c: 9 / 12"><p style="font-size:14px; line-height:1.6">The project is born from the contemplation of the ephemeral: that instant when a flower reaches its highest point of beauty before fading.</p><p class="caps s">Roboto Mono Regular · 14 / 22</p><p style="font-size:11px; line-height:16px">Why Roboto Mono: it needed to be easy to master and available across platforms, since she would be creating her own content and wanted the system to be easy to apply.</p></div>
      <p class="caps s c1 row3">Cormorant Upright semibold</p>
      <div class="rule gap"></div>
      <p class="corm c1 row3" style="--c: 1 / 9; font-size:26px; line-height:1.25">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz 0123456789</p>
      <p class="c3 row3" style="font-size:12px; line-height:1.5">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñopqrstuvwxyz 0123456789 &amp; ¿? ¡! —</p>
    </div>'''
def logo(path, w, h, s):
    return f'<div class="logo" style="width:100%; max-width:{w}px; aspect-ratio:{w}/{h}"><img src="../{im(path)}" alt="" style="{s}"></div>'

body = hero("franciscandrea/cover", "francisc'andrea", "Brand identity", "francisc'andrea", "50% 40%")
body += ficha([("Client", "francisc'andrea"), ("Type", "Client commission"), ("Role", "Brand Identity"), ("Year", "2025"), ("Scope", "Logotype, mark system, typography, stationery, product application")])
body += "  <main>\n"
body += chapter(head("01  Intro", "Just as a pressed flower may seem fragile, it can also contain a powerful presence, suspended in time."),
    pair(("Concept", ["The project is born from the contemplation of the ephemeral: that instant when a flower reaches its highest point of beauty before fading. Right there, we decided to stop time."]),
         ("Visual language", ["The visual language also responds to this duality. The identity of francisc'andrea is built from contrast: a typography that moves between the light and the firm, reflecting the very essence of our creations."])))
body += chapter(head("02  logo System design"), f'''    <div class="marks g">
      <div class="main">{logo("franciscandrea/logotype", 860, 279, "left:-6.68%; top:-.16%; width:113.38%; height:100.16%")}<p>Logotype The visual identity of francisc'andrea is based on the encounter between contrast and harmony. Two names come together through a pause (the apostrophe extracted from the "f"), that does not separate, but connects. This gesture, shaped like a petal, symbolizes the instant in which the ephemeral stops and acquires permanence: the origin of the pressed flower.</p></div>
      <div class="var">{logo("franciscandrea/monogram", 208, 264, "left:-25.42%; top:.79%; width:125.35%; height:98.48%")}<p>Monogram (fcá). The petal, or apostrophe, becomes the core of our isotypes: first as a subtle monogram that keeps the name readable in code.</p></div>
      <div class="var">{logo("franciscandrea/minimal-mark", 162, 246, "left:-60.1%; top:-2.81%; width:159.91%; height:105.69%")}<p>Minimal mark. As an even more abstract form, where the initial (f) and the petal-apostrophe are enough to evoke the entire visual and conceptual universe of the brand.</p></div>
    </div>''')
# 03 The elements (flores sueltas) fuera por ahora: Antonia hará una animación con ellas.
# body += chapter(head("03  The elements"), media([img("franciscandrea/element-flower", "1 / 4", "1 / 3", "1 / 1", "Pressed flower element"), img("franciscandrea/dsc07748", "7 / 12", "3 / 5", "528 / 396", "Petal element")]))
body += chapter(head("03  Applications", text=["Business cards, stationery, graphics and the flower presses themselves. Mockups until the final photos arrive."]),
    media([img(f"franciscandrea/application-{i}", f"{1 + (i - 1) * 4} / {5 + (i - 1) * 4}", "span 4", "467 / 702", "Application") for i in (1, 2, 3)], "bleed"),
    media([img("franciscandrea/stationery-1", "1 / 7", "1 / 3", "711 / 459", "Stationery"), img("franciscandrea/stationery-2", "7 / 13", "3 / 5", "711 / 459", "Stationery")], "bleed"))
body += chapter(head("04  colors"), f'    <div class="swatches g">\n{swatches}\n    </div>')
body += chapter(head("05  Art direction", text=["The art direction I set for the brand's visual world: colour, light and the way flowers are shown."]),
    media([img("franciscandrea/art-direction", "1 / -1", None, "1440 / 700", "Art direction")], "bleed"))
body += chapter(head("06  Instagram today"), media([img("franciscandrea/instagram-1", "2 / 6", "1 / 3", "416 / 751", "francisc'andrea Instagram feed"), img("franciscandrea/instagram-2", "8 / 12", "3 / 5", "416 / 751", "francisc'andrea Instagram feed")]))
body += chapter(head("07  Typeface", low=None, extra='      <p>Cormorant Upright · Roboto Mono</p>').replace('row-gap: var(--s-head)', ''), spec_fa)
body += chapter(head("08  Result &amp; Credits"), credits("Result", "The identity is in use across business cards, stationery, graphics and the flower presses themselves, carrying the brand onto the product. Website currently in development.",
    [("Client", "francisc'andrea"), ("Brand identity", "Antonia Ilic Bromberg"), ("Year", "2025")]))
body += "  </main>\n"
body += nxt("nebular", "nebular/nebular-2", "Editorial", "Nebular", "50% 50%")
write("franciscandrea", page("francisc'andrea", "Brand identity for francisc'andrea, a floral design studio.", "franciscandrea", body, "#ffffff", css=css))

# ================================ NEBULAR ===================================
css = """    .lists { position: relative; }
    @media (min-width: 769px) { .lists .artists { position: relative !important; } }
    .lists .artists { position: absolute; top: 0; text-align: center; white-space: nowrap;
      font-family: "Source Serif 4", serif; font-weight: 600; font-size: 50px; line-height: 1.15; letter-spacing: -.02em; }
    .lists .side { position: absolute; white-space: pre; }
    .lists .side em { font-family: "Source Serif 4", serif; font-style: italic; font-size: 14px; }
    .issue-a .artists { --x: 7; }
    .covers { row-gap: var(--s-block); }
    .covers .cv { position: relative; overflow: hidden; aspect-ratio: 416 / 598; }
    .covers .cv img { position: absolute; max-width: none; }
    .covers .cv:nth-of-type(1) { --c: 3 / 7; --m: 1 / 3; } .covers .cv:nth-of-type(2) { --c: 7 / 11; --m: 3 / 5; }
    .covers > video { --c: 3 / 11; width: 100%; aspect-ratio: 864 / 691; object-fit: cover; }
    .gifs { column-gap: 0; }
    @media (max-width: 768px) { .gifs { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; } .gifs > * { grid-column: auto !important; } }
    .neb-spec { background: #000; color: #fff; font-family: "Geist", sans-serif; font-weight: 300; }
    .neb-spec .otto { font-family: "Source Serif 4", serif; font-weight: 600; }
    .cred3 p { white-space: pre-line; }
    @media (max-width: 1100px) {
      .lists { height: auto; display: flex; flex-direction: column; gap: 24px; }
      .lists > * { position: static !important; transform: none !important; text-align: left !important; }
      .lists .artists { font-size: 34px; white-space: normal; }
      .lists .side { white-space: pre-wrap; }
    }"""
def lists(artists, list_cols, side, side_cols, side_top):
    # la lista se centra dentro de su tramo de columnas
    a = "<br>".join(artists)
    return f'''    <div class="g">
      <div class="lists" style="--c: 1 / -1">
        <p class="artists" style="left: calc({list_cols[0]} * (100% + var(--gutter)) / 12); width: calc({list_cols[1]} * (100% + var(--gutter)) / 12 - var(--gutter))">{a}</p>
        <p class="side" style="left: calc({side_cols} * (100% + var(--gutter)) / 12); top:{side_top}px">{side}</p>
      </div>
    </div>'''
def issue(label, artists, lc, side, sc, st, ed, cover, back, video, name):
    return chapter(head(label), lists(artists, lc, side, sc, st),
        '    <div class="g" ><p class="label-low">Editorial</p></div>\n' + trio(ed).replace('<div class="trio g">', '<div class="trio g" style="margin-top:calc(var(--s-text) - var(--s-block))">'),
        f'''    <div class="covers g">
      <div class="cv"><img src="../{im("nebular/" + cover[0])}" alt="Nebular {name} — cover" style="{cover[1]}" loading="lazy"></div>
      <div class="cv"><img src="../{im("nebular/" + back[0])}" alt="Nebular {name} — back cover" style="{back[1]}" loading="lazy"></div>
      <video src="../img/nebular/{video}.mp4" poster="../img/nebular/{video}.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Pages of Nebular {name}"></video>
    </div>''')
spec_neb = '''    <div class="spec g neb-spec">
      <div class="rule"></div>
      <p class="caps c1 row1">Type specimen</p><p class="caps c2 row1">Otto (Dinamo) — titles</p><p class="caps c3 row1">Geist (Vercel) — text</p>
      <p class="otto big row2" style="font-size:50px; line-height:.96; letter-spacing:-.02em">Emotional Cartography of Art</p>
      <div class="c3 row2" style="display:flex; flex-direction:column; gap:12px"><p style="font-size:17px; line-height:1.55">Art magazine that reflects on why we create, what drives us, and how we translate emotions into visual language.</p><p class="caps s">Geist Light · 17 / 26</p></div>
      <p class="caps s c1 row3">Otto · titles</p>
      <div class="rule gap"></div>
      <p class="otto row3" style="--c: 1 / 9; font-size:26px; line-height:1.25">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz 0123456789</p>
      <p class="c3 row3" style="font-size:12px; line-height:1.5">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñopqrstuvwxyz 0123456789 &amp; ¿? ¡! —</p>
    </div>'''
body = hero("nebular/nebular-2", "Nebular — three issues", "Editorial", "Nebular — Emotional Cartography of Art", "50% 50%")
body += ficha([("Context", "Master in Editorial Design, ELISAVA"), ("Year", "2025–2026"), ("Issues", "Nº1 Exile · Nº2 Grief · Nº3 Body"), ("Editorial direction, art direction &amp; design", "Antonia Ilic Bromberg &amp; Manuela García Aristizábal"), ("Printing", "Tecnoart, Barcelona")])
body += "  <main>\n"
body += chapter(head("01  Intro", "Emotional Cartography of Art", low=None,
    extra='      <p class="label-low">Master in Editorial Design · September 2025 – June 2026</p>\n      <div class="t"><p>Art magazine that reflects on why we create, what drives us, and how we translate emotions into visual language. In a context of visual saturation and the constant production of content, the magazine offers a slower perspective on what happens before the artwork itself: the experiences, emotions, and inner tensions that shape the creative process and are transformed into art through literature, the visual arts, cinema, and music.</p></div>'))
body += chapter(media([f'      <video src="../img/nebular/gif-{n}.mp4" poster="../img/nebular/gif-{n}.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Nebular {t}" style="--c: {1 + i * 4} / {5 + i * 4}; --m: span 4; --r: 480 / 810"></video>' for i, (n, t) in enumerate([("exile", "Nº1 Exile"), ("grief", "Nº2 Grief"), ("body", "Nº3 Body")])], "bleed gifs"),
    head("", text=["Each issue is built around a shared tension connected to a deceased artist, whose legacy serves as the narrative core that links a range of contemporary artists.", "Rather than focusing on the final outcome, we understand creation as a process of transformation and as a way of giving form to the invisible. The magazine explores how experiences such as grief, exile, and bodily trauma transcend time, connecting people through art."]).replace('<h2 class="label"></h2>\n', ''))
body += issue("02  Issue 1 — Exile", ["Ana Mendieta", "Shirin Neshat", "Cristina Peri Rossi", "Ariane Mnouchkine", "Tala Madani", "Larissa Sansour", "Laura El-Tantawy"], (6, 6),
    "      Seven artists,\nseven ways\n         to navigate <em>exile</em>.", 2, 150,
    ["There is a word for the place you can no longer return to, but there is no word for the moment you realize that place has ceased to exist. Not the physical place, but the place as you once knew it, with your body inside it, with the person you were when it still belonged to you. Exile begins long before departure, and often it does not end with return, if return ever comes. What remains is an identity shaped in the space between two places, neither of them entirely your own.",
     "<p>Ana Mendieta’s work begins with the Cuban soil she left behind as a child, and to which she returned decades later to press her body against it, as if physical contact could recover something that time and distance had dissolved. Her Siluetas are not metaphors; they are the literal record of that attempt.</p><p>The fact that the body disappears and only the trace remains expresses something words cannot fully capture about what it means to belong to a place that no longer belongs to you.</p>",
     "From her work, we bring together artists who know that territory from within. Their practices speak of identities shaped through rupture, of languages that are lost and transformed, and of bodies that carry within them the history of the places that formed them. Exile is not only political or geographical; it is also what happens when a version of yourself is left on the other side of something you can no longer cross. It is a friction we have not been able to resolve, nor do we intend to, but one that we can expose and confront through art and community."],
    ("exile-cover", "left:-92.14%; top:-11.78%; width:282.87%; height:127.91%"), ("exile-back", "left:-2.64%; top:0; width:105.52%; height:102.1%"), "pages-exile", "Nº1 Exile")
body += issue("03  Issue 2 — Grief", ["Käthe Kollwitz", "Nan Goldin", "Sarah Sudhoff", "Björk", "Graciela Iturbide", "Joan Jonas", "Charlotte Wells"], (0, 5),
    "Seven artists,\n               seven ways\nto navigate <em>grief.</em>", 9, 60,
    ["Some losses leave an emptiness; others completely reshape the way the body, memory, and images continue to exist. Grief does not always arrive as a single, recognizable moment. Sometimes it slowly settles into the way we look, remember, and inhabit the world after an absence.",
     "In this issue, we approach grief from different perspectives. We are interested in how this experience reshapes identity and transforms the act of making. Käthe Kollwitz’s work opens this conversation. After losing her son Peter during the First World War, her practice became darker and profoundly human. Her prints and sculptures do not depict war through heroism, but through those who remain after loss: mothers, exhausted bodies, and embraces trying to hold on to something that is no longer there.",
     "From her work, we bring together artists who approach that same territory through different artistic languages. Their works speak of absence, memory, and relationships that endure even after disappearance. Some transform grief into image, others into sound, archive, gesture, or ritual. Art emerges in the space left by loss, giving it a form through which it can be seen."],
    ("grief-cover", "left:-92.17%; top:-16.29%; width:285.77%; height:129.22%"), ("grief-back", "left:1.92%; top:3.85%; width:96.16%; height:96.15%"), "pages-grief", "Nº2 Grief")
body += issue("04  Issue 3 — Body", ["Francesca Woodman", "Wangechi Mutu", "Mari Katayama", "Tracey Emin", "Adrian Ghenie", "Siân Davey", "Anne De Keersmaeker"], (6, 6),
    "      Seven artists,\nseven ways\n             to inhabit the <em>body</em>.", 0, 150,
    ["The skin is the body's most sensitive organ, and it seems deeply unfair that it is also the most exposed. Perhaps that is why we speak of feeling something under our skin, because blooming speaks as much of life as it does of death, and we carry both as much on the outside as within. We experience everything through our skin and, when it becomes too much, we want to tear it off with our own hands or beg someone else to do it for us, because the burning makes it impossible to move. The body speaks what we cannot, and perhaps we pay far less attention to it than we should.",
     "<p>Francesca Woodman's work speaks of the desire to disappear, of the ghosts that live within us, and of the walls that prevent us from escaping ourselves. It unsettles us because we have all inhabited that skin and know how difficult it can be to remain inside it.</p><p>Her work brings together artists who use their bodies to speak and to cry out through lived experience. Their practices expose abuse, reclaim space, and invite us into a territory that many of us have inhabited but perhaps never fully recognized.</p>",
     "These works allow us to imagine what the body would say if it could speak, or to read words that, in a better world, should never have to exist side by side because they describe something unacceptable. They also remind us that, contrary to what we are often led to believe, life can exist beyond the silence and isolation imposed by the walls to which we seem to belong. Through these works, we come to understand the weight of everything the world chooses not to name."],
    ("body-cover", "left:-86.93%; top:-11.85%; width:278.03%; height:125.71%"), ("body-back", "left:2.64%; top:3.68%; width:94.72%; height:97.83%"), "pages-body", "Nº3 Body")
body += chapter(head("05  The vellum sleeve"), f'''    <div class="g" style="row-gap:var(--s-head)">
      <img src="../{im("nebular/vellum-sleeve")}" alt="Vellum paper sleeve" loading="lazy" style="--c: 1 / 7; width:100%; aspect-ratio:640/480; object-fit:cover">
      <div class="t" style="--c: 7 / 12"><p>We designed a translucent vellum paper sleeve to separate the magazine from the artwork, as we felt that intervening directly on the piece would be too intrusive. This allows the image to remain clean once the sleeve is removed, giving the publication greater value as a collectible object.</p><p>At the same time, the sleeve reinforces the graphic concept by creating a sense of visual diffusion, echoing a nebula that gradually reveals the content underneath.</p></div>
    </div>''')
body += chapter(head("06  Typeface", extra='      <p>Geist (Vercel) · Otto (Dinamo)</p>'), spec_neb)
body += chapter(head("07  Credits"), '    <div class="trio g cred3">\n' + "\n".join(f'      <p>{t}</p>' for t in [
    "Editorial Direction, Art Direction and Design:\nAntonia Ilic Bromberg\nManuela García Aristizábal\n\nResearch and Archives:\nAntonia Ilic Bromberg\nManuela García Aristizábal\n\nMaster's Degree in Editorial Design\nElisava, Barcelona School of Design and Engineering",
    "Typeface:\nGeist (Vercel)\nOtto (Dinamo)\n\nPaper:\nArena Rough 90 gr\nFundas papel vegetal 90 gr\n\nPrinting:\nTecnoart, Barcelona\n\nBarcelona, 2026",
    "Acknowledgements:\nCarol Monpart\nIsabel Merino\nJosep Román, Affaire\nLaura Meseguer\nAne Guerra\nMaría Dolores Soriano\nMarc Panero"]) + "\n    </div>")
body += "  </main>\n"
body += nxt("wild-lama", "wildlama/wl-25-q1-525", "Art direction", "Wild Lama", "50% 21%")
write("nebular", page("Nebular", "Nebular — Emotional Cartography of Art. Art magazine, three issues. Master in Editorial Design, ELISAVA.", "nebular", body, "#000000", color="#fff", css=css))
print("ok")
