"""Imágenes de vista previa (og:image, 1200×630) para LinkedIn, WhatsApp, correo, etc.
Recorta la imagen de portada de cada caso con el mismo encuadre (pos) que usa la web.
Uso: python3 tools/build_og.py
"""
from pathlib import Path
from PIL import Image

SITE = Path(__file__).resolve().parent.parent / "site"
OUT = SITE / "img" / "og"
W, H = 1200, 630

# slug: (imagen de portada, encuadre "x% y%" igual que --pos en la web)
OG = {
    "home":            ("img/franca/massimo-sanvalentin-1.jpg", "0% 43%"),
    "franca-projects": ("img/franca/massimo-sanvalentin-1.jpg", "0% 43%"),
    "lebor-gabala":    ("img/lebor/cover-noviembre.jpg",        "0% 4.6%"),
    "franciscandrea":  ("img/franciscandrea/cover.jpg",         "50% 40%"),
    "nebular":         ("img/nebular/nebular-composicion.jpg",  "50% 50%"),
    "wild-lama":       ("img/wildlama/wl-25-q1-525.jpg",        "50% 14.7%"),
    "sanguaza":        ("img/sanguaza/libro-centrado.jpg",      "50% 45%"),
    "potra":           ("img/potra/home-crop.jpg",              "50% 50%"),
}

def crop(src, pos):
    im = Image.open(SITE / src).convert("RGB")
    px, py = (float(v.strip("%")) / 100 for v in pos.split())
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - W) * px)
    y = round((im.height - H) * py)
    return im.crop((x, y, x + W, y + H))

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, (src, pos) in OG.items():
        crop(src, pos).save(OUT / f"{slug}.jpg", quality=85, optimize=True, progressive=True)
        print(slug, (OUT / f"{slug}.jpg").stat().st_size // 1024, "KB")
