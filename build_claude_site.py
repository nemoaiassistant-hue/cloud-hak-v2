# -*- coding: utf-8 -*-
"""Generator for the Claude version of the Cloud Hak website (under /claude/).
Distinct premium design, 14 pages, static HTML. Uses absolute paths (/claude/...)."""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "claude")
BASE = "https://cloud-hak.com/claude"

ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization",
    "name": "Cloud Hak Ltd", "url": "https://cloud-hak.com",
    "logo": "https://cloud-hak.com/assets/logo.png",
    "email": "info@cloud-hak.com", "telephone": "+447800920042",
    "sameAs": ["https://www.linkedin.com/company/cloud-hak", "https://x.com/cloudhak"],
    "address": {"@type": "PostalAddress", "streetAddress": "117 Holmes Avenue",
                "addressLocality": "Hove", "addressRegion": "East Sussex",
                "postalCode": "BN3 7LF", "addressCountry": "GB"},
}

def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n,
                 "item": u} for i, (n, u) in enumerate(items)]}

def faqld(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in pairs]}

CSS = """
:root{
--bg:#070b16;--bg-1:#0a0f1c;--bg-2:#0e1626;--bg-3:#13203a;
--blue:#4f6ef7;--teal:#3bb6b3;--green:#22c55e;--amber:#f59e0b;
--white:#f8fafc;--mut:#9aa7bd;--mut-2:#6b7a93;
--line:rgba(148,163,184,.14);--line-2:rgba(148,163,184,.22);
--card:rgba(255,255,255,.035);--card-2:rgba(255,255,255,.06);
--rad:18px;--maxw:1180px;
--grad:linear-gradient(120deg,#5b7bff,#3bb6b3);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;
background:var(--bg);color:var(--white);font-size:16px;line-height:1.65;
-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto;display:block}
button,input,select,textarea{font:inherit}
h1,h2,h3,h4{margin:0;line-height:1.15;letter-spacing:-.02em;font-weight:800}
p{margin:0}
.wrap{width:min(var(--maxw),100%);margin:0 auto;padding:0 26px}
.grad-text{background:var(--grad);-webkit-background-clip:text;background-clip:text;
-webkit-text-fill-color:transparent;color:transparent}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;
letter-spacing:.14em;text-transform:uppercase;color:var(--teal);
padding:7px 14px;border:1px solid var(--line-2);border-radius:999px;
background:rgba(59,182,179,.07)}
.eyebrow::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--teal);
box-shadow:0 0 12px var(--teal)}
.muted{color:var(--mut)}
/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:1000;height:74px;
background:rgba(7,11,22,.72);backdrop-filter:blur(16px) saturate(140%);
border-bottom:1px solid var(--line)}
.nav-in{height:74px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.brand img{width:152px}
.menu{display:flex;align-items:center;gap:6px}
.menu>a,.dd>button{display:inline-flex;align-items:center;gap:6px;color:var(--mut);
font-weight:600;font-size:15px;padding:9px 14px;border-radius:10px;border:0;
background:none;cursor:pointer;transition:.18s}
.menu>a:hover,.dd>button:hover,.menu>a.on{color:var(--white);background:var(--card-2)}
.dd{position:relative}
.dd-menu{position:absolute;top:54px;left:0;min-width:230px;padding:8px;
background:var(--bg-2);border:1px solid var(--line-2);border-radius:14px;
box-shadow:0 24px 60px rgba(0,0,0,.5);opacity:0;visibility:hidden;
transform:translateY(8px);transition:.18s}
.dd:hover .dd-menu,.dd:focus-within .dd-menu{opacity:1;visibility:visible;transform:none}
.dd-menu a{display:flex;flex-direction:column;padding:10px 12px;border-radius:10px;color:var(--white);font-weight:600}
.dd-menu a span{font-size:12.5px;color:var(--mut);font-weight:500}
.dd-menu a:hover{background:var(--card-2)}
.nav-cta{display:flex;align-items:center;gap:10px}
.burger{display:none;width:46px;height:42px;border:1px solid var(--line-2);
border-radius:11px;background:none;cursor:pointer}
.burger span{display:block;width:20px;height:2px;background:var(--white);margin:5px auto;transition:.2s}
.mobile{position:fixed;inset:74px 0 0;background:#000;z-index:1001;display:none;
padding:30px 26px;overflow-y:auto}
.mobile.open{display:block}
.mobile a{display:block;padding:16px 4px;font-size:18px;font-weight:700;
color:#fff;border-bottom:1px solid rgba(255,255,255,.08)}
.mobile .mlabel{color:var(--teal);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
padding:22px 4px 6px;border:0}
body.lock{overflow:hidden}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;
font-weight:700;font-size:15.5px;padding:14px 26px;border-radius:12px;
border:1px solid transparent;cursor:pointer;transition:.2s;min-height:50px}
.btn-pri{background:var(--grad);color:#fff;box-shadow:0 10px 30px rgba(79,110,247,.32)}
.btn-pri:hover{transform:translateY(-2px);box-shadow:0 16px 40px rgba(79,110,247,.45)}
.btn-gho{background:rgba(255,255,255,.06);color:#fff;border-color:var(--line-2)}
.btn-gho:hover{background:rgba(255,255,255,.12);transform:translateY(-2px)}
.btn-sm{padding:10px 18px;min-height:42px;font-size:14.5px}
.btn-block{width:100%}
/* sections */
section{position:relative;padding:96px 0}
.sec-head{max-width:720px;margin:0 0 48px}
.sec-head.center{margin-left:auto;margin-right:auto;text-align:center}
h1{font-size:clamp(34px,5.4vw,60px)}
h2{font-size:clamp(28px,3.6vw,42px)}
.sec-head p{color:var(--mut);font-size:18px;margin-top:16px}
.lead{color:var(--mut);font-size:19px;max-width:620px}
/* hero */
.hero{padding:150px 0 96px;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.5;pointer-events:none;z-index:0}
.orb-a{width:520px;height:520px;background:radial-gradient(circle,#4f6ef7,transparent 70%);top:-160px;left:-120px}
.orb-b{width:460px;height:460px;background:radial-gradient(circle,#3bb6b3,transparent 70%);top:40px;right:-140px;opacity:.4}
.hero .wrap{position:relative;z-index:1}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;align-items:center}
.hero h1{margin:22px 0}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px}
.hero-note{margin-top:22px;color:var(--mut-2);font-size:14px}
.glass-card{background:var(--card);border:1px solid var(--line-2);border-radius:24px;
padding:28px;backdrop-filter:blur(8px);box-shadow:0 30px 70px rgba(0,0,0,.45)}
.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.stat{padding:20px;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.03)}
.stat .n{font-size:30px;font-weight:900}
.stat .l{font-size:13px;color:var(--mut);margin-top:4px}
/* marquee */
.marq{border-top:1px solid var(--line);border-bottom:1px solid var(--line);
background:var(--bg-1);padding:20px 0;overflow:hidden;white-space:nowrap}
.marq-track{display:inline-flex;gap:48px;animation:scroll 28s linear infinite;font-weight:700;color:var(--mut)}
.marq-track span{display:inline-flex;align-items:center;gap:48px}
.marq-track span::after{content:"\\2022";color:var(--teal)}
@keyframes scroll{to{transform:translateX(-50%)}}
/* generic grids */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
/* cards */
.card{position:relative;background:var(--card);border:1px solid var(--line-2);
border-radius:var(--rad);padding:30px;transition:.22s;overflow:hidden}
.card::after{content:"";position:absolute;inset:0;border-radius:var(--rad);
padding:1px;background:var(--grad);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
-webkit-mask-composite:xor;mask-composite:exclude;opacity:0;transition:.22s;pointer-events:none}
.card:hover{transform:translateY(-6px);background:var(--card-2)}
.card:hover::after{opacity:1}
.card .ico{width:54px;height:54px;border-radius:14px;display:grid;place-items:center;
font-size:26px;margin-bottom:18px;background:linear-gradient(135deg,rgba(79,110,247,.22),rgba(59,182,179,.18));
border:1px solid var(--line-2)}
.card h3{font-size:21px;margin-bottom:10px}
.card p{color:var(--mut);font-size:15px}
.card .more{display:inline-flex;align-items:center;gap:7px;margin-top:16px;color:var(--blue);font-weight:700;font-size:14.5px}
.card.click .more::after{content:"";position:absolute;inset:0}
/* bento */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:22px}
.bento .card{margin:0}
.b-wide{grid-column:span 3}
.b-tall{grid-column:span 3}
.b-third{grid-column:span 2}
/* steps */
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.step{position:relative;padding:30px;border:1px solid var(--line);border-radius:var(--rad);
background:var(--card)}
.step .num{font-size:15px;font-weight:900;width:42px;height:42px;border-radius:12px;
display:grid;place-items:center;background:var(--grad);color:#fff;margin-bottom:18px}
.step h3{font-size:20px;margin-bottom:10px}
.step p{color:var(--mut);font-size:15px}
/* feature list */
.flist{list-style:none;padding:0;margin:0;display:grid;gap:12px}
.flist li{position:relative;padding-left:30px;color:var(--mut)}
.flist li::before{content:"";position:absolute;left:0;top:7px;width:18px;height:18px;
border-radius:6px;background:linear-gradient(135deg,var(--blue),var(--teal))}
.flist li::after{content:"\\2713";position:absolute;left:4px;top:5px;color:#fff;font-size:12px;font-weight:900}
/* at a glance */
.glance{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:36px}
.glance>div{padding:20px;border:1px solid var(--line);border-radius:14px;background:var(--card)}
.glance dt{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--teal)}
.glance dd{margin:8px 0 0;font-weight:800;font-size:16px}
/* pricing */
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}
.tier{position:relative;padding:34px;border:1px solid var(--line-2);border-radius:22px;background:var(--card)}
.tier.feat{border-color:transparent;background:linear-gradient(var(--bg-2),var(--bg-2)) padding-box,var(--grad) border-box;
border:2px solid transparent;box-shadow:0 24px 60px rgba(79,110,247,.22)}
.tier .tag{position:absolute;top:-13px;left:34px;background:var(--grad);color:#fff;
font-size:12px;font-weight:800;letter-spacing:.06em;padding:5px 12px;border-radius:999px}
.tier h3{font-size:20px}
.tier .price{font-size:42px;font-weight:900;margin:10px 0 4px}
.tier .price small{font-size:16px;font-weight:700;color:var(--mut)}
.tier .flist{margin:22px 0 26px}
/* roi */
.roi{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center}
.field{margin-bottom:16px}
.field label{display:block;font-weight:700;font-size:14px;margin-bottom:8px}
.field input,.field select,.field textarea{width:100%;padding:14px 15px;border-radius:12px;
border:1px solid var(--line-2);background:rgba(255,255,255,.04);color:#fff}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--blue);
box-shadow:0 0 0 3px rgba(79,110,247,.25)}
.field select option{background:#0e1626}
.roi-out{padding:28px;border-radius:18px;text-align:center;
background:linear-gradient(135deg,rgba(34,197,94,.14),rgba(59,182,179,.12));
border:1px solid rgba(34,197,94,.3)}
.roi-out .big{font-size:44px;font-weight:900;margin:6px 0}
/* testimonials */
.quote{padding:30px;border:1px solid var(--line-2);border-radius:var(--rad);background:var(--card)}
.quote .stars{color:var(--amber);letter-spacing:3px;margin-bottom:14px}
.quote p{color:var(--white);font-size:16px}
.quote .who{margin-top:18px;display:flex;align-items:center;gap:12px}
.quote .av{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;
font-weight:800;background:var(--grad);color:#fff}
.quote .who b{display:block;font-size:15px}
.quote .who span{font-size:13px;color:var(--mut)}
/* split / case */
.split{display:grid;grid-template-columns:1fr 1fr;gap:46px;align-items:center}
.case-visual{min-height:340px;border-radius:22px;padding:34px;display:flex;flex-direction:column;
justify-content:flex-end;background:linear-gradient(135deg,#4f6ef7,#3bb6b3);
box-shadow:inset 0 0 0 1px rgba(255,255,255,.25),0 30px 70px rgba(0,0,0,.4)}
.case-visual b{font-size:32px;line-height:1.1}
.case-visual .pill{align-self:flex-start;margin-bottom:auto;background:rgba(0,0,0,.25);
color:#fff;padding:7px 14px;border-radius:999px;font-size:13px;font-weight:700}
/* faq */
.faq details{border:1px solid var(--line-2);border-radius:14px;padding:20px 22px;
background:var(--card);margin-bottom:14px;transition:.2s}
.faq details[open]{background:var(--card-2);border-color:var(--blue)}
.faq summary{cursor:pointer;font-weight:700;font-size:17px;list-style:none;
display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--teal);font-size:24px;font-weight:700;transition:.2s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq p{color:var(--mut);margin-top:14px}
/* prose */
.prose{max-width:780px}
.prose h2{font-size:24px;margin:34px 0 14px}
.prose p{color:var(--mut);margin-bottom:16px}
/* cta band */
.cta{background:linear-gradient(135deg,rgba(79,110,247,.16),rgba(59,182,179,.12));
border-top:1px solid var(--line);border-bottom:1px solid var(--line);text-align:center}
.cta .wrap{max-width:760px}
.cta h2{margin-bottom:16px}
.cta .btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px}
.cta .fine{margin-top:18px;color:var(--mut-2);font-size:14px}
/* contact */
.cgrid{display:grid;grid-template-columns:1.2fr .8fr;gap:36px;align-items:start}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.info-card{padding:26px;border:1px solid var(--line-2);border-radius:18px;background:var(--card);margin-bottom:18px}
.info-card h3{font-size:18px;margin-bottom:8px}
.info-card p,.info-card a{color:var(--mut)}
.fstatus{margin-top:14px;font-weight:700}
/* footer */
.foot{background:var(--bg-1);border-top:1px solid var(--line);padding:64px 0 0}
.foot-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr 1.2fr;gap:36px}
.foot-brand img{width:158px;margin-bottom:16px}
.foot-brand p{color:var(--mut);font-size:14.5px;max-width:300px}
.foot h4{font-size:14px;letter-spacing:.05em;margin-bottom:16px}
.foot ul{list-style:none;padding:0;margin:0}
.foot li{margin:10px 0}
.foot a{color:var(--mut);font-size:14.5px}
.foot a:hover{color:#fff}
.foot address{font-style:normal;color:var(--mut);font-size:14.5px;line-height:1.9}
.foot-bot{margin-top:54px;border-top:1px solid var(--line);padding:24px 0;
display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.foot-bot p{color:var(--mut-2);font-size:14px}
.soc{display:flex;gap:10px}
.soc a{width:38px;height:38px;border-radius:11px;border:1px solid var(--line-2);
display:grid;place-items:center;color:#fff;font-weight:700;font-size:13px}
.soc a:hover{background:var(--card-2)}
/* reveal */
.rv{opacity:0;transform:translateY(22px);transition:opacity .6s ease,transform .6s ease}
.rv.in{opacity:1;transform:none}
:focus-visible{outline:3px solid var(--teal);outline-offset:3px;border-radius:6px}
/* responsive */
@media(max-width:960px){
.menu,.nav-cta .btn{display:none}.burger{display:block}
.hero-grid,.roi,.split,.cgrid{grid-template-columns:1fr}
.bento{grid-template-columns:1fr 1fr}.b-wide,.b-tall,.b-third{grid-column:span 1}
.g3,.g4,.tiers,.steps{grid-template-columns:1fr}.glance{grid-template-columns:1fr 1fr}
.hero{padding:120px 0 70px}
}
@media(max-width:560px){
.wrap{padding:0 18px}section{padding:64px 0}.hero{padding:108px 0 56px}
.g2,.bento{grid-template-columns:1fr}.glance{grid-template-columns:1fr}
.frow{grid-template-columns:1fr}.stat-grid{grid-template-columns:1fr}
.btn{width:100%}.hero-cta{flex-direction:column}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rv{opacity:1;transform:none}}
"""

