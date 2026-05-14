# DatkaTravel — Project Reference

## Overview

Static multi-page website for **Nomadic Nations** (brand name), a Central Asia tour company founded in 2016. No build tool, no framework — plain HTML, CSS, and vanilla JavaScript. Two parallel site versions exist:

| Version | Entry point | Design system |
|---------|-------------|---------------|
| **Original** | `index_last.html` | `style.css` + `tour-components/style.css` |
| **Luxury (active)** | `index.html` | `assets/css/luxury.css` + `assets/js/luxury.js` |

The luxury version is the primary site. All 21 individual Kyrgyzstan tour pages live in `tours_pages/`. Kazakhstan, Uzbekistan, and Tajikistan tours are card-only in `index.html` (no separate pages — they link to `#contact`).

Served via VS Code Live Server (port 5500) or `npx serve . --listen 5500`.

---

## Project Structure

```
DatkaTravel-main/
│
├── index_last.html              # Original landing page (legacy)
├── index.html                   # Luxury main page (active)
├── style.css                    # Styles for original index_last.html only
├── env.js                       # BASE_URL config for original index_last.html
├── gen_tours.py                 # Python generator — created tours 5–21
│
├── assets/
│   ├── css/luxury.css           # ~2 250 lines — white-theme design system
│   └── js/luxury.js             # ~520 lines — shared JS + multi-country logic
│
├── tours_pages/
│   └── tour-1.html … tour-21.html   # 21 standalone Kyrgyzstan tour pages
│
├── components/                  # Original site only
│   ├── header.html
│   └── footer.html
│
├── script/                      # Original site only
│   ├── load-header-footer.js
│   ├── script1.js
│   ├── script2.js
│   └── tours.list.js
│
├── img/
│   ├── png/                     # Tour icons 1–21.png; UI icons 22–29.png
│   ├── svg/                     # Social icons
│   ├── imgonline-com-ua-Com.jpg # Hero slide 1 background
│   └── 0x0.jpg                  # Hero slide 2 background
│
└── tour-components/             # Original site only
    ├── style.css
    ├── script/script.js
    └── img/
        ├── jpg/1–12.jpg         # Bishkek City Tour photos (slide 3 bg = 1.jpg)
        └── png/1.png
```

---

## Multi-Country Architecture

The site supports **4 countries**: Kyrgyzstan (kg), Kazakhstan (kz), Uzbekistan (uz), Tajikistan (tj).

### Country Switching Flow
1. User clicks a **hero tab** (`[data-hct="kg|kz|uz|tj"]`) or a **cross-border route button**
2. `applyCountry(country)` runs — updates nav, hero features, stats, about section, tours section header
3. Only the active country's filter bar + tour grid are shown; all others `display:none`
4. DOM order: `sectionHead → activeFilter → activeGrid → crossBorderSection`
5. `updateCrossBorderSection(country)` populates `#crossBorderRoutes` with route cards for that country's neighbours
6. Country choice is persisted in `sessionStorage` key `nc_country`

### Tour Grids per Country
| Country | Filter bar ID | Grid ID | Cards | Filter attribute |
|---------|--------------|---------|-------|-----------------|
| Kyrgyzstan | `filterBar` | `toursGrid` | 21 | `data-cat` |
| Kazakhstan | `filterBarKZ` | `toursGridKZ` | 8 | `data-cat-kz` |
| Uzbekistan | `filterBarUZ` | `toursGridUZ` | 6 | `data-cat-uz` |
| Tajikistan | `filterBarTJ` | `toursGridTJ` | 5 | `data-cat-tj` |

KG tour cards link to real `tours_pages/tour-N.html`. All other country cards link to `#contact`.

### Cross-Border Routes Section (`#crossBorderSection`)
Appears below the active country's tour grid. White background, gold top-border accent. Contains dynamically generated `.cross-route-card` elements showing:
- From/to country flags with animated connector
- City-to-city route and border crossing name
- Button that triggers `applyCountry()` for the destination country

