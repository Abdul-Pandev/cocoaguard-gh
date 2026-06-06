import streamlit as st
import datetime
from style import inject_css, app_bar, section_heading, divider

st.set_page_config(
    page_title='FarmEye · Detection',
    page_icon='🔬',
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
    st.markdown("""
    <div style="font-size:0.72rem; color:#7AAB80; line-height:1.9;">
      <b style="color:#3DCC52;">Language</b><br>
      Select below for audio feedback
    </div>
    """, unsafe_allow_html=True)
    language = st.selectbox(
        "Audio Language",
        ["English", "Twi", "Dagbani", "Ewe"],
        label_visibility="collapsed"
    )

# ── Page header ──────────────────────────────────────────────────
st.markdown("""
<div class="hero" style="padding: 36px 40px; margin-bottom: 28px;">
  <div class="hero-label">AI Diagnosis Engine</div>
  <div class="hero-title" style="font-size: 2rem;">🔬 Disease Detection</div>
  <div class="hero-body">Upload a photo of a cocoa leaf, stem, or pod to receive an instant AI diagnosis with confidence score and action recommendations.</div>
</div>
""", unsafe_allow_html=True)


# ── Upload section ───────────────────────────────────────────────
col_upload, col_result = st.columns([1, 1], gap="large")

with col_upload:
    section_heading("📷", "Upload or Capture Image")

    image_source = st.radio(
        "Choose Image Source",
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

        st.image(
            img,
            caption="Selected image",
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        run_btn = st.button(
            "🔬 Run Diagnosis",
            use_container_width=True,
            type="primary"
        )

    else:
        st.markdown("""
        <div style="
          border: 2px dashed rgba(61,204,82,0.2);
          border-radius: 12px;
          padding: 48px 24px;
          text-align: center;
          color: #7AAB80;
          background: rgba(15,34,18,0.4);
        ">
          <div style="font-size: 2.5rem; margin-bottom: 12px;">📸</div>
          <div style="font-size: 0.9rem;">
            Upload an image or take a photo using your camera.
          </div>
        </div>
        """, unsafe_allow_html=True)

        run_btn = False
        
        
        
        
with col_result:
    section_heading("🧠", "Diagnosis Result")

    if uploaded_file and run_btn:
        with st.spinner("Running AI inference…"):
            try:
                import sys
                import os
                sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
                from utils import load_disease_model, load_cocoa_checker, preprocess_image, predict, get_recommendation, confidence_bar_chart
                import numpy as np

                disease_model = load_disease_model()
                cocoa_model   = load_cocoa_checker()

                img_pil = Image.open(uploaded_file).convert("RGB")
                processed = preprocess_image(img_pil)

                # Cocoa check
                cocoa_out = cocoa_model.predict(processed, verbose=0)
                is_cocoa  = float(cocoa_out[0][0]) <= 0.5

                if not is_cocoa:
                    st.markdown("""
                    <div class="alert-cssvd">
                      <div class="alert-title">⚠ Not a Cocoa Image</div>
                      <p style="color:#E8D0CD; font-size:0.9rem; margin:0;">The model could not verify this as a cocoa plant image. Please upload a clear photo of a cocoa leaf, stem, or pod.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    result = predict(disease_model, processed)
                    rec    = get_recommendation(result['predicted_class'])

                    is_cssvd = result['predicted_class'] == 'cssvd'
                    alert_class = "alert-cssvd" if is_cssvd else "alert-healthy"
                    icon = "🔴" if is_cssvd else "🟢"
                    label = "CSSVD DETECTED" if is_cssvd else "HEALTHY"
                    conf  = round(result['confidence'], 1)

                    st.markdown(f"""
                    <div class="{alert_class}">
                      <div class="alert-title">{icon} {label}</div>
                      <div style="font-size: 2rem; font-family: 'Syne', sans-serif; font-weight: 800; margin: 4px 0;">{conf}% <span style="font-size:0.9rem; font-weight:400; color:#7AAB80;">confidence</span></div>
                      <p style="font-size:0.88rem; margin: 8px 0 0; opacity:0.85;">{rec['summary']}</p>
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
                        st.markdown(f'<div style="display:flex;gap:10px;margin-bottom:8px;"><span style="color:{urgency_color};">▸</span><span style="color:#C8DFC9;font-size:0.9rem;">{action}</span></div>', unsafe_allow_html=True)

                    # Audio guide placeholder
                    divider()
                    st.markdown(f'<div style="color:#7AAB80; font-size:0.82rem;">🎙 Audio guide available in: <b style="color:#3DCC52;">{language}</b></div>', unsafe_allow_html=True)
                    audio_path = f"Audio/{result['predicted_class']}_{language.lower()}.mp3"
                    import os
                    if os.path.exists(audio_path):
                        with open(audio_path, 'rb') as af:
                            st.audio(af.read(), format='audio/mp3')
                    else:
                        st.info(f"Audio file not found: {audio_path}")

                    # ── Save to history ──────────────────────────────────────
                    if 'detection_history' not in st.session_state:
                        st.session_state['detection_history'] = []

                    st.session_state['detection_history'].insert(0, {
                        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        'filename': getattr(uploaded_file, "name", "Camera Capture"),
                        'result':    result['predicted_class'],
                        'confidence': conf,
                        'language':  language,
                    })
                    # Cap at 100 entries
                    st.session_state['detection_history'] = st.session_state['detection_history'][:100]

            except Exception as e:
                st.error(f"Model error: {e}")
                st.info("Make sure the model files are present at model/phase2.keras and model/cocoa_checker.keras")

    elif not uploaded_file:
        st.markdown("""
        <div style="
          background: rgba(15,34,18,0.4);
          border: 1px solid rgba(61,204,82,0.12);
          border-radius: 12px;
          padding: 48px 24px;
          text-align: center;
          color: #7AAB80;
        ">
          <div style="font-size:2.5rem; margin-bottom:12px;">🧠</div>
          <div style="font-size:0.9rem;">Upload an image and click<br><b style="color:#3DCC52;">Run Diagnosis</b> to see results here.</div>
        </div>
        """, unsafe_allow_html=True)

divider()
st.markdown('<p style="color:#3A5C3E; font-size:0.72rem; text-align:center;">⚠ Always consult a qualified agricultural officer for final diagnosis decisions · Sankofa Intelligence · 2026</p>', unsafe_allow_html=True)
