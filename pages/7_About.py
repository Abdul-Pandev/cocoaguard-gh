import streamlit as st
from style import inject_css, section_heading, divider

st.set_page_config(page_title='FarmEye · About', page_icon='ℹ', layout='wide', initial_sidebar_state='expanded')
inject_css()

with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin:8px auto 16px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3DCC52,#C9A84C);border-radius:10px;font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-family:Syne,sans-serif;font-weight:800;font-size:1.1rem;color:#0A1A0C;margin-bottom:2px;">CocoaGuard GH</div>', unsafe_allow_html=True)
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
  <div class="hero-label">The Story</div>
  <div class="hero-title" style="font-size:2rem;">ℹ About FarmEye GH</div>
  <div class="hero-body">Built by Sankofa Intelligence to put the power of AI in the hands of Ghana's cocoa farming communities — free, multilingual, and mobile-first.</div>
</div>
""", unsafe_allow_html=True)

section_heading("🎯", "Mission")
st.markdown("""
<div class="feature-card" style="margin-bottom:16px;">
  <p style="color:#0A1A0C;font-size:0.98rem;line-height:1.85;margin:0;">
    FarmEye exists to <b style="color:#1E8C35;">democratise access to agricultural intelligence</b>.
    We believe that every cocoa farmer in Ghana — regardless of education level, language, or
    proximity to specialist services — deserves the same early warning capabilities as the best-resourced research institutions.
  </p>
  <p style="color:#2D6B38;font-size:0.98rem;line-height:1.85;margin:16px 0 0;">CSSVD does not discriminate. Neither should early detection.</p>
</div>
""", unsafe_allow_html=True)

divider()
section_heading("🦅", "The Name: Sankofa Intelligence")
c1, c2 = st.columns([2, 1], gap="large")
with c1:
    st.markdown("""
    <div class="feature-card">
      <p style="color:#0A1A0C;font-size:0.92rem;line-height:1.85;font-style:italic;">"Se wo were fi na wosankofa a yenkyi"</p>
      <p style="color:#2D6B38;font-size:0.82rem;margin-top:-8px;">(Twi) — "It is not wrong to go back for what you forgot."</p>
      <p style="color:#0A1A0C;font-size:0.92rem;line-height:1.85;margin-top:14px;">
        The Sankofa bird looks backward while moving forward — a symbol of learning from the past to build a better future.
        Our AI is trained on historical disease data to protect future harvests: Sankofa in practice.
      </p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="feature-card" style="text-align:center;padding:32px 24px;">
      <div style="font-size:4rem;margin-bottom:8px;">🦅</div>
      <div style="font-family:'Syne',sans-serif;font-weight:700;color:#A67C00;font-size:1.1rem;">Sankofa</div>
      <div style="color:#2D6B38;font-size:0.78rem;margin-top:4px;line-height:1.5;">Akan Adinkra symbol<br>of wisdom & learning</div>
    </div>
    """, unsafe_allow_html=True)

divider()
section_heading("🛠", "Technology Stack")
t1, t2, t3 = st.columns(3)
stack = [
    [("🧠 TensorFlow","Deep learning model training & inference"),("⚡ EfficientNetB0","Pretrained CNN backbone (ImageNet)"),("🔁 JAX","Additional ML computation support")],
    [("🌐 Streamlit","Mobile-first web application framework"),("📊 Plotly","Interactive analytics visualisations"),("🖼 Pillow","Image preprocessing & handling")],
    [("🐍 Python 3.11","Core application language"),("🎙 gTTS / Audio","Multilingual text-to-speech output"),("☁ Streamlit Cloud","Deployment & hosting")],
]
for col, items in zip([t1,t2,t3], stack):
    with col:
        for name, desc in items:
            st.markdown(f"""
            <div style="background:#F0F7F1;border:1px solid rgba(30,140,53,0.18);border-radius:8px;padding:12px 14px;margin-bottom:10px;">
              <div style="font-weight:600;font-size:0.9rem;color:#0A1A0C;margin-bottom:3px;">{name}</div>
              <div style="color:#2D6B38;font-size:0.78rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

divider()
section_heading("📜", "Disclaimer")
st.markdown("""
<div style="background:#FFFBEB;border:1px solid rgba(201,168,76,0.3);border-left:4px solid #C9A84C;
            border-radius:12px;padding:20px 24px;color:#0A1A0C;font-size:0.88rem;line-height:1.8;">
  CocoaGuard GH is designed to <b>assist</b> farmers and extension officers, not replace professional agricultural advice.
  AI predictions are probabilistic — always consult a qualified agricultural extension officer (MOFA)
  or COCOBOD inspector before making irreversible farm management decisions such as roguing.
  <br><br>
  The model was trained on images from Ghanaian cocoa farms. Performance may vary on images from
  significantly different growing conditions or camera qualities.
</div>
""", unsafe_allow_html=True)

divider()
section_heading("🙏", "Acknowledgements")
st.markdown("""
<div class="feature-card">
  <div style="color:#0A1A0C;font-size:0.9rem;line-height:1.85;">
    We thank the <b style="color:#1E8C35;">Ghana Cocoa Board (COCOBOD)</b>, the
    <b style="color:#1E8C35;">Cocoa Research Institute of Ghana (CRIG)</b>, and the
    dedicated extension officers and farming communities who made this dataset possible.
    <br><br>
    FarmEye is a product of <b style="color:#1E8C35;">Sankofa Intelligence</b> — Ghana · 2026.
  </div>
</div>
""", unsafe_allow_html=True)

divider()
st.markdown('<p style="color:#2D6B38;font-size:0.72rem;text-align:center;">Sankofa Intelligence · Ghana · 2026 · Open Source</p>', unsafe_allow_html=True)
