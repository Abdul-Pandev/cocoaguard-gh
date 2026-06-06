import streamlit as st
from style import inject_css, app_bar, section_heading, divider
import datetime

st.set_page_config(
    page_title='FarmEye · Dashboard',
    page_icon='🌿',
    layout='wide',
    initial_sidebar_state='expanded'
)

inject_css()

# ── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin: 8px auto 16px; width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,#3DCC52,#C9A84C); border-radius:10px; font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-family:Syne,sans-serif; font-weight:800; font-size:1.1rem; background:linear-gradient(90deg,#3DCC52,#E8C96A); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:4px;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:0.68rem; color:#7AAB80; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:24px;">Sankofa Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    st.page_link("home.py", label="🏠 Dashboard")
    st.page_link("pages/1_Detection.py", label="🔬 Detection")
    st.page_link("pages/2_Disease_Intelligence.py", label="🗺 Disease Intelligence")
    st.page_link("pages/3_Analytics.py", label="📊 Analytics")
    st.page_link("pages/4_History.py", label="🕘 History")
    st.page_link("pages/6_Impact.py", label="🌍 Impact")
    st.page_link("pages/7_About.py", label="ℹ About")
    st.markdown('<div class="styled-divider" style="margin:20px 0;"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.72rem; color:#7AAB80; line-height:1.6;">Model: EfficientNetB3<br>Threshold: 0.65<br>Classes: CSSVD · Healthy</div>', unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">AI-Powered Early Warning System</div>
  <div class="hero-title">Guard Your Cocoa.<br><span>Protect Ghana's Future.</span></div>
  <div class="hero-body">
    FarmEye uses deep learning to detect Cocoa Swollen Shoot Virus Disease (CSSVD) 
    from a single photograph — giving farmers and extension officers an instant, 
    multilingual diagnosis before the damage becomes irreversible.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stats row ────────────────────────────────────────────────────
section_heading("📈", "At a Glance")

# Pull detection count from session state history
history = st.session_state.get('detection_history', [])
total_scans   = len(history)
cssvd_found   = sum(1 for h in history if h['result'] == 'cssvd')
healthy_found = total_scans - cssvd_found
avg_conf      = round(sum(h['confidence'] for h in history) / total_scans, 1) if total_scans else 0

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="stat-card"><div class="val">{total_scans}</div><div class="lbl">Total Scans</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-card"><div class="val" style="color:#E05A4E;">{cssvd_found}</div><div class="lbl">CSSVD Detected</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="stat-card"><div class="val">{healthy_found}</div><div class="lbl">Healthy Confirmed</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="stat-card"><div class="val" style="color:#C9A84C;">{avg_conf}%</div><div class="lbl">Avg Confidence</div></div>', unsafe_allow_html=True)

divider()

# ── Feature cards ────────────────────────────────────────────────
section_heading("🧩", "What You Can Do")

f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🔬</div>
      <div class="title">Disease Detection</div>
      <div class="desc">Upload or capture a photo of a cocoa leaf, stem, or pod to get an instant AI-powered CSSVD diagnosis with a confidence score.</div>
    </div>
    """, unsafe_allow_html=True)
with f2:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🗺</div>
      <div class="title">Disease Intelligence</div>
      <div class="desc">Understand CSSVD spread patterns, risk zones, and mealybug vector biology to make smarter farm management decisions.</div>
    </div>
    """, unsafe_allow_html=True)
with f3:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🕘</div>
      <div class="title">Detection History</div>
      <div class="desc">Every scan you run is saved locally so you can track patterns on your farm over time and share records with extension officers.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
f4, f5, f6 = st.columns(3)
with f4:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">📊</div>
      <div class="title">Analytics</div>
      <div class="desc">Explore the model's training data, performance charts, and evaluation metrics to understand how the AI was built and validated.</div>
    </div>
    """, unsafe_allow_html=True)
with f5:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🌍</div>
      <div class="title">Impact</div>
      <div class="desc">See how early CSSVD detection saves farms, livelihoods, and Ghana's position as one of the world's leading cocoa producers.</div>
    </div>
    """, unsafe_allow_html=True)
with f6:
    st.markdown("""
    <div class="feature-card">
      <div class="icon">🎙</div>
      <div class="title">Multilingual Audio</div>
      <div class="desc">Diagnosis results are spoken aloud in English, Twi, Dagbani, and Ewe — serving farmers across all regions of Ghana.</div>
    </div>
    """, unsafe_allow_html=True)

divider()

# ── Languages ────────────────────────────────────────────────────
section_heading("🗣", "Supported Languages")
st.markdown("""
<div style="margin: 12px 0 4px;">
  <span class="lang-chip">🇬🇭 English</span>
  <span class="lang-chip">🇬🇭 Twi</span>
  <span class="lang-chip">🇬🇭 Dagbani</span>
  <span class="lang-chip">🇬🇭 Ewe</span>
</div>
<p style="color:#7AAB80; font-size:0.85rem; margin-top:12px;">
  Audio feedback is generated for every diagnosis to ensure accessibility for farmers 
  regardless of literacy level or primary language.
</p>
""", unsafe_allow_html=True)

divider()

# ── CTA ──────────────────────────────────────────────────────────
st.markdown('<div style="text-align:center; padding: 20px 0 8px;">', unsafe_allow_html=True)
st.markdown('<p style="color:#7AAB80; font-size:0.8rem;">⚠ CocoaGuard is designed to assist — always consult a qualified agricultural officer for final decisions.</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#3A5C3E; font-size:0.72rem; margin-top:16px;">Sankofa Intelligence · Ghana · 2026</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
