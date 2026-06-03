import streamlit as st

st.title('Model Information')
st.caption('Technical details about the CocoaGuard GH classification model')
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader('Architecture')
    st.markdown("""
    - **Base Model:** EfficientNetB0
    - **Strategy:** Two-phase Transfer Learning
    - **Input Size:** 224 × 224 × 3
    - **Output:** Binary sigmoid (CSSVD / Healthy)
    - **Classification Threshold:** 0.65
    """)

with col2:
    st.subheader('Training')
    st.markdown("""
    - **Phase 1:** Head training, base frozen
    - **Phase 2:** Fine-tuning, last 20 layers unfrozen
    - **Optimiser:** Adam
    - **Loss:** Binary Crossentropy
    - **Dataset Size:** 5,360 images
    """)

st.divider()

st.subheader('Performance Metrics')

col3, col4, col5, col6 = st.columns(4)

with col3:
    st.metric('Test Accuracy', '83.80%')
with col4:
    st.metric('CSSVD Recall', '83%')
with col5:
    st.metric('Healthy Recall', '87%')
with col6:
    st.metric('Weighted F1', '0.85')

st.divider()

st.subheader('Threshold Selection')
st.markdown("""
The default sigmoid threshold of **0.50** produced a CSSVD recall of only **77%** — 
meaning 23% of infected plants were missed. Through classification report 
analysis across thresholds from 0.50 to 0.70, **0.65** was selected as the 
optimal threshold, improving CSSVD recall to **83%** while maintaining 
balanced performance across both classes.

For a disease detection system, missing an infected plant carries significantly 
higher consequences than a false positive — the threshold was deliberately 
tuned to prioritise detection sensitivity.
""")

st.divider()

with st.expander('Data Augmentation Applied'):
    st.markdown("""
    - Random Horizontal and Vertical Flip
    - Random Rotation (±20%)
    - Random Zoom (±10%)
    - Random Translation (±10%)
    - Random Brightness (±20%)
    - Random Contrast (±20%)
    """)

with st.expander('Preprocessing'):
    st.markdown("""
    EfficientNetB0 internal preprocessing is applied via a custom 
    registered Keras layer — scaling raw pixel values from 0–255 
    to –1 to 1 as required by the EfficientNetB0 ImageNet weights.
    """)
