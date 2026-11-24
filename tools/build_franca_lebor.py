import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_site import *

# ============================== FRANCA =====================================
css = """    .sprite { position: relative; overflow: hidden; aspect-ratio: 442 / 554; }
    .sprite img { position: absolute; top: 0; height: 100%; width: 209.15%; max-width: none; }
    .sprite.a img { left: .09%; } .sprite.b img { left: -109.05%; }
    .ab figure { display: flex; flex-direction: column; gap: var(--s-text); }
    .ab figure:nth-child(1) { --c: 3 / 7; --m: 1 / 3; }
    .ab figure:nth-child(2) { --c: 7 / 11; --m: 3 / 5; }
    .compo { --c: 2 / 11; position: relative; aspect-ratio: 976 / 574; }
    .compo > * { position: absolute; }
    .compo .sprite { aspect-ratio: auto; }
    .compo img.fill { width: 100%; height: 100%; object-fit: cover; }
    .compo .line { height: 1.85px; }
    .compo .line img { display: block; width: 100%; height: 1.85px; }
    .compo .v { transform-origin: 0 0; transform: rotate(90deg); }
    .pillars > div { --m: 1 / -1; display: flex; flex-direction: column; gap: var(--s-text); }
    .pillars > div > p { order: 1; } .pillars > div > p + p { order: 2; }
    @media (min-width: 769px) { .pillars > div > p, .pillars > div > p + p { order: 4; } }
    .pillars > div:nth-child(1) { --c: 1 / 5; } .pillars > div:nth-child(2) { --c: 5 / 9; } .pillars > div:nth-child(3) { --c: 9 / 13; }
    .post { position: relative; overflow: hidden; background: #fff; aspect-ratio: 416 / 520; }
    .post img { position: absolute; object-fit: cover; }
    .post .work  { left: 23.8%; top: 18.65%; width: 76.22%; height: 81.31%; }
    .post .inspo { left: 50%; top: calc(50% + 4.5px); width: 152.64%; height: 81.04%; max-width: none; transform: translate(-50%, -50%) rotate(-90deg); }
    .post .mark, .cp .mark { left: 41.2%; top: 40.96%; width: 17.59%; height: 18.07%; }
    .strip { display: flex; gap: 2px; }
    .strip > * { flex: 1 1 0; min-width: 0; aspect-ratio: 261 / 326; position: relative; overflow: hidden; background: #fff; }
    .strip img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
    .strip img.mid { inset: auto; left: 0; top: 17.88%; height: 64.05%; }
    .strip.four > * { flex: 0 0 calc((100% - 8px) / 5); }
    .carousels { display: flex; flex-direction: column; gap: var(--s-block); }
    @media (max-width: 768px) {
      .strip { overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
      .strip::-webkit-scrollbar { display: none; }
      .strip > *, .strip.four > * { flex: 0 0 88%; scroll-snap-align: start; }
      /* 03 discarded: cuatro en fila */
      .discard > img { --m: span 1 !important; }
      /* 04 the grid: A y B a todo el ancho */
      .ab figure:nth-child(1), .ab figure:nth-child(2) { --m: 1 / -1; }
      .ab { row-gap: var(--s-block); }
      /* 06 content pillars: texto sobre la imagen, en carrusel */
      .pillars { display: flex; gap: 2px; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; padding-inline: var(--margin); scroll-padding-inline: var(--margin); }
      .pillars::-webkit-scrollbar { display: none; }
      .pillars > div { flex: 0 0 88%; scroll-snap-align: start; }
      .pillars .post { order: 3; }
      .pillars-dots { padding-inline: var(--margin); }
    }
    .compo .line { z-index: 2; }"""
discard = [img(f"franca/discard-{i}", c, m, "304 / 380", "Discarded craft exploration")
           for i, c, m in [(1, "1 / 4", "1 / 3"), (2, "4 / 7", "3 / 5"), (3, "7 / 10", "1 / 3"), (4, "10 / 13", "3 / 5")]]
