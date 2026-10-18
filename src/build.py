"""Build Fiona's Bakery.

  site/     production static site: one full HTML document per page + css/js/img
  preview/  single-file preview (all pages hash-routed) for the Artifact link
"""
import json, re, shutil, pathlib, hashlib
from pages import PAGES, ICON, FAQ_ITEMS

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
CSS = (SRC / 'style.css').read_text(encoding='utf-8')
DIMS = json.loads((SRC / 'img-dims.json').read_text())
JS = (SRC / 'main.js').read_text(encoding='utf-8').replace('__DIMS__', json.dumps(DIMS))
# Short content hashes so browsers fetch fresh JS/CSS after every change (Pages caches files ~10 min)
VER_JS = hashlib.md5(JS.encode('utf-8')).hexdigest()[:8]
VER_CSS = hashlib.md5(CSS.encode('utf-8')).hexdigest()[:8]
BASE = 'https://fionasbakery.se/'
FONTS = '<link rel="preload" href="fonts/caprasimo.woff2" as="font" type="font/woff2" crossorigin>'

LOGO = '''<svg class="rose-mark" viewBox="0 0 64 64" aria-hidden="true">
  <circle class="bloom" cx="31" cy="29" r="16"/>
  <path class="stem" d="M31.6 44.2c-.4 5.6.2 11.2 1.6 16.4"/>
  <path class="leaf" d="M32.2 52.6c-4.8.4-8.6-2-10-5.8 4.4-1.4 8.6.6 10 5.8zM32.6 50c3.8-1.6 7.8-.6 9.8 2.6-3.6 2-7.8 1-9.8-2.6z"/>
  <path class="petal" d="M31.5 25.5c1.8-1.6 4.6-.6 4.7 1.8.1 2.6-3 4.2-5.6 3.2-3.2-1.2-3.6-5.6-1.2-8 3-3 8.4-2.6 10.8.8 2.8 4 1.2 9.8-3.2 12-4.8 2.4-11 .4-13.2-4.4-2.2-4.8 0-10.6 4.8-13"/>
  <path class="petal" d="M22.4 22.6c-4.2 4.6-4.6 12-.8 16.8 4.2 5.4 12.4 6.6 18 2.6 5.6-4 7-12 3.4-17.8"/>
  <path class="petal" d="M42.8 20.6c1.8-3.6 1-7.4-1.4-9.6-2.6 2.2-3.8 5.4-3.2 8.6M19.6 26.2c-3.8-.4-6.8-3-7.6-6.4 3.2-1 6.6-.2 8.8 2.2"/>
</svg>'''

BAKERY_LD = {
 "@context":"https://schema.org","@type":"Bakery","name":"Fiona's Bakery",
 "description":"Konditori i Arlöv som bakar tårtor på beställning: bröllopstårtor med handgjorda sockerblommor, barntårtor, födelsedagstårtor, studenttårtor, cupcakes och cakepops.",
 "url":BASE,"telephone":"+46738740378","email":"kontakt@fionasbakery.se",
 "image":BASE+"img/39.jpg",
 "founder":{"@type":"Person","name":"Fiona","jobTitle":"Konditor och sockerblomsdesigner"},
 "address":{"@type":"PostalAddress","streetAddress":"Trossgatan 25","postalCode":"232 36","addressLocality":"Arlöv","addressRegion":"Skåne län","addressCountry":"SE"},
 "priceRange":"60 kr/bit","paymentAccepted":"Swish","sameAs":["https://www.instagram.com/fionasbakery/"],
}
FAQ_LD = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,_ in FAQ_ITEMS]}

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def header(link):
    ORDER = ' class="tab-order"'
    TINT = {'tartor':'rose','smaker':'butter','om':'pistachio','fragor':'rose','bestall':'rose'}
    tabs = ''.join(f'<li class="c-{TINT[s]}"><a href="{link(s)}"{ORDER if s=="bestall" else ""}>{label}</a></li>'
                   for s, _, label, *_ in PAGES if s != 'hem')
    return f'''<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{link('hem')}" aria-label="Fiona's Bakery, startsida">{LOGO}<span><b>Fiona's Bakery</b><small>Konditori i Arlöv</small></span></a>
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="tabs">{ICON['menu']} Meny</button>
    <nav aria-label="Huvudmeny"><ul class="tabs" id="tabs">{tabs}</ul></nav>
  </div>
</header>'''

def footer(link):
    return f'''<footer class="wrap site-foot">
  <div class="slab">
    <div>
      <a class="brand" href="{link('hem')}">{LOGO}<span><b>Fiona's Bakery</b><small>Konditori i Arlöv</small></span></a>
      <p style="margin-top:14px;max-width:26em">Tårtor på beställning, bakade i Arlöv. Leverans går att ordna mot en extra kostnad beroende på avstånd.</p>
    </div>
    <div><h2>Kontakt &amp; hämtning</h2><p><a href="tel:+46738740378">073-874 03 78</a><br><a href="mailto:kontakt@fionasbakery.se">kontakt@fionasbakery.se</a><br>Trossgatan 25, 232 36 Arlöv<br>Hämtning enligt överenskommelse<br>Leverans mot extra kostnad beroende på avstånd<br><a href="https://www.instagram.com/fionasbakery/" rel="noopener" target="_blank">Instagram @fionasbakery</a></p></div>
    <div><h2>Sidor</h2><p>{'<br>'.join(f'<a href="{link(s)}">{label}</a>' for s,_,label,*_ in PAGES if s!='hem')}</p></div>
    <p class="fine"><span>© 2026 Fiona's Bakery</span><span>Godkänd för F-skatt, betalning med Företagsswish</span></p>
  </div>
</footer>'''