JS = """
(function(){
var b=document.querySelector('[data-burger]'),m=document.querySelector('[data-mobile]');
if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');
document.body.classList.toggle('lock',o);b.setAttribute('aria-expanded',o);});}
var io=new IntersectionObserver(function(es){es.forEach(function(e){
if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});
var f=document.querySelector('[data-roi]');
if(f){f.addEventListener('submit',function(ev){ev.preventDefault();
var leads=+f.leads.value||0,appts=+f.appts.value||0,val=+f.val.value||0,
fu=f.fu.value==='5'?5:(+f.fu.value||0);
var missed=Math.max(leads-appts,0);
var pen=Math.min(.38,.12+Math.max(0,5-fu)*.045);
var lost=Math.round(missed*val*pen);
f.querySelector('[data-roi-out]').innerHTML='You are losing approximately'+
'<div class="big grad-text">\\u00a3'+lost.toLocaleString('en-GB')+'</div>'+
'<div class="muted">per month from slow follow-ups and missed leads</div>';});}
document.querySelectorAll('[data-toggle]').forEach(function(g){
var btns=g.querySelectorAll('[data-tab]');
btns.forEach(function(btn){btn.addEventListener('click',function(){
btns.forEach(function(x){x.classList.remove('on');});btn.classList.add('on');
g.querySelectorAll('[data-panel]').forEach(function(p){p.hidden=p.dataset.panel!==btn.dataset.tab;});});});});
var cf=document.querySelector('[data-contact]');
if(cf){cf.addEventListener('submit',function(ev){ev.preventDefault();
var d=new FormData(cf),nm=String(d.get('name')||'').trim().split(/\\s+/);
var s=cf.querySelector('[data-status]');s.textContent='Sending\\u2026';s.style.color='#9aa7bd';
var payload={firstName:nm[0]||'',lastName:nm.slice(1).join(' '),email:d.get('email'),
phone:d.get('phone'),message:'Business: '+(d.get('business')||'')+'\\nService: '+(d.get('need')||'')+'\\n\\n'+(d.get('message')||'')};
fetch(cf.action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
.then(function(){s.textContent='Thank you \\u2014 we have your details and will be in touch within one working day.';s.style.color='#22c55e';cf.reset();})
.catch(function(){s.textContent='Something went wrong. Please call 07800 920042 or email info@cloud-hak.com.';s.style.color='#f59e0b';});});}
})();
"""

SERVICES = [
    ("websites", "Professional Websites", "\U0001F310",
     "Custom-built, lightning-fast, mobile-first sites that turn visitors into booked customers."),
    ("crm", "Cloud Hak CRM", "\U0001F4CA",
     "Lead capture, follow-ups, appointments, reviews and reporting — all on autopilot."),
    ("chatbots", "AI Chatbots", "\U0001F916",
     "24/7 intelligent chat that answers questions, qualifies leads and books appointments."),
    ("voice-ai", "Voice AI Agents", "\U0001F399️",
     "AI answers, routes and books every call so you never miss another lead."),
    ("seo", "SEO & Local Search", "\U0001F50D",
     "Optimised Google profiles, citations and on-page SEO that drives local enquiries."),
]

