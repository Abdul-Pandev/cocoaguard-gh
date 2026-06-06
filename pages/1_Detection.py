import streamlit as st
import datetime
from style import inject_css, section_heading, divider

st.set_page_config(
    page_title='FarmEye · Detection',
    page_icon='🔬',
    layout='wide',
    initial_sidebar_state='expanded'
)

inject_css()

# Language folder mapping
LANG_FOLDER = {
    "English": "eng",
    "Twi":     "twi",
    "Dagbani": "dagbani",
    "Ewe":     "ewe",
}

# ── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin:8px auto 16px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3DCC52,#C9A84C);border-radius:10px;font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-family:Syne,sans-serif;font-weight:800;font-size:1.1rem;background:linear-gradient(90deg,#3DCC52,#E8C96A);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:0.68rem;color:#7AAB80;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:16px;">Sankofa Intelligence</div>', unsafe_allow_html=True)

    # ── Language selector — TOP of sidebar ───────────────────────
    st.markdown("""
    <div style="background:rgba(61,204,82,0.07);border:1px solid rgba(61,204,82,0.2);
                border-radius:10px;padding:12px 14px;margin-bottom:16px;">
      <div style="font-size:0.75rem;color:#3DCC52;font-weight:700;letter-spacing:0.5px;margin-bottom:6px;">
        🎙 Audio Language
      </div>
      <div style="font-size:0.71rem;color:#7AAB80;margin-bottom:8px;">
        Diagnosis will be read aloud in your chosen language
      </div>
    </div>
    """, unsafe_allow_html=True)
    language = st.selectbox(
        "Audio Language",
        list(LANG_FOLDER.keys()),
        index=0,
        label_visibility="collapsed"
    )
    lang_folder = LANG_FOLDER[language]
    st.markdown(f'<div style="font-size:0.78rem;color:#3DCC52;margin-bottom:4px;">✓ <b>{language}</b> selected</div>', unsafe_allow_html=True)

    st.markdown('<div class="styled-divider" style="margin:14px 0;"></div>', unsafe_allow_html=True)

    # ── Navigation ────────────────────────────────────────────────
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    st.page_link("home.py",                         label="🏠  Dashboard")
    st.page_link("pages/1_Detection.py",            label="🔬  Detection")
    st.page_link("pages/2_Disease_Intelligence.py", label="🗺  Disease Intelligence")
    st.page_link("pages/3_Analytics.py",            label="📊  Analytics")
    st.page_link("pages/4_History.py",              label="🕘  History")
    st.page_link("pages/6_Impact.py",               label="🌍  Impact")
    st.page_link("pages/7_About.py",                label="ℹ  About")

# ── Page header ──────────────────────────────────────────────────
st.markdown("""
<div class="hero" style="padding:36px 40px;margin-bottom:28px;">
  <div class="hero-label">AI Diagnosis Engine</div>
  <div class="hero-title" style="font-size:2rem;">🔬 Disease Detection</div>
  <div class="hero-body">Upload a photo or take one with your camera. Diagnosis runs automatically — select your language in the sidebar for audio feedback.</div>
</div>
""", unsafe_allow_html=True)

# ── Layout ───────────────────────────────────────────────────────
col_upload, col_result = st.columns([1, 1], gap="large")

with col_upload:
    section_heading("📷", "Upload or Capture Image")

    image_source = st.radio(
        "Source",
        ["📁 Upload Image", "📷 Take Photo"],
        horizontal=True,
        label_visibility="collapsed"
    )

    uploaded_file = None
    if image_source == "📁 Upload Image":
        uploaded_file = st.file_uploader(
            "Drag & drop or click to browse",
            type=["jpg", "jpeg", "png", "webp"],
            label_visibility="collapsed"
        )
    else:
        uploaded_file = st.camera_input(
            "Take a clear photo of the cocoa leaf, stem, or pod"
        )

    if uploaded_file:
        from PIL import Image
        img = Image.open(uploaded_file)
        st.image(img, caption="Selected image", use_container_width=True)
    else:
        st.markdown("""
        <div style="border:2px dashed rgba(61,204,82,0.2);border-radius:12px;padding:48px 24px;
                    text-align:center;color:#7AAB80;background:rgba(15,34,18,0.4);">
          <div style="font-size:2.5rem;margin-bottom:12px;">📸</div>
          <div style="font-size:0.9rem;">Upload an image or take a photo to begin.</div>
        </div>
        """, unsafe_allow_html=True)

