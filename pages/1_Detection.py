import streamlit as st
from PIL import Image

from utils import (
    load_disease_model,
    load_cocoa_checker,
    preprocess_image,
    predict,
    get_recommendation,
    confidence_bar_chart
)

st.set_page_config(
    page_title='CSSVD Detection System',
    page_icon='🌿',
    layout='wide'
)


st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton > button {
    border-radius: 10px;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

st.title('CSSVD Detection')

st.caption(
    'Upload or capture a photo to receive an instant AI diagnosis'
)

st.divider()

# ── Language Selection ────────────────────────────────────────────
LANGUAGES = {
    "English": "eng",
    "Twi": "twi",
    "Dagbani": "dag",
    "Ewe": "ewe"
}

lang_label = st.selectbox(
    "🌍 Select your language before you continue",
    options=list(LANGUAGES.keys())
)
lang_folder = LANGUAGES[lang_label]
st.success(f"✓ Language set to: {lang_label}")

st.divider()

# ── Load Models ───────────────────────────────────────────────────
disease_model = load_disease_model()
cocoa_model   = load_cocoa_checker()

COCOA_THRESHOLD = 0.65

st.subheader('📸 Select Image Source')

st.info(
    'Choose whether to upload an existing image or capture one live using your camera.'
)

image = None

tab1, tab2 = st.tabs([
    '📁 Upload Image',
    '📷 Use Camera'
])


with tab1:

    uploaded = st.file_uploader(
        'Upload a photo of a cocoa leaf, stem or pod',
        type=['jpg', 'jpeg', 'png'],
        help='Take a clear, close-up photo in good lighting'
    )

    if uploaded:

        image = Image.open(uploaded)


with tab2:

    camera_photo = st.camera_input(
        'Take a photo of a cocoa leaf, stem or pod',
        help='Ensure the image is clear and well lit'
    )

    if camera_photo:

        image = Image.open(camera_photo)


if image:

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            image,
            caption='Selected Image',
            use_container_width=True
        )

    with st.spinner('Checking image...'):

        processed = preprocess_image(image)

        # Step 1 — Verify this is a cocoa image
        cocoa_prob = cocoa_model.predict(processed, verbose=0)[0][0]
        is_cocoa   = cocoa_prob <= 0.5

    if not is_cocoa:

        not_cocoa_url = (
            f"https://raw.githubusercontent.com/Abdul-Pandev/cocoaguard-gh/main/"
            f"Audio/{lang_folder}/non_cocoa.mp3"
        )
        st.audio(not_cocoa_url, format="audio/mp3")
        st.divider()
        st.warning(
            "🍃 This does not appear to be a cocoa leaf or stem. "
            "Please upload a clear photo of a cocoa plant."
        )
        st.stop()

    # Step 2 — Run disease detection only if cocoa confirmed
    with st.spinner('Analysing image using AI model...'):

        result = predict(
            disease_model,
            processed
        )

        recommendation = get_recommendation(
            result['predicted_class']
        )

    with col2:

        st.subheader('Diagnosis Result')

        if result['predicted_class'] == 'healthy':

            st.success('✅ Healthy Plant Detected')

        else:

            st.error('🚨 CSSVD Detected')

        st.metric(
            label='Confidence Score',
            value=f"{result['confidence']:.1f}%"
        )

        st.markdown('### Prediction Confidence')

        fig = confidence_bar_chart(
            result['cssvd_probability'],
            result['healthy_probability']
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ── Audio Feedback ────────────────────────────────────────────
    audio_url = (
        f"https://raw.githubusercontent.com/Abdul-Pandev/cocoaguard-gh/main/"
        f"Audio/{lang_folder}/{result['predicted_class']}.mp3"
    )
    st.audio(audio_url, format="audio/mp3")

    st.divider()

    st.subheader('Recommended Actions')

    if recommendation['urgency'] == 'high':

        st.error(
            f"⚠️ {recommendation['summary']}"
        )

    else:

        st.success(
            f"✅ {recommendation['summary']}"
        )

    st.markdown('### Recommended Steps')

    for action in recommendation['actions']:

        st.markdown(f"- {action}")

    st.divider()

    st.caption(
        '⚠️ This tool is designed to assist farmers and '
        'extension officers. Always consult a qualified '
        'agricultural officer for final diagnosis decisions.'
    )


st.divider()

st.subheader('Visual Reference Guide')

st.caption(
    'Use these examples to understand symptoms before uploading your image.'
)

ref_col1, ref_col2 = st.columns(2)


with ref_col1:

    st.image(
        'assets/sample_healthy.jpeg',
        caption=(
            '✅ Healthy Cocoa Plant — '
            'Even green colour, normal leaf shape, '
            'no distortion or swelling'
        ),
        use_container_width=True
    )

with ref_col2:

    st.image(
        'assets/sample_cssvd.jpeg',
        caption=(
            '🚨 CSSVD Infected Plant — '
            'Mosaic patterns, vein banding, '
            'leaf distortion and swollen shoots'
        ),
        use_container_width=True
    )


with st.expander('What symptoms should I look for?'):

    st.markdown("""

    ## Early CSSVD Symptoms

    - **Leaf mosaic**  
      Irregular light and dark green patches on leaves

    - **Vein banding**  
      Yellowing along the leaf veins

    - **Leaf distortion**  
      Leaves may appear twisted or curled

    - **Reddish flush**  
      Bronze or reddish coloration on young leaves


    ## Advanced CSSVD Symptoms

    - **Swollen shoots**  
      Abnormal thickening of stems and branches

    - **Stunted growth**  
      Tree becomes smaller than surrounding trees

    - **Reduced pod production**  
      Fewer and smaller cocoa pods

    - **Dieback**  
      Branches begin dying from the tips downward


    ## Healthy Plant Signs

    - Uniform deep green leaf colour
    - Normal leaf structure
    - No swelling on stems
    - Active and healthy pod growth

    """)

st.divider()

st.caption(
    '🌍 AI-Powered Cocoa Disease Detection System | '
    'Built with Streamlit and TensorFlow'
)