def nav(active=""):
    def on(k):
        return " on" if active == k else ""
    items = "".join(
        f'<a href="/claude/services/{s}/"><b>{t}</b><span>{d.split(",")[0][:42]}</span></a>'
        for s, t, _i, d in SERVICES)
    return f"""<header class="nav">
<div class="wrap nav-in">
<a class="brand" href="/claude/" aria-label="Cloud Hak home"><img src="/assets/logo.png" alt="Cloud Hak Ltd logo"></a>
<nav class="menu" aria-label="Primary">
<div class="dd"><button type="button" aria-haspopup="true">Services &#9662;</button>
<div class="dd-menu">{items}</div></div>
<a href="/claude/pricing/"{on('pricing')}>Pricing</a>
<a href="/claude/about/"{on('about')}>About</a>
<a href="/claude/work/"{on('work')}>Work</a>
<a href="/claude/contact/"{on('contact')}>Contact</a>
</nav>
<div class="nav-cta">
<a class="btn btn-pri btn-sm" href="/claude/contact/">Book Consultation</a>
<button class="burger" data-burger type="button" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div>
</div>
<nav class="mobile" data-mobile aria-label="Mobile">
<div class="mlabel">Services</div>
{''.join(f'<a href="/claude/services/{s}/">{t}</a>' for s,t,_i,_d in SERVICES)}
<div class="mlabel">Company</div>
<a href="/claude/pricing/">Pricing</a>
<a href="/claude/about/">About</a>
<a href="/claude/work/">Work</a>
<a href="/claude/contact/">Contact</a>
<a class="btn btn-pri btn-block" style="margin-top:22px" href="/claude/contact/">Book Free Consultation</a>
</nav>
</header>"""

FOOTER = """<footer class="foot">
<div class="wrap">
<div class="foot-grid">
<div class="foot-brand">
<a href="/claude/"><img src="/assets/logo.png" alt="Cloud Hak Ltd logo"></a>
<p>We build, automate and grow local businesses with websites, CRM, AI agents and local SEO — done for you by humans and AI.</p>
</div>
<div><h4>Services</h4><ul>
<li><a href="/claude/services/websites/">Websites</a></li>
<li><a href="/claude/services/crm/">CRM</a></li>
<li><a href="/claude/services/chatbots/">Chatbots</a></li>
<li><a href="/claude/services/voice-ai/">Voice AI</a></li>
<li><a href="/claude/services/seo/">SEO</a></li>
</ul></div>
<div><h4>Company</h4><ul>
<li><a href="/claude/about/">About</a></li>
<li><a href="/claude/work/">Work</a></li>
<li><a href="/claude/pricing/">Pricing</a></li>
<li><a href="/claude/contact/">Contact</a></li>
</ul></div>
<div><h4>Contact</h4>
<address>
117 Holmes Avenue<br>Hove, East Sussex BN3 7LF<br>United Kingdom<br><br>
<a href="tel:+447800920042">07800 920042</a><br>
<a href="mailto:info@cloud-hak.com">info@cloud-hak.com</a>
</address>
<h4 style="margin-top:22px">Legal</h4>
<ul><li><a href="/claude/privacy/">Privacy Policy</a></li><li><a href="/claude/terms/">Terms of Service</a></li></ul>
</div>
</div>
<div class="foot-bot">
<p>&copy; 2026 Cloud Hak Ltd. All rights reserved.</p>
<div class="soc">
<a href="https://www.linkedin.com/company/cloud-hak" aria-label="LinkedIn">in</a>
<a href="https://x.com/cloudhak" aria-label="X">X</a>
</div>
</div>
</div>
</footer>"""

def page(path, title, desc, body, active="", ld=None, slug=""):
    canonical = f"{BASE}/{slug}" if slug else f"{BASE}/"
    ld_blocks = [ORG_LD] + (ld or [])
    ld_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in ld_blocks)
    html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{'noindex, follow' if slug=='404' else 'index, follow'}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Cloud Hak">
<meta property="og:image" content="https://cloud-hak.com/assets/logo.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
{ld_html}
</head>
<body>
{nav(active)}
<main>
{body}
</main>
{FOOTER}
<script>{JS}</script>
</body>
</html>
"""
    # Rewrite absolute site paths to RELATIVE paths so the /claude/ site works
    # in any serving context (file://, /claude/ mounted as root, or domain root).
    # Metadata URLs (canonical, og:url, JSON-LD) stay absolute and are untouched.
    import re as _re
    depth = path.count("/")            # index.html=0, pricing/index.html=1, services/x/index.html=2
    up = "../" * depth
    root_href = up if up else "./"
    asset_prefix = up + "assets/"      # self-contained: claude/assets/ exists at the claude root
    html = html.replace('href="/claude/"', f'href="{root_href}"')
    html = html.replace('="/assets/', f'="{asset_prefix}')
    html = html.replace('href="/claude/', f'href="{up}')

    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html), "depth", depth)

def faq_section(title, pairs, label="FAQs"):
    items = "".join(
        f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>'
        for q, a in pairs)
    return f"""<section class="faq"><div class="wrap">
<div class="sec-head"><span class="eyebrow">{label}</span><h2 style="margin-top:18px">{title}</h2></div>
{items}
</div></section>"""

def cta(head="Ready to grow your business?",
        sub="Book a free, no-obligation consultation. We will show you exactly how we can help — no hard sell.",
        primary="Book Free Consultation"):
    return f"""<section class="cta"><div class="wrap">
<span class="eyebrow">Get started</span>
<h2 style="margin-top:18px">{head}</h2>
<p class="muted" style="margin:0 auto;max-width:560px">{sub}</p>
<div class="btns"><a class="btn btn-pri" href="/claude/contact/">{primary}</a>
<a class="btn btn-gho" href="/claude/work/">See Our Work</a></div>
<p class="fine">No contracts. No commitments. Just results.</p>
</div></section>"""

# ---------------- HOME ----------------
def build_home():
    bento = f"""<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">What we do</span>
<h2 style="margin-top:18px">Everything Your Business Needs to Grow</h2>
<p>Five core services, one team of humans and AI handling it all. Click any service to learn more.</p></div>
<div class="bento">
<article class="card click b-wide rv"><div class="ico">{SERVICES[0][2]}</div><h3>{SERVICES[0][1]}</h3>
<p>{SERVICES[0][3]} Built on fast static foundations, designed to rank and convert.</p>
<a class="more" href="/claude/services/websites/">Learn more &#8594;</a></article>
<article class="card click b-tall rv"><div class="ico">{SERVICES[1][2]}</div><h3>{SERVICES[1][1]}</h3>
<p>{SERVICES[1][3]} Your entire customer pipeline, automated end to end.</p>
<a class="more" href="/claude/services/crm/">Learn more &#8594;</a></article>
<article class="card click b-third rv"><div class="ico">{SERVICES[2][2]}</div><h3>{SERVICES[2][1]}</h3>
<p>{SERVICES[2][3]}</p><a class="more" href="/claude/services/chatbots/">Learn more &#8594;</a></article>
<article class="card click b-third rv"><div class="ico">{SERVICES[3][2]}</div><h3>{SERVICES[3][1]}</h3>
<p>{SERVICES[3][3]}</p><a class="more" href="/claude/services/voice-ai/">Learn more &#8594;</a></article>
<article class="card click b-third rv"><div class="ico">{SERVICES[4][2]}</div><h3>{SERVICES[4][1]}</h3>
<p>{SERVICES[4][3]}</p><a class="more" href="/claude/services/seo/">Learn more &#8594;</a></article>
</div></div></section>"""

    how = """<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">How it works</span>
<h2 style="margin-top:18px">Simple. Fast. Done For You.</h2>
<p style="margin-left:auto;margin-right:auto">From first call to live system in days, not months.</p></div>
<div class="steps">
<div class="step rv"><div class="num">1</div><h3>Free Consultation</h3>
<p>Tell us about your business. We recommend exactly what you need — no jargon, no hard sell.</p></div>
<div class="step rv"><div class="num">2</div><h3>We Build Everything</h3>
<p>Our team of humans and AI agents builds your website, CRM, chatbot and automations in days.</p></div>
<div class="step rv"><div class="num">3</div><h3>You Grow</h3>
<p>Launch and watch the leads come in. We handle the technology; you handle your business.</p></div>
</div></div></section>"""

    roi = """<section><div class="wrap">
<div class="roi">
<div><span class="eyebrow">ROI calculator</span>
<h2 style="margin:18px 0 14px">How Much Revenue Are You Losing?</h2>
<p class="muted">Slow follow-ups and missed enquiries quietly cost local businesses thousands every month. Estimate yours in seconds.</p>
<p class="muted" style="margin-top:16px">&#9889; Our AI agents respond in under 60 seconds, 24/7.</p></div>
<form class="glass-card" data-roi>
<div class="frow"><div class="field"><label for="leads">Monthly leads</label><input id="leads" name="leads" type="number" value="100" min="0"></div>
<div class="field"><label for="appts">Monthly appointments</label><input id="appts" name="appts" type="number" value="20" min="0"></div></div>
<div class="frow"><div class="field"><label for="val">Average deal value (&pound;)</label><input id="val" name="val" type="number" value="2000" min="0"></div>
<div class="field"><label for="fu">Follow-up attempts</label><select id="fu" name="fu"><option>0</option><option>1</option><option selected>2</option><option>3</option><option>4</option><option value="5">5+</option></select></div></div>
<button class="btn btn-pri btn-block" type="submit">Calculate my lost revenue</button>
<div class="roi-out" style="margin-top:18px" data-roi-out>You are losing approximately<div class="big grad-text">&pound;0</div><div class="muted">per month from slow follow-ups and missed leads</div></div>
</form>
</div></div></section>"""

    pricing = f"""<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Pricing</span>