Border routes defined in `COUNTRY_DATA[country].crossRoutes`:
| Active country | Neighbours shown |
|---------------|-----------------|
| KG | → KZ (Korday), → UZ (Dostuk, Osh→Andijan), → TJ (Karameik, Osh→Khodjand) |
| KZ | → KG (Korday), → UZ (Zhybek Zholy) |
| UZ | → KG (Dostuk), → TJ (Oybek, Samarkand→Dushanbe), → KZ (Zhybek Zholy) |
| TJ | → UZ (Oybek), → KG (Karameik) |

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

### Hero — Fullscreen Photo Slideshow + Country Tabs

| Element | Description |
|---------|-------------|
| `.hero-slides` | Container for 3 absolutely-positioned slide divs |
| `.hero-slide` | Each slide: `background-image` set inline, CSS `@keyframes heroSlide` fades + Ken Burns zoom |
| `.hero-overlay` | Dual gradient: left dark (for text), bottom dark (for strip) |
| `.hero-country-tabs` | 4 pill buttons (KG/KZ/UZ/TJ) — dark glass effect, `backdrop-filter: blur` |
| `.hero-ctab.active` | Gold fill (`rgba(184,148,62,0.75)`) + gold border + glow |
| `.hero-ctab` (inactive) | `rgba(0,0,0,0.38)` bg + white text `0.82` opacity — readable on any photo |
| `.hero-features` | Right panel: 5 glass pill cards rebuilt per country; hidden on ≤ 1100px |

**Slide images** (paths relative to `index.html` at root):
1. `img/imgonline-com-ua-Com.jpg`
2. `img/0x0.jpg`
3. `tour-components/img/jpg/1.jpg`

**Slideshow timing**: each slide visible 6s, crossfade 0.5s, total cycle 18s.

### Key CSS Components

| Class | Description |
|-------|-------------|
| `.lux-nav` | Fixed nav; `.scrolled` at `scrollY > 60` |
| `.mobile-menu` | Full-screen dark overlay menu; `.open` toggles it |
| `.hero` | Full-viewport dark hero (background `#06060f`) |
| `.stats-bar` | Light gray (`--bg-2`) band with animated counters |
| `.tour-card` | White card, `box-shadow`, gold border on hover; 3D tilt via JS |
| `.tour-card-img` | Dark gradient bg — keeps icons visible |
| `.kz-img-*` | KZ card gradient backgrounds (city/food/canyon/lake/adventure/history) |
| `.kz-card-icon` | Large emoji icon centered in KZ card image area |
| `.uz-img-*` | UZ card gradient backgrounds (city/history/nature/multi) |
| `.uz-card-icon` | Large emoji icon centered in UZ card image area |
| `.tj-img-*` | TJ card gradient backgrounds (city/nature/adventure/multi) |
| `.tj-card-icon` | Large emoji icon centered in TJ card image area |
| `.filter-btn-kz/.filter-btn-uz/.filter-btn-tj` | Country-specific filter buttons; `.active` = gold |
| `.cross-border-section` | White bg, gold top border (3px), `box-shadow` — appears after active tour grid |
| `.cross-route-card` | `--bg-2` bg, gold border on hover, `translateY(-3px)` lift |
| `.reveal` / `.reveal-left` / `.reveal-right` | Scroll-reveal via IntersectionObserver → `.visible` |
| `.tour-hero` | Full-viewport dark hero on tour pages |
| `.lux-footer` | Dark `#0a0a18` footer |

### Responsive Breakpoints
| Breakpoint | Changes |
|-----------|---------|
| `≤ 1100px` | 2-col tour grid, hide `.hero-features` panel |
| `≤ 768px` | Show burger, single-col layouts, cross-border routes stack to 1 col |
| `≤ 480px` | Stack buttons, center hero text |

---

## Image Path Convention — CRITICAL

Tour card images use CSS custom properties: `style="--img:url('...')"`.

**Chrome resolves `url()` in custom properties relative to the CSS file**, not the HTML file.  
`luxury.css` is at `assets/css/` — so all `url()` paths must be **relative to `assets/css/`**.

