import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_site import *

# =============================== WILD LAMA ==================================
css = """    .campaign { row-gap: var(--gutter); }
    .campaign > .info { --c: 1 / 4; display: flex; flex-direction: column; gap: 24px; } /* 24 entre grupos, 12 dentro de cada grupo */
    .campaign > .info p { white-space: pre-line; }
    .campaign > .cells { --c: 4 / 13; display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: var(--gutter); }
    .cells img { grid-column: span 3; width: 100%; aspect-ratio: 304 / 457; object-fit: cover; background: var(--ph); }
    .cells img.w2 { grid-column: span 6; aspect-ratio: 640 / 457; }
    .cells img.w3 { grid-column: span 9; aspect-ratio: 976 / 457; }
    .cells img.w3.low { aspect-ratio: 976 / 378; }
    .stats > div { display: flex; flex-direction: column; gap: var(--s-text); }
    .emails img { object-position: top; }
    @media (max-width: 768px) {
      .campaign > .info, .campaign > .cells { --m: 1 / -1; }
      .cells { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; gap: 8px !important; }
      .cells img { grid-column: span 1; } .cells img.w2, .cells img.w3 { grid-column: span 2; }
      .stats .display { font-size: 48px; }
    }"""
def cells(items):
    out = []
    for f, cls, pos in items:
        c = f' class="{cls}"' if cls else ""
        st = f' style="object-position:{pos}"' if pos else ""
        out.append(f'<img{c} src="../{im("wildlama/" + f)}" alt="Wild Lama campaign" loading="lazy"{st}>')
    return "".join(out)
team1 = "Team:\n\nCreative Direction\nCamila Espinoza\n\nArt Direction\nAntonia Ilic, Fernanda González\n\nPhotography\nAndrés Mora\n\nVideo\nRafael Núñez\n\nModels (Elite Models Chile)\nMartina Schneeberger\nDeco"
team2 = "Team:\n\nCreative Direction\nCamila Espinoza\n\nArt Direction\nAntonia Ilic, Fernanda González\n\nPhotography\nAndrés Mora\n\nVideo\nRafael Núñez\n\nModels: We Love Models Chile"
c1 = cells([("c1-01", "", ""), ("c1-02", "", ""), ("c1-03", "", ""), ("c1-04", "", ""), ("c1-05", "", ""), ("c1-06", "", ""), ("c1-07", "", ""), ("c1-08", "w2", ""), ("c1-09", "", ""), ("c1-10", "", ""), ("c1-11", "", ""), ("c1-12", "w3", "")])
c2 = cells([("c2-01", "w3", "50% 31%"), ("c2-02", "", ""), ("c2-03", "", ""), ("c2-04", "", ""), ("c2-05", "w3 low", ""), ("c2-06", "", ""), ("c2-07", "", ""), ("c2-08", "", ""), ("c2-09", "w2", ""), ("c2-10", "", "")])
body = hero("wildlama/wl-25-q1-525", "Wild Lama campaign", "Art direction", "Wild Lama", "50% 14.7%")
body += ficha([("Client", "Wild Lama — sustainable lifestyle brand, Chile"), ("Role", "Brand designer"), ("Period", "March 2024 – August 2025"), ("Web", '<a href="https://www.wildlama.com" target="_blank" rel="noopener">www.wildlama.com</a>')])
body += "  <main>\n"
body += chapter(head("01  Intro", "Maintaining a focus on identity, community, and visual culture."),
    pair(("The brand", ["The brand integrates environmental and social awareness criteria (it is a certified B Corporation) through the use of responsible materials, support for environmental causes, and continuous improvement of its value chain, maintaining a focus on identity, community, and visual culture."]),
         ("Role", ["Art direction and campaign production.<br>Event production with clients, linked to the brand's cause-driven pillar.<br>Photography direction for e-commerce.<br>Art direction for on-location / lifestyle productions.<br>Development of the visual system applied to Instagram.<br>Storytelling-based marketing strategy, aimed at boosting sales through social media and email marketing.<br>Web design (landing pages and UX/UI improvements)."])))
