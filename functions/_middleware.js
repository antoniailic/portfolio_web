// Analítica: Cloudflare Web Analytics (lo inserta Cloudflare) + Umami Cloud (se inserta aquí, da la ciudad).
// Visitas propias: abrir cualquier página con ?yo deja una cookie en ese navegador (el ?yo se queda en la barra, se puede guardar en favoritos).
// Con esa cookie no se inserta Umami y se quita el contador de Cloudflare, así que la visita no se cuenta.
const COOKIE = "yo=1";
const UN_ANO = 60 * 60 * 24 * 365;
const UMAMI = '<script defer src="https://cloud.umami.is/script.js" data-website-id="e8aa9cd1-c20a-47ac-a8da-2a097f2950ee" data-domains="antoniailicb.com,www.antoniailicb.com,antoniailicb.pages.dev"></script>';

export async function onRequest(context) {
  const url = new URL(context.request.url);

  const res = await context.next();
  const cookies = context.request.headers.get("Cookie") || "";
  const marcar = url.searchParams.has("yo");
  const esMio = marcar || cookies.split(/;\s*/).includes(COOKIE);
  const esHtml = (res.headers.get("Content-Type") || "").includes("text/html");
  if (!esHtml) return res;

  if (!esMio) {
    return new HTMLRewriter()
      .on("head", { element(el) { el.append(UMAMI, { html: true }); } })
      .transform(res);
  }

  const limpio = new HTMLRewriter()
    .on('script[src*="cloudflareinsights"]', { element(el) { el.remove(); } })
    .transform(res);
  if (!marcar) return limpio;

  // ?yo se queda en la barra (para poder guardarlo en favoritos) y deja la marca en este navegador.
  const conMarca = new Response(limpio.body, limpio);
  conMarca.headers.append("Set-Cookie", `${COOKIE}; Max-Age=${UN_ANO}; Path=/; Secure; SameSite=Lax`);
  conMarca.headers.set("Cache-Control", "no-store");
  return conMarca;
}
