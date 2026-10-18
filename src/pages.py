# Page bodies. Links written as @slug are resolved by build.py
# (slug.html for the static site, #slug for the single-file preview).

import pathlib as _pl
_IC = _pl.Path(__file__).parent / 'icons'
def _ph(name):
    return (_IC / f'{name}.svg').read_text().replace('<svg ', '<svg class="icon" aria-hidden="true" focusable="false" ', 1)
# Phosphor Icons (regular), MIT licence
ICON = {k: _ph(v) for k, v in {'arrow':'arrow-right','clock':'clock','pin':'map-pin','slice':'cake','minus':'minus','plus':'plus',
        'x':'x','left':'caret-left','right':'caret-right','menu':'list'}.items()}
A = '<span class="ico">' + ICON['arrow'] + '</span>'

POTS_HOME = ''.join(
    f'<li><button type="button" class="pot c-{c}" data-occ="{k}" aria-pressed="{str(k=="brollop").lower()}"><i></i>{label}</button></li>'
    for k, c, label in [('brollop','rose','Bröllop'),('barn','butter','Barnkalas & dop'),('fest','butter','Födelsedag'),('student','pistachio','Student'),('bakelser','pistachio','Företag & event')])

HEM = f'''
<div class="wrap">
  <div class="opening">
    <div class="words slab">
      <h1>Tårtor på beställning i Malmö och Arlöv</h1>
      <p class="lede measure">Bröllopstårtor med handgjorda sockerblommor, barntårtor och bakelser. Bakade för hand av Fiona i Arlöv, nära Malmö.</p>
      <div class="acts">
        <a class="btn btn-gel" href="@bestall">Beställ tårta {A}</a>
        <a class="btn btn-line" href="@tartor">Se tårtorna</a>
      </div>
      <div class="picker">
        <h2>Vad firar ni? Välj och se vad Fiona har gjort.</h2>
        <ul class="pots">{POTS_HOME}</ul>
      </div>
    </div>
    <figure class="photo slab">
      <div class="frame">
        <img id="heroImg" data-k="39" src="img/39.jpg" alt="Bröllopstårtor: sockerblommor från Fiona's Bakery" fetchpriority="high">
      </div>
      <figcaption class="see"><span class="tag c-rose" id="heroTag">Sockerblommor</span><a class="go" id="heroSee" href="@tartor" data-filter="brollop"><span>Se fler bröllopstårtor</span>{A}</a></figcaption>
    </figure>
  </div>
</div>

<section class="wrap" aria-labelledby="range-h">
 <div class="slab c-pistachio range-slab">
  <div class="range-head">
    <h2 id="range-h">Från sockerrosor till Super Mario, bakat av samma händer</h2>
    <p class="lede">Fiona är både konditor och sockerblomsdesigner. Samma precision som i en pion av socker går in i en valp i sockerpasta eller en studentmössa.</p>
  </div>
  <div class="range">
    <figure><div class="slab c-rose"><img src="img/02.jpg" alt="Bröllopstårta med pioner och rosor i socker" loading="lazy"></div><figcaption>Pioner och rosor i socker<span>Bröllop</span></figcaption></figure>
    <figure><div class="slab c-rose"><img src="img/16.jpg" alt="Barntårta med Mario-figurer i sockerpasta" loading="lazy"></div><figcaption>Mario-äventyr<span>Barnkalas</span></figcaption></figure>
    <figure><div class="slab c-butter"><img src="img/40.jpg" alt="Födelsedagstårta formad som ett roulettebord" loading="lazy"></div><figcaption>Roulette<span>Födelsedag</span></figcaption></figure>
    <figure><div class="slab c-pistachio"><img src="img/07.jpg" alt="Cupcakes med monogram till företagsevent" loading="lazy"></div><figcaption>Cupcakes med monogram<span>Företag</span></figcaption></figure>
  </div>
 </div>
</section>

<section class="wrap" aria-labelledby="calc-h">
 <div class="slab c-butter calc">
  <div>
    <h2 id="calc-h">Vad kostar en tårta?</h2>
    <p class="lede measure" style="margin-top:18px">Alla tårtor kostar 60 kr per bit, med botten och två moussefyllningar. Dekorationen offereras efter hur detaljerad den är, och du får alltid priset innan något är bestämt.</p>
    <p style="margin-top:20px"><a class="go" href="@smaker">Se smaker och hela prislistan {A}</a></p>
  </div>
  <div class="slab c-sugar lift meter">
    <label for="guests">Hur många gäster? <span class="num" id="guestsN">30</span></label>
    <input type="range" id="guests" min="8" max="120" step="1" value="30">
    <div class="scale num"><span>8</span><span>120</span></div>
    <div class="big" id="guestsKr" data-v="1800" aria-live="polite">1 800 kr</div>
    <p class="per">för tårtan före dekoration, 60 kr per bit</p>
    <div><a class="btn btn-gel" id="guestsGo" href="@bestall"><span>Beställ för 30 personer</span> {A}</a></div>
  </div>
 </div>
</section>

<section class="wrap meet" aria-labelledby="meet-h">
  <div class="slab c-rose words">
    <h2 id="meet-h">Hej, jag heter Fiona</h2>
    <p class="measure">Jag är konditor, sugarpaste-dekoratör och designer av tårtor och sockerblommor. Jag bakar för barnfamiljen som vill överraska tvååringen och för brudparet som vill ha en romantisk dröm att sätta tårtspaden i.</p>
    <p class="measure">Vill du ha en enklare tårta går det lika bra. Är du osäker på vilka smaker som passar ihop hjälper jag dig.</p>
    <a class="go" href="@om">Så går en beställning till {A}</a>
  </div>
  <div class="photo slab c-rose"><img src="img/13.jpg" alt="Körsbärsgren och ros formade i socker av Fiona" loading="lazy"></div>
</section>

<section class="wrap close" aria-labelledby="close-h">
  <div class="slab c-pistachio">
    <h2 id="close-h">Berätta om er dag, så bakar Fiona tårtan</h2>
    <p class="lede">Designtårtor beställs 1-2 veckor i förväg, tårtor med sockerblommor gärna en månad innan. Hämtas i Arlöv, och leverans kan ordnas, men då tillkommer en extra kostnad beroende på avstånd.</p>
    <div class="acts"><a class="btn btn-gel" href="@bestall">Beställ tårta {A}</a><a class="btn btn-line" href="tel:+46738740378">Ring 073-874 03 78</a></div>
  </div>
</section>
'''

