(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const DIMS = __DIMS__;
  const wh = k => DIMS[k] ? `width="${DIMS[k][0]}" height="${DIMS[k][1]}"` : '';
  const kr = n => n.toLocaleString('sv-SE') + ' kr';
  const PRICE = 60;
  /* Antal bitar: minst 8, jämna tal eller tal som slutar på 5 (15, 25, 35 …) */
  const MIN_N = 8, MAX_N = 400;
  const okN = n => n >= MIN_N && n <= MAX_N && (n % 2 === 0 || n % 10 === 5);
  const stepN = (n, d) => { n = Math.min(MAX_N, Math.max(MIN_N - 1, n)); do { n += d; } while (n > MIN_N && n < MAX_N && !okN(n)); return Math.min(MAX_N, Math.max(MIN_N, n)); };
  const snapN = n => { n = Math.round(n) || MIN_N; if (n <= MIN_N) return MIN_N; if (n >= MAX_N) return MAX_N; if (okN(n)) return n; return okN(n + 1) ? n + 1 : n - 1; };

  /* ---------- shared order state (survives page changes) ---------- */
  const store = (() => {
    let mem = {};
    try { mem = JSON.parse(sessionStorage.getItem('fb-order') || '{}'); } catch (_) {}
    return {
      get: k => mem[k],
      set(k, v) { mem[k] = v; try { sessionStorage.setItem('fb-order', JSON.stringify(mem)); } catch (_) {} }
    };
  })();

  /* ---------- colours per occasion ---------- */
  const OCC = {
    brollop:  {label:'Bröllop',            c:'rose',      c2:'pistachio', img:'39', tag:'Sockerblommor', title:'Bröllopstårtor'},
    barn:     {label:'Barnkalas & dop',    c:'butter',    c2:'rose',      img:'28', tag:'Modellerade figurer', title:'Barntårtor'},
    fest:     {label:'Födelsedag',         c:'butter',    c2:'pistachio', img:'30', tag:'Marmor & färska blommor', title:'Födelsedagstårtor'},
    student:  {label:'Student',            c:'pistachio', c2:'rose',      img:'34', tag:'Studentmössa i sockerpasta', title:'Studenttårtor'},
    bakelser: {label:'Bakelser',           c:'pistachio', c2:'butter',    img:'31', tag:'Cakepops & macarons', title:'Bakelser'},
  };
  const cssVar = c => `var(--${c})`;

  /* ---------- tiny number ticker ---------- */
  function tick(el, to, fmt = kr) {
    const from = +(el.dataset.v || 0);
    el.dataset.v = to;
    if (reduced || from === to) { el.textContent = fmt(to); return; }
    const t0 = performance.now(), dur = 520;
    const step = t => {
      const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(2, -10 * p);
      el.textContent = fmt(Math.round(from + (to - from) * (p === 1 ? 1 : e)));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* ---------- gentle rise for slabs entering the viewport ---------- */
  if (!reduced && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), {rootMargin: '0px 0px -8% 0px'});
    const arm = () => $$('main section > .slab, .range figure, .tile').forEach(el => {
      if (el.classList.contains('in') || el.dataset.armed) return;
      if (el.getBoundingClientRect().top > innerHeight) { el.dataset.armed = 1; el.classList.add('rise'); io.observe(el); }
    });
    arm(); document.addEventListener('page', () => setTimeout(arm, 0)); document.addEventListener('gallery', arm);
  }

  /* ---------- menu ---------- */
  const menuBtn = $('#menuBtn'), tabs = $('#tabs');
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = tabs.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open);
    });
    addEventListener('keydown', e => { if (e.key === 'Escape' && tabs.classList.contains('open')) { tabs.classList.remove('open'); menuBtn.setAttribute('aria-expanded', false); menuBtn.focus(); } });
    tabs.addEventListener('click', e => { if (e.target.closest('a')) { tabs.classList.remove('open'); menuBtn.setAttribute('aria-expanded', false); } });
  }

  /* ---------- preview routing (single-file build only) ---------- */
  const pages = $$('[data-page]');
  if (pages.length > 1) {
    const ids = pages.map(p => p.dataset.page);
    const show = scroll => {
      const id = ids.includes(location.hash.slice(1)) ? location.hash.slice(1) : 'hem';
      pages.forEach(p => p.hidden = p.dataset.page !== id);
      $$('#tabs a').forEach(a => a.getAttribute('href') === '#' + id ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current'));
      document.dispatchEvent(new CustomEvent('page', {detail: id}));
      if (scroll) window.scrollTo(0, 0);
    };
    addEventListener('hashchange', () => show(true));
    show(false);
  }

  /* ---------- HOME: occasion pots re-tint the opening ---------- */
  const opening = $('.opening');
  if (opening) {
    const img = $('#heroImg'), tag = $('#heroTag'), see = $('#heroSee');
    const set = key => {
      const o = OCC[key];
      opening.style.setProperty('--tint', cssVar(o.c));
      opening.style.setProperty('--tint-2', cssVar(o.c2));
      $$('.pot', opening).forEach(p => p.setAttribute('aria-pressed', p.dataset.occ === key));
      tag.textContent = o.tag; tag.className = `tag c-${o.c}`;
      see.querySelector('span').textContent = `Se fler ${o.title.toLowerCase()}`;
      see.dataset.filter = key;
      if (img.dataset.k === o.img) return;
      const swap = () => { img.src = `img/${o.img}.webp`; img.dataset.k = o.img; img.alt = `${o.title}: ${o.tag.toLowerCase()} från Fiona's Bakery`; };
      if (reduced) return swap();
      img.classList.add('out');
      setTimeout(() => { swap(); img.onload = () => img.classList.remove('out'); if (img.complete) img.classList.remove('out'); }, 280);
    };
    $$('.pot', opening).forEach(p => p.addEventListener('click', () => { set(p.dataset.occ); store.set('occ', p.dataset.occ); }));
  }
  $$('[data-filter]').forEach(a => a.addEventListener('click', () => store.set('filter', a.dataset.filter)));

  /* ---------- HOME: slice calculator ---------- */
  const guests = $('#guests');
  if (guests) {
    const out = $('#guestsKr'), n = $('#guestsN'), go = $('#guestsGo');
    const upd = () => {
      const v = snapN(+guests.value); guests.value = v;
      guests.style.setProperty('--p', ((v - guests.min) / (guests.max - guests.min) * 100) + '%');
      tick(out, v * PRICE); n.textContent = v;
      go.querySelector('span').textContent = `Beställ för ${v} personer`;
    };
    guests.addEventListener('input', upd);
    go.addEventListener('click', () => store.set('servings', +guests.value));
    upd();
  }

  /* ---------- GALLERY ---------- */
  const CATS = {alla:['Alla','sugar'], brollop:['Bröllop','rose'], sockerblommor:['Sockerblommor','rose'], barn:['Barn & dop','butter'], fest:['Fest & jubileum','butter'], student:['Student','pistachio'], bakelser:['Bakelser','pistachio']};
  const WORKS = [
    ['39','Skulpterat socker & körsbärsblom','brollop','Skulpterat socker',1],['28','Valpar till Hector','barn','Modellerade figurer'],
    ['08','Designerväskor','fest','3D-form'],['02','Pioner och rosor','sockerblommor','Sockerblommor'],
    ['05','Babyshower med nallar','barn','Modellerade figurer'],['16','Mario-äventyr','barn','Modellerade figurer',1],
    ['37','Räfflad grädde & färska rosor','brollop','Färska blommor'],['30','Marmor & champagne till 60','fest','Marmor'],
    ['31','Cakepops med guldstänk','bakelser','Cakepops'],['34','Studentmössa med rosor','student','3D-form'],
    ['14','Körsbärsblommor','sockerblommor','Sockerblommor'],['23','Leia fyller tre','barn','Modellerade figurer'],
    ['00','Tre våningar med sockerrosor','brollop','Sockerblommor',1],['33','Monogram i marinblått','fest','Mönster'],
    ['04','Vildblommor & spets','brollop','Färska blommor'],['07','Cupcakes med monogram','brollop','Cupcakes'],
    ['24','Bondgården','barn','Modellerade figurer'],['25','Bokstapel','fest','3D-form'],
    ['12','Sockerrosor i blush','sockerblommor','Sockerblommor'],['20','Kattunge med rosett','barn','Modellerad figur'],
    ['40','Roulette','fest','3D-form',1],['03','Pion & bladguld','brollop','Drip & bladguld'],
    ['09','Macarons till babyshower','bakelser','Macarons'],['26','Racerbil','barn','Modellerad figur'],
    ['29','Happy Birthday i guld','fest','Bladguld'],['35','Blå sockerros','sockerblommor','Sockerblommor'],
    ['38','Studentmössa','student','3D-form'],['19','Liten drake','barn','Modellerad figur'],
    ['32','Maränglollipops','bakelser','Maräng'],['15','Artonårstårta','fest','3D-detaljer'],
    ['27','Nalle & bokstavsklossar','barn','Modellerade figurer'],['11','Cupcakes med monogram','brollop','Cupcakes'],
    ['06','Nallar i balett','barn','Modellerade figurer'],['22','Handväska','fest','3D-form'],
    ['21','Cupcakes med tryck','bakelser','Tryck'],['01','Sockerpion','sockerblommor','Sockerblommor'],
    ['10','Gender reveal','barn','Överraskning inuti'],['13','Körsbärsblom i kanna','sockerblommor','Sockerblommor'],
    ['48','Smörkräm & sockerrosor','brollop','Sockerblommor'],['49','Grön bröllopstårta med sockerblad','brollop','Sockerblommor'],
    ['50','Sockerrosor & sockerblad','brollop','Sockerblommor'],['45','Grattis till examen','student','3D-detaljer'],
    ['47','Studentmössa & vinfat','student','3D-form'],['46','Cupcakes med fotspår','barn','Cupcakes'],
    ['41','Cakesicles & cakepops i blått','bakelser','Cakepops'],['42','Mousse med äppelchips','bakelser','Logotyp'],
    ['43','Mousse med rosa swirl','bakelser','Logotyp'],['44','Frukter i mousse','bakelser','Formade bakelser'],
    ['51','Nalle med kulor & fjärilar','barn','Tryckt motiv'],['52','Baby girl & baby boy','barn','Modellerade figurer'],
    ['53','Hobbitstugan','fest','Modellerade detaljer'],
  ];
  const KW = {brollop:'Bröllopstårta', sockerblommor:'Tårta med sockerblommor', barn:'Barntårta', fest:'Festtårta', student:'Studenttårta', bakelser:'Bakelser'};
  const grid = $('#grid');
  let visible = [];
  function setFilter(k) {
    if (!grid || !CATS[k]) return;
    $$('#filters .pot').forEach(p => p.setAttribute('aria-pressed', p.dataset.cat === k));
    const head = $('#tartorHead'); if (head) head.style.setProperty('--c', cssVar(k === 'alla' ? 'rose' : CATS[k][1]));
    visible = WORKS.filter(w => k === 'alla' || w[2] === k);
    grid.innerHTML = visible.map((w, i) => `
      <figure class="tile c-${CATS[w[2]][1]}${w[4] && k === 'alla' ? ' wide' : ''}">
        <div class="frame"><button type="button" data-i="${i}" aria-label="Visa större: ${w[1]}"></button>
        <img src="img/${w[0]}.webp" ${wh(w[0])} alt="${KW[w[2]]}: ${w[1]}" loading="lazy" decoding="async"></div>
        <figcaption><span class="name">${w[1]}</span><span class="tag c-${CATS[w[2]][1]}">${w[3]}</span></figcaption>
      </figure>`).join('');
    $('#count').textContent = `${visible.length} tårtor`;
    document.dispatchEvent(new Event('gallery'));
  }
  if (grid) {
    const f = $('#filters');
    f.innerHTML = Object.entries(CATS).map(([k, [label, c]]) =>
      `<li><button class="pot c-${c}" type="button" data-cat="${k}" aria-pressed="false"><i></i>${label}</button></li>`).join('');
    f.addEventListener('click', e => { const b = e.target.closest('.pot'); if (b) { setFilter(b.dataset.cat); store.set('filter', b.dataset.cat); } });
    const init = () => setFilter(store.get('filter') || 'alla');
    init();
    document.addEventListener('page', e => { if (e.detail === 'tartor') init(); });

    const lb = $('#lb'); let cur = 0, last = null;
    const show = i => {
      cur = (i + visible.length) % visible.length; const w = visible[cur];
      $('#lbImg').src = `img/${w[0]}.webp`; $('#lbImg').alt = `${KW[w[2]]}: ${w[1]}`;
      $('#lbCap').innerHTML = `${w[1]} <span class="tag c-${CATS[w[2]][1]}">${w[3]}</span>`;
    };
    grid.addEventListener('click', e => { const b = e.target.closest('button[data-i]'); if (!b) return; last = b; show(+b.dataset.i); lb.hidden = false; $('#lbX').focus(); });
    const close = () => { lb.hidden = true; last && last.focus(); };
    $('#lbX').onclick = close; $('#lbPrev').onclick = () => show(cur - 1); $('#lbNext').onclick = () => show(cur + 1);
    lb.addEventListener('click', e => { if (e.target === lb || e.target.tagName === 'FIGURE') close(); });
    addEventListener('keydown', e => { if (lb.hidden) return;
      if (e.key === 'Tab') { const c = [$('#lbX'), $('#lbPrev'), $('#lbNext')], i = c.indexOf(document.activeElement); e.preventDefault(); c[(i + (e.shiftKey ? c.length - 1 : 1)) % c.length].focus(); return; }
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(cur - 1); if (e.key === 'ArrowRight') show(cur + 1); });
  }

  /* ---------- FLAVOURS: build the cross-section ---------- */
  const cake = $('#cake');
  if (cake) {
    const groups = {base:'Vanilj', m1:'', m2:''};
    const paint = () => {
      ['base','m1','m2'].forEach(g => {
        const v = store.get(g) ?? groups[g];
        $(`[data-layer="${g}"] small`).textContent = v || 'välj';
        $$(`[data-group="${g}"] .chip`).forEach(c => c.setAttribute('aria-pressed', c.dataset.v === v));
      });
      const extra = (store.get('m1') === 'Pistage' ? 5 : 0) + (store.get('m2') === 'Nougat' ? 5 : 0);
      tick($('#perSlice'), PRICE + extra);
    };
    $$('[data-group]').forEach(g => g.addEventListener('click', e => {
      const c = e.target.closest('.chip'); if (!c) return;
      store.set(g.dataset.group, c.dataset.v); paint();
    }));
    paint();
    document.addEventListener('page', e => { if (e.detail === 'smaker') paint(); });
  }

  /* ---------- ORDER ---------- */
  const form = $('#orderForm');
  if (!form) return;
  const card = $('#orderCard'), today = new Date(); today.setHours(0,0,0,0);
  const iso = d => `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  const f = id => $('#' + id);
  f('date').min = iso(today);

  const restore = () => {
    const occ = store.get('occ'); if (occ) { const r = form.querySelector(`input[name=occ][value="${occ}"]`); if (r) r.checked = true; }
    if (store.get('servings')) f('servings').value = snapN(+store.get('servings'));
    if (store.get('base')) f('base').value = store.get('base');
    if (store.get('m1')) f('m1').value = store.get('m1');
    if (store.get('m2')) f('m2').value = store.get('m2');
    update();
  };

  function days() { const v = f('date').value; return v ? Math.round((new Date(v + 'T00:00') - today) / 864e5) : null; }
  function update() {
    const occ = form.querySelector('input[name=occ]:checked');
    card.style.setProperty('--tint', cssVar(occ ? OCC[occ.value].c : 'rose'));
    const n = Math.max(0, parseInt(f('servings').value, 10) || 0);
    const extra = (f('m1').value === 'Pistage' ? 5 : 0) + (f('m2').value === 'Nougat' ? 5 : 0);
    tick(f('estimate'), n * (PRICE + extra));
    if (f('mEst')) { f('mEst').textContent = kr(n * (PRICE + extra)); f('mN').textContent = `${n} bitar före dekoration`; }
    f('sumN').textContent = n ? `${n} bitar` : 'Ej valt';
    f('sumPer').textContent = `${PRICE + extra} kr`;
    f('sumOcc').textContent = occ ? OCC[occ.value].label : 'Ej valt';
    const d = days(), sf = f('flowers').checked, band = f('band'), txt = f('bandText');
    band.className = 'band';
    if (d === null) txt.textContent = sf ? 'Tårtor med sockerblommor beställs gärna en månad i förväg.' : 'Designtårtor beställs 1-2 veckor i förväg.';
    else if (d < 0) { band.classList.add('warn'); txt.textContent = 'Det datumet har redan varit. Välj ett kommande datum.'; }
    else if (sf && d < 30) { band.classList.add('warn'); txt.textContent = `Om ${d} dagar. Sockerblommor behöver helst en månad, men skicka ändå, så ser Fiona vad som hinns.`; }
    else if (d < 7) { band.classList.add('warn'); txt.textContent = `Om ${d} dagar. Kort varsel, men hör av dig, så ser Fiona vad som går.`; }
    else { band.classList.add('ok'); txt.textContent = `Om ${d} dagar. Gott om tid.`; }
    f('sumDate').textContent = f('date').value ? new Date(f('date').value + 'T00:00').toLocaleDateString('sv-SE', {day:'numeric', month:'short'}) : 'Ej valt';
  }
  form.addEventListener('input', update);
  form.addEventListener('change', e => {
    if (e.target.name === 'occ') store.set('occ', e.target.value);
    if (['base','m1','m2'].includes(e.target.id)) store.set(e.target.id, e.target.value);
    if (e.target.id === 'servings') { e.target.value = snapN(parseInt(e.target.value, 10)); store.set('servings', +e.target.value); update(); }
  });
  $$('.stepper button').forEach(b => b.addEventListener('click', () => {
    const i = f('servings'); i.value = stepN(parseInt(i.value, 10) || MIN_N, +b.dataset.d);
    store.set('servings', +i.value); update();
  }));

  const rules = [
    ['occ', () => form.querySelector('input[name=occ]:checked'), 'Vilket tillfälle tårtan är till'],
    ['date', () => f('date').value && days() >= 0, 'Ett datum som inte redan har varit'],
    ['servings', () => okN(parseInt(f('servings').value, 10)), 'Antal bitar: minst 8, jämnt antal eller 15, 25, 35 …'],
    ['wish', () => f('wish').value.trim().length >= 5, 'Några ord om hur tårtan ska se ut'],
    ['name', () => f('name').value.trim(), 'Ditt namn'],
    ['phone', () => f('phone').value.replace(/\D/g,'').length >= 7, 'Ett telefonnummer Fiona kan nå dig på'],
    ['email', () => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f('email').value.trim()), 'En giltig e-postadress, t.ex. namn@exempel.se'],
  ];
  form.addEventListener('submit', e => {
    e.preventDefault();
    const miss = rules.filter(([id, ok]) => { const bad = !ok(); const el = f('w-' + id); if (el) el.setAttribute('aria-invalid', bad); const ctl = id === 'occ' ? null : f(id); if (ctl) ctl.setAttribute('aria-invalid', bad); return bad; });
    const box = f('errors');
    if (miss.length) {
      box.innerHTML = 'Nästan klart. Det här saknas:<ul>' + miss.map(m => `<li>${m[2]}</li>`).join('') + '</ul>';
      box.hidden = false;
      const first = miss[0][0] === 'occ' ? form.querySelector('input[name=occ]') : f(miss[0][0]);
      first && first.focus(); return;
    }
    box.hidden = true;
    const occ = OCC[form.querySelector('input[name=occ]:checked').value];
    const n = parseInt(f('servings').value, 10);
    const extra = (f('m1').value === 'Pistage' ? 5 : 0) + (f('m2').value === 'Nougat' ? 5 : 0);
    const date = new Date(f('date').value + 'T00:00').toLocaleDateString('sv-SE', {weekday:'long', day:'numeric', month:'long', year:'numeric'});
    const body = [
      'Hej Fiona!', '',
      `Jag skulle vilja beställa en tårta till ${occ.label.toLowerCase()}, ${date}, för ungefär ${n} personer.`, '',
      `Botten: ${f('base').value}`,
      `Mousse 1: ${f('m1').value || 'gärna ett förslag'}`,
      `Mousse 2: ${f('m2').value || 'gärna ett förslag'}`,
      `Sockerblommor: ${f('flowers').checked ? 'ja, gärna' : 'nej'}`,
      `Hämtning/leverans: ${f('pickup').value}`, '',
      'Så här tänker jag mig tårtan:', f('wish').value.trim(), '',
      ...(f('inspo').value.trim() ? [`Inspirationsbild: ${f('inspo').value.trim()}`, ''] : []),
      `Uppskattat baspris: ${kr(n * (PRICE + extra))} före dekoration.`, '',
      'Vänliga hälsningar', f('name').value.trim(), f('phone').value.trim(), f('email').value.trim()
    ].join('\n');
    const subject = `Tårtförfrågan: ${occ.label}, ${f('date').value}`;
    f('resultText').textContent = `Till: kontakt@fionasbakery.se\nÄmne: ${subject}\n\n${body}`;
    f('mailLink').href = `mailto:kontakt@fionasbakery.se?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    f('copyStatus').textContent = '';
    f('result').hidden = false;
    f('result').scrollIntoView({behavior: reduced ? 'auto' : 'smooth', block: 'start'});
    f('resultHead').focus({preventScroll: true});
  });
  f('copyBtn').addEventListener('click', () => {
    const pre = f('resultText');
    const sel = () => { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); f('copyStatus').textContent = 'Texten är markerad. Kopiera med ⌘C eller Ctrl+C.'; };
    try { navigator.clipboard.writeText(pre.textContent).then(() => f('copyStatus').textContent = 'Kopierat. Klistra in i ett mejl till Fiona.', sel); } catch (_) { sel(); }
  });
  restore();
  document.addEventListener('page', e => { if (e.detail === 'bestall') restore(); });
})();