body += chapter(head("02  Selected Campaigns"),
    f'''    <div class="campaign g">
      <div class="info"><p>Campaign 1 — Autumn

Shot over three days in the south of Chile, between Puerto Varas, Puerto Montt and Cochamó. The challenge was organising everything from Santiago before travelling south for the shoot.</p><p>Responsibilities:

Art Direction, Styling, Planning, Casting and Production in collaboration with the creative team.</p><p>{team1}</p></div>
      <div class="cells">{c1}</div>
    </div>''',
    f'''    <div class="campaign g">
      <div class="info"><p>Campaign 2 — Santiago

A one-day shoot in Santiago across two locations: a warehouse that rents out props, then an abandoned house in a sanctuary on the hill.</p><p>{team2}</p></div>
      <div class="cells">{c2}</div>
    </div>''')
body += chapter(media([img("wildlama/c2-03", "1 / -1", None, "1440 / 810", "")], "bleed"))
body += chapter(head("03  Results", text=["Key results from the branding team during the period worked:"]),
    '''    <div class="trio g stats">
      <div><p class="display">1.33%</p><p>Reached the brand's highest-ever organic Instagram engagement (1.33% average in 2024).</p></div>
      <div><p class="display">9.43%</p><p>Produced the brand's best-performing organic post, achieving 9.43% engagement.</p></div>
      <div><p class="display">ROAS 20+</p><p>Email campaigns in Klaviyo maintained a ROAS above 20 across key launches.</p></div>
    </div>''',
    '    <div class="head g"><div class="t"><p>Purpose-driven content consistently outperformed average organic performance.</p></div></div>')
body += chapter(head("04  Content strategy", "Storytelling-based marketing strategy, aimed at boosting sales through social media and email marketing."),
    media([img(f"wildlama/content-{i}", f"{1 + (i - 1) * 4} / {5 + (i - 1) * 4}", ["1 / 3", "3 / 5", "1 / 3"][i - 1], "392 / 521", "Instagram content", "50% 41.5%") for i in (1, 2, 3)]))
body += chapter(head("05  Email marketing", text=["Email campaigns in Klaviyo maintained a ROAS above 20 across key launches."]),
    media([img(f"wildlama/email-{i}", f"{1 + (i - 1) * 4} / {5 + (i - 1) * 4}", ["1 / 3", "3 / 5", "1 / 3"][i - 1], r, "Email campaign") for i, r in ((1, "346 / 1672"), (2, "346 / 1739"), (3, "346 / 1783"))], "emails", "align-items:start"))
body += "  </main>\n"
body += nxt("sanguaza", "sanguaza/libro-centrado", "Editorial", "Una pizca de sangre y un vaso de sanguaza", "50% 45%")
write("wild-lama", page("Wild Lama", "Art direction, campaigns, content strategy and email marketing for Wild Lama.", "wild-lama", body, "#ffffff", css=css))

# ================================ SANGUAZA ==================================
css = """    .paper { position: relative; color: #fff; background: #2333c8 url("../img/sanguaza/paper-blue.jpg") center / cover; aspect-ratio: 1440 / 1149; padding-top: 40px; }
    .paper .head { row-gap: 36px; }
    .sg-spec { background: #fff; color: #2333c8; font-family: "Source Serif 4", serif; }
    @media (max-width: 768px) { .paper { aspect-ratio: auto; min-height: 70vh; } }"""
spec_sg = '''    <div class="spec g sg-spec">
      <div class="rule"></div>
      <p class="caps c1 row1">Type specimen</p><p class="caps c2 row1">Source Serif 4 — titles</p><p class="caps c3 row1">Source Serif 4 — text</p>
      <p class="big row2" style="font-size:calc(var(--fs-display) * 1.486); line-height:.96; letter-spacing:-.02em; font-weight:500">A Pinch of Blood and a Glass of Sanguaza</p>
      <div class="c3 row2" style="display:flex; flex-direction:column; gap:12px"><p style="font-size:17px; line-height:1.55">Whether it is a grandmother's birthday celebration or a "coming of age" ceremony among the Swazi people, we have never stopped creating rites.</p><p class="caps s">Source Serif 4 Regular · 17 / 26</p></div>
      <p class="caps s c1 row3" style="font-weight:600">Source Serif 4 MEDIUM · titles</p>
      <div class="rule gap"></div>
      <p class="row3" style="--c: 1 / 9; font-size:26px; line-height:1.25; font-weight:300">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz 0123456789</p>
      <p class="c3 row3" style="font-size:12px; line-height:1.5">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñopqrstuvwxyz 0123456789 &amp; ¿? ¡! —</p>
    </div>'''
