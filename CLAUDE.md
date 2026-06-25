# Cloud Hak v2 — Full Agency Website Build

You are building the complete website for Cloud Hak Ltd, an AI & automation agency for local businesses. This is a static HTML/CSS/JS site — no frameworks, no WordPress, no build tools. Every page must be a single self-contained HTML file with inline `<style>` and `<script>` where needed.

## Brand Identity
- **Company:** Cloud Hak Ltd (AI & Automation Agency for Local Businesses)
- **Tagline:** "We Build, Automate & Grow Local Businesses"
- **Logo:** `assets/logo.png` (blue cloud + "CLOUD HAK" text, 500×160px, transparent PNG)
- **Address:** 117 Holmes Avenue, Hove, East Sussex BN3 7LF, UK
- **Phone:** 07800 920042
- **Email:** info@cloud-hak.com
- **Website:** cloud-hak.com

## Design System

### Colours
```
--dark-bg: #0a0f1c          /* Deep navy — primary dark background */
--dark-bg-light: #111827    /* Slightly lighter dark for cards/sections */
--dark-bg-lighter: #1e293b  /* Even lighter dark for hover states */
--accent-blue: #4f6ef7      /* Electric blue — primary accent, CTAs */
--accent-teal: #3bb6b3      /* Teal — secondary accent, from logo */
--accent-green: #22c55e     /* Success green — results, positive stats */
--accent-amber: #f59e0b     /* Warning amber — highlights, badges */
--text-white: #f8fafc       /* Primary text on dark */
--text-light: #94a3b8       /* Secondary text on dark */
--text-dark: #0f172a        /* Primary text on light */
--text-muted: #64748b       /* Muted text on light */
--light-bg: #f8fafc         /* Light section backgrounds */
--light-card: #ffffff       /* White cards */
--border-dark: #1e293b      /* Borders on dark */
--border-light: #e2e8f0     /* Borders on light */
```

### Typography
- **Font:** Inter (Google Fonts: `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap`)
- **H1:** 48px / 700 weight / line-height 1.1 / letter-spacing -0.02em
- **H2:** 36px / 700 weight / line-height 1.2
- **H3:** 24px / 600 weight / line-height 1.3
- **H4:** 18px / 600 weight / line-height 1.4
- **Body:** 16px / 400 weight / line-height 1.6
- **Small:** 14px / 400 weight / line-height 1.5
- **Responsive:** Scale down 15-20% on mobile (below 768px)

### Spacing
- Section padding: 80px vertical (48px mobile)
- Container max-width: 1200px, centered, 24px horizontal padding
- Card padding: 32px
- Gap between grid items: 24px
- Gap between elements in a section: 16px

### Components
- **Buttons:**
  - Primary: `background: var(--accent-blue); color: white; border-radius: 8px; padding: 14px 32px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.2s;`
  - Primary hover: `background: #4058e0; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(79,110,247,0.3);`
  - Secondary: `background: transparent; border: 1px solid var(--accent-blue); color: var(--accent-blue); border-radius: 8px; padding: 14px 32px; font-weight: 600;`
  - Ghost: `background: rgba(255,255,255,0.1); color: white; border-radius: 8px; padding: 14px 32px; font-weight: 600; border: 1px solid rgba(255,255,255,0.15);`

- **Cards:**
  - Dark bg: `background: var(--dark-bg-light); border: 1px solid var(--border-dark); border-radius: 12px; padding: 32px;`
  - Light bg: `background: var(--light-card); border: 1px solid var(--border-light); border-radius: 12px; padding: 32px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);`