L = "../img/franca/"
compo = f'''    <div class="g">
      <div class="compo" aria-label="Posts composed on grid A and grid B">
        <div class="sprite b" style="left:53.06%; top:0; width:46.94%; height:100%"><img src="{L}grid-ab.jpg" alt=""></div>
        <img class="fill" src="{L}leandra-19.jpg" alt="" style="left:67.84%; top:3.97%; width:30.09%; height:76.35%">
        <div class="sprite a" style="left:0; top:0; width:46.94%; height:100%"><img src="{L}grid-ab.jpg" alt=""></div>
        <div class="sprite b" style="left:53.06%; top:0; width:46.94%; height:100%"><img src="{L}grid-ab.jpg" alt=""></div>
        <img class="fill" src="{L}zara-girl.jpg" alt="" style="left:61.45%; top:4.15%; width:36.28%; height:46.07%">
        <div class="line v" style="left:97.67%; top:.18%; width:58.6%"><img src="{L}line-1.svg" alt=""></div>
        <div class="line v" style="left:61.45%; top:.36%; width:58.6%"><img src="{L}line-1.svg" alt=""></div>
        <div class="line" style="left:53.49%; top:3.79%; width:46.4%"><img src="{L}line-3.svg" alt=""></div>
        <div class="line v" style="left:1.27%; top:.18%; width:58.07%"><img src="{L}line-4.svg" alt=""></div>
        <div class="line" style="left:.21%; top:2.17%; width:46.72%"><img src="{L}line-2.svg" alt=""></div>
        <img class="fill" src="{L}img-3204.jpg" alt="" style="left:1.49%; top:2.17%; width:35.13%; height:79.63%">
        <div class="line" style="left:.21%; top:81.95%; width:46.72%"><img src="{L}line-2.svg" alt=""></div>
      </div>
    </div>'''
def strip(files, caption, extra=""):
    cells = "".join(f'<div><img src="../{im("franca/" + f)}" alt="" loading="lazy"></div>' for f in files)
    return f'      <div class="t"><div class="strip" data-carousel>{cells}</div><p class="cap">{caption}</p></div>'
finat = (f'      <div class="t"><div class="strip four" data-carousel>'
         f'<div><img class="mark" src="../{im("franca/fran-finat-mark")}" alt="" style="position:absolute; inset:auto; left:41.2%; top:40.96%; width:17.59%; height:18.07%"></div>'
         f'<div><img src="../{im("franca/fran-finat-77")}" alt=""><img src="../{im("franca/fran-finat-80")}" alt=""></div>'
         f'<div><img class="mid" src="../{im("franca/fran-finat-76")}" alt=""></div>'
         f'<div><img src="../{im("franca/fran-finat-78")}" alt=""></div>'
         f'</div><p class="cap">Collaborator profile — Fran Finat, fashion photographer</p></div>')
feed = ["feed-1", "feed-2", "feed-3", "feed-4", "massimo-sanvalentin-1", "feed-6", "massimo-linen-1", "feed-8", "feed-9"]
feed_imgs = [img(f"franca/{f}", f"{1 + (i % 3) * 4} / {5 + (i % 3) * 4}", None, "434 / 543", "Franca Projects feed") for i, f in enumerate(feed)]
feed_imgs = [x.replace('style="--c:', 'style="--m: span 4; --c:') for x in feed_imgs]

body = hero("franca/massimo-sanvalentin-1", "Franca Projects — Massimo Dutti San Valentín", "Art direction", "Franca Projects", "0% 43%")
body += ficha([("Client", "Franca Projects"), ("Studio", "Wizards Only"), ("Role", "Art Direction, Instagram System, Grid Design"), ("Year", "2026"), ("Channel", "Instagram")])
body += "  <main>\n"
body += chapter(head("01  Intro", "An ever-evolving archive"),
    pair(("Context", ["Franca Projects is a fashion production company, founded in January 2026. Their Instagram showcases the productions they work on for their clients. In October 2026 they began a monthly Social Creative Direction retainer with Wizards Only."]),
         ("Challenge &amp; role", ["Franca wanted an aesthetic that leaned towards craft. Through a workshop with the team, we defined what craft meant for them: it had to feel human, but with extreme care so the system never interfered with their clients' images. I led the full structure of the account, from defining its visual language to the system behind every post."])))
# 02 Defining craft fuera: no exponer el proceso del estudio (la intro del challenge ya lo explica)
body += chapter(head("02  Discarded explorations", text=["Early tests explored more literal expressions of craft. They always ended up dirtying work that needed to be shown clean. Discarding them clarified the line: the craft had to live in the structure, not on top of the images."]),
    media(discard, "discard"))
