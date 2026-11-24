# antoniailicb.com

Web del portafolio. HTML/CSS/JS plano, sin build. Construida desde el Figma "Portfolio — claude".

## Un solo flujo

- **Se edita aquí:** repo `antoniailic/portfolio_web`, rama `main`.
  - `site/` — la web publicada.
  - `tools/` — scripts Python que generan las páginas (`python3 tools/build_franca_lebor.py`, `build_fa_neb.py`, `build_rest.py`). Los cambios de las landings se hacen en estos generadores y luego se regenera; no editar a mano los HTML de `site/projects/`.
- **Se publica en:** Cloudflare Pages, proyecto `antoniailicb` → https://antoniailicb.pages.dev (y antoniailicb.com cuando el dominio esté activo). Cada push a `main` se publica solo. Configuración en Cloudflare: sin comando de build, carpeta de salida `site`.
- Netlify ya no se usa.

## Reglas de diseño

- Retícula de 12 columnas (1440, margen 64, gutter 32); cuerpo a 5 columnas.
- Espaciados: título → contenido 40 · párrafo → párrafo 12 · bloque → bloque 160 · capítulo → capítulo 240 (ver tokens en `site/css/base.css`).
- Todo cambio en una landing se aplica a todas, salvo que se diga lo contrario.
- Nunca una palabra sola en la última línea.

Fuentes provisionales: Inter (en lugar de Unica77) y Xanh Mono (en lugar de Right Serif Mono) hasta tener las licencias.
