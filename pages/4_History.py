import streamlit as st
from style import inject_css, section_heading, divider
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title='FarmEye · History',
    page_icon='🕘',
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
  <div class="hero-label">Scan Records</div>
  <div class="hero-title" style="font-size: 2rem;">🕘 Detection History</div>
  <div class="hero-body">Every diagnosis run in this session is saved here. Track patterns across your farm over time and export records to share with your extension officer.</div>
</div>
""", unsafe_allow_html=True)

# ── Fetch history ────────────────────────────────────────────────
history = st.session_state.get('detection_history', [])

# ── Summary stats ────────────────────────────────────────────────
total     = len(history)
cssvd_n   = sum(1 for h in history if h['result'] == 'cssvd')
healthy_n = total - cssvd_n
avg_conf  = round(sum(h['confidence'] for h in history) / total, 1) if total else 0

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown(f'<div class="stat-card"><div class="val">{total}</div><div class="lbl">Total Scans</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown(f'<div class="stat-card"><div class="val" style="color:#E05A4E;">{cssvd_n}</div><div class="lbl">CSSVD Detected</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown(f'<div class="stat-card"><div class="val">{healthy_n}</div><div class="lbl">Healthy</div></div>', unsafe_allow_html=True)
with s4:
    st.markdown(f'<div class="stat-card"><div class="val" style="color:#C9A84C;">{avg_conf}%</div><div class="lbl">Avg Confidence</div></div>', unsafe_allow_html=True)

divider()

if not history:
    st.markdown("""
    <div style="
      background: rgba(15,34,18,0.4);
      border: 1px solid rgba(61,204,82,0.12);
      border-radius: 12px;
      padding: 64px 24px;
      text-align: center;
      color: #7AAB80;
    ">
      <div style="font-size:3rem; margin-bottom:16px;">🕘</div>
      <div style="font-size:1rem; font-family:'Syne',sans-serif; color:#E8F5E9; margin-bottom:8px;">No scans yet</div>
      <div style="font-size:0.88rem;">Go to <b style="color:#3DCC52;">Detection</b> and run your first diagnosis to see it here.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    # ── Charts ───────────────────────────────────────────────────
    if total >= 3:
        section_heading("📈", "Scan Trends")
        c1, c2 = st.columns(2)
        with c1:
            # Result breakdown pie
            fig = px.pie(
                names=['CSSVD', 'Healthy'],
                values=[cssvd_n, healthy_n],
                color_discrete_sequence=['#E05A4E', '#3DCC52'],
                title='Result Breakdown',
                hole=0.5,
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#E8F5E9', family='DM Sans'),
                title_font=dict(family='Syne', size=13),
            )
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            # Confidence over scans
            df = pd.DataFrame(history[::-1])  # chronological order
            df['scan_num'] = range(1, len(df)+1)
            fig2 = px.line(df, x='scan_num', y='confidence', color='result',
                           color_discrete_map={'cssvd': '#E05A4E', 'healthy': '#3DCC52'},
                           title='Confidence Per Scan',
                           labels={'scan_num': 'Scan #', 'confidence': 'Confidence (%)', 'result': 'Result'})
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#E8F5E9', family='DM Sans'),
                title_font=dict(family='Syne', size=13),
                legend=dict(bgcolor='rgba(0,0,0,0)'),
            )
            fig2.update_traces(line_width=2.5)
            st.plotly_chart(fig2, use_container_width=True)

        divider()

    # ── Filter ───────────────────────────────────────────────────
    section_heading("🗂", "All Scans")
    col_f1, col_f2, _ = st.columns([1, 1, 2])
    with col_f1:
        filter_result = st.selectbox("Filter by result", ["All", "CSSVD", "Healthy"], label_visibility="collapsed")
    with col_f2:
        sort_order = st.selectbox("Sort", ["Newest first", "Oldest first", "Highest confidence", "Lowest confidence"], label_visibility="collapsed")

    filtered = history.copy()
    if filter_result == "CSSVD":
        filtered = [h for h in filtered if h['result'] == 'cssvd']
    elif filter_result == "Healthy":
        filtered = [h for h in filtered if h['result'] == 'healthy']

    if sort_order == "Oldest first":
        filtered = filtered[::-1]
    elif sort_order == "Highest confidence":
        filtered = sorted(filtered, key=lambda x: x['confidence'], reverse=True)
    elif sort_order == "Lowest confidence":
        filtered = sorted(filtered, key=lambda x: x['confidence'])

    st.markdown('<br>', unsafe_allow_html=True)

    # ── History rows ─────────────────────────────────────────────
    for idx, h in enumerate(filtered):
        is_cssvd = h['result'] == 'cssvd'
        badge_class = "badge-cssvd" if is_cssvd else "badge-healthy"
        badge_label = "CSSVD" if is_cssvd else "HEALTHY"
        conf_color  = "#E05A4E" if is_cssvd else "#3DCC52"
        icon = "🔴" if is_cssvd else "🟢"

        st.markdown(f"""
        <div class="history-row">
          <div style="font-size:1.2rem;">{icon}</div>
          <div style="flex:1;">
            <div style="font-weight:600; font-size:0.9rem; color:#E8F5E9;">{h.get('filename', 'Unknown file')}</div>
            <div class="history-meta">{h['timestamp']} &nbsp;·&nbsp; 🎙 {h.get('language','—')}</div>
          </div>
          <span class="history-badge {badge_class}">{badge_label}</span>
          <div class="history-conf" style="color:{conf_color};">{h['confidence']}%</div>
        </div>
        """, unsafe_allow_html=True)

    divider()

    # ── Export ───────────────────────────────────────────────────
    section_heading("📤", "Export Records")
    df_export = pd.DataFrame(history)
    if not df_export.empty:
        csv = df_export.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇ Download as CSV",
            data=csv,
            file_name="FarmEye_history.csv",
            mime="text/csv",
        )

    # ── Clear ─────────────────────────────────────────────────────
    st.markdown('<br>', unsafe_allow_html=True)
    if st.button("🗑 Clear All History"):
        st.session_state['detection_history'] = []
        st.rerun()

divider()
st.markdown('<p style="color:#3A5C3E; font-size:0.72rem; text-align:center;">History is stored for this session only · Sankofa Intelligence · Ghana · 2026</p>', unsafe_allow_html=True)