body += chapter(head("03  The grid", text=["We didn't want paper to be the answer. My proposal was to work in the space between digital and print: laying out the feed on the page grid of an editorial magazine, built to show their work. Franca often brings magazines to their productions for their clients, so the solution grew out of their own way of working."]),
    pair(("", ["I presented a grid for laying out images and building compositions. Each post is composed on it; then the grid is removed and the post stays clean, with white bands framing the images like the margins of a printed page."]),
         ("", ["Franca liked the idea of a system that would make them recognisable, but worried it could become boring, with the formula too obvious. So I presented two grids instead of one. Posts alternate between them: no single post reads as a template, but across the feed the structure comes through."])).replace("<p></p>", ""),
    f'''    <div class="ab g">
      <figure><figcaption>A.</figcaption><div class="sprite a"><img src="{L}grid-ab.jpg" alt="Grid A"></div></figure>
      <figure><figcaption>B.</figcaption><div class="sprite b"><img src="{L}grid-ab.jpg" alt="Grid B"></div></figure>
    </div>''')
body += chapter(head("04  Composition", text=["Within the grid, I composed each post by deciding its structure, which images work together, where the contrasts sit and in what order they unfold. The system sets the rules; the composition is where art direction comes in."]), compo)
body += chapter(head("05  Content pillars"), f'''    <div class="pillars g" data-carousel data-dots-class="pillars-dots">
      <div><div class="post"><img class="work" src="../{im("franca/sandra-handmade")}" alt="Massimo Dutti Handmade FW25 x Sandra" loading="lazy"></div><p>01  Work — 65%</p><p>Franca's projects do the talking. The feed shows two types: new productions and work from their catalogue. Every post is credited with what it is, the client, the title and the main contributors, and composed on grids A and B.</p></div>
      <div><div class="post"><img class="inspo" src="../{im("franca/inspo-79")}" alt="Inspiration post" loading="lazy"></div><p>02  Inspo — 25%</p><p>Behind the work, there's a lot of work. This pillar opens up Franca's inspo folders: essays, paintings, locations, objects, film stills. No commentary, just credits, and always a reference for past or future projects. I set these posts full-bleed, outside the grids, to set them apart.</p></div>
      <div><div class="post"><img class="mark" src="../{im("franca/fran-finat-mark")}" alt="Collaborator profile cover" loading="lazy"></div><p>03  Collaborators — 10%</p><p>A large part of Franca's job is connecting the right people at the right time for the right project. Showing their network of collaborators is the best way to show what they do best.</p></div>
    </div>''')
body += chapter(head("06  Carousels"), '    <div class="g carousels">\n' + "\n".join([
    strip([f"massimo-sanvalentin-{i}" for i in range(1, 6)], "Art Buying for Massimo Dutti — San Valentín special"),
    strip([f"massimo-linen-{i}" for i in range(1, 6)], "Art Buying for Massimo Dutti — Menswear Linen Collection"),
    finat]) + "\n    </div>")
body += chapter(head("07  The Feed"), media(feed_imgs, "tight feed3"))
body += chapter(head("08  Result &amp; Credits"), credits(None, "An ongoing monthly retainer since October 2026.",
    [("Client", "Franca Projects"), ("Studio", "Wizards Only, Barcelona"), ("Art direction, Instagram system, grid design", "Antonia Ilic Bromberg"), ("Narrative", "Jordi Martinez")]))
body += "  </main>\n"
body += nxt("lebor-gabala", "lebor/cover-noviembre", "Art direction", "Lebor Gabala", "0% 30%")
write("franca-projects", page("Franca Projects", "Art direction, Instagram system and grid design for Franca Projects.", "franca-projects", body, "#f6f6f6", "#ececea", css=css))

# ============================== LEBOR ======================================
css = """    .story-row { row-gap: var(--gutter); }
    .story-row > .label-low { --c: 1 / 3; --m: 1 / -1; }
    .story-row > img { aspect-ratio: 236 / 420; object-fit: cover; width: 100%; background: var(--ph); }
    .story-row > img:nth-of-type(1) { --c: 3 / 5; --m: 1 / 3; }
    .story-row > img:nth-of-type(2) { --c: 5 / 7; --m: 3 / 5; }
    .story-row > img:nth-of-type(3) { --c: 7 / 9; --m: 1 / 3; }
    .stories { display: flex; flex-direction: column; gap: var(--s-block); }
    .lg-feed { column-gap: 6px; row-gap: 6px; background: #fff; }"""
feed = ["feed-craft-01", "feed-17", "feed-16", "feed-craft-04", "feed-14", "feed-03", "feed-12", None, "feed-10", "feed-09", "feed-08", "feed-05", "feed-06", "feed-04", "feed-4b", "feed-07", "feed-02", "feed-11"]
cells = []
for i, f in enumerate(feed):
    c = f"{1 + (i % 3) * 4} / {5 + (i % 3) * 4}"
    if f is None:
        cells.append(f'      <div style="--c: {c}; --m: span 4; background:#000; aspect-ratio: 475.61 / 634.39"></div>')
    else:
        cells.append(img(f"lebor/{f}", c, "span 4", "475.61 / 634.39", "Lebor Gabala AW26 — Instagram post"))
