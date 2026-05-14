/* ============================================================
   LUXURY.JS — Shared animations & interactions
   ============================================================ */

'use strict';

// ── Scroll-reveal via IntersectionObserver ──────────────────
function initReveal() {
  const els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  if (!els.length) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => io.observe(el));
}

// ── Sticky nav on scroll ────────────────────────────────────
function initNav() {
  const nav = document.querySelector('.lux-nav');
  if (!nav) return;
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 60);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// ── Mobile menu toggle ──────────────────────────────────────
function initMobileMenu() {
  const burger = document.querySelector('.burger');
  const menu   = document.querySelector('.mobile-menu');
  if (!burger || !menu) return;
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.querySelectorAll('span').forEach((s, i) => {
      if (open) {
        if (i === 0) s.style.transform = 'rotate(45deg) translate(5px, 5px)';
        if (i === 1) s.style.opacity = '0';
        if (i === 2) s.style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        s.style.transform = '';
        s.style.opacity = '';
      }
    });
    document.body.style.overflow = open ? 'hidden' : '';
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    menu.classList.remove('open');
    burger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    document.body.style.overflow = '';
  }));
}

// ── Animated counters ───────────────────────────────────────
function animateCounter(el, target, duration) {
  const isText = isNaN(parseInt(target));
  if (isText) { el.textContent = target; return; }
  const num = parseInt(target);
  const suffix = target.replace(/[\d]/g, '');
  let start = null;
  const step = ts => {
    if (!start) start = ts;
    const progress = Math.min((ts - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(ease * num) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

function initCounters() {
  const counters = document.querySelectorAll('.stat-num[data-count]');
  if (!counters.length) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        animateCounter(e.target, e.target.dataset.count, 1800);
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });
  counters.forEach(c => io.observe(c));
}

// ── Tour card 3-D tilt ──────────────────────────────────────
function initCardTilt() {
  document.querySelectorAll('.tour-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width  - 0.5;
      const y = (e.clientY - r.top)  / r.height - 0.5;
      card.style.transform = `translateY(-8px) rotateY(${x * 8}deg) rotateX(${-y * 6}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.style.transition = 'transform 0.5s cubic-bezier(0.4,0,0.2,1)';
      setTimeout(() => { card.style.transition = ''; }, 500);
    });
  });
}

// ── Tour filter ─────────────────────────────────────────────
function initFilter() {
  const btns     = document.querySelectorAll('.filter-btn');
  const wrappers = document.querySelectorAll('#toursGrid > [data-cat]');
  if (!btns.length) return;
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;
      wrappers.forEach(w => {
        const show = cat === 'all' || w.dataset.cat === cat;
        w.style.display = show ? '' : 'none';
      });
    });
  });
}

// ── Hero search bar ─────────────────────────────────────────
function initHeroSearch() {
  const btn = document.getElementById('heroSearchBtn');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const dest = document.getElementById('searchDest').value;
    const dur  = document.getElementById('searchDur').value;
    const type = document.getElementById('searchType').value;

    // Priority: type > dest > dur
    const cat = type !== 'all' ? type : dest !== 'all' ? dest : dur !== 'all' ? dur.split(',')[0] : 'all';

    const toursSection = document.querySelector('#tours');
    if (!toursSection) return;
    toursSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    setTimeout(() => {
      const filterBtn = document.querySelector(`.filter-btn[data-filter="${cat}"]`);
      if (filterBtn) filterBtn.click();
    }, 600);
  });
}

// ── Smooth anchor scroll ────────────────────────────────────
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

// ── Hero parallax (light) ───────────────────────────────────
function initHeroParallax() {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const bg = hero.querySelector('.hero-bg');
    if (bg) bg.style.transform = `translateY(${scrolled * 0.35}px)`;
  }, { passive: true });
}

// ── Cursor glow ─────────────────────────────────────────────
function initCursorGlow() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  const glow = document.createElement('div');
  glow.style.cssText = `
    position:fixed; pointer-events:none; z-index:9999;
    width:300px; height:300px; border-radius:50%;
    background:radial-gradient(circle, rgba(200,164,90,0.07) 0%, transparent 70%);
    transform:translate(-50%,-50%); transition:opacity 0.3s;
    top:0; left:0;
  `;
  document.body.appendChild(glow);
  window.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top  = e.clientY + 'px';
  }, { passive: true });
}

// ── Page loader fade ────────────────────────────────────────
function initPageLoader() {
  window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.6s ease';
    requestAnimationFrame(() => { document.body.style.opacity = '1'; });
  });
}

// ── Country content data ────────────────────────────────────
const COUNTRY_DATA = {
  kg: {
    navFlag: '🇰🇬', navLabel: 'Kyrgyzstan',
    heroLabel: "TripAdvisor's #1 Choice · Est. 2016",
    heroTitle: 'Discover the <em>Soul</em><br>of Kyrgyzstan',
    heroSub: 'Private tours crafted with passion — from the ancient Silk Road to high-altitude nomad lakes. 3,000+ happy travellers served.',
    heroFeatures: [
      { icon:'🏔️', label:'Tian Shan Mountains',  sub:'Hiking · Wildlife · Scenic Trails'  },
      { icon:'🌊', label:'Issyk-Kul Lake',        sub:'Beaches · Canyons · Day Trips'      },
      { icon:'🏕️', label:'Song-Kul Nomad Life',   sub:'Yurt Camps · Horses · Stargazing'   },
      { icon:'🦅', label:'Eagle Hunting',          sub:'Ancient Tradition · Culture'        },
      { icon:'🐎', label:'Horseback Riding',       sub:'Multi-day Treks · Adventure'        },
    ],
    stats: ['8+','3000+','21','#1'],
    statLabels: ['Years of Experience','Happy Clients','Unique Tours','TripAdvisor Rated'],
    badgeNum: '2016', badgeText: 'Founded',
    aboutTitle: 'Born during the <em>World Nomad Games</em>',
    aboutLead1: 'Nomadic Nations opened for business in 2016 and quickly developed a reputation for efficient, unique and high-quality customized tours for individuals and groups across Kyrgyzstan.',
    aboutLead2: 'Join us and experience the amazing nature of Kyrgyzstan while learning about nomadic lifestyles through visits with local people along the ancient routes of the Silk Road.',
    toursLabel: 'Our Collection',
    toursTitle: '21 Extraordinary <em>Experiences</em>',
    toursLead: 'From half-day city walks to 5-day nomadic expeditions — every tour is private, customised, and led by the finest local guides.',
    crossRoutes: [
      { toCode:'kz', toFlag:'🇰🇿', toName:'Kazakhstan', fromCity:'Bishkek', toCity:'Almaty',    border:'Korday Border Crossing',   time:'~3–4 hrs by road' },
      { toCode:'uz', toFlag:'🇺🇿', toName:'Uzbekistan', fromCity:'Osh',     toCity:'Andijan',   border:'Dostuk Border Crossing',   time:'~4–5 hrs by road' },
      { toCode:'tj', toFlag:'🇹🇯', toName:'Tajikistan', fromCity:'Osh',     toCity:'Khodjand',  border:'Karameik Border Crossing', time:'~5–6 hrs by road' },
    ],
  },
  kz: {
    navFlag: '🇰🇿', navLabel: 'Kazakhstan',
    heroLabel: 'New Destination · Now Booking',
    heroTitle: 'Discover the <em>Soul</em><br>of Kazakhstan',
    heroSub: 'Private tours across the vast Great Steppe — from cosmopolitan Almaty to the Grand Canyon of Central Asia. Crafted by the same team behind 3,000+ happy travellers.',
    heroFeatures: [
      { icon:'🏜️', label:'Charyn Canyon',         sub:'Trekking · Red Rocks · Photography' },
      { icon:'🌆', label:'Almaty City',            sub:'Markets · Culture · Architecture'   },
      { icon:'🏔️', label:'Kolsai & Kaindy Lakes', sub:'Alpine Trek · Sunken Forest'         },
      { icon:'🦅', label:'Kazakh Eagle Hunting',   sub:'4,000-Year-Old Tradition · UNESCO'  },
      { icon:'🏛️', label:'Ancient Turkestan',      sub:'Silk Road · UNESCO Mausoleum'       },
    ],
    stats: ['8+','500+','8','NEW'],
    statLabels: ['Years of Experience','Happy Clients','Kazakhstan Tours','Destination 2024'],
    badgeNum: '2024', badgeText: 'Launched',
    aboutTitle: 'Expanding to the <em>Great Steppe</em>',
    aboutLead1: 'Building on 8 years of award-winning tours in Kyrgyzstan, Nomadic Nations now brings the same passion and quality to Kazakhstan — Central Asia\'s largest and most diverse country.',
    aboutLead2: 'From the ultramodern skyline of Almaty to the ancient Silk Road city of Turkestan and the breathtaking Charyn Canyon — Kazakhstan is a destination of epic contrasts waiting to be explored.',
    toursLabel: 'Kazakhstan Collection',
    toursTitle: '8 Kazakhstan <em>Experiences</em>',
    toursLead: 'Handcrafted private tours across Kazakhstan — from half-day city walks in Almaty to multi-day canyon and mountain adventures.',
    crossRoutes: [
      { toCode:'kg', toFlag:'🇰🇬', toName:'Kyrgyzstan', fromCity:'Almaty',    toCity:'Bishkek',  border:'Korday Border Crossing',       time:'~3–4 hrs by road' },
      { toCode:'uz', toFlag:'🇺🇿', toName:'Uzbekistan', fromCity:'Shymkent',  toCity:'Tashkent', border:'Zhybek Zholy Border Crossing', time:'~2 hrs by road'   },
    ],
  },
  uz: {
    navFlag: '🇺🇿', navLabel: 'Uzbekistan',
    heroLabel: 'UNESCO Silk Road · Now Booking',
    heroTitle: 'Discover the <em>Silk Road</em><br>of Uzbekistan',
    heroSub: 'Step into the world of Tamerlane and the Silk Road — private tours across Tashkent, Samarkand, Bukhara and Khiva. Four UNESCO cities, one extraordinary journey.',
    heroFeatures: [
      { icon:'🏛️', label:'Registan, Samarkand',  sub:'UNESCO · Silk Road Masterpiece'      },
      { icon:'🌙', label:'Bukhara Old City',      sub:'Medieval Streets · Ancient Bazaars'  },
      { icon:'🏰', label:'Khiva Ichan Kala',      sub:'Walled City · Living Museum'         },
      { icon:'🕌', label:'Tashkent Bazaars',      sub:'Chorsu Market · Metro Art'           },
      { icon:'🗺️', label:'Silk Road Route',       sub:'Tashkent → Samarkand → Bukhara'     },
    ],
    stats: ['8+','200+','6','UNESCO'],
    statLabels: ['Years of Experience','Happy Clients','Uzbekistan Tours','Silk Road Cities'],
    badgeNum: '2025', badgeText: 'Launched',
    aboutTitle: 'Unveiling the <em>Silk Road Legacy</em>',
    aboutLead1: 'Nomadic Nations now extends the same award-winning private tour experience into Uzbekistan — the heart of the ancient Silk Road and home to four UNESCO World Heritage cities.',
    aboutLead2: 'From the legendary Registan of Samarkand to the walled oasis of Khiva, our local guides reveal centuries of Islamic architecture, trade history, and living traditions that have shaped Central Asian civilisation.',
    toursLabel: 'Uzbekistan Collection',
    toursTitle: '6 Silk Road <em>Experiences</em>',
    toursLead: 'Private tours across Uzbekistan\'s UNESCO cities — from half-day city walks to the complete four-city Silk Road journey.',
    crossRoutes: [
      { toCode:'kg', toFlag:'🇰🇬', toName:'Kyrgyzstan', fromCity:'Andijan',   toCity:'Osh',       border:'Dostuk Border Crossing',       time:'~4–5 hrs by road' },
      { toCode:'tj', toFlag:'🇹🇯', toName:'Tajikistan', fromCity:'Samarkand', toCity:'Dushanbe',  border:'Oybek Border Crossing',        time:'~4–5 hrs by road' },
      { toCode:'kz', toFlag:'🇰🇿', toName:'Kazakhstan', fromCity:'Tashkent',  toCity:'Shymkent',  border:'Zhybek Zholy Border Crossing', time:'~2 hrs by road'   },
    ],
  },
  tj: {
    navFlag: '🇹🇯', navLabel: 'Tajikistan',
    heroLabel: 'Roof of the World · Now Booking',
    heroTitle: 'Discover the <em>Pamir</em><br>of Tajikistan',
    heroSub: 'Venture to the world\'s second-highest mountain range — private tours across the Pamir Highway, Wakhan Valley and the Fann Mountains. Raw, remote and unforgettable.',
    heroFeatures: [
      { icon:'🛣️', label:'Pamir Highway M41',     sub:'Highest Roads · Epic Landscapes'     },
      { icon:'🏔️', label:'Fann Mountains',         sub:'Alpine Lakes · Trekking · Wildlife'  },
      { icon:'🏕️', label:'Wakhan Valley',           sub:'Ancient Corridor · Fortress Ruins'  },
      { icon:'🏙️', label:'Dushanbe City',           sub:'Capital · Bazaars · Culture'         },
      { icon:'💧', label:'Iskanderkul Lake',        sub:'Alexander\'s Lake · Waterfalls'      },
    ],
    stats: ['8+','100+','5','PAMIR'],
    statLabels: ['Years of Experience','Happy Clients','Tajikistan Tours','Roof of the World'],
    badgeNum: '2025', badgeText: 'Launched',
    aboutTitle: 'Into the <em>Roof of the World</em>',
    aboutLead1: 'Nomadic Nations brings its expertise in high-altitude adventures to Tajikistan — one of the most remote and spectacular destinations in Central Asia, home to the Pamir mountain range.',
    aboutLead2: 'Drive the legendary Pamir Highway, trek to turquoise alpine lakes in the Fann Mountains, and explore the ancient Wakhan Corridor — a landscape of breathtaking raw beauty unchanged for centuries.',
    toursLabel: 'Tajikistan Collection',
    toursTitle: '5 Pamir <em>Expeditions</em>',
    toursLead: 'Private tours across Tajikistan\'s wildest landscapes — from Dushanbe city walks to multi-day Pamir Highway adventures.',
    crossRoutes: [
      { toCode:'uz', toFlag:'🇺🇿', toName:'Uzbekistan', fromCity:'Dushanbe',  toCity:'Samarkand', border:'Oybek Border Crossing',    time:'~4–5 hrs by road' },
      { toCode:'kg', toFlag:'🇰🇬', toName:'Kyrgyzstan', fromCity:'Khodjand',  toCity:'Osh',       border:'Karameik Border Crossing', time:'~5–6 hrs by road' },
    ],
  },
};

// ── Rebuild hero features panel ─────────────────────────────
function rebuildHeroFeatures(features) {
  const wrap = document.querySelector('.hero-features');
  if (!wrap) return;
  wrap.innerHTML = `
    <div class="hero-features-head">
      <span class="hero-features-head-line"></span>
      <span>Top Experiences</span>
      <span class="hero-features-head-line"></span>
    </div>
    ${features.map(f => `
    <a href="#tours" class="hero-feature">
      <span class="hero-feature-icon">${f.icon}</span>
      <div class="hero-feature-body">
        <div class="hero-feature-label">${f.label}</div>
        <div class="hero-feature-sub">${f.sub}</div>
      </div>
      <span class="hero-feature-arrow">›</span>
    </a>`).join('')}
  `;
}

// ── Build cross-border routes section ───────────────────────
function updateCrossBorderSection(country) {
  const d = COUNTRY_DATA[country] || COUNTRY_DATA.kg;
  const container = document.getElementById('crossBorderRoutes');
  if (!container || !d.crossRoutes || !d.crossRoutes.length) return;

  container.innerHTML = d.crossRoutes.map(route => `
    <div class="cross-route-card">
      <div class="cross-route-flags">
        <span class="cross-route-flag">${d.navFlag}</span>
        <div class="cross-route-connector">
          <div class="cross-route-connector-line"></div>
          <span class="cross-route-connector-arrow">→</span>
        </div>
        <span class="cross-route-flag">${route.toFlag}</span>
      </div>
      <div>
        <div class="cross-route-title">${d.navLabel} → ${route.toName}</div>
        <div class="cross-route-detail">${route.fromCity} → ${route.toCity}</div>
        <div class="cross-route-border">🛂 ${route.border} · ${route.time}</div>
      </div>
      <button class="cross-route-btn" data-target="${route.toCode}">
        Explore ${route.toName} Tours →
      </button>
    </div>
  `).join('');

  container.querySelectorAll('.cross-route-btn[data-target]').forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = document.querySelector(`.hero-ctab[data-hct="${btn.dataset.target}"]`);
      if (tab) tab.click();
      document.getElementById('tours')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

// ── Apply country to entire page ─────────────────────────────
function applyCountry(country) {
  const d = COUNTRY_DATA[country] || COUNTRY_DATA.kg;

  // Nav
  const flagEl  = document.getElementById('navCountryFlag');
  const labelEl = document.getElementById('navCountryLabel');
  if (flagEl)  flagEl.textContent  = d.navFlag;
  if (labelEl) labelEl.textContent = d.navLabel;

  // Sync hero tabs
  document.querySelectorAll('.hero-ctab').forEach(t =>
    t.classList.toggle('active', t.dataset.hct === country)
  );

  // Hero features panel
  rebuildHeroFeatures(d.heroFeatures);

  // Stats
  [0,1,2,3].forEach(i => {
    const numEl = document.getElementById('statNum' + i);
    const lblEl = document.getElementById('statLbl' + i);
    if (numEl) { numEl.textContent = d.stats[i]; numEl.dataset.count = d.stats[i]; }
    if (lblEl) lblEl.textContent = d.statLabels[i];
  });

  // About
  const badgeNum   = document.getElementById('aboutBadgeNum');
  const badgeText  = document.getElementById('aboutBadgeText');
  const aboutTitle = document.getElementById('aboutTitle');
  const lead1      = document.getElementById('aboutLead1');
  const lead2      = document.getElementById('aboutLead2');
  if (badgeNum)   badgeNum.textContent   = d.badgeNum;
  if (badgeText)  badgeText.textContent  = d.badgeText;
  if (aboutTitle) aboutTitle.innerHTML   = d.aboutTitle;
  if (lead1)      lead1.textContent      = d.aboutLead1;
  if (lead2)      lead2.textContent      = d.aboutLead2;

  // Tours section header
  const toursLabelEl = document.querySelector('#tours .section-head .label');
  const toursTitleEl = document.querySelector('#tours .section-head .h2');
  const toursLeadEl  = document.querySelector('#tours .section-head .lead');
  if (toursLabelEl) toursLabelEl.textContent = d.toursLabel;
  if (toursTitleEl) toursTitleEl.innerHTML   = d.toursTitle;
  if (toursLeadEl)  toursLeadEl.textContent  = d.toursLead;

  // Tour grids: show active country only, hide rest
  const grids = {
    kg: { filter: 'filterBar',   grid: 'toursGrid'   },
    kz: { filter: 'filterBarKZ', grid: 'toursGridKZ' },
    uz: { filter: 'filterBarUZ', grid: 'toursGridUZ' },
    tj: { filter: 'filterBarTJ', grid: 'toursGridTJ' },
  };
  const sectionHead  = document.querySelector('#tours .section-head');
  const crossBorder  = document.getElementById('crossBorderSection');
  const activeFilter = document.getElementById(grids[country]?.filter);
  const activeGrid   = document.getElementById(grids[country]?.grid);

  Object.entries(grids).forEach(([code, ids]) => {
    const f = document.getElementById(ids.filter);
    const g = document.getElementById(ids.grid);
    if (f) f.style.display = code === country ? '' : 'none';
    if (g) g.style.display = code === country ? '' : 'none';
  });

  if (sectionHead && activeFilter && activeGrid && crossBorder) {
    sectionHead.after(activeFilter, activeGrid, crossBorder);
  }

  // Cross-border routes
  updateCrossBorderSection(country);
}

// ── KZ tour filter ──────────────────────────────────────────
function initFilterKZ() {
  const btns     = document.querySelectorAll('.filter-btn-kz');
  const wrappers = document.querySelectorAll('#toursGridKZ > [data-cat-kz]');
  if (!btns.length) return;
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filterKz;
      wrappers.forEach(w => {
        w.style.display = cat === 'all' || w.dataset.catKz === cat ? '' : 'none';
      });
    });
  });
}

// ── UZ tour filter ──────────────────────────────────────────
function initFilterUZ() {
  const btns     = document.querySelectorAll('.filter-btn-uz');
  const wrappers = document.querySelectorAll('#toursGridUZ > [data-cat-uz]');
  if (!btns.length) return;
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filterUz;
      wrappers.forEach(w => {
        w.style.display = cat === 'all' || w.dataset.catUz === cat ? '' : 'none';
      });
    });
  });
}

// ── TJ tour filter ──────────────────────────────────────────
function initFilterTJ() {
  const btns     = document.querySelectorAll('.filter-btn-tj');
  const wrappers = document.querySelectorAll('#toursGridTJ > [data-cat-tj]');
  if (!btns.length) return;
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filterTj;
      wrappers.forEach(w => {
        w.style.display = cat === 'all' || w.dataset.catTj === cat ? '' : 'none';
      });
    });
  });
}

// ── Hero country tabs ────────────────────────────────────────
function initHeroCountryTabs() {
  const tabs = document.querySelectorAll('.hero-ctab');
  if (!tabs.length) return;

  function selectTab(country) {
    if (!COUNTRY_DATA[country]) country = 'kg';
    tabs.forEach(t => t.classList.toggle('active', t.dataset.hct === country));
    sessionStorage.setItem('nc_country', country);
    applyCountry(country);
  }

  tabs.forEach(tab => tab.addEventListener('click', () => {
    selectTab(tab.dataset.hct);
    document.querySelector('#tours')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }));

  // Restore last choice
  const saved = sessionStorage.getItem('nc_country');
  if (saved && COUNTRY_DATA[saved] && saved !== 'kg') selectTab(saved);
  else applyCountry('kg');
}

// ── Init all ────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initHeroCountryTabs();
  initFilter();
  initFilterKZ();
  initFilterUZ();
  initFilterTJ();
  initNav();
  initMobileMenu();
  initReveal();
  initCounters();
  initCardTilt();
  initHeroSearch();
  initSmoothScroll();
  initHeroParallax();
  initCursorGlow();
});
