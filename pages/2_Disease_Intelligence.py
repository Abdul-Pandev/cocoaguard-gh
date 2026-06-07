import streamlit as st
from style import inject_css, section_heading, divider

st.set_page_config(page_title='FarmEye · Disease Intelligence', page_icon='🗺', layout='wide', initial_sidebar_state='expanded')
inject_css()

with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin:8px auto 16px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3DCC52,#C9A84C);border-radius:10px;font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-family:Syne,sans-serif;font-weight:800;font-size:1.1rem;color:#0A1A0C;margin-bottom:2px;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:0.68rem;color:#2D6B38;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:24px;">Sankofa Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    st.page_link("home.py",                         label="🏠  Dashboard")
    st.page_link("pages/1_Detection.py",            label="🔬  Detection")
    st.page_link("pages/2_Disease_Intelligence.py", label="🗺  Disease Intelligence")
    st.page_link("pages/3_Analytics.py",            label="📊  Analytics")
    st.page_link("pages/4_History.py",              label="🕘  History")
    st.page_link("pages/6_Impact.py",               label="🌍  Impact")
    st.page_link("pages/7_About.py",                label="ℹ  About")

st.markdown("""
<div class="hero" style="padding:36px 40px;margin-bottom:28px;">
  <div class="hero-label">Knowledge Base</div>
  <div class="hero-title" style="font-size:2rem;">🗺 Disease Intelligence</div>
  <div class="hero-body">Deep-dive knowledge on CSSVD — how it spreads, what it looks like, and how to contain it before it destroys an entire farm.</div>
</div>
""", unsafe_allow_html=True)