<h2 style="margin-top:18px">Monthly Growth Packages</h2>
<p style="margin-left:auto;margin-right:auto">Everything working together. One simple monthly fee.</p></div>
<div class="tiers">
<div class="tier rv"><h3>Starter</h3><div class="price">&pound;150<small>/mo</small></div>
<p class="muted">For businesses getting organised.</p>
<ul class="flist"><li>Cloud Hak CRM setup</li><li>Core automations</li><li>Lead capture forms</li><li>Monthly performance report</li><li>Email support</li><li>No long contract</li></ul>
<a class="btn btn-gho btn-block" href="/claude/contact/">Get Started</a></div>
<div class="tier feat rv"><span class="tag">RECOMMENDED</span><h3>Growth</h3><div class="price">&pound;300<small>/mo</small></div>
<p class="muted">Our most popular all-in-one bundle.</p>
<ul class="flist"><li>Everything in Starter</li><li>Professional website</li><li>AI chatbot</li><li>Email &amp; SMS campaigns</li><li>Local SEO</li><li>Monthly optimisation</li><li>Priority support</li></ul>
<a class="btn btn-pri btn-block" href="/claude/contact/">Get Started</a></div>
<div class="tier rv"><h3>Scale</h3><div class="price">&pound;500<small>/mo</small></div>
<p class="muted">For businesses ready to dominate locally.</p>
<ul class="flist"><li>Everything in Growth</li><li>Voice AI agent</li><li>Full automation management</li><li>Advanced reporting</li><li>Quarterly strategy session</li><li>Priority support</li></ul>
<a class="btn btn-gho btn-block" href="/claude/contact/">Get Started</a></div>
</div>
<p style="text-align:center;margin-top:30px"><a class="more" style="position:static" href="/claude/pricing/">View individual service pricing &#8594;</a></p>
</div></section>"""

    testi = """<section><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Testimonials</span>
<h2 style="margin-top:18px">What Our Clients Say</h2></div>
<div class="grid g3">
<figure class="quote rv" style="margin:0"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
<p>&ldquo;Cloud Hak transformed how we handle new patients. Our response time went from hours to seconds. The chatbot alone has booked over 40 consultations this month.&rdquo;</p>
<figcaption class="who"><span class="av">JG</span><span><b>Jessica G.</b><span>Airway Clinic, Stockholm</span></span></figcaption></figure>
<figure class="quote rv" style="margin:0"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
<p>&ldquo;I was sceptical about AI, but the results speak for themselves. We are converting 35% more leads and the CRM automations save me at least 10 hours a week.&rdquo;</p>
<figcaption class="who"><span class="av">JT</span><span><b>James T.</b><span>Brighton Dental Practice</span></span></figcaption></figure>
<figure class="quote rv" style="margin:0"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
<p>&ldquo;Finally, a tech partner that actually understands local business. They built our site, set up our CRM, and the voice agent handles all our after-hours calls. Game changer.&rdquo;</p>
<figcaption class="who"><span class="av">SM</span><span><b>Sarah M.</b><span>Hove Physiotherapy</span></span></figcaption></figure>
</div></div></section>"""

    case = """<section style="background:var(--bg-1)"><div class="wrap">
<div class="split">
<div class="case-visual rv"><span class="pill">Featured case study</span><b>Airway Clinic<br>Stockholm</b><p style="color:rgba(255,255,255,.9);margin-top:10px">Bilingual website &middot; AI chatbot &middot; automated patient pipeline</p></div>
<div><span class="eyebrow">Case study</span>
<h2 style="margin:18px 0 16px">40+ consultations booked in the first month</h2>
<p class="muted">When Airway Clinic Stockholm came to us, they had no online presence and were manually following up with every lead. We built their bilingual website (English &amp; Swedish), deployed an AI chatbot, and automated their entire patient pipeline.</p>
<dl class="glance"><div><dt>Bookings</dt><dd>40+ in month one</dd></div><div><dt>Response</dt><dd>60 seconds</dd></div><div><dt>Missed calls</dt><dd>Zero after-hours</dd></div><div><dt>Languages</dt><dd>EN + SV</dd></div></dl>
<div style="display:flex;gap:14px;margin-top:28px;flex-wrap:wrap"><a class="btn btn-gho" href="/claude/work/">View case study</a><a class="btn btn-pri" href="/claude/contact/">Book your consultation</a></div></div>
</div></div></section>"""

    faqs = [
        ("What does Cloud Hak build for local businesses?",
         "Cloud Hak builds websites, CRM systems, AI chatbots, voice agents and local SEO that help businesses capture, follow up and convert more leads — fully managed for you."),
        ("How much do Cloud Hak packages cost?",
         "Monthly growth packages start at £150, with Growth at £300 and Scale at £500 per month. Individual services start from £100."),
        ("How quickly can you get me set up?",
         "Most systems launch within days of your consultation. A typical website, CRM and chatbot bundle is live in one to two weeks."),
        ("Do I need technical knowledge to use it?",
         "No. Cloud Hak is fully done-for-you. We build, launch and manage the technology while you focus on running your business."),
        ("Is there a long-term contract?",
         "No long contracts. Packages are transparent and month to month, with terms agreed clearly before any work begins."),
    ]
    hero = f"""<section class="hero">
<div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><div class="hero-grid">
<div><span class="eyebrow">AI &amp; Automation Agency</span>
<h1>We Build, Automate &amp; Grow Your Business <span class="grad-text">While You Focus on What You Do Best</span></h1>
<p class="lead">Websites, CRM, AI chatbots, voice agents and SEO — all managed for you by our team of humans + AI.</p>
<div class="hero-cta"><a class="btn btn-pri" href="/claude/contact/">Book Free Consultation</a>
<a class="btn btn-gho" href="/claude/work/">See Our Work</a></div>
<p class="hero-note">&#10003; No contracts &nbsp; &#10003; Free consultation &nbsp; &#10003; Live in days, not months</p></div>
<div class="glass-card rv">
<div class="stat-grid">
<div class="stat"><div class="n grad-text">&lt;60s</div><div class="l">Lead response time</div></div>
<div class="stat"><div class="n grad-text">40+</div><div class="l">Bookings in month one</div></div>
<div class="stat"><div class="n grad-text">24/7</div><div class="l">AI agents on duty</div></div>
<div class="stat"><div class="n grad-text">5</div><div class="l">Core services, one team</div></div>
</div>
<a class="btn btn-pri btn-block" style="margin-top:18px" href="/claude/services/">Explore all services</a>
</div>
</div></div></section>
<div class="marq"><div class="marq-track">
<span>Clinics &amp; dental&nbsp;&nbsp; Trades &amp; home services&nbsp;&nbsp; Hospitality&nbsp;&nbsp; Wellness &amp; physio&nbsp;&nbsp; Professional services&nbsp;&nbsp; Trusted across the UK &amp; Europe</span>
<span>Clinics &amp; dental&nbsp;&nbsp; Trades &amp; home services&nbsp;&nbsp; Hospitality&nbsp;&nbsp; Wellness &amp; physio&nbsp;&nbsp; Professional services&nbsp;&nbsp; Trusted across the UK &amp; Europe</span>
</div></div>"""

    body = hero + bento + how + roi + pricing + testi + case + \
        faq_section("Frequently asked questions", faqs) + cta()
    page("index.html",
         "Cloud Hak — AI & Automation Agency for Local Businesses",
         "We build websites, set up CRM systems, deploy AI chatbots, voice agents, and SEO for local businesses. Everything you need to grow — done for you.",
         body, active="home", ld=[faqld(faqs)], slug="")

# ---------------- SERVICES HUB ----------------
def build_services_hub():
    cards = "".join(
        f"""<article class="card click rv"><div class="ico">{i}</div><h3>{t}</h3>
<p>{d}</p><a class="more" href="/claude/services/{s}/">Learn more &#8594;</a></article>"""
        for s, t, i, d in SERVICES)
    why = """<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Why Cloud Hak</span>
<h2 style="margin-top:18px">One Team. Every System. Working Together.</h2>
<p style="margin-left:auto;margin-right:auto">Most agencies do one thing. We connect your website, CRM, chatbot, voice AI and SEO into a single growth engine.</p></div>
<div class="grid g3">
<div class="card rv"><div class="ico">&#9889;</div><h3>Fast delivery</h3><p>Systems launch in days, not months. We move quickly so you see results sooner.</p></div>
<div class="card rv"><div class="ico">&#129309;</div><h3>Humans + AI</h3><p>Human strategy with AI execution — the speed of automation with the judgement of people.</p></div>
<div class="card rv"><div class="ico">&#128202;</div><h3>Done for you</h3><p>We build, launch and manage everything. You focus on serving your customers.</p></div>
</div></div></section>"""
    faqs = [
        ("What does Cloud Hak do?",
         "Cloud Hak builds websites, CRM systems, AI chatbots, voice agents and local SEO for local businesses, fully managed."),
        ("Who does Cloud Hak help?",
         "We help clinics, trades, hospitality, wellness and professional services that need more leads and faster follow-up."),
        ("Can I combine services?",
         "Yes. Most clients combine services into a monthly bundle so their website, CRM, AI and SEO all work together."),
        ("How quickly can a project start?",
         "Most projects begin within one week of your free consultation and a quick scope confirmation."),
    ]
    hero = """<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">Our services</span>
<h1 style="margin:20px 0;max-width:880px">Everything Your Business Needs to <span class="grad-text">Grow Online</span></h1>
<p class="lead">Strategy, build work and automation — so you capture more enquiries and convert them faster.</p>
<dl class="glance"><div><dt>Services</dt><dd>5 core systems</dd></div><div><dt>Delivery</dt><dd>Done for you</dd></div><div><dt>Best for</dt><dd>Local growth</dd></div><div><dt>Support</dt><dd>Ongoing</dd></div></dl>
</div></section>"""
    body = hero + f"""<section><div class="wrap"><div class="grid g3">{cards}</div></div></section>""" \
        + why + faq_section("Services FAQs", faqs) \
        + cta("Need the right mix of services?",
              "Book a free consultation and we will recommend the simplest stack for your business.")
    page("services/index.html", "Our Services — Cloud Hak",
         "Explore Cloud Hak services: websites, CRM systems, AI chatbots, voice agents and local SEO for local businesses.",
         body, active="",
         ld=[breadcrumb([("Home", BASE + "/"), ("Services", BASE + "/services/")]), faqld(faqs)],
         slug="services/")