def srow(label, files):
    imgs = "".join(f'<img src="../{im("lebor/" + f)}" alt="Lebor Gabala story" loading="lazy">' for f in files)
    return f'      <div class="story-row g" style="padding:0"><p class="label-low">{label}</p>{imgs}</div>'
reels = [f'      <video src="../img/lebor/reel-{i}.mp4" poster="../img/lebor/reel-{i}.jpg" muted loop playsinline autoplay preload="metadata" aria-label="Instagram ad — AW26" style="--c: {1 + (i - 1) * 3} / {4 + (i - 1) * 3}; --m: span 2; --r: 316 / 563"></video>' for i in range(1, 5)]

body = hero("lebor/cover-noviembre", "Lebor Gabala AW26", "Art direction", "Lebor Gabala — AW26", "0% 4.6%")
body += ficha([("Client", "Lebor Gabala"), ("Studio", "Wizards Only"), ("Role", "Art Direction, Content Plan, Social Graphics, Shoot Assistance"), ("Year", "2026"), ("Channel", "Instagram")])
body += "  <main>\n"
body += chapter(head("01  Intro", "Translate a slow, craft-driven brand into Instagram's rhythm without losing its quietness."),
    pair(("Context", ["Lebor Gabala is a Barcelona knitwear label founded in 1989 by Maite Muñoz. Its name comes from Lebor Gabála Érenn, a book of Irish mythology, chosen for the bond between Ireland and the wool tradition. The brand designs for durability: pieces meant to last and to mix with garments from earlier collections."]),
         ("Challenge &amp; role", ["Content had to feel as considered as the garments: elegant, tactile and unhurried. I built the AW26 Instagram content plan, designed the graphic system for stories and posts, and supported the campaign shoot on set."])))
body += chapter(head("02  The Feed", text=["Planned as a whole: images split across posts so the grid reads as one surface."]),
    media(cells, "bleed lg-feed feed3"))
body += chapter(media([img("lebor/feed-16", "1 / 7", "1 / 3", "720 / 810", ""), img("lebor/feed-10", "7 / 13", "3 / 5", "720 / 810", "")], "bleed"))
body += chapter(head("03  Stories"), '    <div class="g"><div class="stories">\n' + "\n".join([
    srow("Full-bleed editorial", ["story-01", "cover-noviembre", "story-03"]),
    srow("Colour treatment", ["story-colour-1", "story-colour-2", "story-colour-3"]),
    srow("Typographic statements", ["story-type-1", "story-type-2"]),
    srow("Lookbook", ["story-lookbook-1", "story-lookbook-2", "story-lookbook-3"]),
    srow("Invitation", ["story-invitation"])]) + "\n    </div></div>")
body += chapter(head("04  Video editing — Instagram ads (AW26)"), media(reels),
    '    <div class="head g"><div class="t"><p>Edited for Instagram ads: vertical 9:16 cuts from the AW26 shoot.</p></div></div>')
body += chapter(head("05  graphic Detail"), media([img("lebor/detail", "1 / -1", None, "1440 / 900", "Graphic detail", "50% 4.6%")], "bleed"))
body += chapter(head("06  On set"), media([img("lebor/onset-7537", "3 / 6", "1 / 3", "346 / 615", "On set"), img("lebor/onset-7628", "8 / 11", "3 / 5", "346 / 615", "On set")]))
body += chapter(head("07  Result &amp; Credits"), credits(None, "A modular system for vertical formats that alternates full-bleed editorial imagery, colour-treated statements and lookbook line-ups. AW26 content rolling out on Lebor Gabala's Instagram from November 2026.",
    [("Client", "Lebor Gabala"), ("Studio", "Wizards Only, Barcelona"), ("Content plan, social graphics, shoot assistance", "Antonia Ilic Bromberg"), ("Photography", "Nereis Ferrer"), ("Creative production", "Alba Mitchell")]))
body += "  </main>\n"
body += nxt("franciscandrea", "franciscandrea/cover", "Brand identity", "francisc'andrea", "50% 40%")
write("lebor-gabala", page("Lebor Gabala — AW26", "AW26 art direction, content plan and social graphics for Lebor Gabala.", "lebor-gabala", body, "#fdfbf9", css=css))
print("ok")
