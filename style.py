import streamlit as st

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── Root tokens ──────────────────────────────────────── */
:root {
  --green-deep:   #0A1A0C;
  --green-dark:   #0F2212;
  --green-mid:    #1A3D1E;
  --green-accent: #3DCC52;
  --green-bright: #56E86D;
  --gold:         #C9A84C;
  --gold-light:   #E8C96A;
  --cream:        #F0EAD6;
  --text-primary: #E8F5E9;
  --text-muted:   #7AAB80;
  --red-alert:    #E05A4E;
  --border:       rgba(61,204,82,0.15);
  --card-bg:      rgba(15,34,18,0.8);
  --radius:       12px;
  --radius-lg:    20px;
}

/* ── Global reset ─────────────────────────────────────── */
html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  color: var(--text-primary);
}

.main { background: var(--green-deep); }

/* Remove streamlit header chrome but keep sidebar toggle */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1100px; }

/* Keep sidebar always expanded */
[data-testid="stSidebarCollapsedControl"] { display: none !important; }
[data-testid="stSidebar"][aria-expanded="false"] { display: flex !important; transform: none !important; }
section[data-testid="stSidebar"] { min-width: 244px !important; width: 244px !important; }

/* ── Sidebar ──────────────────────────────────────────── */
[data-testid="stSidebar"] {
  background: var(--green-dark) !important;
  border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif; }

/* ── Top app bar ─────────────────────────────────────── */
.app-bar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 0 24px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 32px;
}
.app-bar-logo {
  width: 44px; height: 44px;
  background: linear-gradient(135deg, var(--green-accent), var(--gold));
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 22px;
}
.app-bar-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(90deg, var(--green-accent), var(--gold-light));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  letter-spacing: -0.5px;
}
.app-bar-sub {
  font-size: 0.72rem;
  color: var(--text-muted);
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-top: 1px;
}

/* ── Hero banner ─────────────────────────────────────── */
.hero {
  background: linear-gradient(135deg, var(--green-dark) 0%, rgba(26,61,30,0.6) 100%);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 48px 40px;
  position: relative;
  overflow: hidden;
  margin-bottom: 32px;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 80% 50%, rgba(61,204,82,0.08) 0%, transparent 65%);
}
.hero-label {
  font-size: 0.7rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--green-accent);
  font-weight: 600;
  margin-bottom: 12px;
}
.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
  color: var(--text-primary);
  margin-bottom: 16px;
}
.hero-title span { color: var(--green-accent); }
.hero-body {
  font-size: 1rem;
  color: var(--text-muted);
  max-width: 560px;
  line-height: 1.7;
}

/* ── Section heading ─────────────────────────────────── */
.section-heading {
  font-family: 'Syne', sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 32px 0 16px;
  display: flex; align-items: center; gap: 10px;
}
.section-heading::after {
  content: '';
  flex: 1; height: 1px;
  background: var(--border);
}

/* ── Stat card ───────────────────────────────────────── */
.stat-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px 20px;
  text-align: center;
  transition: border-color 0.25s, transform 0.2s;
  backdrop-filter: blur(8px);
}
.stat-card:hover {
  border-color: rgba(61,204,82,0.4);
  transform: translateY(-2px);
}
.stat-card .val {
  font-family: 'Syne', sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--green-accent);
  line-height: 1;
}
.stat-card .lbl {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 6px;
  letter-spacing: 0.5px;
}

/* ── Feature card ────────────────────────────────────── */
.feature-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  height: 100%;
  transition: border-color 0.25s;
  backdrop-filter: blur(8px);
}
.feature-card:hover { border-color: rgba(201,168,76,0.35); }
.feature-card .icon { font-size: 1.8rem; margin-bottom: 12px; }
.feature-card .title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 8px;
  color: var(--text-primary);
}
.feature-card .desc { font-size: 0.875rem; color: var(--text-muted); line-height: 1.6; }