TARTOR = f'''
<div class="wrap page-head">
  <div class="slab" id="tartorHead" style="--c:var(--rose)">
    <div>
      <h1>Våra tårtor</h1>
      <p class="lede measure" style="margin-top:16px">Bröllopstårtor, barntårtor, studenttårtor och tårtor med handgjorda sockerblommor, bakade i Arlöv.</p>
    </div>
    <p class="num" id="count" aria-live="polite" style="font-weight:600;justify-self:end">36 tårtor</p>
    <ul class="pots filters" id="filters" aria-label="Visa tårtor för" style="grid-column:1/-1"></ul>
    <div class="grid" id="grid"></div>
  </div>
</div>
<section class="wrap close" aria-labelledby="t-close">
  <div class="slab c-pistachio">
    <h2 id="t-close">Har du sett något du gillar?</h2>
    <p class="lede">Berätta vilken tårta som inspirerat dig. Fiona gör den till er egen.</p>
    <div class="acts"><a class="btn btn-gel" href="@bestall">Beställ tårta {A}</a></div>
  </div>
</section>
<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Bildvisning">
  <button class="ctl x" id="lbX" aria-label="Stäng">{ICON['x']}</button>
  <button class="ctl prev" id="lbPrev" aria-label="Föregående tårta">{ICON['left']}</button>
  <figure><img id="lbImg" src="img/39.jpg" alt=""><figcaption id="lbCap"></figcaption></figure>
  <button class="ctl next" id="lbNext" aria-label="Nästa tårta">{ICON['right']}</button>
</div>
'''