section_heading("🦠", "What Is CSSVD?")
c1, c2 = st.columns([3, 2], gap="large")
with c1:
    st.markdown("""
    <div class="feature-card">
      <p style="color:#0A1A0C;line-height:1.85;font-size:0.95rem;">
        <b style="color:#1E8C35;">Cocoa Swollen Shoot Virus Disease (CSSVD)</b> is one of the most devastating
        plant diseases in West Africa, caused by <i>Cacao swollen shoot virus</i> (CSSV) — a member of the <i>Badnavirus</i> genus.
      </p>
      <p style="color:#0A1A0C;line-height:1.85;font-size:0.95rem;">
        First recorded in Ghana in 1936, CSSVD has since destroyed over <b style="color:#C0392B;">300 million cocoa trees</b>.
        It spreads primarily through mealybug vectors feeding on infected trees and moving to healthy ones.
      </p>
      <p style="color:#0A1A0C;line-height:1.85;font-size:0.95rem;">
        There is <b style="color:#C0392B;">no cure</b>. The only management strategy is early detection followed by
        controlled removal (roguing) of infected trees to prevent further spread.
      </p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="feature-card" style="background:#FEF9F9;">
      <div class="icon">⚡</div><div class="title">Fast Facts</div>
      <div style="display:flex;flex-direction:column;gap:10px;margin-top:12px;">
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#C0392B;min-width:18px;">▸</span><span style="color:#0A1A0C;">First detected in Ghana: <b>1936</b></span></div>
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#C0392B;min-width:18px;">▸</span><span style="color:#0A1A0C;">Trees destroyed: <b>&gt;300 million</b></span></div>
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#C0392B;min-width:18px;">▸</span><span style="color:#0A1A0C;">Affected area: <b>~500,000 ha</b></span></div>
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#C0392B;min-width:18px;">▸</span><span style="color:#0A1A0C;">Vector: <b>Mealybugs (Planococcus spp.)</b></span></div>
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#C0392B;min-width:18px;">▸</span><span style="color:#0A1A0C;">Cure: <b style="color:#C0392B;">None — prevention only</b></span></div>
        <div style="display:flex;gap:10px;font-size:0.85rem;"><span style="color:#1E8C35;min-width:18px;">▸</span><span style="color:#0A1A0C;">Solution: <b style="color:#1E8C35;">Early detection + roguing</b></span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

divider()
section_heading("🔍", "Recognising Symptoms")
s1, s2, s3 = st.columns(3)
symptoms = [
    ("🍃", "Leaf Symptoms", ["Red vein banding along midrib & veins", "Chlorotic (yellow-green) mottling on young leaves", "Leaf distortion and cupping", "Reduced leaf size on new flushes"]),
    ("🌿", "Stem & Pod Symptoms", ["Swollen, distorted stems and chupons", "Lesions and necrosis on main trunk", "Swollen, misshapen pods", "Premature pod drop"]),
    ("🌱", "Tree-level Signs", ["Reduced canopy and sparse foliage", "Stunted overall growth", "Dieback of branches over time", "Complete tree death in late stages"]),
]
for col, (icon, title, points) in zip([s1, s2, s3], symptoms):
    with col:
        bullets = "".join(f'<div style="display:flex;gap:8px;margin-bottom:7px;font-size:0.84rem;"><span style="color:#1E8C35;">•</span><span style="color:#0A1A0C;">{p}</span></div>' for p in points)
        st.markdown(f'<div class="feature-card"><div class="icon">{icon}</div><div class="title">{title}</div><div style="margin-top:10px;">{bullets}</div></div>', unsafe_allow_html=True)

divider()
section_heading("🐛", "How CSSVD Spreads")
st.markdown("""
<div class="feature-card" style="margin-bottom:16px;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;">
    <div><div style="color:#A67C00;font-weight:700;font-family:'Syne',sans-serif;margin-bottom:8px;">① Mealybug Feeding</div><div style="color:#0A1A0C;font-size:0.85rem;line-height:1.7;">Mealybugs acquire the virus by feeding on infected trees for as little as 15 minutes.</div></div>
    <div><div style="color:#A67C00;font-weight:700;font-family:'Syne',sans-serif;margin-bottom:8px;">② Movement</div><div style="color:#0A1A0C;font-size:0.85rem;line-height:1.7;">Mealybugs walk between adjacent trees or are carried by ants, wind, and human activity.</div></div>
    <div><div style="color:#A67C00;font-weight:700;font-family:'Syne',sans-serif;margin-bottom:8px;">③ Inoculation</div><div style="color:#0A1A0C;font-size:0.85rem;line-height:1.7;">A single viruliferous mealybug can infect a healthy tree within minutes of feeding.</div></div>
    <div><div style="color:#A67C00;font-weight:700;font-family:'Syne',sans-serif;margin-bottom:8px;">④ Incubation</div><div style="color:#0A1A0C;font-size:0.85rem;line-height:1.7;">Symptoms appear 3–6 months after infection. Nearby trees may already be infected by then.</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

divider()
section_heading("🛡", "Management & Control")
m1, m2 = st.columns(2)
with m1:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🌿</div><div class="title">Recommended Actions</div>
      <div style="margin-top:10px;">
        <div style="display:flex;gap:8px;margin-bottom:9px;font-size:0.85rem;"><span style="color:#1E8C35;font-weight:700;">1.</span><span style="color:#0A1A0C;"><b>Regular monitoring</b> — Inspect farms every 2–4 weeks.</span></div>
        <div style="display:flex;gap:8px;margin-bottom:9px;font-size:0.85rem;"><span style="color:#1E8C35;font-weight:700;">2.</span><span style="color:#0A1A0C;"><b>Immediate isolation</b> — Flag and isolate suspected trees immediately.</span></div>
        <div style="display:flex;gap:8px;margin-bottom:9px;font-size:0.85rem;"><span style="color:#1E8C35;font-weight:700;">3.</span><span style="color:#0A1A0C;"><b>Controlled roguing</b> — Remove infected trees under COCOBOD supervision.</span></div>
        <div style="display:flex;gap:8px;margin-bottom:9px;font-size:0.85rem;"><span style="color:#1E8C35;font-weight:700;">4.</span><span style="color:#0A1A0C;"><b>Buffer zone</b> — Remove symptomless trees within a 3-tree buffer radius.</span></div>
        <div style="display:flex;gap:8px;font-size:0.85rem;"><span style="color:#1E8C35;font-weight:700;">5.</span><span style="color:#0A1A0C;"><b>Replant</b> — Use CRIG-approved hybrid seedlings.</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <div class="feature-card" style="background:#F7FCF8;">
      <div class="icon">📞</div><div class="title">Who to Contact</div>
      <div style="margin-top:10px;display:flex;flex-direction:column;gap:12px;">
        <div style="background:#F0FAF2;border:1px solid rgba(30,140,53,0.2);border-radius:8px;padding:12px;">
          <div style="color:#0A1A0C;font-weight:600;font-size:0.88rem;">COCOBOD</div>
          <div style="color:#2D6B38;font-size:0.8rem;margin-top:2px;">Ghana Cocoa Board — national regulatory body</div>
        </div>
        <div style="background:#F0FAF2;border:1px solid rgba(30,140,53,0.2);border-radius:8px;padding:12px;">
          <div style="color:#0A1A0C;font-weight:600;font-size:0.88rem;">CRIG</div>
          <div style="color:#2D6B38;font-size:0.8rem;margin-top:2px;">Cocoa Research Institute of Ghana</div>
        </div>
        <div style="background:#F0FAF2;border:1px solid rgba(30,140,53,0.2);border-radius:8px;padding:12px;">
          <div style="color:#0A1A0C;font-weight:600;font-size:0.88rem;">Local Extension Officer</div>
          <div style="color:#2D6B38;font-size:0.8rem;margin-top:2px;">Your district agricultural extension officer (MOFA)</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

divider()
st.markdown('<p style="color:#2D6B38;font-size:0.72rem;text-align:center;">Sankofa Intelligence · Ghana · 2026</p>', unsafe_allow_html=True)