/* ── Alert boxes ─────────────────────────────────────── */
.alert-cssvd {
  background: rgba(224,90,78,0.12);
  border: 1px solid rgba(224,90,78,0.4);
  border-left: 4px solid var(--red-alert);
  border-radius: var(--radius);
  padding: 20px 24px;
}
.alert-healthy {
  background: rgba(61,204,82,0.1);
  border: 1px solid rgba(61,204,82,0.35);
  border-left: 4px solid var(--green-accent);
  border-radius: var(--radius);
  padding: 20px 24px;
}
.alert-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 8px;
}

/* ── History table ───────────────────────────────────── */
.history-row {
  display: flex; align-items: center; gap: 14px;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 14px 18px;
  margin-bottom: 10px;
  transition: border-color 0.2s;
}
.history-row:hover { border-color: rgba(61,204,82,0.3); }
.history-badge {
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
}
.badge-cssvd { background: rgba(224,90,78,0.2); color: #F08070; border: 1px solid rgba(224,90,78,0.4); }
.badge-healthy { background: rgba(61,204,82,0.15); color: var(--green-accent); border: 1px solid rgba(61,204,82,0.35); }
.history-meta { font-size: 0.8rem; color: var(--text-muted); }
.history-conf { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.95rem; margin-left: auto; }

/* ── Upload zone ─────────────────────────────────────── */
[data-testid="stFileUploader"] {
  border: 2px dashed var(--border) !important;
  border-radius: var(--radius) !important;
  background: var(--card-bg) !important;
  padding: 8px !important;
}

/* ── Buttons ─────────────────────────────────────────── */
.stButton > button {
  background: linear-gradient(135deg, var(--green-accent), #2AAF3D) !important;
  color: #020902 !important;
  border: none !important;
  border-radius: 8px !important;
  font-family: 'Syne', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 0.3px !important;
  padding: 10px 24px !important;
  transition: opacity 0.2s, transform 0.15s !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }

/* ── Sidebar nav label ───────────────────────────────── */
.nav-label {
  font-family: 'Syne', sans-serif;
  font-size: 0.65rem;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--text-muted);
  padding: 16px 8px 8px;
}

/* ── Divider ─────────────────────────────────────────── */
.styled-divider {
  height: 1px;
  background: var(--border);
  margin: 28px 0;
}

/* ── Impact metric ───────────────────────────────────── */
.impact-block {
  background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(61,204,82,0.06));
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: var(--radius-lg);
  padding: 32px;
  text-align: center;
}
.impact-num {
  font-family: 'Syne', sans-serif;
  font-size: 3rem;
  font-weight: 800;
  color: var(--gold-light);
}
.impact-lbl { color: var(--text-muted); font-size: 0.9rem; margin-top: 4px; }

/* ── Language chips ──────────────────────────────────── */
.lang-chip {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(61,204,82,0.1);
  border: 1px solid rgba(61,204,82,0.25);
  border-radius: 24px;
  padding: 6px 14px;
  font-size: 0.85rem;
  color: var(--green-accent);
  margin: 4px;
}

/* ── Scrollbar ───────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--green-dark); }
::-webkit-scrollbar-thumb { background: var(--green-mid); border-radius: 3px; }

/* ── Progress bar ────────────────────────────────────── */
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, var(--green-accent), var(--gold)) !important;
}
</style>
"""

def inject_css():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    # Force sidebar open on Streamlit Cloud via JS
    st.markdown("""
    <script>
    (function() {
        function tryOpenSidebar() {
            try {
                var sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
                if (sidebar && sidebar.getAttribute("aria-expanded") === "false") {
                    var btn = window.parent.document.querySelector('[data-testid="stSidebarCollapsedControl"] button');
                    if (btn) btn.click();
                }
            } catch(e) {}
        }
        setTimeout(tryOpenSidebar, 200);
        setTimeout(tryOpenSidebar, 600);
        setTimeout(tryOpenSidebar, 1200);
    })();
    </script>
    """, unsafe_allow_html=True)

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