body = hero("sanguaza/libro-centrado", "A Pinch of Blood and a Glass of Sanguaza — the book", "Editorial", "Una pizca de sangre y un vaso de sanguaza", "50% 45%")
body += ficha([("Title", "A Pinch of Blood and a Glass of Sanguaza"), ("Context", "Master's Degree in Editorial Design, ELISAVA"), ("Year", "September 2025 – June 2026"), ("Editorial direction, art direction &amp; design", "Antonia Ilic Bromberg &amp; Francesca Garre Buscaglia")])
body += "  <main>\n"
body += chapter(head("01  Intro", "Across history, the one thing we have consistently maintained is the need to create rituals that bring us together as a society."),
    pair(("Why we still need it", ["By exploring the symbols, elements, and rhythms that make ritual possible, we begin to understand why we continue to need it. Even today, amid productive routines and weakened social bonds, we keep searching for moments that allow us to belong, transform, and make the passage of time visible."]),
         ("Editorial concept", ["Whether it is a grandmother's birthday celebration or a \"coming of age\" ceremony among the Swazi people, we have never stopped creating rites. Yet we have lost the ability to pause and become aware of their meaning, depriving ourselves of the opportunity to mark history.", "Different schools of thought have pointed out that rituals serve an essential function in human life. They not only create spaces for encounter and belonging, but also give shape to time, organize experience, and allow meanings to be shared with others. When a ritual loses its significance or disappears, the symbolic structures that sustain communal life are weakened as well."])))
body += chapter(head("02  The book"),
    pair(("The architecture of ritual", ["The graphic concept reflects the \"architecture of ritual\" through the rhythm of the book. Drawing on Arnold van Gennep's structure of rites of passage, the reading flow alternates between continuity and interruption, translating the process of separation, transformation, and reintegration into the editorial experience."]),
         ("Four reading levels", ["The book is structured through four reading levels. The editorial voice guides the reader through chapter introductions, while the essays provide the theoretical framework. Poems and silver-printed images offer an experiential reading of ritual, interrupting the academic discourse with a more intimate, symbolic, and emotional perspective. Like ritual experiences, whose memories often remain fragmented and elusive, the images move away from literal representation to evoke what cannot be fully explained."])),
    media(['      <video src="../img/sanguaza/libro-post-full.mp4" poster="../img/sanguaza/libro-post-full.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Pages of the book being turned" style="--c: 5 / 9; --m: 1 / -1; --r: 720 / 654"></video>']))
body += chapter(head("03  the ink", text=["The images of rituals are printed in silver ink. Some rituals are so intense that they are hard to remember clearly: like ritual experiences, whose memories often remain fragmented and elusive, the silver images move away from literal representation to open a less structured, almost dreamlike space, evoking what cannot be fully explained. The poems do the same at certain moments of the book."]),
    media(['      <video src="../img/sanguaza/tinta.mp4" poster="../img/sanguaza/tinta.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Silver ink catching the light" style="--c: 5 / 9; --m: 1 / -1; --r: 1080 / 1350"></video>']))
# Doble página a todo el ancho para quebrar el ritmo
body += chapter(media([img("sanguaza/doble-banner", "1 / -1", "1 / -1", "2400 / 1000", "Double-page spread on blue paper")], "bleed"))
body += f'''  <section class="paper">
{head("04  the paper", extra='      <p style="--c: 1 / 7">Curious Matter Adiron Blue, 270 g/m² (Arjowiggins).</p>')}
  </section>
'''
body += chapter(head("05  Typeface"), spec_sg, top=True)
body += chapter(head("06  Credits"), credits(None, None, [("Editorial direction, art direction &amp; design", "Antonia Ilic Bromberg, Francesca Garre Buscaglia"), ("Research &amp; archives", "Antonia Ilic Bromberg, Francesca Garre Buscaglia"), ("Typeface", "Source Serif 4, by Frank Grießhammer"), ("Paper", "Munken Print Cream 80 g/m², Curious Matter Adiron Blue 270 g/m²"), ("Printing", "Tecnoart, Barcelona, 2026"), ("Acknowledgements", "Pol Nadal (Studiopol), Josep Román (Affaire), Laura Meseguer, Ane Guerra, María Dolores Soriano, Marc Panero")], wide=True))
body += "  </main>\n"
body += nxt("potra", "potra/home-crop", "Web design", "POTRA", "50% 50%")
write("sanguaza", page("Una pizca de sangre y un vaso de sanguaza", "A Pinch of Blood and a Glass of Sanguaza — editorial book on ritual. Master in Editorial Design, ELISAVA.", "sanguaza", body, "#ffffff", css=css))

