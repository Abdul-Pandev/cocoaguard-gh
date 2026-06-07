import streamlit as st

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── Root tokens ──────────────────────────────────────── */
:root {
  --green-deep:   #FFFFFF;
  --green-dark:   #FFFFFF;
  --green-mid:    #F0F7F1;
  --green-accent: #1E8C35;
  --green-bright: #25A340;
  --gold:         #A67C00;
  --gold-light:   #C9A84C;
  --cream:        #F9F6EE;
  --text-primary: #0A1A0C;
  --text-muted:   #2D6B38;
  --red-alert:    #C0392B;
  --border:       rgba(30,140,53,0.15);
  --card-bg:      rgba(255,255,255,0.9);
  --radius:       12px;
  --radius-lg:    20px;
}

/* ── Global reset ─────────────────────────────────────── */
html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  color: var(--text-primary);
}

.main { background: #FFFFFF !important; }
.stApp { background: #FFFFFF !important; }

/* Remove streamlit header chrome but keep sidebar toggle */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1100px; }

/* ── Sidebar — collapsible, styled ───────────────────── */
[data-testid="stSidebar"] {
  background: #FFFFFF !important;
  border-right: 1px solid rgba(30,140,53,0.15) !important;
  box-shadow: 2px 0 12px rgba(0,0,0,0.06) !important;
}
[data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif; }

/* Style the collapse toggle button */
[data-testid="stSidebarCollapsedControl"] {
  background: #FFFFFF !important;
  border: 1px solid rgba(30,140,53,0.2) !important;
  border-radius: 0 8px 8px 0 !important;
  box-shadow: 2px 0 8px rgba(0,0,0,0.08) !important;
}
[data-testid="stSidebarCollapsedControl"] button {
  color: #1E8C35 !important;
}

/* Hide Streamlit's auto-generated page nav — we use our own */
[data-testid="stSidebarNav"] { display: none !important; }

/* ── Hero banner ─────────────────────────────────────── */
.hero {
  background: linear-gradient(135deg, #0F2212 0%, #1A3D1E 60%, #0D3318 100%);
  border: none;
  border-radius: var(--radius-lg);
  padding: 48px 40px;
  position: relative;
  overflow: hidden;
  margin-bottom: 32px;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 80% 50%, rgba(61,204,82,0.12) 0%, transparent 65%);
}
.hero-label {
  font-size: 0.7rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #56E86D;
  font-weight: 600;
  margin-bottom: 12px;
}
.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
  color: #FFFFFF;
  margin-bottom: 16px;
}
.hero-title span { color: #3DCC52; }
.hero-body {
  font-size: 1rem;
  color: rgba(255,255,255,0.85);
  max-width: 560px;
  line-height: 1.7;
}

/* ── Section heading ─────────────────────────────────── */
.section-heading {
  font-family: 'Syne', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  color: #0A1A0C;
  margin: 32px 0 16px;
  display: flex; align-items: center; gap: 10px;
}
.section-heading::after {
  content: '';
  flex: 1; height: 1px;
  background: rgba(30,140,53,0.15);
}

/* ── Stat card ───────────────────────────────────────── */
.stat-card {
  background: #FFFFFF;
  border: 1px solid rgba(30,140,53,0.15);
  border-radius: var(--radius);
  padding: 24px 20px;
  text-align: center;
  transition: border-color 0.25s, transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.stat-card:hover {
  border-color: rgba(30,140,53,0.35);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(30,140,53,0.12);
}
.stat-card .val {
  font-family: 'Syne', sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  color: #1E8C35;
  line-height: 1;
}
.stat-card .lbl {
  font-size: 0.78rem;
  color: #2D6B38;
  margin-top: 6px;
  letter-spacing: 0.5px;
}

/* ── Feature card ────────────────────────────────────── */
.feature-card {
  background: #FFFFFF;
  border: 1px solid rgba(30,140,53,0.15);
  border-radius: var(--radius);
  padding: 24px;
  height: 100%;
  transition: border-color 0.25s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.feature-card:hover {
  border-color: rgba(166,124,0,0.3);
  box-shadow: 0 6px 20px rgba(0,0,0,0.09);
}
.feature-card .icon { font-size: 1.8rem; margin-bottom: 12px; }
.feature-card .title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 8px;
  color: #0A1A0C;
}
.feature-card .desc { font-size: 0.875rem; color: #2D6B38; line-height: 1.6; }

/* ── Alert boxes ─────────────────────────────────────── */
.alert-cssvd {
  background: #FEF2F2;
  border: 1px solid rgba(192,57,43,0.25);
  border-left: 4px solid #C0392B;
  border-radius: var(--radius);
  padding: 20px 24px;
}
.alert-healthy {
  background: #F0FAF2;
  border: 1px solid rgba(30,140,53,0.25);
  border-left: 4px solid #1E8C35;
  border-radius: var(--radius);
  padding: 20px 24px;
}
.alert-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 8px;
  color: #0A1A0C;
}

/* ── History rows ────────────────────────────────────── */
.history-row {
  display: flex; align-items: center; gap: 14px;
  background: #FFFFFF;
  border: 1px solid rgba(30,140,53,0.12);
  border-radius: var(--radius);
  padding: 14px 18px;
  margin-bottom: 10px;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.history-row:hover {
  border-color: rgba(30,140,53,0.28);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.history-badge {
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
}
.badge-cssvd   { background: #FEE2E2; color: #991B1B; border: 1px solid rgba(192,57,43,0.2); }
.badge-healthy { background: #DCFCE7; color: #166534; border: 1px solid rgba(30,140,53,0.2); }
.history-meta  { font-size: 0.8rem; color: #2D6B38; }
.history-conf  { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.95rem; margin-left: auto; }

/* ── Upload zone ─────────────────────────────────────── */
[data-testid="stFileUploader"] {
  border: 2px dashed rgba(30,140,53,0.25) !important;
  border-radius: var(--radius) !important;
  background: #F7FCF8 !important;
}

/* ── Buttons ─────────────────────────────────────────── */
.stButton > button {
  background: linear-gradient(135deg, #1E8C35, #166028) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 8px !important;
  font-family: 'Syne', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 0.3px !important;
  padding: 10px 24px !important;
  transition: opacity 0.2s, transform 0.15s !important;
  box-shadow: 0 2px 8px rgba(30,140,53,0.3) !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }

/* ── Sidebar nav label ───────────────────────────────── */
.nav-label {
  font-family: 'Syne', sans-serif;
  font-size: 0.65rem;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: #2D6B38;
  padding: 16px 8px 8px;
}

/* ── Divider ─────────────────────────────────────────── */
.styled-divider {
  height: 1px;
  background: rgba(30,140,53,0.12);
  margin: 28px 0;
}

/* ── Impact metric ───────────────────────────────────── */
.impact-block {
  background: linear-gradient(135deg, #FFFBEB, #F0FAF2);
  border: 1px solid rgba(166,124,0,0.2);
  border-radius: var(--radius-lg);
  padding: 32px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.impact-num {
  font-family: 'Syne', sans-serif;
  font-size: 3rem;
  font-weight: 800;
  color: #A67C00;
}
.impact-lbl { color: #2D6B38; font-size: 0.9rem; margin-top: 4px; }

/* ── Language chips ──────────────────────────────────── */
.lang-chip {
  display: inline-flex; align-items: center; gap: 6px;
  background: #F0FAF2;
  border: 1px solid rgba(30,140,53,0.2);
  border-radius: 24px;
  padding: 6px 14px;
  font-size: 0.85rem;
  color: #1E8C35;
  margin: 4px;
}

/* ── Scrollbar ───────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #FFFFFF; }
::-webkit-scrollbar-thumb { background: #C8E6C9; border-radius: 3px; }

/* ── Progress bar ────────────────────────────────────── */
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, #1E8C35, #A67C00) !important;
}

/* Streamlit selectbox, radio styling */
[data-testid="stSelectbox"] > div > div {
  background: #FFFFFF !important;
  border-color: rgba(30,140,53,0.2) !important;
}

/* ── Inline text colour fixes for white bg ───────────── */
p, li, span, label, div {
  color: inherit;
}
.stMarkdown p { color: #0A1A0C; }
</style>
"""

def inject_css():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def app_bar():
    st.markdown("""
    <div class="app-bar">
      <div class="app-bar-logo">🌿</div>
      <div>
        <div class="app-bar-title">CocoaGuard GH</div>
        <div class="app-bar-sub">Sankofa Intelligence · Ghana 2026</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

def section_heading(icon, title):
    st.markdown(f'<div class="section-heading">{icon} {title}</div>', unsafe_allow_html=True)

def divider():
    st.markdown('<div class="styled-divider"></div>', unsafe_allow_html=True)