# ---------------- SERVICE DETAIL ----------------
def service_page(slug, title_h1, tagline, intro, get, who, tiers, process, faqs,
                 glance, meta_title, meta_desc, label):
    get_li = "".join(f"<li>{g}</li>" for g in get)
    who_li = "".join(f"<li>{w}</li>" for w in who)
    glance_h = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in glance)
    tier_h = ""
    for name, price, sub, feats, feat in tiers:
        feats_li = "".join(f"<li>{x}</li>" for x in feats)
        cls = "tier feat rv" if feat else "tier rv"
        tag = '<span class="tag">POPULAR</span>' if feat else ""
        btn = "btn-pri" if feat else "btn-gho"
        tier_h += f"""<div class="{cls}">{tag}<h3>{name}</h3><div class="price">{price}</div>
<p class="muted">{sub}</p><ul class="flist">{feats_li}</ul>
<a class="btn {btn} btn-block" href="/claude/contact/">Get Started</a></div>"""
    steps_h = "".join(
        f'<div class="step rv"><div class="num">{i+1}</div><h3>{n}</h3><p>{d}</p></div>'
        for i, (n, d) in enumerate(process))
    hero = f"""<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">{label}</span>
<h1 style="margin:20px 0;max-width:900px">{title_h1}</h1>
<p class="lead">{tagline}</p>
<div class="hero-cta"><a class="btn btn-pri" href="/claude/contact/">Book Free Consultation</a>
<a class="btn btn-gho" href="/claude/pricing/">View Pricing</a></div>
<dl class="glance">{glance_h}</dl>
</div></section>"""
    body = hero + f"""<section><div class="wrap"><div class="split">
<div><span class="eyebrow">Overview</span><h2 style="margin:18px 0 16px">{intro[0]}</h2>
<p class="muted">{intro[1]}</p>
<h3 style="font-size:18px;margin:26px 0 14px">What you get</h3><ul class="flist">{get_li}</ul></div>
<div class="glass-card"><h3 style="font-size:18px;margin-bottom:16px">Who it's for</h3>
<ul class="flist">{who_li}</ul></div>
</div></div></section>
<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Pricing</span><h2 style="margin-top:18px">Simple, transparent pricing</h2>
<p style="margin-left:auto;margin-right:auto">Pick the tier that fits today — you can scale up any time.</p></div>
<div class="tiers">{tier_h}</div></div></section>
<section><div class="wrap"><div class="sec-head center"><span class="eyebrow">Process</span>
<h2 style="margin-top:18px">How we deliver</h2></div><div class="steps">{steps_h}</div></div></section>""" \
        + faq_section(f"{label} FAQs", faqs) + cta("Ready to build this for your business?")
    page(f"services/{slug}/index.html", meta_title, meta_desc, body, active="",
         ld=[
             {"@context": "https://schema.org", "@type": "Service",
              "serviceType": label, "provider": {"@type": "Organization", "name": "Cloud Hak Ltd"},
              "areaServed": "GB", "url": f"{BASE}/services/{slug}/",
              "description": meta_desc},
             breadcrumb([("Home", BASE + "/"), ("Services", BASE + "/services/"),
                         (label, f"{BASE}/services/{slug}/")]),
             faqld(faqs)],
         slug=f"services/{slug}/")

def build_service_pages():
    service_page(
        "websites", "A Website That Actually Brings In Customers",
        "Custom-built, lightning-fast, mobile-first websites designed to turn visitors into booked customers — not just look pretty.",
        ("What is a Cloud Hak website?",
         "A Cloud Hak website is a fast, mobile-first site engineered around one goal: converting visitors into enquiries and bookings. Built on clean static foundations, it loads instantly, ranks well and integrates directly with your CRM and chatbot."),
        ["Conversion-focused page structure", "Mobile-first responsive design", "Lightning-fast static build",
         "SEO-ready pages and metadata", "Contact forms and click-to-call CTAs", "Analytics and tracking setup"],
        ["Clinics and dental practices", "Trades and home services", "Hospitality and venues",
         "Coaches and consultants", "Local professional services"],
        [("Starter", "&pound;150", "A clean one-page site that converts.",
          ["Single-page website", "Mobile responsive", "Contact form", "Basic SEO setup", "Go live in days"], False),
         ("Standard", "&pound;300", "A full multi-page business site.",
          ["Up to 6 pages", "Conversion copywriting", "On-page SEO", "CRM &amp; chatbot ready", "Analytics setup"], True),
         ("Advanced", "&pound;500", "A premium site for serious growth.",
          ["10+ pages", "Bespoke design", "Advanced SEO", "Booking integration", "Priority delivery"], False)],
        [("Plan", "We map your services, audience and the actions you want visitors to take."),
         ("Build", "We design and build a fast, conversion-focused site — reviewed with you before launch."),
         ("Launch", "We go live, connect your CRM and tracking, and hand over a site that works.")],
        [("What is a Cloud Hak website?", "A fast, mobile-first website engineered to convert visitors into enquiries and bookings, integrated with your CRM and chatbot."),
         ("Who are websites for?", "Local service businesses such as clinics, trades, hospitality, coaches and professional services."),
         ("How much does a website cost?", "Websites start at £150 for a Starter site, £300 Standard and £500 Advanced."),
         ("How long does it take?", "Most websites launch within days to two weeks, depending on the number of pages and content."),
         ("Can you write the content?", "Yes. We offer conversion copywriting on Standard and Advanced builds so your pages sell, not just describe.")],
        [("Best for", "Local businesses"), ("From", "£150"), ("Build time", "Days"), ("Mobile", "First-class")],
        "Professional Websites for Local Businesses — Cloud Hak",
        "Custom-built, lightning-fast, mobile-first websites for local businesses. Designed to convert visitors into customers. From £150.",
        "Websites")

    service_page(
        "crm", "Stop Losing Leads. Automate Everything.",
        "Cloud Hak CRM puts your entire customer pipeline on autopilot — lead capture, follow-ups, appointments and reviews, all handled automatically.",
        ("What is Cloud Hak CRM?",
         "Cloud Hak CRM is a fully managed customer management system that captures every lead, follows up instantly across SMS, email and WhatsApp, books appointments and requests reviews — without you lifting a finger."),
        ["Visual sales pipelines", "Automated follow-up sequences", "SMS, email &amp; WhatsApp messaging",
         "Calendar &amp; appointment booking", "Automatic review requests", "Reporting and dashboards"],
        ["Businesses losing leads to slow follow-up", "Teams juggling spreadsheets", "Appointment-led services",
         "Multi-channel enquiry handlers", "Anyone wanting more reviews"],
        [("Starter", "&pound;100", "Get organised and follow up fast.",
          ["CRM setup", "1 pipeline", "Core automations", "Email support"], False),
         ("Standard", "&pound;200", "Full multi-channel automation.",
          ["Everything in Starter", "SMS &amp; email campaigns", "Appointment booking", "Review requests", "Reporting"], True),
         ("Advanced", "&pound;350", "Fully managed growth engine.",
          ["Everything in Standard", "WhatsApp integration", "Advanced automations", "Priority support"], False)],
        [("Connect", "We import your contacts and connect your lead sources, calendar and channels."),
         ("Automate", "We build your pipelines and follow-up sequences so no lead slips through."),
         ("Optimise", "We refine automations monthly based on what converts best for you.")],
        [("What is Cloud Hak CRM?", "A fully managed CRM that captures leads, automates follow-up across SMS, email and WhatsApp, books appointments and requests reviews."),
         ("Who is the CRM for?", "Any local business losing leads to slow follow-up or juggling enquiries across spreadsheets and inboxes."),
         ("How much does the CRM cost?", "CRM plans start at £100 Starter, £200 Standard and £350 Advanced per month."),
         ("How long does setup take?", "Most CRM setups are live within a few days, with automations refined in the first two weeks."),
         ("Will it work with my calendar?", "Yes. The CRM connects to your calendar for automated appointment booking and reminders.")],
        [("Best for", "Lead follow-up"), ("From", "£100/mo"), ("Setup", "Days"), ("Channels", "SMS, email, WhatsApp")],
        "Cloud Hak CRM — Your Business on Autopilot",
        "Cloud Hak CRM automates lead capture, follow-ups, appointments, reviews and reporting for local businesses. From £100/mo.",
        "CRM")

    service_page(
        "chatbots", "Your 24/7 Sales Team That Never Sleeps",
        "AI chatbots that answer questions instantly, qualify leads and book appointments around the clock — turning website visitors into customers.",
        ("What is a Cloud Hak AI chatbot?",
         "A Cloud Hak AI chatbot is a trained assistant on your website that answers customer questions in natural language, qualifies enquiries, captures contact details and books appointments directly into your calendar — 24 hours a day."),
        ["Trained on your business", "Instant question answering", "Lead qualification", "Appointment booking",
         "CRM integration", "Handover to a human when needed"],
        ["High-traffic websites losing leads", "Businesses with repetitive enquiries", "After-hours enquiry capture",
         "Appointment-led services", "Multilingual customer bases"],
        [("Starter", "&pound;150", "Answer FAQs and capture leads.",
          ["Website chatbot", "Trained on your FAQs", "Lead capture", "Email alerts"], False),
         ("Standard", "&pound;300", "Qualify leads and book appointments.",
          ["Everything in Starter", "Lead qualification", "Calendar booking", "CRM integration"], True),
         ("Advanced", "&pound;500", "Full conversational sales agent.",
          ["Everything in Standard", "Multilingual", "Custom workflows", "Priority tuning"], False)],
        [("Train", "We train the chatbot on your services, FAQs, tone and booking rules."),
         ("Deploy", "We add it to your website and connect it to your CRM and calendar."),
         ("Improve", "We review real conversations and keep improving answers and conversions.")],
        [("What is an AI chatbot?", "A trained AI assistant on your website that answers questions, qualifies leads and books appointments 24/7."),
         ("Who are chatbots for?", "Businesses with website traffic, repetitive enquiries or a need to capture leads after hours."),
         ("How much does a chatbot cost?", "Chatbots start at £150 Starter, £300 Standard and £500 Advanced."),
         ("How long does it take?", "Most chatbots are trained and live within a week, then refined from real conversations."),
         ("Can it book appointments?", "Yes. From the Standard tier the chatbot books directly into your connected calendar.")],
        [("Best for", "24/7 lead capture"), ("From", "£150"), ("Live in", "About a week"), ("Hours", "24/7")],
        "AI Chatbots That Turn Visitors Into Customers — Cloud Hak",
        "AI chatbots that answer questions, qualify leads and book appointments 24/7 for local businesses. From £150.",
        "Chatbots")

    service_page(
        "voice-ai", "Every Call Answered. Every Lead Captured.",
        "AI voice agents that answer, route and book calls 24/7 — so you never miss another lead, even after hours.",
        ("What is a Cloud Hak voice AI agent?",
         "A Cloud Hak voice AI agent is an intelligent phone assistant that answers inbound calls in a natural voice, books appointments, transfers urgent calls and logs everything to your CRM — capturing leads you would otherwise miss."),
        ["Inbound call handling", "Outbound follow-up campaigns", "Appointment booking", "Smart call transfer rules",
         "Multilingual options", "Automatic CRM call logging"],
        ["Businesses that miss calls", "After-hours enquiry handling", "Clinics and booking-led services",
         "Sales teams needing follow-up", "Multilingual local businesses"],
        [("Starter", "&pound;300", "Never miss an inbound call.",
          ["Inbound call answering", "Appointment booking", "Call logging", "Email summaries"], False),
         ("Professional", "&pound;500", "Inbound and outbound, fully managed.",
          ["Everything in Starter", "Outbound campaigns", "Call transfer rules", "CRM integration", "Priority support"], True),
         ("Enterprise", "Custom", "High-volume and multilingual.",
          ["Everything in Professional", "Multilingual agents", "Custom integrations", "Dedicated tuning"], False)],
        [("Configure", "We set up your call flows, booking rules and transfer logic to match your business."),
         ("Connect", "We connect the agent to your phone number, calendar and CRM."),
         ("Refine", "We review call recordings and tune the agent for better outcomes.")],
        [("What is a voice AI agent?", "An AI phone assistant that answers calls in a natural voice, books appointments, transfers urgent calls and logs everything to your CRM."),
         ("Who is voice AI for?", "Businesses that miss calls, need after-hours cover or want every enquiry captured and booked."),
         ("How much does voice AI cost?", "Voice AI starts at £300 Starter and £500 Professional, with custom Enterprise pricing for high volume."),
         ("How long does it take?", "Most voice agents are configured and live within one to two weeks."),
         ("Can it handle multiple languages?", "Yes. Multilingual agents are available on the Enterprise tier for diverse customer bases.")],
        [("Best for", "Missed-call recovery"), ("From", "£300/mo"), ("Live in", "1–2 weeks"), ("Cover", "24/7")],
        "AI Voice Agents — Never Miss a Call Again — Cloud Hak",
        "AI voice agents answer, route and book calls 24/7 for local businesses, so you never miss a lead. From £300/mo.",
        "Voice AI")

    service_page(
        "seo", "Be the First Business They See on Google",
        "Local SEO that gets you found — optimised Google profiles, citations and on-page SEO that drive calls, clicks and foot traffic.",
        ("What is Cloud Hak local SEO?",
         "Cloud Hak local SEO is a managed service that optimises your Google Business Profile, builds consistent citations and improves your on-page SEO so your business ranks higher in local search and Google Maps — bringing in more nearby customers."),
        ["Google Business Profile optimisation", "Local keyword targeting", "On-page SEO improvements",
         "Citation building &amp; clean-up", "Review strategy", "Monthly ranking reports"],
        ["Businesses invisible on Google", "Service-area &amp; local trades", "Multi-location businesses",
         "Clinics and practices", "Anyone wanting more foot traffic"],
        [("Starter", "&pound;100", "Get your Google profile right.",
          ["Google Business Profile setup", "Core citations", "Keyword research", "Monthly report"], False),
         ("Standard", "&pound;200", "Climb the local rankings.",
          ["Everything in Starter", "On-page SEO", "Citation building", "Review strategy"], True),
         ("Advanced", "&pound;300", "Dominate your local market.",
          ["Everything in Standard", "Content optimisation", "Competitor tracking", "Priority support"], False)],
        [("Audit", "We audit your Google profile, citations and on-page SEO to find the gaps."),
         ("Optimise", "We fix your profile, build citations and improve your pages for local keywords."),
         ("Report", "We track rankings monthly and keep improving your local visibility.")],
        [("What is local SEO?", "A managed service that optimises your Google Business Profile, citations and on-page SEO to rank higher in local search and Maps."),
         ("Who is SEO for?", "Local businesses that are hard to find on Google or want more calls, clicks and foot traffic."),
         ("How much does SEO cost?", "Local SEO starts at £100 Starter, £200 Standard and £300 Advanced per month."),
         ("How long does SEO take?", "Local SEO improvements often show within weeks, with stronger rankings building over two to three months."),
         ("Do you guarantee rankings?", "No reputable agency can guarantee exact rankings, but we focus on the proven factors that reliably improve local visibility.")],
        [("Best for", "Local visibility"), ("From", "£100/mo"), ("Results", "Weeks"), ("Focus", "Google &amp; Maps")],
        "Local SEO — Get Found on Google — Cloud Hak",
        "Local SEO for local businesses: Google Business Profile optimisation, citations and on-page SEO that drive enquiries. From £100/mo.",
        "SEO")