# ================================== POTRA ===================================
css = """    .pillars5 > div { display: flex; flex-direction: column; gap: 12px; }
    .pillars5 p { text-align: center; }
    .pillars5 img { width: 100%; aspect-ratio: 250 / 300; object-fit: contain; }
    .po-spec { background: #cccaff; color: #331a2a; font-family: "Mona Sans", sans-serif; }
    .ppal { column-gap: 0; }
    .ppal > div { aspect-ratio: 288 / 480; position: relative; }
    .ppal p { position: absolute; left: 9.15%; bottom: 20px; }
    .phones img { object-fit: contain; }
    @media (max-width: 768px) { .ppal > div { aspect-ratio: 1 / 2; } }"""
pil = [("Finanzas", "finanzas"), ("Comunicación", "comunicacion"), ("Derechos", "derechos"), ("Creatividad", "creatividad"), ("Biomindset", "biomindset")]
pillars = "\n".join(f'      <div style="--c: {2 + i * 2} / {4 + i * 2}; --m: span 2"><p class="label-low">{n}</p><img src="../{im("potra/obj-" + f)}" alt="" loading="lazy"></div>' for i, (n, f) in enumerate(pil))
spec_po = '''    <div class="spec g po-spec">
      <div class="rule"></div>
      <p class="caps c1 row1">Type specimen</p><p class="caps c2 row1">Mona Sans — titles</p><p class="caps c3 row1">Mona Sans — text</p>
      <p class="big row2" style="font-size:calc(var(--fs-display) * 1.714); line-height:.92; letter-spacing:-.03em; font-weight:700">Hack the Productive Sphere</p>
      <div class="c3 row2" style="display:flex; flex-direction:column; gap:12px"><p style="font-size:17px; line-height:1.55">Potra exists for anyone who feels they don't quite belong in that narrative.</p><p class="caps s">Mona Sans Regular · 17 / 26</p></div>
      <p class="caps s c1 row3">Mona Sans Bold · titles</p>
      <div class="rule gap"></div>
      <p class="row3" style="--c: 1 / 9; font-size:26px; line-height:1.25; font-weight:700">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz 0123456789</p>
      <p class="c3 row3" style="font-size:12px; line-height:1.5">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñopqrstuvwxyz 0123456789 &amp; ¿? ¡! —</p>
    </div>'''
pal = [("#8ab0cf", "#000"), ("#680139", "#fff"), ("#341c2f", "#fff"), ("#daef20", "#000"), ("#cccaff", "#000")]
palette = '    <div class="ppal g bleed" style="grid-template-columns: repeat(5, 1fr)">\n' + "\n".join(f'      <div style="--c: auto; --m: auto; background:{b}"><p style="color:{t}">{b.upper()}</p></div>' for b, t in pal) + "\n    </div>"
body = hero("potra/home-crop", "POTRA website", "Web design", "POTRA", "50% 50%")
body += ficha([("Project", "POTRA — Tools, Insights &amp; Masterclasses to Hack the Productive Sphere"), ("Context", "Master's Degree in Editorial Design, ELISAVA"), ("Editorial direction, art direction &amp; design", "Antonia Ilic Bromberg &amp; Andie Puentes Fernández"), ("Typeface", "Mona Sans")])
body += "  <main>\n"
body += chapter(head("01  Intro", "We've been sold an idea of productivity built on systems that weren't designed with us in mind."),
    '    <div class="head g"><div class="t"><p>About</p><p>The alarm goes off. 6 a.m. This is the week you\'ll finally become "that" person: wake up early, work out, meal prep, journal, optimize. At least, that\'s what the TikToks you saved last night promised. Reality? It\'s 8 a.m., you\'re rushing out the door, and breakfast is whatever you can grab on the way.</p><p>We keep trying to fit into models that leave little room for real life: for emotions, uncertainty, care, or simply being human.</p></div></div>')
body += chapter(head("02  The platform", text=["POTRA", "Potra exists for anyone who feels they don't quite belong in that narrative. Instead of asking you to adapt to the system, we offer tools, classes, resources, and community-driven knowledge that help you navigate professional life on your own terms."]),
    media(['      <video src="../img/potra/home.mp4" poster="../img/potra/home-poster.jpg" muted loop playsinline autoplay preload="metadata" aria-label="POTRA home" style="--c: 1 / -1; --r: 2580 / 1450"></video>'], "bleed"),
    media([img("potra/screen-1", "1 / 7", "1 / -1", "711 / 430", "POTRA web screen"), img("potra/screen-2", "7 / 13", "1 / -1", "711 / 430", "POTRA web screen")], "bleed"),
    media([img("potra/screen-3", "1 / 7", "1 / -1", "711 / 430", "POTRA web screen"), img("potra/screen-4", "7 / 13", "1 / -1", "711 / 430", "POTRA web screen")], "bleed"))