- **Navigation:**
  - Fixed top, `background: rgba(10,15,28,0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border-dark); height: 72px; z-index: 1000;`
  - Logo left, nav links center, CTA button right
  - Mobile: hamburger menu (right side), full-screen overlay nav with SOLID BLACK background (#000)

- **Footer:**
  - Dark background (`var(--dark-bg)`)
  - 4-column grid: Services | Company | Contact | Legal
  - Bottom bar: copyright + social links

### Animations
- Subtle entrance animations on scroll (fade up, 0.6s ease)
- Button hover micro-interactions
- Smooth scroll for anchor links
- NO heavy animations, NO parallax, NO auto-playing video backgrounds

## Files to Create

### 1. `index.html` — Homepage
**Title:** Cloud Hak — AI & Automation Agency for Local Businesses
**Meta description:** We build websites, set up CRM systems, deploy AI chatbots, voice agents, and SEO for local businesses. Everything you need to grow — done for you.

**Sections (in order):**

**A. Hero Section (dark bg)**
- Nav bar (fixed, logo left, links: Services, Pricing, About, Work | "Book Consultation" CTA button)
- Main heading: "We Build, Automate & Grow Your Business — While You Focus on What You Do Best"
- Subheading: "Websites, CRM, AI Chatbots, Voice Agents & SEO — all managed for you by our team of humans + AI"
- Two CTAs: "Book Free Consultation" (primary) + "See Our Work" (ghost/secondary)
- Subtle gradient background or abstract geometric pattern (CSS only, no images)
- Below fold: trust bar with text "Trusted by local businesses across the UK & Europe"

**B. Services Overview (dark bg, slightly lighter)**
- Section heading: "Everything Your Business Needs to Grow"
- Subheading: "Five core services, one team handling it all"
- 5 service cards in a grid (responsive: 3+2 on desktop, stack on mobile):
  1. 🌐 **Professional Websites** — Custom-built, lightning-fast, mobile-first sites that convert visitors into customers
  2. 📊 **Cloud Hak CRM** — Your entire customer management on autopilot. Lead capture, follow-ups, appointments — all automated
  3. 🤖 **AI Chatbots** — 24/7 intelligent chat that answers questions, qualifies leads, and books appointments
  4. 🎙️ **Voice AI Agents** — Never miss a call again. AI answers, routes, and books while you focus on clients
  5. 🔍 **SEO & Local Search** — Get found on Google. Optimised profiles, citations, and on-page SEO that drives foot traffic
- Each card: icon, title, short description, link to service page
- ENTIRE CARD must be clickable (not just the link text)
- Card hover: slight lift, border glow

**C. How It Works (light bg)**
- Section heading: "Simple. Fast. Done For You."
- 3 numbered steps

**D. ROI Calculator (dark bg)** — KEEP SIMPLE
- 4 inputs + Calculate button + result display

**E. Bundle Packages Preview (light bg)**
- 3 pricing cards (Starter £150, Growth £300, Scale £500)

**F. Testimonials (dark bg)**
- 3 testimonial cards with real-sounding quotes

**G. Case Study Spotlight (light bg)**
- Airway Clinic Stockholm feature

**H. Final CTA (dark bg)**

**I. Footer**

### 2. `services/index.html` — Services Hub
### 3. `services/websites/index.html`
### 4. `services/crm/index.html`
### 5. `services/chatbots/index.html`
### 6. `services/voice-ai/index.html`
### 7. `services/seo/index.html`
### 8. `pricing/index.html`
### 9. `about/index.html`
### 10. `work/index.html`
### 11. `contact/index.html`
### 12. `privacy/index.html`
### 13. `terms/index.html`
### 14. `404.html`

## SEO Requirements (EVERY PAGE)
- Meta description, robots, canonical, Open Graph, Twitter cards
- JSON-LD: Organization, Service, BreadcrumbList, FAQPage, LocalBusiness

## AEO Requirements
- Clear H1 answering a question
- FAQ sections with concise answers
- Structured data for FAQs
- Semantic HTML

## CRITICAL RULES
1. Mobile-first responsive (375px, 768px, 1024px, 1440px)
2. No external JS libraries, no jQuery, no Tailwind, no Bootstrap
3. Accessible — heading hierarchy, alt text, ARIA labels, focus states
4. Consistent nav/footer across ALL pages
5. Relative paths for links and assets
6. No placeholders — real content everywhere
7. British English
8. Currency in GBP (£)
9. Every page standalone with complete head, styles, scripts
10. Mobile menu: SOLID BLACK background (#000), no transparency, no blur