# ---------------- PRICING ----------------
def build_pricing():
    indiv = "".join(
        f"""<article class="card rv"><div class="ico">{i}</div><h3>{t}</h3>
<p>{d}</p><div class="price grad-text" style="font-size:30px;font-weight:900;margin:10px 0">From {p}</div>
<a class="more" style="position:static" href="/claude/services/{s}/">View service &#8594;</a></article>"""
        for s, t, i, d, p in [
            ("websites", "Websites", SERVICES[0][2], "Fast local business websites.", "&pound;150"),
            ("crm", "CRM", SERVICES[1][2], "Automated pipelines and follow-up.", "&pound;100"),
            ("chatbots", "Chatbots", SERVICES[2][2], "24/7 website lead capture.", "&pound;150"),
            ("voice-ai", "Voice AI", SERVICES[3][2], "AI phone answering and booking.", "&pound;300"),
            ("seo", "SEO", SERVICES[4][2], "Local Google visibility.", "&pound;100"),
        ])
    bundles = """<div class="tiers">
<div class="tier rv"><h3>Starter</h3><div class="price">&pound;150<small>/mo</small></div>
<p class="muted">For businesses getting organised.</p>
<ul class="flist"><li>Cloud Hak CRM setup</li><li>Core automations</li><li>Lead capture forms</li><li>Monthly report</li><li>Email support</li><li>No long contract</li></ul>
<a class="btn btn-gho btn-block" href="/claude/contact/">Get Started</a></div>
<div class="tier feat rv"><span class="tag">RECOMMENDED</span><h3>Growth</h3><div class="price">&pound;300<small>/mo</small></div>
<p class="muted">Everything working together.</p>
<ul class="flist"><li>Everything in Starter</li><li>Professional website</li><li>AI chatbot</li><li>Email &amp; SMS campaigns</li><li>Local SEO</li><li>Monthly optimisation</li><li>Priority support</li></ul>
<a class="btn btn-pri btn-block" href="/claude/contact/">Get Started</a></div>
<div class="tier rv"><h3>Scale</h3><div class="price">&pound;500<small>/mo</small></div>
<p class="muted">For market leaders.</p>
<ul class="flist"><li>Everything in Growth</li><li>Voice AI agent</li><li>Full automation management</li><li>Advanced reporting</li><li>Quarterly strategy</li><li>Priority support</li></ul>
<a class="btn btn-gho btn-block" href="/claude/contact/">Get Started</a></div>
</div>"""
    faqs = [
        ("Are prices fixed?", "Published prices cover standard scopes. We confirm any extras clearly before work starts — no surprises."),
        ("Do I need a bundle?", "Bundles are best value when you want CRM, website, AI and SEO working together under one monthly fee."),
        ("Is there a long contract?", "No. Packages are transparent and month to month, with terms agreed before launch."),
        ("Can I start with one service?", "Yes. Many clients begin with a single service and add automation as results grow."),
        ("Do prices include VAT?", "Prices are shown in pounds sterling. VAT treatment is confirmed in your written proposal."),
        ("What payment methods do you accept?", "We confirm payment options during onboarding and keep billing simple for UK businesses."),
        ("Can I change plans later?", "Absolutely. You can upgrade, downgrade or add services as your needs change."),
        ("Is the consultation really free?", "Yes — the first consultation is completely free with no obligation."),
    ]
    hero = """<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">Pricing</span>
<h1 style="margin:20px 0;max-width:820px">Simple, <span class="grad-text">Transparent</span> Pricing</h1>
<p class="lead">Choose individual services or a monthly growth bundle. Every recommendation is scoped around your goals.</p>
<dl class="glance"><div><dt>Currency</dt><dd>GBP (&pound;)</dd></div><div><dt>Bundles from</dt><dd>&pound;150/mo</dd></div><div><dt>Services from</dt><dd>&pound;100</dd></div><div><dt>Consultation</dt><dd>Free</dd></div></dl>
</div></section>"""
    body = hero + f"""<section><div class="wrap" data-toggle>
<div class="sec-head center"><span class="eyebrow">Choose your path</span>
<h2 style="margin-top:18px">Two simple ways to work with us</h2></div>
<div style="display:flex;gap:10px;justify-content:center;margin-bottom:40px;flex-wrap:wrap">
<button class="btn btn-gho btn-sm on" data-tab="bundles" type="button">Monthly Bundles</button>
<button class="btn btn-gho btn-sm" data-tab="indiv" type="button">Individual Services</button></div>
<div data-panel="bundles">{bundles}</div>
<div data-panel="indiv" hidden><div class="grid g3">{indiv}</div></div>
</div></section>""" + faq_section("Pricing FAQs", faqs) \
        + cta("Not sure what you need?", "Book a free consultation and we will map the right setup for your budget and goals.")
    page("pricing/index.html", "Pricing — Cloud Hak",
         "Simple, transparent pricing for Cloud Hak services and monthly bundles. Bundles from £150/mo, individual services from £100.",
         body, active="pricing",
         ld=[breadcrumb([("Home", BASE + "/"), ("Pricing", BASE + "/pricing/")]), faqld(faqs)],
         slug="pricing/")