def _img(m):
    k = m.group(1); w, h = DIMS.get(k, (None, None))
    return f'src="img/{k}.webp"' + (f' width="{w}" height="{h}"' if w else '')

def resolve(html, link):
    html = re.sub(r'src="img/(\w+)\.jpg"', _img, html)
    return re.sub(r'href="@(\w+)"', lambda m: f'href="{link(m.group(1))}"', html)

# ---------- production site ----------
def build_site():
    out = ROOT / 'site'
    if out.exists(): shutil.rmtree(out)
    (out / 'css').mkdir(parents=True); (out / 'js').mkdir()
    shutil.copytree(ROOT / 'img', out / 'img', ignore=shutil.ignore_patterns('orig'))
    shutil.copytree(ROOT / 'fonts', out / 'fonts')
    (out / 'css/style.css').write_text(CSS.replace('FONTDIR', '../fonts'), encoding='utf-8')
    (out / 'js/main.js').write_text(JS, encoding='utf-8')
    files = {s: f for s, f, *_ in PAGES}
    link = lambda s: 'index.html' if s == 'hem' else f'{files[s]}.html'
    for slug, fname, label, title, desc, body in PAGES:
        canon = BASE if slug == 'hem' else f'{BASE}{fname}.html'
        extra = ld(BAKERY_LD) if slug == 'hem' else (ld(FAQ_LD) if slug == 'fragor' else '')
        head = header(link).replace(f'href="{link(slug)}"', f'href="{link(slug)}" aria-current="page"', 1) if slug != 'hem' else header(link)
        doc = f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="Fiona's Bakery">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}img/39.jpg">
<meta name="theme-color" content="#F6EEE1">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='30' r='26' fill='%23F8D8DC'/%3E%3Cpath d='M31.5 25.5c1.8-1.6 4.6-.6 4.7 1.8.1 2.6-3 4.2-5.6 3.2-3.2-1.2-3.6-5.6-1.2-8 3-3 8.4-2.6 10.8.8 2.8 4 1.2 9.8-3.2 12-4.8 2.4-11 .4-13.2-4.4-2.2-4.8 0-10.6 4.8-13M22.4 22.6c-4.2 4.6-4.6 12-.8 16.8 4.2 5.4 12.4 6.6 18 2.6 5.6-4 7-12 3.4-17.8' fill='none' stroke='%23B22A47' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E">
{FONTS}
<link rel="stylesheet" href="css/style.css?v={VER_CSS}">
{extra}
</head>
<body>
<a class="skip" href="#main">Hoppa till innehållet</a>
{head}
<main id="main" tabindex="-1">
{resolve(body, link)}
</main>
{footer(link)}
<script src="js/main.js?v={VER_JS}" defer></script>
</body>
</html>
'''
        (out / f'{fname}.html').write_text(doc, encoding='utf-8')
    nf = (out / 'index.html').read_text(encoding='utf-8')
    body404 = resolve('''<div class="wrap page-head"><div class="slab c-rose"><div><h1>Sidan finns inte</h1>
      <p class="lede measure" style="margin-top:16px">Länken kan vara gammal eller felstavad. Här hittar du tårtorna och beställningen.</p>
      <p style="margin-top:28px;display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-gel" href="@bestall">Beställ tårta</a><a class="btn btn-line" href="@tartor">Se tårtorna</a></p></div></div></div>''', link)
    s0 = nf.index('<main id="main" tabindex="-1">') + len('<main id="main" tabindex="-1">'); s1 = nf.index('</main>')
    nf = nf[:s0] + '\n' + body404 + '\n' + nf[s1:]
    nf = re.sub(r'<title>.*?</title>', "<title>Sidan finns inte | Fiona's Bakery</title>", nf)
    nf = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', nf, flags=re.S)
    nf = nf.replace('<link rel="canonical" href="https://fionasbakery.se/">', '<meta name="robots" content="noindex">')
    (out / '404.html').write_text(nf, encoding='utf-8')
    print('site/ written:', ', '.join(f'{f}.html' for _, f, *_ in PAGES))

# ---------- single-file preview ----------
def build_preview():
    out = ROOT / 'preview'; out.mkdir(exist_ok=True)
    link = lambda s: f'#{s}'
    arts = ''.join(f'<article data-page="{s}" aria-label="{label}"{"" if s=="hem" else " hidden"}>\n{resolve(body, link)}\n</article>\n'
                   for s, _, label, _, _, body in PAGES)
    hem = PAGES[0]
    doc = f'''<title>Fiona's Bakery</title>
<meta name="description" content="{hem[4]}">
{FONTS}
<style>
{CSS.replace('FONTDIR', 'fonts')}
</style>
{header(link)}
<main id="main">
{arts}
</main>
{footer(link)}
<script>
{JS}
</script>
'''
    (out / 'index.html').write_text(doc, encoding='utf-8')
    print('preview/index.html written', len(doc)//1024, 'KB')

if __name__ == '__main__':
    build_site(); build_preview()