def chips(group, items):
    out = []
    for v, extra in items:
        x = f'<small>+{extra} kr</small>' if extra else ''
        out.append(f'<button type="button" class="chip" data-v="{v}" aria-pressed="false">{v}{x}</button>')
    return f'<div class="chips" data-group="{group}">' + ''.join(out) + '</div>'

M1 = [('Blåbär',0),('Hallon',0),('Mango',0),('Passion',0),('Skogsbär',0),('Jordgubb',0),('Jordgubb & rabarber',0),('Pistage',5)]
M2 = [('Vit choklad',0),('Mjölkchoklad',0),('Mörk choklad',0),('Pannacotta',0),('Citron',0),('Nougat',5)]

SMAKER = f'''
<div class="wrap page-head">
  <div class="slab c-butter">
    <div>
      <h1>Smaker &amp; priser</h1>
      <p class="lede measure" style="margin-top:16px">Tårta från 60 kr per bit. Välj botten och två moussefyllningar, så växer tårtan fram här bredvid.</p>
    </div>
    <p style="justify-self:end;text-align:right"><span class="big num" id="perSlice" data-v="60">60 kr</span><br><span style="font-weight:600">per bit med dina val</span></p>
  </div>
</div>

<section class="wrap" aria-label="Komponera din tårta">
 <div class="slab c-sugar lift builder">
  <div class="section-cake" id="cake" aria-live="polite">
    <div class="layers">
      <div class="layer top">Dekoration <small>efter önskemål</small></div>
      <div class="layer m2" data-layer="m2">Mousse 2 <small>välj</small></div>
      <div class="layer sp" data-layer="base">Botten <small>Vanilj</small></div>
      <div class="layer m1" data-layer="m1">Mousse 1 <small>välj</small></div>
      <div class="layer sp">Botten <small>samma som ovan</small></div>
      <div class="plate"></div>
    </div>
    <p>Dina val följer med till beställningen. Hittar du inte din smak? Skriv vad du önskar, det finns fler alternativ.</p>
  </div>
  <div class="choose"><h2 class="sr">Välj smaker</h2>
    <div><h3>Botten</h3>{chips('base',[('Vanilj',0),('Choklad',0)])}</div>
    <div><h3>Mousse 1</h3>{chips('m1',M1)}</div>
    <div><h3>Mousse 2</h3>{chips('m2',M2)}</div>
    <p><a class="btn btn-gel" href="@bestall">Beställ med de här smakerna {A}</a></p>
  </div>
 </div>
</section>

<section class="wrap" aria-labelledby="pl-h">
 <div class="slab c-rose">
  <h2 id="pl-h">Prislista</h2>
  <div class="price-rows">
    <div class="price-row"><h3>Designtårta</h3><p>Botten och två moussefyllningar. Dekorationen prissätts efter antal detaljer och svårighetsgrad.</p><div class="amt">60 kr<small>per bit</small></div></div>
    <div class="price-row"><h3>Bageritårtor</h3><p>Tiramisu, moussetårta, vit chokladcheesecake på mördegsbotten, prinsesstårta.</p><div class="amt">60 kr<small>per bit</small></div></div>
    <div class="price-row"><h3>Cakepops, macarons, mini cupcakes</h3><p>Minst 12 stycken.</p><div class="amt">25 kr<small>per st</small></div></div>
    <div class="price-row"><h3>Bakelser</h3><p>Pannacotta eller moussebakelse i glas, maränglollipop, mini popsicles, stora cupcakes med marängsmörkräm. Minst 4 stycken.</p><div class="amt">45 kr<small>per st</small></div></div>
    <div class="price-row"><h3>Logga, tema eller specialdekor</h3><p>Tillägg på bakelser med logotyp, specialspritsning eller färg.</p><div class="amt">+10 kr<small>per st</small></div></div>
  </div>
 </div>
</section>
'''