body += chapter(head("03  The metaphor", text=["The project begins with the metaphor of the bag we carry when we know a long day lies ahead. We leave home carrying objects that symbolize the weight of everyday life, and by grouping these items, we identified five core pillars of education:"]),
    media([img("potra/la-bolsa", "1 / -1", None, "1312 / 560", "The bag and its objects", extra_style=" object-fit: contain; background: transparent;")]))
body += chapter(head("04  Content pillars", text=["Finances, communication, rights, creativity and biomindset: these are the topics that affect us in our professional development, and each one became a content pillar for the platform."]),
    f'    <div class="pillars5 g">\n{pillars}\n    </div>')
body += chapter(head("05  Typeface and color", text=["The typeface used is Mona Sans, set in its Regular weight and Expanded style for headings and highlighted content. The selected color palette is drawn from the visual universe of the objects featured throughout the project."]), spec_po, palette)
body += chapter(head("06  Social media", text=["A distinctive social media voice was developed to make complex topics feel approachable, using irony and a sharp editorial tone to inform while building a genuine connection with the audience."]),
    media([img("potra/redes", "4 / 10", "1 / -1", "648 / 464", "POTRA Instagram post", extra_style=" object-fit: contain; background: transparent;")]),
    media([img("potra/phone-1", "4 / 6", "1 / 3", "232 / 475", "POTRA Instagram profile"), img("potra/phone-2", "8 / 10", "3 / 5", "232 / 475", "POTRA Instagram story")], "phones", "--ph: transparent"))
body += chapter(head("07  mobile"), media(['      <video src="../img/potra/mobile.mp4" poster="../img/potra/mobile.jpg" muted loop playsinline autoplay preload="metadata" aria-label="POTRA mobile" style="--c: 3 / 11; --r: 901 / 539; object-fit: contain; background: transparent; width:100%; height:auto"></video>']))
body += chapter(head("08  Credits"), credits(None, None, [("Editorial direction, art direction &amp; design", "Antonia Ilic Bromberg, Andie Puentes Fernández"), ("Research &amp; archives", "Antonia Ilic Bromberg, Andie Puentes Fernández"), ("Acknowledgements", "Camilo Roa (Réplica), Javier Pereda (Esiete), Albert Folch, Josep Román (Affaire), Laura Meseguer, Ane Guerra, Marc Panero")], wide=True))
body += "  </main>\n"
body += nxt("franca-projects", "franca/massimo-sanvalentin-1", "Art direction", "Franca Projects", "0% 48%")
write("potra", page("POTRA", "POTRA — Tools, Insights &amp; Masterclasses to Hack the Productive Sphere. Web design.", "potra", body, "#ffffff", css=css))

# ============================ ABOUT / CONTACT ===============================
def simple(fname, title, desc, body, css, current):
    n = nav("", dark=True, current=current)
    html_ = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Antonia Ilic Bromberg</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/case.css">
  <style>
{css}
  </style>
</head>
<body>
{n}
{body}
  <script src="js/main.js"></script>