# ── Result column — auto-runs when image present ──────────────────
with col_result:
    section_heading("🧠", "Diagnosis Result")

    if not uploaded_file:
        st.markdown("""
        <div style="background:rgba(15,34,18,0.4);border:1px solid rgba(61,204,82,0.12);
                    border-radius:12px;padding:48px 24px;text-align:center;color:#7AAB80;">
          <div style="font-size:2.5rem;margin-bottom:12px;">🧠</div>
          <div style="font-size:0.9rem;">Provide an image on the left<br>and diagnosis will appear here automatically.</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        with st.spinner("Running AI inference…"):
            try:
                import sys, os
                import numpy as np
                from PIL import Image

                root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if root not in sys.path:
                    sys.path.insert(0, root)

                from utils import (load_disease_model, load_cocoa_checker,
                                   preprocess_image, predict,
                                   get_recommendation, confidence_bar_chart)

                disease_model = load_disease_model()
                cocoa_model   = load_cocoa_checker()

                img_pil   = Image.open(uploaded_file).convert("RGB")
                processed = preprocess_image(img_pil)

                # ── Cocoa check ──────────────────────────────────
                cocoa_raw  = cocoa_model.predict(processed, verbose=0)
                cocoa_prob = float(cocoa_raw[0][0])
                is_cocoa   = cocoa_prob <= 0.5

                if not is_cocoa:
                    # Not a cocoa image
                    st.markdown(f"""
                    <div class="alert-cssvd">
                      <div class="alert-title">⚠ Not a Cocoa Image</div>
                      <p style="color:#E8D0CD;font-size:0.9rem;margin:8px 0 0;">
                        Cocoa confidence: <b>{round(cocoa_prob*100,1)}%</b>. 
                        Please upload a clear photo of a cocoa leaf, stem, or pod.
                      </p>
                    </div>
                    """, unsafe_allow_html=True)

                    # Play non_cocoa audio
                    audio_path = os.path.join(root, "Audio", lang_folder, "non_cocoa.mp3")
                    if os.path.exists(audio_path):
                        st.markdown(f'<div style="color:#7AAB80;font-size:0.8rem;margin-top:16px;">🎙 Playing audio in <b style="color:#3DCC52;">{language}</b></div>', unsafe_allow_html=True)
                        with open(audio_path, "rb") as af:
                            st.audio(af.read(), format="audio/mp3")
                    else:
                        st.caption(f"⚠ Audio not found: Audio/{lang_folder}/non_cocoa.mp3")

                else:
                    # ── Disease diagnosis ────────────────────────
                    result = predict(disease_model, processed)
                    rec    = get_recommendation(result['predicted_class'])

                    is_cssvd    = result['predicted_class'] == 'cssvd'
                    alert_class = "alert-cssvd" if is_cssvd else "alert-healthy"
                    icon        = "🔴" if is_cssvd else "🟢"
                    label       = "CSSVD DETECTED" if is_cssvd else "HEALTHY"
                    conf        = round(result['confidence'], 1)
                    audio_file  = "cssvd.mp3" if is_cssvd else "healthy.mp3"

                    st.markdown(f"""
                    <div class="{alert_class}">
                      <div class="alert-title">{icon} {label}</div>
                      <div style="font-size:2rem;font-family:'Syne',sans-serif;font-weight:800;margin:4px 0;">
                        {conf}% <span style="font-size:0.9rem;font-weight:400;color:#7AAB80;">confidence</span>
                      </div>
                      <p style="font-size:0.88rem;margin:8px 0 0;opacity:0.85;">{rec['summary']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown('<br>', unsafe_allow_html=True)

                    # Confidence chart
                    fig = confidence_bar_chart(result['cssvd_probability'], result['healthy_probability'])
                    st.plotly_chart(fig, use_container_width=True)

                    # Recommended actions
                    section_heading("📋", "Recommended Actions")
                    urgency_color = "#E05A4E" if rec['urgency'] == 'high' else "#3DCC52"
                    for action in rec['actions']:
                        st.markdown(
                            f'<div style="display:flex;gap:10px;margin-bottom:8px;">'
                            f'<span style="color:{urgency_color};">▸</span>'
                            f'<span style="color:#C8DFC9;font-size:0.9rem;">{action}</span></div>',
                            unsafe_allow_html=True
                        )

                    # ── Audio feedback ───────────────────────────
                    divider()
                    audio_path = os.path.join(root, "Audio", lang_folder, audio_file)
                    st.markdown(f"""
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                      <span style="font-size:1.2rem;">🎙</span>
                      <div>
                        <div style="color:#E8F5E9;font-size:0.85rem;font-weight:600;">Audio Diagnosis</div>
                        <div style="color:#7AAB80;font-size:0.75rem;">Playing in <b style="color:#3DCC52;">{language}</b></div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if os.path.exists(audio_path):
                        with open(audio_path, "rb") as af:
                            st.audio(af.read(), format="audio/mp3")
                    else:
                        st.warning(f"Audio file not found: Audio/{lang_folder}/{audio_file}")
                        st.caption("Check that the Audio folder is in your project root.")

                    # ── Save to history ──────────────────────────
                    if 'detection_history' not in st.session_state:
                        st.session_state['detection_history'] = []

                    fname = getattr(uploaded_file, 'name', 'Camera Capture')
                    last  = st.session_state['detection_history']
                    if not last or last[0].get('filename') != fname or last[0].get('confidence') != conf:
                        st.session_state['detection_history'].insert(0, {
                            'timestamp':  datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                            'filename':   fname,
                            'result':     result['predicted_class'],
                            'confidence': conf,
                            'language':   language,
                        })
                        st.session_state['detection_history'] = st.session_state['detection_history'][:100]

            except Exception as e:
                st.error(f"Model error: {e}")
                st.info("Make sure model/phase2.keras and model/cocoa_checker.keras exist in your project root.")

divider()
st.markdown('<p style="color:#3A5C3E;font-size:0.72rem;text-align:center;">⚠ Always consult a qualified agricultural officer for final decisions · Sankofa Intelligence · 2026</p>', unsafe_allow_html=True)