OM = f'''
<div class="wrap page-head">
  <div class="slab c-butter">
    <div>
      <h1>Om Fiona, konditor i Arlöv</h1>
      <p class="lede measure" style="margin-top:16px">Konditor, sugarpaste-dekoratör och Cake and Sugarflower designer, med verkstad några minuter från Malmö.</p>
    </div>
  </div>
</div>
<section class="wrap">
 <div class="slab c-pistachio about">
  <div class="pics">
    <img src="img/13.jpg" alt="Körsbärsgren och ros formade i socker" loading="lazy">
    <img src="img/35.jpg" alt="Blå ros i socker på en tårta" loading="lazy">
  </div>
  <div class="text measure">
    <p class="lede" style="color:var(--plum)">Fiona driver Fiona's Bakery i Arlöv. Hon bakar skräddarsydda tårtor för bröllop, födelsedagar, dop och babyshowers, och trendiga bakelser som cakepops, popsicles, cupcakes och macarons.</p>
    <p>Sockerblommorna är hennes signatur. Varje kronblad kavlas, formas och färgas för hand och får torka innan det sätts på tårtan, därför behöver de lite extra tid. Figurerna i sockerpasta, från nallar till Super Mario, modelleras på samma sätt.</p>
    <p>Fiona bakar för alla, oavsett var du bor, i mån av tid. Tårtan hämtas i Arlöv, och leverans kan ordnas, men då tillkommer en extra kostnad beroende på avstånd.</p>
  </div>
 </div>
</section>
<section class="wrap" aria-labelledby="steps-h">
 <div class="slab c-butter">
  <h2 id="steps-h">Så beställer du en tårta</h2>
  <ol class="steps">
    <li class="c-rose"><span class="n">1</span><h3>Skicka en förfrågan</h3><p>Datum, antal bitar och ungefär vad du tänker dig.</p></li>
    <li class="c-butter"><span class="n">2</span><h3>Smak och design</h3><p>Ni pratar igenom tårtan. Inspirationsbilder bifogar du när ni mejlar vidare.</p></li>
    <li class="c-pistachio"><span class="n">3</span><h3>Offert och betalning</h3><p>Pris efter antal bitar och dekorationens detaljer. Betalning med Företagsswish.</p></li>
    <li class="c-rose"><span class="n">4</span><h3>Hämta och fira</h3><p>Tårtan hämtas i Arlöv på överenskommen tid, eller levereras efter överenskommelse.</p></li>
  </ol>
  <p style="margin-top:32px"><a class="btn btn-gel" href="@bestall">Beställ tårta {A}</a></p>
 </div>
</section>
'''

