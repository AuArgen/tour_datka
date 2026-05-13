# DatkaTravel — Project Reference

## Overview

Static multi-page website for **Datka Travel**, a Kyrgyzstan tour company founded in 2016. No build tool, no framework — plain HTML, CSS, and vanilla JavaScript. Two parallel site versions exist:

| Version | Entry point | Design system |
|---------|-------------|---------------|
| **Original** | `index.html` | `style.css` + `tour-components/style.css` |
| **Luxury (active)** | `index_second.html` | `assets/css/luxury.css` + `assets/js/luxury.js` |

The luxury version is the primary site. All 21 individual tour pages live in `tours_pages/`.

Served via VS Code Live Server (port 5500) or `npx serve . --listen 5500`.

---

## Project Structure

```
DatkaTravel-main/
│
├── index.html                        # Original landing page (legacy)
├── index_second.html                 # Luxury main page (active)
├── style.css                         # Styles for original index.html only
├── env.js                            # BASE_URL config for original index.html
├── gen_tours.py                      # Python generator — created tours 5–21
│
├── assets/
│   ├── css/luxury.css                # ~1 500 lines — white-theme design system
│   └── js/luxury.js                  # ~180 lines — shared JS interactions
│
├── tours_pages/
│   └── tour-1.html … tour-21.html   # 21 standalone tour pages
│
├── components/                       # Original site only
│   ├── header.html
│   └── footer.html
│
├── script/                           # Original site only
│   ├── load-header-footer.js
│   ├── script1.js
│   ├── script2.js
│   └── tours.list.js
│
├── img/
│   ├── png/                          # Tour icons 1–21.png; UI icons 22–29.png
│   ├── svg/                          # Social icons
│   ├── imgonline-com-ua-Com.jpg      # Hero slide 1 background
│   └── 0x0.jpg                       # Hero slide 2 background
│
└── tour-components/                  # Original site only
    ├── style.css
    ├── script/script.js
    └── img/
        ├── jpg/1–12.jpg              # Bishkek City Tour photos (slide 3 bg = 1.jpg)
        └── png/1.png
```

---

## Luxury Design System (`assets/css/luxury.css`)

### Theme — White Background

The site uses a **light/white theme** with a dark full-screen hero and dark footer.

```css
:root {
  /* Page backgrounds — white */
  --bg-0: #0d0d1a;       /* hero & footer only */
  --bg-1: #ffffff;        /* main body */
  --bg-2: #f5f5fa;        /* alternate sections, stats bar */
  --bg-card: #ffffff;     /* cards */

  /* Accent */
  --gold: #b8943e;
  --gold-bright: #d4aa52;
  --gold-dim: #8a6c28;
  --gold-glow: rgba(184,148,62,0.13);

  /* Text — dark for white bg */
  --text-1: #0f0f1a;
  --text-2: #383858;
  --text-3: #7878a0;
  --text-4: #b2b2cc;

  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Inter', -apple-system, sans-serif;
}
```

### Nav Behaviour
- Default (floating over dark hero): transparent, white text
- On scroll > 60px (`.scrolled`): white opaque `rgba(255,255,255,0.96)`, dark text, subtle shadow
- Mobile burger visible at ≤ 768px

### Hero — Fullscreen Photo Slideshow

The `index_second.html` hero is a fullscreen auto-playing photo slideshow:

| Element | Description |
|---------|-------------|
| `.hero-slides` | Container for 3 absolutely-positioned slide divs |
| `.hero-slide` | Each slide: `background-image` set inline, CSS `@keyframes heroSlide` fades + Ken Burns zoom |
| `.hero-overlay` | Dual gradient: left dark (for text), bottom dark (for strip) |
| `.hero-inner` | Full-width flex container — left content + right features panel |
| `.hero-content` | Left-aligned text: label, title, sub, actions, progress dots |
| `.hero-dots` | 3 animated gold progress bars synced with slide timing (6s each, 18s cycle) |
| `.hero-features` | Right panel: 5 glass pill cards (destinations); hidden on ≤ 1100px |
| `.hero-orb-1/2` | Floating blurred radial orbs for depth |
| `.hero-scroll` | Animated scroll indicator at bottom center |

**Slide images** (paths relative to `index_second.html` at root):
1. `img/imgonline-com-ua-Com.jpg`
2. `img/0x0.jpg`
3. `tour-components/img/jpg/1.jpg`

**Slideshow timing**: each slide visible 6s, crossfade 0.5s, total cycle 18s.  
`@keyframes heroSlide`: `0% opacity:0 scale:1.08 → 6% opacity:1 → 30% scale:1.0 → 36% opacity:0`

### Key CSS Components

