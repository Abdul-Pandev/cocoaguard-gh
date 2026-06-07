import streamlit as st
from style import inject_css, section_heading, divider
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title='FarmEye · Analytics',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

inject_css()

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin:8px auto 16px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3DCC52,#C9A84C);border-radius:10px;font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-weight:800;font-size:1.1rem;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:0.7rem;color:#4A7A52;">Sankofa Intelligence</div>', unsafe_allow_html=True)

    st.markdown("### Navigation")
    st.page_link("home.py", label="🏠 Dashboard")
    st.page_link("pages/1_Detection.py", label="🔬 Detection")
    st.page_link("pages/2_Disease_Intelligence.py", label="🗺 Disease Intelligence")
    st.page_link("pages/3_Analytics.py", label="📊 Analytics")
    st.page_link("pages/4_History.py", label="🕘 History")
    st.page_link("pages/6_Impact.py", label="🌍 Impact")
    st.page_link("pages/7_About.py", label="ℹ About")

# ---------------- HERO ---------------- #
st.markdown("""
<div class="hero" style="padding:36px 40px;margin-bottom:28px;">
  <div class="hero-label">Model Performance & Dataset</div>
  <div class="hero-title" style="font-size:2rem;">📊 Analytics</div>
  <div class="hero-body">
    Explore dataset structure, training history, and performance metrics of the Cocoa disease detection model.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- MODEL PERFORMANCE ---------------- #
section_heading("🏆", "Model Performance")

c1, c2, c3, c4 = st.columns(4)
metrics = [
    ("83.80%", "Test Accuracy"),
    ("83%", "CSSVD Recall"),
    ("87%", "Healthy Recall"),
    ("0.85", "Weighted F1")
]

for col, (val, lbl) in zip([c1, c2, c3, c4], metrics):
    with col:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="val">{val}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

divider()

# ---------------- DATASET ---------------- #
section_heading("🗂", "Dataset Distribution")

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        names=['CSSVD', 'Healthy'],
        values=[2491, 2869],
        title='Dataset Class Distribution',
        hole=0.45,
        color_discrete_sequence=['#E05A4E', '#3DCC52']
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9')
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.bar(
        x=['Training', 'Validation', 'Test'],
        y=[1699, 425, 246],
        title='Dataset Split',
        color=['Training', 'Validation', 'Test'],
        color_discrete_map={
            'Training': '#3DCC52',
            'Validation': '#C9A84C',
            'Test': '#3B8BEB'
        }
    )
    fig2.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9')
    )
    st.plotly_chart(fig2, use_container_width=True)

divider()

# ---------------- TRAINING HISTORY ---------------- #
section_heading("📈", "Training History")

# -------- PHASE 1 -------- #
train_acc_1 = [0.6396, 0.7127, 0.7438, 0.7559, 0.7654, 0.7836,
                0.7947, 0.7907, 0.8053, 0.8043, 0.8111, 0.8025,
                0.8103, 0.8204, 0.8174, 0.8179, 0.8267, 0.8219,
                0.8252, 0.8356, 0.8315]

val_acc_1 = [0.7161, 0.7727, 0.7986, 0.8163, 0.8280, 0.8351,
             0.8292, 0.8410, 0.8386, 0.8351, 0.8386, 0.8386,
             0.8410, 0.8469, 0.8457, 0.8516, 0.8386, 0.8363,
             0.8398, 0.8398, 0.8398]

train_loss_1 = [0.6931, 0.5817, 0.5240, 0.5002, 0.4853, 0.4557,
                0.4387, 0.4397, 0.4191, 0.4212, 0.4150, 0.4178,
                0.4032, 0.3983, 0.4016, 0.4005, 0.3960, 0.3780,
                0.3774, 0.3649, 0.3748]

val_loss_1 = [0.5656, 0.4862, 0.4420, 0.4201, 0.4032, 0.3938,
             0.3817, 0.3790, 0.3703, 0.3720, 0.3647, 0.3855,
             0.3710, 0.3642, 0.3766, 0.3651, 0.3800, 0.3747,
             0.3729, 0.3696, 0.3681]

tab1, tab2 = st.tabs(["Phase 1 — Head Training", "Phase 2 — Fine Tuning"])

with tab1:
    fig_acc = go.Figure()
    fig_acc.add_trace(go.Scatter(y=train_acc_1, name="Train Accuracy"))
    fig_acc.add_trace(go.Scatter(y=val_acc_1, name="Val Accuracy"))
    fig_acc.update_layout(title="Accuracy - Phase 1")
    st.plotly_chart(fig_acc, use_container_width=True)

    fig_loss = go.Figure()
    fig_loss.add_trace(go.Scatter(y=train_loss_1, name="Train Loss"))
    fig_loss.add_trace(go.Scatter(y=val_loss_1, name="Val Loss"))
    fig_loss.update_layout(title="Loss - Phase 1")
    st.plotly_chart(fig_loss, use_container_width=True)

# -------- PHASE 2 -------- #
train_acc_2 = [0.8172, 0.8290, 0.8371, 0.8308, 0.8411, 0.8411,
               0.8431, 0.8487, 0.8494, 0.8545, 0.8552, 0.8575,
               0.8638, 0.8608, 0.8603, 0.8583, 0.8575]

val_acc_2 = [0.8481, 0.8469, 0.8504, 0.8410, 0.8504, 0.8504,
             0.8528, 0.8504, 0.8504, 0.8539, 0.8516, 0.8492,
             0.8528, 0.8539, 0.8539, 0.8539, 0.8539]

train_loss_2 = [0.3952, 0.3802, 0.3702, 0.3655, 0.3584, 0.3496,
                0.3517, 0.3396, 0.3397, 0.3344, 0.3249, 0.3281,
                0.3203, 0.3254, 0.3207, 0.3172, 0.3160]

val_loss_2 = [0.3591, 0.3616, 0.3496, 0.3663, 0.3472, 0.3552,
             0.3390, 0.3552, 0.3494, 0.3368, 0.3577, 0.3681,
             0.3487, 0.3498, 0.3497, 0.3502, 0.3466]

with tab2:
    fig_acc2 = go.Figure()
    fig_acc2.add_trace(go.Scatter(y=train_acc_2, name="Train Accuracy"))
    fig_acc2.add_trace(go.Scatter(y=val_acc_2, name="Val Accuracy"))
    fig_acc2.update_layout(title="Accuracy - Phase 2")
    st.plotly_chart(fig_acc2, use_container_width=True)

    fig_loss2 = go.Figure()
    fig_loss2.add_trace(go.Scatter(y=train_loss_2, name="Train Loss"))
    fig_loss2.add_trace(go.Scatter(y=val_loss_2, name="Val Loss"))
    fig_loss2.update_layout(title="Loss - Phase 2")
    st.plotly_chart(fig_loss2, use_container_width=True)

divider()

st.markdown(
    '<p style="text-align:center;color:#3A5C3E;font-size:0.75rem;">Sankofa Intelligence · Ghana · 2026</p>',
    unsafe_allow_html=True
)


divider()
section_heading("🏗", "Model Architecture")

st.markdown("""
<div class="feature-card">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;">

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">BASE MODEL</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">EfficientNetB3</div>
      <div style="color:#7AAB80;font-size:0.8rem;">Pretrained on ImageNet</div>
    </div>

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">INPUT SIZE</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">224 × 224 px</div>
      <div style="color:#7AAB80;font-size:0.8rem;">RGB images</div>
    </div>

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">OUTPUT</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">Sigmoid (binary)</div>
      <div style="color:#7AAB80;font-size:0.8rem;">CSSVD vs Healthy</div>
    </div>

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">THRESHOLD</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">0.65 (optimal)</div>
      <div style="color:#7AAB80;font-size:0.8rem;">Tuned on validation set</div>
    </div>

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">AUGMENTATION</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">Flip, Rotate, Zoom</div>
      <div style="color:#7AAB80;font-size:0.8rem;">Applied during training</div>
    </div>

    <div>
      <div style="color:#C9A84C;font-weight:700;font-size:0.85rem;margin-bottom:6px;">FRAMEWORK</div>
      <div style="color:#E8F5E9;font-size:0.95rem;font-weight:600;">TensorFlow / Keras</div>
      <div style="color:#7AAB80;font-size:0.8rem;">Fine-tuning pipeline</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)