FAQ_ITEMS = [
 ('Hur långt i förväg behöver jag beställa tårta?', 'Designtårtor minst 1-2 veckor innan, tårtor med sockerblommor gärna en månad i förväg. Är det bråttom går det ofta att lösa, så hör av dig ändå.', 'rose'),
 ('Vad kostar en tårta eller bröllopstårta?', 'Grundpriset är 60 kr per bit. Pistage- eller nougatmousse kostar 5 kr extra per bit. Dekorationen prissätts efter antal detaljer och hur avancerade de är, och du får alltid en offert först.', 'butter'),
 ('Kan jag skicka inspirationsbilder?', 'Ja, gärna. Skicka först din förfrågan. När Fiona svarar kan du bifoga bilder på hur du vill att tårtan ska se ut.', 'pistachio'),
 ('Hur betalar jag?', 'Med Företagsswish. Fiona\'s Bakery är godkänt för F-skatt, vilket gör det enkelt för företag att beställa.', 'butter'),
 ('Kan ni ta hänsyn till allergier?', 'Skriv om allergier och specialkost i förfrågan, så berättar Fiona vilka alternativ som går att göra.', 'rose'),
]
FRAGOR = '''
<div class="wrap page-head">
  <div class="slab c-pistachio">
    <div>
      <h1>Frågor om tårtbeställning</h1>
      <p class="lede measure" style="margin-top:16px">Det här undrar de flesta. Hittar du inte svaret? Ring 073-874 03 78.</p>
    </div>
  </div>
</div>
<section class="wrap"><div class="slab c-butter"><div class="faq">
''' + ''.join(f'<details class="c-{c}"{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a,c) in enumerate(FAQ_ITEMS)) + f'''
</div></div></section>
<section class="wrap close"><div class="slab c-rose"><h2>Redo att beställa?</h2><div class="acts"><a class="btn btn-gel" href="@bestall">Beställ tårta {A}</a></div></div></section>
'''

POTS_ORDER = ''.join(
    f'<li><label class="pot c-{c}"><input type="radio" name="occ" value="{k}"><i></i>{label}</label></li>'
    for k, c, label in [('brollop','rose','Bröllop'),('barn','butter','Barnkalas & dop'),('fest','butter','Födelsedag'),('student','pistachio','Student'),('bakelser','pistachio','Företag & event')])

def opts(items, first):
    return f'<option value="">{first}</option>' + ''.join(f'<option value="{v}">{v}{" (+5 kr/bit)" if e else ""}</option>' for v, e in items)

BESTALL = f'''
<div class="order-page"><div class="wrap order">
  <div class="slab order-card" id="orderCard">
    <h1>Beställ tårta</h1>
    <p class="lede measure">Fyll i det du vet. Förfrågan är inte bindande, Fiona återkommer med förslag och offert.</p>
    <form id="orderForm" novalidate>
      <fieldset class="fs field" id="w-occ">
        <legend>Vad ska ni fira?</legend>
        <ul class="pots">{POTS_ORDER}</ul>
      </fieldset>
      <div class="fs row2">
        <div class="field" id="w-date">
          <label class="lbl" for="date">Datum</label>
          <input type="date" id="date" aria-required="true" aria-describedby="errors">
        </div>
        <div class="field" id="w-servings">
          <label class="lbl" for="servings">Antal bitar</label>
          <div class="stepper">
            <button type="button" data-d="-1" aria-label="En bit färre">{ICON['minus']}</button>
            <input type="number" id="servings" min="8" max="400" value="30" inputmode="numeric" aria-required="true" aria-describedby="errors">
            <button type="button" data-d="1" aria-label="En bit fler">{ICON['plus']}</button>
          </div>
        </div>
      </div>
      <div class="band" id="band" role="status">{ICON['clock']}<span id="bandText">Designtårtor beställs 1-2 veckor i förväg.</span></div>
      <div class="fs" style="margin-top:clamp(24px,3vw,32px)">
        <span class="lbl">Smaker <small>(valfritt, Fiona hjälper gärna till)</small></span>
        <div class="row2" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">
          <div class="field"><label for="base" class="sr">Botten</label><select id="base"><option value="Vanilj">Vaniljbotten</option><option value="Choklad">Chokladbotten</option></select></div>
          <div class="field"><label for="m1" class="sr">Mousse 1</label><select id="m1">{opts(M1,'Mousse 1: välj')}</select></div>
          <div class="field"><label for="m2" class="sr">Mousse 2</label><select id="m2">{opts(M2,'Mousse 2: välj')}</select></div>
        </div>
      </div>
      <div class="fs"><label class="toggle"><input type="checkbox" id="flowers"><i></i>Jag önskar handgjorda sockerblommor</label></div>
      <div class="fs field" id="w-wish">
        <label class="lbl" for="wish">Hur tänker du dig tårtan?</label>
        <textarea id="wish" aria-required="true" aria-describedby="errors" placeholder="Tema, färger, text på tårtan, allergier …"></textarea>
      </div>
      <div class="fs field">
        <label class="lbl" for="pickup">Hämtning</label>
        <select id="pickup"><option>Hämtar i Arlöv</option><option>Önskar leverans (extra kostnad beroende på avstånd)</option></select>
      </div>
      <div class="fs row2">
        <div class="field" id="w-name"><label class="lbl" for="name">Namn</label><input id="name" autocomplete="name" aria-required="true" aria-describedby="errors"></div>
        <div class="field" id="w-phone"><label class="lbl" for="phone">Telefon</label><input id="phone" type="tel" autocomplete="tel" aria-required="true" aria-describedby="errors"></div>
      </div>
      <div class="fs field" id="w-email"><label class="lbl" for="email">E-post</label><input id="email" type="email" autocomplete="email" aria-required="true" aria-describedby="errors"></div>
      <div class="errors" id="errors" hidden role="alert"></div>
      <div class="submit-row">
        <button class="btn btn-gel" type="submit">Skapa förfrågan {A}</button>
        <p>Du ser hela texten innan något skickas.</p>
      </div>
    </form>
    <div class="result" id="result" hidden>
      <h2 id="resultHead" tabindex="-1">Din förfrågan är klar</h2>
      <p>Öppna den i ditt e-postprogram, eller kopiera texten och skicka den till kontakt@fionasbakery.se.</p>
      <pre id="resultText"></pre>
      <div class="acts">
        <a class="btn btn-gel" id="mailLink" href="#">Öppna i e-post</a>
        <button class="btn btn-line" type="button" id="copyBtn">Kopiera texten</button>
        <span class="status" id="copyStatus" aria-live="polite"></span>
      </div>
    </div>
  </div>
  <aside class="summary" aria-label="Sammanfattning">
    <div class="slab c-butter">
      <span style="font-weight:600">Uppskattat baspris</span>
      <div class="big" id="estimate" data-v="1800" aria-live="polite">1 800 kr</div>
      <dl class="num">
        <dt>Tillfälle</dt><dd id="sumOcc">Ej valt</dd>
        <dt>Datum</dt><dd id="sumDate">Ej valt</dd>
        <dt>Antal</dt><dd id="sumN">30 bitar</dd>
        <dt>Pris per bit</dt><dd id="sumPer">60 kr</dd>
      </dl>
      <p class="fine-note">Före dekoration. Slutpriset kommer i offerten.</p>
    </div>
    <div class="slab c-sugar lift contact">
      <span>Hellre prata direkt?</span>
      <strong><a href="tel:+46738740378">073-874 03 78</a></strong>
      <a href="mailto:kontakt@fionasbakery.se">kontakt@fionasbakery.se</a>
      <a href="https://www.instagram.com/fionasbakery/" rel="noopener" target="_blank">Instagram @fionasbakery</a>
    </div>
  </aside>
</div>
<div class="mbar" aria-hidden="true"><span>Uppskattat baspris<br><small id="mN">30 bitar</small></span><b id="mEst">1 800 kr</b></div>
</div>
'''

PAGES = [
 # slug, file, nav label, <title>, description, body
 ('hem', 'index', 'Hem', "Tårtor på beställning i Malmö & Arlöv | Fiona's Bakery",
  "Beställ tårta i Malmö och Arlöv. Bröllopstårtor med handgjorda sockerblommor, barntårtor, födelsedagstårtor, studenttårtor och cupcakes med logga. Från 60 kr/bit.", HEM),
 ('tartor', 'tartor', 'Tårtor', "Bröllopstårtor, barntårtor & studenttårtor | Fiona's Bakery",
  "Bilder på bröllopstårtor med sockerblommor, barntårtor med figurer, studenttårtor och bakelser från Fiona's Bakery i Arlöv.", TARTOR),
 ('smaker', 'smaker-priser', 'Smaker & priser', "Smaker & priser: tårta från 60 kr/bit | Fiona's Bakery",
  "Välj vanilj- eller chokladbotten och två moussefyllningar. Tårta 60 kr/bit, cakepops och macarons 25 kr/st, bakelser 45 kr/st.", SMAKER),
 ('om', 'om-fiona', 'Om Fiona', "Om Fiona: konditor & sockerblomsdesigner i Arlöv | Fiona's Bakery",
  "Fiona är konditor och sockerblomsdesigner i Arlöv. Så beställer du en tårta, från förfrågan till hämtning.", OM),
 ('fragor', 'fragor', 'Frågor', "Frågor om tårtbeställning | Fiona's Bakery",
  "Hur långt i förväg beställer man tårta, vad kostar det och var hämtas den? Svar på vanliga frågor om att beställa tårta i Malmö och Arlöv.", FRAGOR),
 ('bestall', 'bestall', 'Beställ tårta', "Beställ tårta: Malmö, Lund & Arlöv | Fiona's Bakery",
  "Skicka en tårtförfrågan till Fiona's Bakery. Välj tillfälle, datum, antal bitar och smaker och se ett uppskattat pris direkt.", BESTALL),
]