| Location of HTML file | Correct `url()` path |
|----------------------|---------------------|
| `index.html` (root) | `url('../../img/png/N.png')` |
| `tours_pages/tour-N.html` | `url('../../img/png/N.png')` |

KZ/UZ/TJ cards use emoji icons + CSS gradient backgrounds instead of PNG images — no `--img` property needed on these cards.

Regular `<img src>` attributes are resolved relative to the HTML file and use `../img/png/N.png` for tour pages — this is correct and should NOT be changed.

---

## Luxury JavaScript (`assets/js/luxury.js`)

### Core Functions
| Function | Trigger | What it does |
|----------|---------|--------------|
| `initNav()` | scroll | `.scrolled` on `.lux-nav` when `scrollY > 60` |
| `initMobileMenu()` | click `.burger` | Toggles `.open`; animates spans; locks `body.overflow` |
| `initReveal()` | IntersectionObserver (0.12) | `.visible` on `.reveal*` |
| `initCounters()` | IntersectionObserver (0.3) | Count-up animation for `.stat-num[data-count]` |
| `initCardTilt()` | mousemove / mouseleave | 3D `rotateY/rotateX` tilt on `.tour-card` |
| `initFilter()` | click `.filter-btn` | Show/hide `[data-cat]` wrappers (KG tours) |
| `initFilterKZ()` | click `.filter-btn-kz` | Show/hide `[data-cat-kz]` wrappers |
| `initFilterUZ()` | click `.filter-btn-uz` | Show/hide `[data-cat-uz]` wrappers |
| `initFilterTJ()` | click `.filter-btn-tj` | Show/hide `[data-cat-tj]` wrappers |
| `initHeroSearch()` | click `#heroSearchBtn` | Scrolls to `#tours`, clicks matching filter button |
| `initSmoothScroll()` | click `a[href^="#"]` | `scrollIntoView({ behavior:'smooth' })` |
| `initCursorGlow()` | mousemove (desktop) | 300px gold radial glow follows cursor |

### Multi-Country Functions
| Function | What it does |
|----------|--------------|
| `COUNTRY_DATA` | Object with `kg/kz/uz/tj` keys — holds hero text, stats, about text, tour section labels, `crossRoutes` array |
| `rebuildHeroFeatures(features)` | Replaces `.hero-features` innerHTML with per-country destination pills |
| `updateCrossBorderSection(country)` | Renders `.cross-route-card` elements in `#crossBorderRoutes`; binds click → `applyCountry` |
| `applyCountry(country)` | Master function — updates nav, hero features, stats, about, tours header, shows/hides grids, calls `updateCrossBorderSection` |
| `initHeroCountryTabs()` | Binds `.hero-ctab` clicks; restores from `sessionStorage`; calls `applyCountry('kg')` on first load |

---

## `index.html` — Sections

| Anchor | Section | Notes |
|--------|---------|-------|
| (hero) | Fullscreen Slideshow Hero | 3-photo slideshow + country tabs (KG/KZ/UZ/TJ) + right features panel |
| (hero-search) | Search Bar | Destination / Duration / Type dropdowns → scroll + filter |
| (stats) | Stats Bar | 4 counters — updated per country via `applyCountry` |
| `#about` | About Section | 2-col: photos / text — updated per country via `applyCountry` |
| `#tours` | All Tours | Active country filter bar + tour grid + cross-border section |
| `#why` | Why Book With Us | 4 benefit cards |
| `#contact` | Book / Contact | Inquiry form + contact details |

### Kyrgyzstan Tour Filter Categories
`all` · `city` · `nature` · `history` · `adventure` · `lake`

### Kazakhstan Tour Filter Categories (`data-filter-kz`)
`all` · `city` · `nature` · `adventure` · `history`

### Uzbekistan Tour Filter Categories (`data-filter-uz`)
`all` · `city` · `history` · `nature` · `multi`

### Tajikistan Tour Filter Categories (`data-filter-tj`)
`all` · `city` · `nature` · `adventure` · `multi`

---

## Tour Catalogues