# ---------------- ABOUT ----------------
def build_about():
    faqs = [
        ("Who founded Cloud Hak?", "Nima Hakimmaani founded Cloud Hak to make advanced business technology accessible to local companies."),
        ("Where is Cloud Hak based?", "Cloud Hak is based in Brighton & Hove, UK, with client work also connected to Stockholm, Sweden."),
        ("What makes Cloud Hak different?", "We combine human strategy with AI-assisted execution to deliver useful systems quickly, transparently and affordably."),
        ("Do you only work with local businesses?", "Our focus is local service businesses, but the same systems work for any business that relies on leads and follow-up."),
    ]
    hero = """<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">About Cloud Hak</span>
<h1 style="margin:20px 0;max-width:920px">Making Enterprise-Grade Tech <span class="grad-text">Accessible to Every Local Business</span></h1>
<p class="lead">Cloud Hak helps local businesses use the same automation, CRM and AI advantages that larger companies take for granted.</p>
<dl class="glance"><div><dt>Founder</dt><dd>Nima Hakimmaani</dd></div><div><dt>Model</dt><dd>Humans + AI</dd></div><div><dt>Values</dt><dd>Speed &amp; transparency</dd></div><div><dt>Locations</dt><dd>Hove &amp; Stockholm</dd></div></dl>
</div></section>"""
    story = """<section><div class="wrap"><div class="split">
<div><span class="eyebrow">Our story</span><h2 style="margin:18px 0 16px">Nima's Story</h2>
<p class="muted">Nima Hakimmaani founded Cloud Hak after years of running his own local businesses. He experienced first-hand how difficult it was for small businesses to access the same technology that big corporations take for granted. Cloud Hak was born to change that.</p>
<p class="muted" style="margin-top:16px">Today, Cloud Hak gives local businesses an unfair advantage: enterprise-grade websites, CRM, AI and automation — without the enterprise price tag or complexity.</p></div>
<div class="glass-card"><span class="eyebrow">Our team</span><h3 style="font-size:22px;margin:16px 0 12px">Humans + AI Agents</h3>
<p class="muted">Our team combines human expertise with AI efficiency. Nima leads strategy and client relationships, while our AI agents, Nemo and Hermie, handle execution — building websites, managing CRMs, deploying chatbots and running automations at scale.</p></div>
</div></div></section>"""
    values = """<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">What we stand for</span><h2 style="margin-top:18px">Our Values</h2></div>
<div class="grid g4">
<div class="card rv"><div class="ico">&#9889;</div><h3>Speed</h3><p>Useful systems should launch in days and weeks, not drift for months.</p></div>
<div class="card rv"><div class="ico">&#128270;</div><h3>Transparency</h3><p>You always know what is being built, why it matters and what it costs.</p></div>
<div class="card rv"><div class="ico">&#127919;</div><h3>Results Over Promises</h3><p>We focus on response time, lead capture, bookings and practical growth.</p></div>
<div class="card rv"><div class="ico">&#127757;</div><h3>Accessibility</h3><p>Advanced technology should be available to local businesses, not only large firms.</p></div>
</div>
<div class="split" style="margin-top:56px;align-items:center">
<div class="case-visual rv"><span class="pill">Where we work</span><b>Brighton &amp; Hove<br>&amp; Stockholm</b><p style="color:rgba(255,255,255,.9);margin-top:10px">Local roots, international reach.</p></div>
<div><h2 style="margin-bottom:16px">Local roots, international reach</h2>
<p class="muted">We are proudly based in Brighton & Hove on the UK south coast, with active client work connected to Stockholm, Sweden. Wherever you are, we build systems that work for local businesses serving real communities.</p></div>
</div></div></section>"""
    body = hero + story + values + faq_section("About FAQs", faqs) \
        + cta("Let's work together", "Tell us what you want to grow and we will show you the practical route to get there.")
    page("about/index.html", "About Cloud Hak — AI-Powered Agency for Local Business",
         "Cloud Hak makes enterprise-grade websites, CRM, AI and automation accessible to local businesses. Founded by Nima Hakimmaani in Brighton & Hove.",
         body, active="about",
         ld=[breadcrumb([("Home", BASE + "/"), ("About", BASE + "/about/")]), faqld(faqs)],
         slug="about/")

# ---------------- WORK ----------------
def build_work():
    projects = """<div class="grid g3">
<article class="card click rv"><div class="ico">&#127973;</div><h3>Airway Clinic Stockholm</h3>
<p>Bilingual website, AI chatbot and an automated patient pipeline for a specialist clinic.</p>
<a class="more" href="/claude/contact/">Want results like these? &#8594;</a></article>
<article class="card click rv"><div class="ico">&#129463;</div><h3>Brighton Dental Practice</h3>
<p>CRM automations and instant follow-up that lifted lead conversion by 35%.</p>
<a class="more" href="/claude/contact/">Discuss a similar build &#8594;</a></article>
<article class="card click rv"><div class="ico">&#127939;</div><h3>Hove Physiotherapy</h3>
<p>Website, CRM and after-hours voice AI for reliable missed-call recovery.</p>
<a class="more" href="/claude/contact/">Discuss a similar build &#8594;</a></article>
</div>"""
    faqs = [
        ("What results did Airway Clinic Stockholm get?", "Airway Clinic booked 40+ consultations via chatbot in the first month and reached 60-second lead response times with zero missed after-hours calls."),
        ("What kind of work does Cloud Hak show?", "We showcase websites, CRM systems, chatbots, voice AI and local SEO projects that measurably improve lead handling."),
        ("Can my business get similar results?", "Results depend on your offer, traffic and follow-up, but the same systems adapt to many local businesses."),
        ("Can I see a live demo?", "Yes. Book a free consultation and we will walk you through a working chatbot, CRM and automation demo."),
    ]
    hero = """<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">Our work</span>
<h1 style="margin:20px 0;max-width:820px">See What We've <span class="grad-text">Built</span></h1>
<p class="lead">Practical systems that capture leads, improve response speed and cut manual admin.</p>
<dl class="glance"><div><dt>Featured</dt><dd>Airway Clinic</dd></div><div><dt>Bookings</dt><dd>40+ in month one</dd></div><div><dt>Response</dt><dd>60 seconds</dd></div><div><dt>Scope</dt><dd>Web, chatbot, CRM</dd></div></dl>
</div></section>"""
    featured = """<section><div class="wrap"><div class="split">
<div class="case-visual rv"><span class="pill">Featured case study</span><b>Airway Clinic<br>Stockholm</b><p style="color:rgba(255,255,255,.9);margin-top:10px">Bilingual website &middot; AI chatbot &middot; automated pipeline</p></div>
<div><span class="eyebrow">Case study</span><h2 style="margin:18px 0 16px">From no online presence to a booked-out pipeline</h2>
<p class="muted">Airway Clinic Stockholm needed a credible online presence and a faster way to manage new patient enquiries. Cloud Hak built a bilingual website in English and Swedish, deployed an AI chatbot and automated the entire patient pipeline.</p>
<ul class="flist" style="margin-top:20px"><li>40+ consultations booked via chatbot in the first month</li><li>60-second lead response time</li><li>Zero missed after-hours calls</li><li>Manual follow-up replaced with CRM automations</li></ul>
<a class="btn btn-pri" style="margin-top:26px" href="/claude/contact/">Book your consultation</a></div>
</div></div></section>"""
    body = hero + featured + f"""<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Selected projects</span><h2 style="margin-top:18px">More of our work</h2>
<p style="margin-left:auto;margin-right:auto">A snapshot of systems we have built for local businesses.</p></div>{projects}</div></section>""" \
        + faq_section("Work FAQs", faqs) + cta("Want results like these?", "Book a consultation and we will map the exact system your business needs.")
    page("work/index.html", "Our Work — Cloud Hak",
         "See Cloud Hak's work: bilingual websites, AI chatbots, CRM automations and voice AI that deliver real results for local businesses.",
         body, active="work",
         ld=[breadcrumb([("Home", BASE + "/"), ("Work", BASE + "/work/")]), faqld(faqs)],
         slug="work/")

