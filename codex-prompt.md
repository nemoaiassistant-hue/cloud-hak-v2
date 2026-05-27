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
  - Mobile: hamburger menu (right side), full-screen overlay nav

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
- Each card: icon (emoji or CSS shape), title, short description, "Learn More →" link to service page
- Card hover: slight lift (`translateY(-4px)`), border glow (`box-shadow: 0 0 0 1px var(--accent-blue)`)

**C. How It Works (light bg)**
- Section heading: "Simple. Fast. Done For You."
- 3 numbered steps in a horizontal layout:
  1. **Free Consultation** — Tell us about your business. We'll recommend exactly what you need. No hard sell.
  2. **We Build Everything** — Our team (humans + AI agents) builds your website, CRM, chatbot, and automations in days, not months.
  3. **You Grow** — Launch and watch the leads come in. We handle the tech, you handle your business.
- Each step: large number (100px, faint accent-blue), heading, description

**D. ROI Calculator (dark bg)** — KEEP SIMPLE, no complex JS
- Section heading: "How Much Revenue Are You Losing?"
- Simple inline calculator with 4 inputs:
  - Monthly leads (number input, default 100)
  - Monthly appointments (number input, default 20)
  - Average deal value (number input, default £2000)
  - Follow-up attempts (select: 0, 1, 2, 3, 4, 5+)
- "Calculate" button
- Result display: "You're losing approximately **£X/month** from slow follow-ups and missed leads"
- Note: "Our AI agents respond in under 60 seconds, 24/7"

**E. Bundle Packages Preview (light bg)**
- Section heading: "Monthly Growth Packages"
- Subheading: "Everything working together. One monthly fee."
- 3 pricing cards (middle one highlighted/recommended):
  - **Starter — £150/mo**: CRM + basic automations + monthly report
  - **Growth — £300/mo** ⭐ RECOMMENDED: CRM + website + chatbot + email campaigns + SEO
  - **Scale — £500/mo**: Everything + voice AI + full automation management + priority support
- Each card: price, feature list (6-8 items with ✓), "Get Started" CTA
- Link: "View individual services pricing →"

**F. Testimonials (dark bg)**
- Section heading: "What Our Clients Say"
- 3 testimonial cards:
  - "Cloud Hak transformed how we handle new patients. Our response time went from hours to seconds. The chatbot alone has booked over 40 consultations this month." — Jessica G., Airway Clinic Stockholm
  - "I was sceptical about AI, but the results speak for themselves. We're converting 35% more leads and the CRM automations save me at least 10 hours a week." — James T., Brighton Dental Practice
  - "Finally, a tech partner that actually understands local business. They built our site, set up our CRM, and the voice agent handles all our after-hours calls. Game changer." — Sarah M., Hove Physiotherapy
- Each card: quote text, name, business, star rating (5 stars, CSS)

**G. Case Study Spotlight (light bg)**
- Section heading: "Featured: Airway Clinic Stockholm"
- Two columns: left = image placeholder (rounded card with "Airway Clinic" text overlay), right = text
- Brief writeup: "When Airway Clinic Stockholm came to us, they had no online presence and were manually following up with every lead. We built their bilingual website (English + Swedish), deployed an AI chatbot, and automated their entire patient pipeline. Results: 40+ consultations booked via chatbot in the first month, 60-second lead response time, and zero missed after-hours calls."
- "View Case Study →" link + "Book Your Consultation →" CTA

**H. Final CTA (dark bg with gradient overlay)**
- Heading: "Ready to Grow Your Business?"
- Subheading: "Book a free, no-obligation consultation. We'll show you exactly how we can help."
- "Book Free Consultation" large CTA button
- Below: "No contracts. No commitments. Just results."

**I. Footer (darkest bg)**
- Logo (white version — use CSS filter or just the PNG)
- 4 columns: Services (list), Company (About, Work, Pricing, Blog), Contact (address, phone, email), Legal (Privacy, Terms)
- Bottom: "© 2026 Cloud Hak Ltd. All rights reserved." + social icons (LinkedIn, X/Twitter — use SVG or Unicode)