| Class | Description |
|-------|-------------|
| `.lux-nav` | Fixed nav; `.scrolled` at `scrollY > 60` |
| `.mobile-menu` | Full-screen dark overlay menu; `.open` toggles it |
| `.hero` | Full-viewport dark hero (background `#06060f`) |
| `.stats-bar` | Light gray (`--bg-2`) band with animated counters |
| `.tour-card` | White card, `box-shadow`, gold border on hover; 3D tilt via JS |
| `.tour-card-img` | Dark gradient bg `#0e0e22→#141430` — keeps PNG icons visible on white page |
| `.tour-card-img-inner` | `background-image: var(--img)` — CSS custom property set inline in HTML |
| `.filter-btn[data-filter]` | Category filter; `.active` = gold |
| `[data-cat]` on wrappers | Shown/hidden by `initFilter()` JS |
| `.reveal` / `.reveal-left` / `.reveal-right` | Scroll-reveal via IntersectionObserver → `.visible` |
| `.tour-hero` | Full-viewport dark hero on tour pages |
| `.tour-hero-bg` | Inline `<style>` per tour page sets unique radial-gradient |
| `.tour-highlights` | White card with gold `border-top: 3px` |
| `.itinerary` | Numbered timeline; gold vertical line |
| `.incl-card` / `.price-card` | White cards with shadow; `.featured` has gold top bar |
| `.booking-wrap` | Light gray booking form wrapper |
| `.lux-footer` | Dark `#0a0a18` footer |

### Responsive Breakpoints
| Breakpoint | Changes |
|-----------|---------|
| `≤ 1100px` | 2-col tour grid, hide `.hero-features` panel |
| `≤ 768px` | Show burger, single-col layouts, hide `.hero-features` |
| `≤ 480px` | Stack buttons, center hero text |

---

## Image Path Convention — CRITICAL

Tour card images use CSS custom properties: `style="--img:url('...')"`.

**Chrome resolves `url()` in custom properties relative to the CSS file**, not the HTML file.  
`luxury.css` is at `assets/css/` — so all `url()` paths must be **relative to `assets/css/`**.

| Location of HTML file | Correct `url()` path |
|----------------------|---------------------|
| `index_second.html` (root) | `url('../../img/png/N.png')` |
| `tours_pages/tour-N.html` | `url('../../img/png/N.png')` |

Regular `<img src>` attributes are resolved relative to the HTML file and use `../img/png/N.png` for tour pages — this is correct and should NOT be changed.

---

## Luxury JavaScript (`assets/js/luxury.js`)

| Function | Trigger | What it does |
|----------|---------|--------------|
| `initNav()` | scroll | `.scrolled` on `.lux-nav` when `scrollY > 60` |
| `initMobileMenu()` | click `.burger` | Toggles `.open`; animates spans; locks `body.overflow` |
| `initReveal()` | IntersectionObserver (0.12) | `.visible` on `.reveal*` |
| `initCounters()` | IntersectionObserver (0.3) | Count-up animation for `.stat-num[data-count]` |
| `initCardTilt()` | mousemove / mouseleave | 3D `rotateY/rotateX` tilt on `.tour-card` |
| `initFilter()` | click `.filter-btn` | Show/hide `[data-cat]` wrappers |
| `initSmoothScroll()` | click `a[href^="#"]` | `scrollIntoView({ behavior:'smooth' })` |
| `initHeroParallax()` | scroll | `translateY` on `.hero-bg` (legacy, no effect on slideshow) |
| `initCursorGlow()` | mousemove (desktop) | 300px gold radial glow follows cursor |

---

## `index_second.html` — Sections

| Anchor | Section | Notes |
|--------|---------|-------|
| (hero) | Fullscreen Slideshow Hero | 3-photo slideshow + left text + right features |
| (stats) | Stats Bar | 4 counters: `8+` years, `3000+` clients, `21` tours, `#1` TripAdvisor |
| `#about` | About Datka Travel | 2-col: photos with badge / text with feature icons |
| `#tours` | All Tours | Filter bar + 21 tour cards in `[data-cat]` wrappers |
| `#why` | Why Book With Us | 4 benefit cards |
| `#contact` | Book / Contact | Inquiry form + contact details |

### Tour Filter Categories
`all` · `city` · `food` · `culture` · `nature` · `history` · `adventure` · `lake`

---

## Individual Tour Pages (`tours_pages/`)

### Shared Page Structure
1. `.lux-nav` → links to `../index_second.html`
2. `.tour-hero` — dark gradient bg (inline `<style>`) + floating PNG icon (`<img src="../img/png/N.png">`)
3. `.tour-stats` — 5-col stat bar (duration, difficulty, group, language, price)
4. `.tour-about` — 2-col: paragraphs + highlights card
5. `.itinerary` — numbered steps with gold vertical line
6. `.incl-grid` — included / excluded two-col
7. `.prices-grid` — 4 price tiers
8. `.booking-wrap` — booking form (`#book`)
9. `.related-grid` — 3 related tour cards
10. `.lux-footer`

### Hero Gradient Colors per Category
| Category | Key color |
|----------|-----------|
| City / History | Purple-blue `rgba(100,80,200,0.18)` |
| Food / Culture | Warm red `rgba(180,60,40,0.18)` |
| Family dinner | Amber `rgba(200,120,30,0.18)` |
| Nature / Hiking | Forest green `rgba(30,120,60,0.18)` |
| History (Burana) | Sand-amber `rgba(160,110,30,0.18)` |
| Adventure | Orange-red `rgba(180,80,20,0.18)` |
| Song-Kul | Midnight blue `rgba(60,80,180,0.18)` |
| Issyk-Kul | Deep ocean `rgba(20,80,160,0.18)` |

