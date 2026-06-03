import streamlit as st

st.title('About CocoaGuard GH')

st.divider()

st.subheader('Understanding CSSVD')

col1, col2 = st.columns(2)

with col1:
    st.image(
        'assets/sample_healthy.jpeg',
        caption='Healthy Cocoa Plant',
        use_container_width=True
    )

with col2:
    st.image(
        'assets/sample_cssvd.jpeg',
        caption='CSSVD Infected Plant',
        use_container_width=True
    )

st.markdown("""
CSSVD is caused by the **Cocoa swollen shoot virus** and transmitted 
by mealybugs. Once a tree is infected there is no cure — the only 
control method is removing infected trees to prevent spread to 
neighbouring plants.

Ghana loses thousands of acres of cocoa farmland to CSSVD annually. 
Early detection through tools like CocoaGuard GH gives farmers the 
best chance of protecting their farms before the disease spreads.
""")

st.divider()

st.markdown("""
## The Problem

Cocoa Swollen Shoot Virus Disease (CSSVD) is one of the most 
destructive threats to cocoa farming in Ghana. The disease spreads 
through mealybugs and has no cure — infected trees must be removed 
to protect surrounding plants.

Early detection is the only effective intervention. However, many 
farmers lack access to expert diagnosis, and symptoms in early stages 
are easy to miss without trained eyes.

## The Solution

CocoaGuard GH uses a deep learning model trained on thousands of 
cocoa leaf images to detect CSSVD from a single photo. The system 
was built and validated specifically for Ghanaian cocoa conditions.

## Technology Stack
- **TensorFlow / Keras** — model training and inference
- **EfficientNetB0** — pre-trained base model (ImageNet)
- **Streamlit** — web application framework
- **Plotly** — interactive visualisations
- **Python** — core language

## Developed By
**Sankofa Intelligence**
Ghana | 2026
""")

st.divider()
st.caption('For inquiries contact Sankofa Intelligence')