# ---------------- CONTACT ----------------
def build_contact():
    faqs = [
        ("How do I book a Cloud Hak consultation?", "Complete the form or call 07800 920042. We will review your needs and suggest the best next step."),
        ("Is the consultation free?", "Yes. The first consultation is completely free with no obligation."),
        ("What should I prepare?", "Bring your website, current lead sources, main services and the biggest bottleneck in your follow-up process."),
        ("How quickly will you reply?", "We aim to respond to every enquiry within one working day."),
    ]
    hero = """<section class="hero"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">Contact</span>
<h1 style="margin:20px 0;max-width:820px">Let's Talk About <span class="grad-text">Growing Your Business</span></h1>
<p class="lead">Tell us what you need help with and we will respond with a practical, no-pressure recommendation.</p>
</div></section>"""
    form = """<section><div class="wrap"><div class="cgrid">
<form class="glass-card" action="https://services.leadconnectorhq.com/hooks/BjKd0mLr" method="post" data-contact">
<h2 style="font-size:24px;margin-bottom:8px">Book your free consultation</h2>
<p class="muted" style="margin-bottom:22px">No obligation. We reply within one working day.</p>
<div class="frow"><div class="field"><label for="name">Name</label><input id="name" name="name" required></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div></div>
<div class="frow"><div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel"></div>
<div class="field"><label for="business">Business name</label><input id="business" name="business"></div></div>
<div class="field"><label for="need">What do you need help with?</label>
<select id="need" name="need"><option>Website</option><option>CRM</option><option>Chatbot</option><option>Voice AI</option><option>SEO</option><option>Not sure</option></select></div>
<div class="field"><label for="message">Message</label><textarea id="message" name="message" rows="5" required></textarea></div>
<button class="btn btn-pri btn-block" type="submit">Send Enquiry</button>
<p class="fstatus muted" data-status></p>
</form>
<aside>
<div class="info-card"><h3>Prefer to talk?</h3>
<p>Call us at <a class="grad-text" style="font-weight:700" href="tel:+447800920042">07800 920042</a><br>or email <a class="grad-text" style="font-weight:700" href="mailto:info@cloud-hak.com">info@cloud-hak.com</a>.</p></div>
<div class="info-card"><h3>Find us</h3>
<address style="font-style:normal;color:var(--mut);line-height:1.9">117 Holmes Avenue<br>Hove, East Sussex BN3 7LF<br>United Kingdom</address></div>
<div class="case-visual" role="img" aria-label="Map-style panel showing Cloud Hak based in Brighton and Hove"><span class="pill">Based in</span><b>Brighton &amp; Hove</b><p style="color:rgba(255,255,255,.9);margin-top:8px">Serving local businesses across the UK &amp; Europe</p></div>
</aside>
</div></div></section>"""
    local_ld = {
        "@context": "https://schema.org", "@type": "LocalBusiness", "name": "Cloud Hak Ltd",
        "url": "https://cloud-hak.com", "logo": "https://cloud-hak.com/assets/logo.png",
        "image": "https://cloud-hak.com/assets/logo.png", "email": "info@cloud-hak.com",
        "telephone": "+447800920042", "priceRange": "££",
        "address": ORG_LD["address"],
        "openingHours": "Mo-Fr 09:00-17:30"}
    body = hero + form + faq_section("Contact FAQs", faqs)
    page("contact/index.html", "Book a Free Consultation — Cloud Hak",
         "Contact Cloud Hak to book a free, no-obligation consultation about websites, CRM, AI chatbots, voice agents and local SEO.",
         body, active="contact",
         ld=[breadcrumb([("Home", BASE + "/"), ("Contact", BASE + "/contact/")]), local_ld, faqld(faqs)],
         slug="contact/")

# ---------------- LEGAL ----------------
def legal_page(slug, h1, intro, label, sections, faqs, meta_title, meta_desc):
    prose = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in sections)
    hero = f"""<section class="hero"><div class="orb orb-a"></div>
<div class="wrap"><span class="eyebrow">{label}</span>
<h1 style="margin:20px 0;max-width:840px">{h1}</h1>
<p class="lead">{intro}</p>
<p class="muted" style="margin-top:14px">Last updated: 28 May 2026</p>
</div></section>"""
    body = hero + f"""<section><div class="wrap"><article class="prose">{prose}</article></div></section>""" \
        + faq_section(f"{label} FAQs", faqs)
    page(f"{slug}/index.html", meta_title, meta_desc, body, active="",
         ld=[breadcrumb([("Home", BASE + "/"), (label, f"{BASE}/{slug}/")]), faqld(faqs)],
         slug=f"{slug}/")

def build_legal():
    legal_page(
        "privacy", "How Does Cloud Hak Protect Your Privacy?",
        "This policy explains how Cloud Hak Ltd collects, uses and protects personal data in line with UK GDPR.",
        "Privacy",
        [("What we collect",
          ["Cloud Hak Ltd collects only the personal data needed to respond to enquiries, provide services, manage client relationships and comply with legal obligations. This may include your name, email address, phone number, business name, website details, project notes and billing information."]),
         ("How we use your data",
          ["We use this data to communicate with you, prepare proposals, and deliver websites, CRM systems, chatbots, voice AI, SEO and support services. We do not sell personal data.",
           "We may share limited data with trusted service providers where required to deliver our work, such as hosting, CRM, analytics, email or automation tools."]),
         ("How long we keep it",
          ["We keep personal data only for as long as needed for the purpose collected, contractual records or legal requirements. We use reasonable technical and organisational measures to protect data from unauthorised access, loss or misuse."]),
         ("Your rights",
          ["Under UK GDPR, you may request access, correction, deletion, restriction or portability of your personal data. You may also object to certain processing. To exercise these rights, email info@cloud-hak.com.",
           "If you are unhappy with our response, you can contact the UK Information Commissioner's Office. This policy may be updated as our services or legal requirements change."])],
        [("What personal data does Cloud Hak collect?", "We collect contact details, business information and messages you send through forms, email, phone or project communication."),
         ("Why does Cloud Hak use personal data?", "We use personal data to respond to enquiries, deliver services, manage billing and meet legal obligations."),
         ("Can I request my data?", "Yes. You can request access, correction or deletion at any time by emailing info@cloud-hak.com."),
         ("Do you sell my data?", "No. Cloud Hak never sells personal data and only shares it with trusted providers needed to deliver our services.")],
        "Privacy Policy — Cloud Hak",
        "Cloud Hak's privacy policy: how we collect, use and protect your personal data in line with UK GDPR.")

    legal_page(
        "terms", "What Are Cloud Hak's Terms of Service?",
        "These terms explain the practical basis for working with Cloud Hak Ltd.",
        "Terms",
        [("Scope of services",
          ["These terms apply when Cloud Hak Ltd provides websites, CRM setup, AI chatbots, voice AI, SEO, automation, consulting or related digital services. A project begins when scope, deliverables, pricing and payment terms are agreed in writing."]),
         ("Client responsibilities",
          ["Clients are responsible for providing accurate business information, approvals, access to relevant accounts and lawful content. Cloud Hak will use reasonable skill and care to deliver the agreed work, but results such as rankings, leads or revenue cannot be guaranteed because they depend on market conditions, traffic, offer strength and client operations."]),
         ("Fees and payment",
          ["Fees, subscriptions and payment dates are set out in the proposal or invoice. Late payment may pause work or support. Third-party platforms, hosting, domains, messaging costs, advertising spend and software licences may be billed separately unless expressly included."]),
         ("Ownership",
          ["Final approved deliverables are assigned or licensed as stated in the proposal after payment is received. Pre-existing tools, templates, workflows and know-how remain the property of Cloud Hak or relevant third parties."]),
         ("Termination and liability",
          ["Either party may end ongoing services according to the agreed notice period. Cloud Hak is not liable for indirect loss, loss of profit or issues caused by third-party outages, unauthorised account changes or client-provided materials."])],
        [("What do these terms cover?", "These terms cover Cloud Hak services including websites, CRM, chatbots, voice AI, SEO and automation support."),
         ("When does work begin?", "Work begins after scope, pricing and payment terms are agreed in writing."),
         ("Who owns the final content?", "Client ownership of final approved deliverables is confirmed in the proposal, subject to payment and third-party licences."),
         ("Can I cancel ongoing services?", "Yes. Either party may end ongoing services according to the notice period agreed in your proposal.")],
        "Terms of Service — Cloud Hak",
        "Cloud Hak's terms of service for websites, CRM, AI chatbots, voice AI, SEO and automation support.")

# ---------------- 404 ----------------
def build_404():
    body = """<section class="hero" style="text-align:center"><div class="orb orb-a"></div><div class="orb orb-b"></div>
<div class="wrap"><span class="eyebrow">Error 404</span>
<h1 style="margin:22px auto;max-width:760px">This Page Has <span class="grad-text">Wandered Off</span></h1>
<p class="lead" style="margin:0 auto">The page you are looking for has moved or no longer exists. Let's get you back to growing your business.</p>
<div class="hero-cta" style="justify-content:center"><a class="btn btn-pri" href="/claude/">Back to Homepage</a>
<a class="btn btn-gho" href="/claude/contact/">Book Free Consultation</a></div>
</div></section>
<section style="background:var(--bg-1)"><div class="wrap">
<div class="sec-head center"><span class="eyebrow">Popular pages</span><h2 style="margin-top:18px">Pick up where you left off</h2></div>
<div class="grid g3">
<article class="card click rv"><div class="ico">&#129518;</div><h3>Our Services</h3><p>Websites, CRM, AI chatbots, voice agents and local SEO for local businesses.</p><a class="more" href="/claude/services/">Explore services &#8594;</a></article>
<article class="card click rv"><div class="ico">&#128176;</div><h3>Pricing</h3><p>Simple, transparent pricing with individual services and monthly bundles.</p><a class="more" href="/claude/pricing/">View pricing &#8594;</a></article>
<article class="card click rv"><div class="ico">&#128172;</div><h3>Book a Consultation</h3><p>Tell us about your business and we will recommend exactly what you need.</p><a class="more" href="/claude/contact/">Get in touch &#8594;</a></article>
</div></div></section>"""
    page("404.html", "Page Not Found (404) — Cloud Hak",
         "The page you are looking for could not be found. Explore Cloud Hak services, pricing and contact options.",
         body, active="", ld=None, slug="404")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_home()
    build_services_hub()
    build_service_pages()
    build_pricing()
    build_about()
    build_work()
    build_contact()
    build_legal()
    build_404()
    print("DONE")