### 2. `services/index.html` — Services Hub
**Title:** Our Services — Cloud Hak
**Sections:**
- Hero: "Everything Your Business Needs to Grow Online"
- 5 detailed service cards (same as homepage but expanded with more text)
- Each links to its own page
- CTA at bottom

### 3. `services/websites/index.html` — Website Service
**Title:** Professional Websites for Local Businesses — Cloud Hak
**Sections:**
- Hero: "A Website That Actually Brings In Customers"
- What you get (bullet list)
- Who it's for (industry list)
- Pricing tiers: Starter £150, Standard £300, Advanced £500
- Process: 3 steps
- FAQ (5 questions)
- CTA

### 4. `services/crm/index.html` — CRM Service
**Title:** Cloud Hak CRM — Your Business on Autopilot
**Sections:**
- Hero: "Stop Losing Leads. Automate Everything."
- What you get: pipelines, automations, SMS, email, WhatsApp, calendar, review requests
- Who it's for
- Pricing tiers: Starter £100, Standard £200, Advanced £350
- FAQ
- CTA

### 5. `services/chatbots/index.html` — Chatbot Service
**Title:** AI Chatbots That Turn Visitors Into Customers — Cloud Hak
**Sections:**
- Hero: "Your 24/7 Sales Team That Never Sleeps"
- What you get
- Pricing: Starter £150, Standard £300, Advanced £500
- FAQ
- CTA

### 6. `services/voice-ai/index.html` — Voice AI Service
**Title:** AI Voice Agents — Never Miss a Call Again — Cloud Hak
**Sections:**
- Hero: "Every Call Answered. Every Lead Captured."
- What you get: inbound handling, outbound campaigns, appointment booking, call transfer, multilingual
- Pricing: Starter £300, Professional £500, Enterprise custom
- FAQ
- CTA

### 7. `services/seo/index.html` — SEO Service
**Title:** Local SEO — Get Found on Google — Cloud Hak
**Sections:**
- Hero: "Be the First Business They See on Google"
- What you get: GBP optimisation, on-page SEO, citations, local keyword targeting
- Pricing: Starter £100, Standard £200, Advanced £300
- FAQ
- CTA

### 8. `pricing/index.html` — Pricing Page
**Title:** Pricing — Cloud Hak
**Sections:**
- Hero: "Simple, Transparent Pricing"
- Toggle: "Individual Services" ↔ "Monthly Bundles"
- Individual services: summary cards for each service with 3 tiers
- Monthly bundles: Starter £150/mo, Growth £300/mo, Scale £500/mo (detailed feature lists)
- "Not sure? Book a free consultation" CTA
- FAQ (6-8 questions about pricing)

### 9. `about/index.html` — About Page
**Title:** About Cloud Hak — AI-Powered Agency for Local Business
**Sections:**
- Hero: "Making Enterprise-Grade Tech Accessible to Every Local Business"
- Founder section: Nima's story (placeholder text — "Nima Hakimmaani founded Cloud Hak after years of running his own local businesses. He experienced first-hand how difficult it was for small businesses to access the same technology that big corporations take for granted. Cloud Hak was born to change that.")
- Team section: "Humans + AI Agents" — "Our team combines human expertise with AI efficiency. Nima leads strategy and client relationships, while our AI agents (Nemo & Hermie) handle execution — building websites, managing CRMs, deploying chatbots, and running automations at scale."
- Values: Speed, Transparency, Results Over Promises, Accessibility
- Location: Brighton & Hove, UK + Stockholm, Sweden
- CTA: "Let's Work Together"

### 10. `work/index.html` — Portfolio / Case Studies
**Title:** Our Work — Cloud Hak
**Sections:**
- Hero: "See What We've Built"
- Featured case study: Airway Clinic Stockholm (full writeup with results)
- Grid of project cards (start with Airway Clinic, more to come)
- CTA: "Want Results Like These?"

