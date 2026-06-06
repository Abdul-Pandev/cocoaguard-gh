import streamlit as st
from style import inject_css, section_heading, divider

st.set_page_config(page_title='FarmEye · Impact', page_icon='🌍', layout='wide', initial_sidebar_state='expanded')
inject_css()

with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin:8px auto 16px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3DCC52,#C9A84C);border-radius:10px;font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-family:Syne,sans-serif;font-weight:800;font-size:1.1rem;background:linear-gradient(90deg,#3DCC52,#E8C96A);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:0.68rem;color:#7AAB80;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:24px;">Sankofa Intelligence</div>', unsafe_allow_html=True)
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
  <div class="hero-label">Why This Matters</div>
  <div class="hero-title" style="font-size:2rem;">🌍 Impact</div>
  <div class="hero-body">Ghana's cocoa sector supports over 800,000 farming families. CSSVD threatens the livelihoods, food security, and futures of millions. FarmEye is our contribution to turning the tide.</div>
</div>
""", unsafe_allow_html=True)

section_heading("📊", "The Scale of the Problem")
i1, i2, i3 = st.columns(3)
with i1: st.markdown('<div class="impact-block"><div class="impact-num">800K+</div><div class="impact-lbl">Farming families dependent on cocoa in Ghana</div></div>', unsafe_allow_html=True)
with i2: st.markdown('<div class="impact-block"><div class="impact-num">300M+</div><div class="impact-lbl">Cocoa trees destroyed by CSSVD since 1936</div></div>', unsafe_allow_html=True)
with i3: st.markdown('<div class="impact-block"><div class="impact-num">$1.5B+</div><div class="impact-lbl">Annual cocoa export value at risk</div></div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
i4, i5, i6 = st.columns(3)
with i4: st.markdown('<div class="impact-block"><div class="impact-num">~17%</div><div class="impact-lbl">Of Ghana\'s GDP comes from cocoa</div></div>', unsafe_allow_html=True)
with i5: st.markdown('<div class="impact-block"><div class="impact-num">500K ha</div><div class="impact-lbl">Of farmland affected by CSSVD</div></div>', unsafe_allow_html=True)
with i6: st.markdown('<div class="impact-block"><div class="impact-num">60%</div><div class="impact-lbl">Of infections missed until late stage without AI</div></div>', unsafe_allow_html=True)

divider()
section_heading("🌱", "What Early Detection Changes")
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">⏱</div><div class="title">Time Is Everything</div>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">CSSVD spreads silently for 3–6 months before visible symptoms appear. By the time a farmer notices damage, dozens of surrounding trees may already be infected.</p>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">AI-powered early detection using leaf images can <b style="color:#3DCC52;">catch CSSVD weeks before visible symptoms</b> — giving farmers a critical window to act.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">💰</div><div class="title">Economic Protection</div>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">Each mature cocoa tree represents years of investment. A single late-stage outbreak can wipe out an entire season's harvest — or an entire farm.</p>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">Early detection limits roguing to only the infected cluster, <b style="color:#3DCC52;">saving 70–90% of surrounding trees</b> that would otherwise fall victim to delayed response.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
c3, c4 = st.columns(2)
with c3:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🌐</div><div class="title">Democratising Expertise</div>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">Ghana has fewer than 1,500 agricultural extension officers serving over 800,000 cocoa farmers. FarmEye puts expert-level disease recognition directly in every farmer's pocket — <b style="color:#3DCC52;">no specialist required</b>.</p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🗣</div><div class="title">No Language Barrier</div>
      <p style="color:#C8DFC9;font-size:0.88rem;line-height:1.75;">By delivering results in Twi, Dagbani, Ewe, and English via audio, FarmEye reaches farmers who may not be literate in written English — ensuring the most vulnerable communities are not left behind.</p>
    </div>
    """, unsafe_allow_html=True)

divider()
section_heading("🎯", "SDG Alignment")
sdgs = [
    ("SDG 1","No Poverty","Protecting cocoa incomes directly prevents rural households from falling into poverty."),
    ("SDG 2","Zero Hunger","Healthy cocoa farms ensure food security and livelihoods for farming families."),
    ("SDG 8","Decent Work","Supporting cocoa farmers protects Ghana's largest rural employment sector."),
    ("SDG 9","Innovation","AI-powered agri-tech brings frontier technology to smallholder farmers."),
    ("SDG 15","Life on Land","Healthy farms reduce pressure to clear more forest for replacement planting."),
    ("SDG 17","Partnerships","FarmEye builds on collaboration between academia, COCOBOD, and farmers."),
]
g1, g2, g3 = st.columns(3)
for col, (num, name, desc) in zip([g1,g2,g3,g1,g2,g3], sdgs):
    with col:
        st.markdown(f"""
        <div class="feature-card" style="margin-bottom:14px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <span style="background:rgba(201,168,76,0.15);border:1px solid rgba(201,168,76,0.3);border-radius:6px;padding:3px 8px;font-family:'Syne',sans-serif;font-weight:700;font-size:0.75rem;color:#E8C96A;">{num}</span>
            <span style="font-family:'Syne',sans-serif;font-weight:700;font-size:0.9rem;">{name}</span>
          </div>
          <div style="color:#7AAB80;font-size:0.82rem;line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

divider()
st.markdown('<p style="color:#3A5C3E;font-size:0.72rem;text-align:center;">Sankofa Intelligence · Ghana · 2026</p>', unsafe_allow_html=True)
