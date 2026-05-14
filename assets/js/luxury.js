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

// ── Init all ────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initMobileMenu();
  initReveal();
  initCounters();
  initCardTilt();
  initFilter();
  initHeroSearch();
  initSmoothScroll();
  initHeroParallax();
  initCursorGlow();
});