### 11. `contact/index.html` — Contact / Book Consultation
**Title:** Book a Free Consultation — Cloud Hak
**Sections:**
- Hero: "Let's Talk About Growing Your Business"
- Contact form: Name, Email, Phone, Business Name, "What do you need help with?" (dropdown: Website, CRM, Chatbot, Voice AI, SEO, Not sure), Message textarea
- Form submits to: `https://services.leadconnectorhq.com/hooks/BjKd0mLr` (POST, JSON: firstName, lastName, email, phone, message)
- Alternative: "Prefer to talk? Call us at 07800 920042"
- Address and map placeholder

### 12. `privacy/index.html` — Privacy Policy
**Title:** Privacy Policy — Cloud Hak
Simple privacy policy page. Include standard UK GDPR-compliant text.

### 13. `terms/index.html` — Terms of Service
**Title:** Terms of Service — Cloud Hak
Simple terms page.

## SEO Requirements (EVERY PAGE)

Each page must include:
```html
<meta name="description" content="...">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://cloud-hak.com/...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:type" content="website">
<meta property="og:url" content="https://cloud-hak.com/...">
<meta property="og:site_name" content="Cloud Hak">
<meta name="twitter:card" content="summary_large_image">
```

JSON-LD structured data on each page:
- Organization schema on every page
- Service schema on service pages
- BreadcrumbList schema on sub-pages
- FAQPage schema on pages with FAQs
- LocalBusiness schema on contact page

## AEO (Answer Engine Optimisation) Requirements

Every page must:
1. Have a clear `<h1>` that answers a question (e.g. "What is Cloud Hak CRM?")
2. Include an FAQ section with questions formatted as `<h3>` or `<h4>` with direct, concise answers (under 50 words per answer)
3. Use structured data (FAQPage schema) to mark up FAQs
4. Include key facts in a "Key Facts" or "At a Glance" section using `<dl>` or `<ul>` with clear labels
5. Have descriptive `alt` text on all images
6. Use semantic HTML: `<article>`, `<section>`, `<nav>`, `<header>`, `<footer>`, `<main>`, `<aside>`
7. Each service page should answer: What is it? Who is it for? How much does it cost? How long does it take?

## Navigation (IDENTICAL ON EVERY PAGE)

**Desktop:**
```
[LOGO]  Services ▾   Pricing   About   Work   [Book Consultation]
```
Services dropdown: Websites, CRM, Chatbots, Voice AI, SEO

**Mobile:** Hamburger menu → full-screen overlay with all links

**Footer (IDENTICAL ON EVERY PAGE):**
4 columns:
- Services: Websites, CRM, Chatbots, Voice AI, SEO
- Company: About, Work, Pricing, Contact
- Contact: 117 Holmes Avenue, Hove, BN3 7LF | 07800 920042 | info@cloud-hak.com
- Legal: Privacy Policy, Terms of Service
Bottom bar: © 2026 Cloud Hak Ltd

## CRITICAL RULES

1. **Mobile-first responsive** — Test at 375px, 768px, 1024px, 1440px
2. **Fast loading** — No external JS libraries. No jQuery. No heavy images. CSS animations only.
3. **Accessible** — Proper heading hierarchy, alt text, ARIA labels, focus states, contrast ratios
4. **Consistent nav/footer** — Copy the exact same HTML for header and footer across ALL pages
5. **Relative paths** — Use relative paths for links and assets (e.g. `./assets/logo.png` from root, `../assets/logo.png` from sub-pages, `../../assets/logo.png` from services/*/)
6. **No placeholders** — Use real content everywhere. No "Lorem ipsum". No "Coming soon".
7. **No external dependencies** — Except Google Fonts (Inter). No Tailwind, no Bootstrap, no icon libraries. Use CSS for icons or inline SVGs.
8. **British English** — "optimised" not "optimized", "colour" not "color" (in text content), "enquiry" not "inquiry"
9. **Currency in GBP (£)** — Show prices in pounds sterling
10. **Every page standalone** — Each HTML file must work independently with its own complete `<head>`, styles, and scripts

## Build Order
Start with index.html (homepage) — get it perfect, then build the rest. Each page should feel like it belongs to the same site: same colours, same typography, same nav, same footer, same quality.