### Tour Catalogue
| # | File | Title | Category | From |
|---|------|-------|----------|------|
| 1 | tour-1.html | Bishkek City Tour: Soviet to Modern | City | $35 |
| 2 | tour-2.html | 4 Hours Private Bishkek Food Tasting Tour | Food | $40 |
| 3 | tour-3.html | Kyrgyz Family Dinner: Meet, Eat, and Talk | Cultural | $35 |
| 4 | tour-4.html | Wildlife Hiking Adventure in Ala Archa NP | Nature/Hiking | $50 |
| 5 | tour-5.html | All in One-Day: Bishkek City Tour & Ala-Archa | City+Nature | $60 |
| 6 | tour-6.html | Full Day in Nature: Chunkurchak & Ala Archa | Nature | $60 |
| 7 | tour-7.html | Medieval Burana Tower and Bishkek City Tour | History | $55 |
| 8 | tour-8.html | Day Trip to Burana Tower and Konorchek Canyons | History+Nature | $60 |
| 9 | tour-9.html | Kol Tor Lake Hike and Burana Tower | Hiking+History | $70 |
| 10 | tour-10.html | Kegeti Waterfall and Burana Tower | Nature+History | $60 |
| 11 | tour-11.html | Horseback Riding in Chon-Kemin Valley | Adventure | $80 |
| 12 | tour-12.html | Nomad Day: Horseback Riding & Archery | Adventure | $90 |
| 13 | tour-13.html | 2 Days in Song-Kul Lake as a Nomad | Song-Kul 2D | $250 |
| 14 | tour-14.html | 2 Days Horseback Riding to Song-Kul Lake | Song-Kul 2D | $280 |
| 15 | tour-15.html | 3 Days Horseback Riding to Song-Kul Lake | Song-Kul 3D | $380 |
| 16 | tour-16.html | Issyk-Kul Lake Day Trip | Issyk-Kul 1D | $70 |
| 17 | tour-17.html | 2 Days Issyk-Kul: Canyons & Beaches | Issyk-Kul 2D | $180 |
| 18 | tour-18.html | 3 Days Issyk-Kul: Beaches, Eagles & Canyons | Issyk-Kul 3D | $280 |
| 19 | tour-19.html | 4 Days Issyk-Kul & Altyn-Arashan Hot Springs | Issyk-Kul 4D | $420 |
| 20 | tour-20.html | 4 Days Song-Kul & Issyk-Kul Combination | Multi-region 4D | $480 |
| 21 | tour-21.html | 5 Days Gems of Issyk-Kul | Issyk-Kul 5D | $580 |

---

## `gen_tours.py`

Python script at the project root. Generated `tours_pages/tour-5.html` through `tour-21.html`. Run with `py gen_tours.py` (uses Python 3). Re-running overwrites those files. Output path is hardcoded as an absolute path — update `BASE` if the project is moved.

---

## Images Reference

### `img/png/` — Tour thumbnails & UI icons
| Range | Usage |
|-------|-------|
| 1–21.png | Tour icons — used in card `--img` and tour-hero `<img src>` |
| 22–24.png | "How to Buy" step icons (original index only) |
| 25–28.png | "Why Book" benefit icons (original index only) |
| 29.png | LinkedIn logo (original header) |

### `img/` — Full photos (used in luxury hero slideshow)
| File | Usage |
|------|-------|
| `imgonline-com-ua-Com.jpg` | Hero slide 1 |
| `0x0.jpg` | Hero slide 2 |
| `tour-components/img/jpg/1.jpg` | Hero slide 3 |

### `img/svg/` — Social icons
`4.svg` = Facebook · `6.svg` = Instagram · `7.svg` = Twitter · `1-3.svg` = footer

### `tour-components/img/jpg/` — Bishkek City Tour photos
`1.jpg` = hero bg · `2–4.jpg` = about grid · `5–12.jpg` = gallery strip

---

## Contact Info
- Phone: +996 556 078880
- Email: datkatravel@gmail.com
- Social: `/DatkaTravel` on Facebook, Instagram, Twitter, LinkedIn

---

## Known Issues

| # | File | Issue |
|---|------|-------|
| 1 | `tour-components/script/script.js` | Commented out in HTML — parallax disabled |
| 2 | `script.js` (original) | `smoothScroll` defined twice; `querySelector('your-button-selector')` throws |
| 3 | `tour-components/style.css` | `body { height: 700vh }` forces excessive page height |
| 4 | `index.html` | About Us images from external tildacdn.pro CDN |
| 5 | All forms | No backend handler — submit does nothing |
| 6 | `initHeroParallax()` | Targets `.hero-bg` which no longer exists in slideshow hero — no-op |
