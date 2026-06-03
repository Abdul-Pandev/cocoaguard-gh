import streamlit as st

st.set_page_config(
    page_title='FarmEye',
    page_icon='🌿',
    layout='centered'
)

st.title('FarmEye')
st.caption('CSSVD Early Detection — Powered by Sankofa Intelligence')
st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.image('assets/logo.jpeg', width=200)

with col2:
    st.markdown("""
    ## What is FarmEye?

    FarmEye is an AI-powered tool designed to help
    Ghanaian cocoa farmers detect **Cocoa Swollen Shoot Virus
    Disease (CSSVD)** early using a photo of a leaf, stem or pod.

    Early detection saves farms. CSSVD spreads silently —
    by the time visible damage is severe, nearby trees are
    already infected.

    ---

    ### How to Use
    1. Navigate to **Detection** in the sidebar
    2. Select your preferred language
    3. Upload or capture a photo of a cocoa leaf or stem
    4. Receive an instant AI diagnosis with confidence score
    5. Follow the recommended actions and listen to the audio guide
    """)

st.divider()

col3, col4, col5, col6 = st.columns(4)

with col3:
    st.info("**Detection**\n\nUpload a photo for instant CSSVD diagnosis with audio feedback")

with col4:
    st.info("**Analytics**\n\nExplore dataset and model training performance data")

with col5:
    st.info("**Model Info**\n\nUnderstand how the AI model was built and evaluated")

with col6:
    st.info("**About**\n\nLearn about CSSVD and the story behind FarmEye")

st.divider()

st.markdown("""
### Supported Languages
FarmEye provides audio diagnosis feedback in four languages
to serve farmers across Ghana.
""")

lang_col1, lang_col2, lang_col3, lang_col4 = st.columns(4)

with lang_col1:
    st.success("🇬🇭 English")
with lang_col2:
    st.success("🇬🇭 Twi")
with lang_col3:
    st.success("🇬🇭 Dagbani")
with lang_col4:
    st.success("🇬🇭 Ewe")

st.divider()

st.caption(
    '⚠️ FarmEye is designed to assist farmers and extension officers. '
    'Always consult a qualified agricultural officer for final diagnosis decisions.'
)

st.caption('Sankofa Intelligence | Ghana | 2026')