</body>
</html>
'''
    open(f"{ROOT}/{fname}", "w").write(html_)
def item(a, b, c=None):
    x = f"<p>{c}</p>" if c else ""
    return f'        <div class="item"><p>{a}</p><p>{b}</p>{x}</div>'
about_css = """    .about-page { padding-block: 160px var(--s-section); row-gap: var(--s-head); }
    .about-page .display { --c: 1 / 6; }
    .about-page .portrait { --c: 10 / 13; --m: 1 / 3; grid-row: 1 / 3; width: 100%; aspect-ratio: 325 / 444; object-fit: cover; }
    .about-page .t { --c: 1 / 6; }
    .cv { --c: 1 / -1; display: grid; grid-template-columns: subgrid; margin-top: calc(160px - var(--s-head)); row-gap: 28px; }
    .cv section { display: flex; flex-direction: column; gap: 24px; }
    .cv .edu { grid-column: 1 / 5; } .cv .exp { grid-column: 6 / 11; }
    .cv .item { display: flex; flex-direction: column; gap: 4px; }
    @media (max-width: 768px) {
      .about-page { padding-top: 96px; }
      .about-page .display, .about-page .t { --m: 1 / -1; }
      .about-page .portrait { grid-row: auto; }
      .cv .edu, .cv .exp { grid-column: 1 / -1; }
    }"""
about = f'''  <main class="about-page g">
    <h1 class="display">Designer with a holistic and editorial approach.</h1>
    <img class="portrait" src="{im("about/portrait")}" alt="Antonia Ilic Bromberg">
    <div class="t"><p>I work on identity, editorial, branding, and art direction projects from a strategic and conceptual perspective, placing emphasis on the construction of coherent visual narratives and systems that hold up over time.</p><p>My goal is to articulate content, form, and narrative to give structure and meaning to brands and projects.</p></div>
    <div class="cv">
      <section class="edu">
        <h2 class="label">Education</h2>
{item("Elisava", "Master's Degree in Editorial Design · September 2025 – July 2026")}
{item("University of the Arts London", "Art Direction Course · 2022")}
{item("Pontificia Universidad Católica de Chile", "Degree in Integral Design · July 2015 – November 2020", "Holistic, critical, and interdisciplinary design approach, with a focus on sustainability and social responsibility.")}
      </section>
      <section class="exp">
        <h2 class="label">Experience</h2>
{item("Wild Lama — Brand designer", "Sustainable lifestyle brand, Chile · March 2024 – August 2025", "Marketing strategy and brand positioning development. Art direction and fashion campaign production. Graphic design of digital and physical pieces.")}
{item("Falabella Art Direction Team — Intern", "Major Latin American retail and department store chain · February 2023 – March 2024", "Design of graphic pieces for digital and physical media. Development of key visuals for campaigns. Fashion production assistance for shootings.")}
{item("Falabella — Web designer", "Major Latin American retail and department store chain · April 2021 – March 2024", "Mailing design, media strategy, landing pages, key visuals, and campaign lead for select graphic campaigns.")}
{item("Fundación Paiz de Guatemala, Bienal 22° — Graphic designer", "Cultural foundation, contemporary art biennial · October 2019 – May 2021", "Design of graphic pieces for digital media. Editorial design of the biennial catalogue. Editorial design of the biennial atlas. Web design.")}
{item("Enrique Concha &amp; Co. — Intern", "Interior design and architecture firm, Chile · January 2019", "Design of the architecture and interior design projects portfolio.")}
      </section>
    </div>
  </main>'''
simple("about.html", "About", "Antonia Ilic Bromberg — designer with a holistic and editorial approach. Education and experience.", about, about_css, "about")
contact_css = """    .contact-page { padding-block: 219px 160px; row-gap: 56px; }
    .contact-page .display { --c: 1 / 10; }
    .contact-page > p { --c: 1 / 8; }
    .contact-page .data { --c: 1 / -1; display: grid; grid-template-columns: subgrid; }
    .contact-page .data > div { display: flex; flex-direction: column; gap: var(--s-text); }
    .contact-page .data > div:nth-child(1) { grid-column: 1 / 4; } .contact-page .data > div:nth-child(2) { grid-column: 4 / 7; } .contact-page .data > div:nth-child(3) { grid-column: 7 / 10; }
    .contact-page .data a:hover { text-decoration: underline; text-underline-offset: 3px; }
    @media (max-width: 768px) { .contact-page { padding-top: 120px; row-gap: 32px; } .contact-page .data > div { grid-column: 1 / -1 !important; margin-bottom: 16px; } }"""
contact = '''  <main class="contact-page g">
    <h1 class="display">If you have a project, a collaboration, or an idea in development, contact me!</h1>
    <p>I work on identity, editorial, branding, web, and art direction projects, participating in both the conceptual definition and the visual construction.</p>
    <div class="data">
      <div><p>Email</p><a href="mailto:antonia.ilic@gmail.com">antonia.ilic@gmail.com</a></div>
      <div><p>Instagram</p><a href="https://www.instagram.com/bai__antonia" target="_blank" rel="noopener">@bai__antonia</a></div>
      <div><p>Location</p><p>Barcelona, Spain</p></div>
    </div>
  </main>'''
simple("contact.html", "Contact", "Contact Antonia Ilic Bromberg — identity, editorial, branding, web and art direction projects.", contact, contact_css, "contact")
print("ok")
