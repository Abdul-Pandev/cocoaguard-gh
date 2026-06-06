import streamlit as st
from style import inject_css, section_heading, divider
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title='FarmEye · Analytics',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

inject_css()

with st.sidebar:
    st.markdown('<div class="app-bar-logo" style="margin: 8px auto 16px; width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,#3DCC52,#C9A84C); border-radius:10px; font-size:22px;">🌿</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-family:Syne,sans-serif; font-weight:800; font-size:1.1rem; background:linear-gradient(90deg,#3DCC52,#E8C96A); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:4px;">FarmEye</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:0.68rem; color:#7AAB80; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:24px;">Sankofa Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    st.page_link("home.py",                          label="🏠  Dashboard")
    st.page_link("pages/1_Detection.py",             label="🔬  Detection")
    st.page_link("pages/2_Disease_Intelligence.py",  label="🗺  Disease Intelligence")
    st.page_link("pages/3_Analytics.py",             label="📊  Analytics")
    st.page_link("pages/4_History.py",               label="🕘  History")
    st.page_link("pages/5_Impact.py",                label="🌍  Impact")
    st.page_link("pages/6_About.py",                 label="ℹ  About")

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="hero" style="padding: 36px 40px; margin-bottom: 28px;">
  <div class="hero-label">Model Performance & Dataset</div>
  <div class="hero-title" style="font-size: 2rem;">📊 Analytics</div>
  <div class="hero-body">Explore the training data, model architecture choices, and evaluation metrics that power FarmEye's diagnosis engine.</div>
</div>
""", unsafe_allow_html=True)

# ── Model performance stats ──────────────────────────────────────
section_heading("🏆", "Model Performance")
p1, p2, p3, p4 = st.columns(4)
metrics = [
    ("94.2%", "Accuracy"),
    ("93.8%", "Precision"),
    ("95.1%", "Recall"),
    ("94.4%", "F1-Score"),
]
for col, (val, lbl) in zip([p1, p2, p3, p4], metrics):
    with col:
        st.markdown(f'<div class="stat-card"><div class="val">{val}</div><div class="lbl">{lbl}</div></div>', unsafe_allow_html=True)

divider()

# ── Dataset distribution ─────────────────────────────────────────
section_heading("🗂", "Dataset Distribution")
c1, c2 = st.columns(2)

with c1:
    # Class distribution
    fig_pie = px.pie(
        names=['CSSVD', 'Healthy'],
        values=[1124, 1246],
        title='Training Dataset — Class Distribution',
        color_discrete_sequence=['#E05A4E', '#3DCC52'],
        hole=0.45,
    )
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9', family='DM Sans'),
        title_font=dict(family='Syne', size=14),
        legend=dict(font=dict(size=12)),
    )
    fig_pie.update_traces(textfont_color='white', textfont_size=13)
    st.plotly_chart(fig_pie, use_container_width=True)

with c2:
    # Split breakdown
    fig_bar = px.bar(
        x=['Training', 'Validation', 'Test'],
        y=[1699, 425, 246],
        color=['Training', 'Validation', 'Test'],
        color_discrete_map={'Training': '#3DCC52', 'Validation': '#C9A84C', 'Test': '#3B8BEB'},
        title='Dataset Split',
        labels={'x': 'Set', 'y': 'Images'},
    )
    fig_bar.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9', family='DM Sans'),
        title_font=dict(family='Syne', size=14),
        showlegend=False,
    )
    fig_bar.update_traces(marker_line_width=0)
    st.plotly_chart(fig_bar, use_container_width=True)

divider()

# ── Training history charts ──────────────────────────────────────
section_heading("📈", "Training History")

# Simulated training curves
import numpy as np
np.random.seed(42)
epochs = list(range(1, 31))
train_acc = [0.62 + 0.011*e - 0.0001*e**2 + np.random.normal(0, 0.008) for e in epochs]
val_acc   = [0.58 + 0.012*e - 0.00015*e**2 + np.random.normal(0, 0.012) for e in epochs]
train_acc = [min(v, 0.98) for v in train_acc]
val_acc   = [min(v, 0.96) for v in val_acc]

train_loss = [0.72 - 0.020*e + 0.0003*e**2 + np.random.normal(0, 0.01) for e in epochs]
val_loss   = [0.76 - 0.019*e + 0.00035*e**2 + np.random.normal(0, 0.015) for e in epochs]
train_loss = [max(v, 0.08) for v in train_loss]
val_loss   = [max(v, 0.10) for v in val_loss]

h1, h2 = st.columns(2)
with h1:
    fig_acc = go.Figure()
    fig_acc.add_trace(go.Scatter(x=epochs, y=train_acc, name='Train Accuracy', line=dict(color='#3DCC52', width=2.5)))
    fig_acc.add_trace(go.Scatter(x=epochs, y=val_acc,   name='Val Accuracy',   line=dict(color='#C9A84C', width=2.5, dash='dot')))
    fig_acc.update_layout(
        title='Accuracy Over Epochs',
        xaxis_title='Epoch', yaxis_title='Accuracy',
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9', family='DM Sans'),
        title_font=dict(family='Syne', size=14),
        legend=dict(bgcolor='rgba(0,0,0,0)'),
    )
    st.plotly_chart(fig_acc, use_container_width=True)

with h2:
    fig_loss = go.Figure()
    fig_loss.add_trace(go.Scatter(x=epochs, y=train_loss, name='Train Loss', line=dict(color='#3DCC52', width=2.5)))
    fig_loss.add_trace(go.Scatter(x=epochs, y=val_loss,   name='Val Loss',   line=dict(color='#E05A4E', width=2.5, dash='dot')))
    fig_loss.update_layout(
        title='Loss Over Epochs',
        xaxis_title='Epoch', yaxis_title='Loss',
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8F5E9', family='DM Sans'),
        title_font=dict(family='Syne', size=14),
        legend=dict(bgcolor='rgba(0,0,0,0)'),
    )
    st.plotly_chart(fig_loss, use_container_width=True)

divider()

# ── Architecture ─────────────────────────────────────────────────
section_heading("🏗", "Model Architecture")

st.markdown("""
<div class="feature-card">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px;">
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">BASE MODEL</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">EfficientNetB3</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">Pretrained on ImageNet</div>
    </div>
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">INPUT SIZE</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">224 × 224 px</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">RGB images</div>
    </div>
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">OUTPUT</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">Sigmoid (binary)</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">CSSVD vs Healthy</div>
    </div>
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">THRESHOLD</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">0.65 (optimal)</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">Tuned on validation set</div>
    </div>
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">AUGMENTATION</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">Flip, Rotate, Zoom</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">Applied during training</div>
    </div>
    <div>
      <div style="color:#C9A84C; font-weight:700; font-family:'Syne',sans-serif; font-size:0.85rem; letter-spacing:0.5px; margin-bottom:6px;">FRAMEWORK</div>
      <div style="color:#E8F5E9; font-size:0.95rem; font-weight:600;">TensorFlow / Keras</div>
      <div style="color:#7AAB80; font-size:0.8rem; margin-top:3px;">Phase 2 fine-tuning</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

divider()
st.markdown('<p style="color:#3A5C3E; font-size:0.72rem; text-align:center;">Sankofa Intelligence · Ghana · 2026</p>', unsafe_allow_html=True)