### Kyrgyzstan (21 tours — `tours_pages/tour-N.html`)
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

### Kazakhstan (8 tours — cards in `index.html`, link to `#contact`)
| # | Title | Category | From |
|---|-------|----------|------|
| 1 | Almaty City Tour: Soviet Legacy to Modern Metropolis | City | $35 |
| 2 | Almaty Food & Green Bazaar Tour | City/Food | $40 |
| 3 | Charyn Canyon: Grand Canyon of Central Asia | Nature | $55 |
| 4 | Big Almaty Lake & Ili-Alatau Mountains | Nature | $45 |
| 5 | Kolsai Lakes & Kaindy Sunken Forest | Nature | $65 |
| 6 | Kazakh Eagle Hunting Tradition | Adventure | $65 |
| 7 | Ancient Turkestan & Silk Road 2-Day Tour | History | $180 |
| 8 | Almaty & Charyn Canyon 2-Day Explorer | Nature+City | $160 |

### Uzbekistan (6 tours — cards in `index.html`, link to `#contact`)
| # | Title | Category | From |
|---|-------|----------|------|
| 1 | Tashkent City Tour: Ancient Bazaars to Modern Capital | City | $35 |
| 2 | Samarkand: Registan & the Silk Road Masterpieces | History | $45 |
| 3 | Bukhara: The Holiest City of Central Asia | History | $40 |
| 4 | Khiva: The Living Museum of Central Asia | History | $50 |
| 5 | 2 Days Samarkand & Bukhara Silk Road Express | Multi | $160 |
| 6 | 4 Days Uzbekistan Silk Road: Tashkent, Samarkand, Bukhara & Khiva | Multi | $320 |

### Tajikistan (5 tours — cards in `index.html`, link to `#contact`)
| # | Title | Category | From |
|---|-------|----------|------|
| 1 | Dushanbe City Tour: Capital of the Roof of the World | City | $35 |
| 2 | Iskanderkul Lake: Jewel of the Fann Mountains | Nature | $65 |
| 3 | Pamir Highway: Drive the Roof of the World | Adventure | $80 |
| 4 | Wakhan Valley 2-Day Expedition | Multi | $180 |
| 5 | 3 Days Pamir Adventure: Khorog, Wakhan & High Lakes | Multi | $280 |

---

## Individual Tour Pages (`tours_pages/`) — Kyrgyzstan only

### Shared Page Structure
1. `.lux-nav` → links to `../index.html`
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

---

## `gen_tours.py`

Python script at the project root. Generated `tours_pages/tour-5.html` through `tour-21.html`. Run with `py gen_tours.py` (uses Python 3). Re-running overwrites those files. Output path is hardcoded as an absolute path — update `BASE` if the project is moved.

---

## Images Reference

### `img/png/` — Tour thumbnails & UI icons
| Range | Usage |
|-------|-------|
| 1–21.png | KG tour icons — used in card `--img` and tour-hero `<img src>` |
| 22–24.png | "How to Buy" step icons (original index only) |
| 25–28.png | "Why Book" benefit icons |
| 29.png | LinkedIn logo (original header) |

KZ/UZ/TJ cards use **emoji icons** (`.kz-card-icon`, `.uz-card-icon`, `.tj-card-icon`) instead of PNG files.

### `img/` — Full photos (used in luxury hero slideshow)
| File | Usage |
|------|-------|
| `imgonline-com-ua-Com.jpg` | Hero slide 1 |
| `0x0.jpg` | Hero slide 2 |
| `tour-components/img/jpg/1.jpg` | Hero slide 3 |

### `img/svg/` — Social icons
`4.svg` = Facebook · `6.svg` = Instagram · `7.svg` = Twitter · `1-3.svg` = footer

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
| 4 | `index_last.html` | About Us images from external tildacdn.pro CDN |
| 5 | All forms | No backend handler — submit does nothing |
| 6 | `initHeroParallax()` | Targets `.hero-bg` which no longer exists in slideshow hero — no-op |
| 7 | KZ/UZ/TJ tour cards | No dedicated detail pages — all link to `#contact` |
