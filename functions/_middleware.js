// Visitas propias: abrir cualquier página con ?yo deja una cookie en ese navegador.
// Con esa cookie, se quita el contador de Cloudflare Web Analytics del HTML y la visita no se cuenta.
const COOKIE = "yo=1";
const UN_ANO = 60 * 60 * 24 * 365;

export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.searchParams.has("yo")) {
    url.searchParams.delete("yo");
    return new Response(null, {
      status: 302,
      headers: {
        Location: url.pathname + url.search,
        "Set-Cookie": `${COOKIE}; Max-Age=${UN_ANO}; Path=/; Secure; SameSite=Lax`,
        "Cache-Control": "no-store",
      },
    });
  }

  const res = await context.next();
  const cookies = context.request.headers.get("Cookie") || "";
  const esMio = cookies.split(/;\s*/).includes(COOKIE);
  const esHtml = (res.headers.get("Content-Type") || "").includes("text/html");
  if (!esMio || !esHtml) return res;

  return new HTMLRewriter()
    .on('script[src*="cloudflareinsights"]', { element(el) { el.remove(); } })
    .transform(res);
}
