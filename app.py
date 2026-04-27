"""
LIDATO — Client de Transparencia Portal
CSS embebido directamente (más robusto en Streamlit Cloud)
"""

import streamlit as st
import plotly.graph_objects as go
import os, base64
from html import escape
from pathlib import Path
from data_config import CLIENTES, CLIENTE_ACTIVO, ERRORES_VALIDACION

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Lidato | Client de Transparencia Portal",
    page_icon="🟩",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
#  CSS — embebido directamente para máxima compatibilidad
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap');

/* ─── Variables ─── */
:root {
  --teal:       #2AB5A3;
  --teal-dark:  #1E9285;
  --teal-light: #D6F2EF;
  --orange:     #F5A623;
  --orange-drk: #D4891A;
  --orange-lt:  #FEF3DC;
  --bg:         #F0F2F5;
  --white:      #FFFFFF;
  --txt-dk:     #1A2B3C;
  --txt-md:     #4A5568;
  --txt-lt:     #8A9BB0;
  --border:     #E2E8F0;
  --grid:       #E8EDF2;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
.main .block-container { padding: 0 1.4rem 2rem 1.4rem !important; max-width: 1440px !important; }
.stAppViewContainer { background: var(--bg) !important; }
header[data-testid="stHeader"] { background: transparent !important; }
footer { display: none !important; }
div[data-testid="column"] { padding: 0 5px !important; }
section[data-testid="stSidebar"] { background: var(--white) !important; }
.block-container { padding-top: 0 !important; }

/* ─── HEADER ─── */
.ldt-header {
  background: linear-gradient(135deg, #ffffff 0%, #f0faf9 100%);
  border-radius: 0 0 18px 18px;
  box-shadow: 0 4px 20px rgba(42,181,163,0.15);
  margin-bottom: 16px;
  overflow: hidden;
  border-bottom: 4px solid transparent;
  background-clip: padding-box;
}
.ldt-header-inner {
  display: flex; align-items: center;
  justify-content: space-between;
  padding: 16px 28px 14px 20px;
}
.ldt-logo-area {
  display: flex; flex-direction: column;
  align-items: center; gap: 3px;
  min-width: 100px;
}
.ldt-logo-name {
  font-family: 'Nunito', sans-serif; font-weight: 900;
  font-size: 18px; color: var(--teal); letter-spacing: 0.5px;
}
.ldt-center { text-align: center; flex: 1; padding: 0 20px; }
.ldt-empresa {
  font-family: 'Nunito', sans-serif; font-weight: 900;
  font-size: 30px; color: var(--txt-dk); line-height: 1.1;
  letter-spacing: 0.5px;
}
.ldt-portal {
  font-family: 'Nunito', sans-serif; font-weight: 800;
  font-size: 15px; color: var(--teal);
  letter-spacing: 2px; text-transform: uppercase; margin-top: 2px;
}
.ldt-user {
  display: flex; align-items: center; gap: 8px;
  background: var(--teal-light); border: 2px solid var(--teal);
  border-radius: 30px; padding: 8px 18px;
  font-family: 'Nunito', sans-serif; font-weight: 800;
  font-size: 13px; color: var(--teal-dark); white-space: nowrap;
}
.ldt-bar {
  height: 5px;
  background: linear-gradient(90deg, var(--teal) 0%, var(--teal) 65%, var(--orange) 100%);
}

/* ─── KPI CARDS ─── */
.kpi-card {
  background: var(--white); border-radius: 14px;
  padding: 16px 14px 14px 14px;
  box-shadow: 0 2px 14px rgba(0,0,0,0.07);
  border: 1px solid var(--border); border-top: 3px solid var(--teal);
  height: 100%;
}
.kpi-title {
  font-family: 'Nunito', sans-serif; font-weight: 800;
  font-size: 10.5px; color: var(--txt-md);
  text-transform: uppercase; letter-spacing: 0.9px; margin-bottom: 8px;
}
.kpi-num-orange {
  font-family: 'Nunito', sans-serif; font-weight: 900;
  color: var(--orange); line-height: 1;
}
.kpi-num-dark {
  font-family: 'Nunito', sans-serif; font-weight: 900;
  color: var(--txt-dk); line-height: 1;
}
.kpi-sub { font-size: 11px; color: var(--txt-lt); margin-top: 5px; }

.prog-wrap {
  background: var(--grid); border-radius: 8px;
  height: 14px; margin: 12px 0 8px; overflow: hidden;
}
.prog-fill {
  height: 100%; border-radius: 8px;
  background: linear-gradient(90deg, var(--orange), #F7C05A);
}
.otd-circle {
  background: var(--orange); border-radius: 50%;
  width: 60px; height: 60px;
  display: inline-flex; align-items: center; justify-content: center;
  margin-bottom: 6px;
  box-shadow: 0 4px 12px rgba(245,166,35,0.4);
}
.status-dot {
  display: inline-block; width: 10px; height: 10px;
  border-radius: 50%; background: var(--orange);
  margin-right: 5px; vertical-align: middle;
}

/* ─── SECTION CARDS ─── */
.sec-card {
  background: var(--white); border-radius: 14px;
  padding: 16px 14px 12px 14px;
  box-shadow: 0 2px 14px rgba(0,0,0,0.07);
  border: 1px solid var(--border); height: 100%;
}
.sec-title {
  font-family: 'Nunito', sans-serif; font-weight: 800;
  font-size: 11px; color: var(--txt-dk);
  text-transform: uppercase; letter-spacing: 0.9px; margin-bottom: 12px;
}
.sec-sub { font-weight: 600; text-transform: none; font-size: 10px; color: var(--txt-md); }

/* ─── GANTT LEGEND ─── */
.g-legend {
  display: flex; gap: 14px; justify-content: flex-end;
  margin-top: 6px;
}
.g-legend-item {
  display: flex; align-items: center;
  gap: 5px; font-size: 10px; color: var(--txt-md);
}
.g-dot { width: 12px; height: 12px; border-radius: 3px; }
.g-teal   { background: var(--teal); }
.g-teal-l { background: #A8DDD8; }

/* ─── IMPACTO ─── */
.imp-wrap { text-align: center; padding: 8px 4px; }
.imp-icon { font-size: 28px; margin-bottom: 4px; display: block; }
.imp-num {
  font-family: 'Nunito', sans-serif; font-weight: 900;
  font-size: 38px; color: var(--orange); line-height: 1;
}
.imp-unit {
  font-family: 'Nunito', sans-serif; font-weight: 700;
  font-size: 13px; color: var(--txt-md);
}
.imp-lbl { font-size: 10px; color: var(--txt-lt); margin-top: 3px; line-height: 1.35; }

/* ─── AUDITORÍA ─── */
.aud-month {
  font-family: 'Nunito', sans-serif; font-weight: 700;
  font-size: 12px; color: var(--txt-md); margin-bottom: 10px;
}
.aud-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
.aud-cell {
  border-radius: 10px; padding: 13px 6px; text-align: center;
  font-family: 'Nunito', sans-serif; font-weight: 800;
  font-size: 12px; color: white; line-height: 1.5;
}
.a-orange { background: var(--orange); }
.a-teal   { background: var(--teal); }
.a-gray   { background: #B8C5D0; }

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
  background: var(--teal-dark) !important;
  padding: 0 !important; gap: 0 !important;
  border-radius: 12px 12px 0 0 !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  color: rgba(255,255,255,0.55) !important;
  font-family: 'Nunito', sans-serif !important;
  font-weight: 800 !important; font-size: 12px !important;
  letter-spacing: 1px !important; text-transform: uppercase !important;
  padding: 14px 24px !important;
  border: none !important; border-radius: 0 !important;
  transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
  background: var(--orange) !important;
  color: white !important;
  border-radius: 10px 10px 0 0 !important;
}
.stTabs [data-baseweb="tab-panel"] {
  background: var(--white) !important; padding: 20px !important;
  border-radius: 0 0 14px 14px !important;
  border: 1px solid var(--border) !important; border-top: none !important;
}

/* ─── TABLES ─── */
.l-tbl { width: 100%; border-collapse: collapse; font-size: 13px; }
.l-tbl th {
  background: #F7F9FB;
  font-family: 'Nunito', sans-serif; font-weight: 800;
  color: var(--txt-md); font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.9px;
  padding: 10px 14px; text-align: left;
  border-bottom: 2px solid var(--border);
}
.l-tbl td { padding: 10px 14px; border-bottom: 1px solid #F0F4F8; color: var(--txt-dk); }
.l-tbl tr:last-child td { border-bottom: none; }
.l-tbl tr:hover td { background: #FAFCFF; }

/* ─── BADGES ─── */
.bdg {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 3px 12px; border-radius: 20px;
  font-size: 11px; font-weight: 700;
}
.bg-green  { background: #E6F9F1; color: #1A7F4B; }
.bg-yellow { background: var(--orange-lt); color: var(--orange-drk); }
.bg-gray   { background: #EDF0F3; color: #607080; }
.bg-blue   { background: #E3F0FF; color: #1A5FAB; }
.bg-purple { background: #EDE7F6; color: #4527A0; }
.bg-teal   { background: var(--teal-light); color: var(--teal-dark); }

/* ─── CERT BOX ─── */
.cert-box {
  background: var(--teal-light); border: 1.5px solid var(--teal);
  border-radius: 12px; padding: 16px;
  font-size: 12px; color: var(--txt-md); line-height: 1.7;
}
.cert-title {
  font-family: 'Nunito', sans-serif; font-weight: 800;
  color: var(--teal-dark); display: block; margin-bottom: 8px;
}
.cert-date {
  color: var(--teal-dark);
  font-family: 'Nunito', sans-serif;
  font-weight: 800; font-size: 13px;
}

/* Filtros Streamlit */
.stSelectbox label { font-size: 11px !important; font-weight: 700 !important; color: var(--txt-md) !important; }
div[data-baseweb="select"] { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════
BASE_DIR = Path(__file__).parent

def s(v) -> str:
    return escape(str(v))

def bdg(estado: str) -> str:
    mapa = {
        "Aprobado":   ("bg-green",  "●"),
        "En Proceso": ("bg-yellow", "●"),
        "Pendiente":  ("bg-gray",   "●"),
        "Publicado":  ("bg-teal",   "●"),
        "Alta":       ("bg-yellow", "▲"),
        "Media":      ("bg-blue",   "►"),
        "Baja":       ("bg-green",  "▼"),
    }
    cls, icon = mapa.get(estado, ("bg-gray", "●"))
    return f'<span class="bdg {cls}">{icon} {s(estado)}</span>'

def aud_cell(label, estado):
    cls = {"completado":"a-orange","en_proceso":"a-teal","pendiente":"a-gray"}.get(estado,"a-gray")
    icon = "✓" if estado == "completado" else ("⏳" if estado == "en_proceso" else "")
    return f'<div class="aud-cell {cls}">{icon}<br>{s(label)}</div>'

def tbl(headers, rows_html):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return f'<table class="l-tbl"><thead><tr>{ths}</tr></thead><tbody>{rows_html}</tbody></table>'


# ─── LOGO ────────────────────────────────────────────────────
_SVG = """<svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="4"  y="4"  width="18" height="46" rx="4" fill="#2AB5A3"/>
  <rect x="4"  y="40" width="44" height="18" rx="4" fill="#2AB5A3"/>
  <rect x="30" y="4"  width="13" height="13" rx="3" fill="#2AB5A3"/>
  <rect x="47" y="4"  width="13" height="13" rx="3" fill="#F5A623"/>
  <rect x="30" y="21" width="13" height="13" rx="3" fill="#2AB5A3"/>
  <rect x="47" y="21" width="13" height="13" rx="3" fill="#2AB5A3"/>
</svg>"""

@st.cache_data
def get_logo(path: str) -> str:
    try:
        p = Path(path)
        if p.exists() and p.stat().st_size > 0:
            b64 = base64.b64encode(p.read_bytes()).decode()
            return f'<img src="data:image/png;base64,{b64}" style="height:64px;width:auto;" alt="Lidato">'
    except Exception:
        pass
    return _SVG

logo_html = get_logo(str(BASE_DIR / "assets" / "logo.png"))


# ─── GRÁFICAS CACHEADAS ──────────────────────────────────────
@st.cache_data
def build_gauge(value: int) -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=value,
        number={"suffix":"%","font":{"size":40,"family":"Nunito","color":"#F5A623","weight":"bold"}},
        gauge={
            "axis":{"range":[0,100],"showticklabels":False,"tickwidth":0},
            "bar":{"color":"#F5A623","thickness":0.4},
            "bgcolor":"#E8EDF2","borderwidth":0,
            "steps":[{"range":[0,100],"color":"#E8EDF2"}],
            "shape":"angular",
        },
    ))
    fig.update_layout(margin=dict(t=30,b=0,l=16,r=16), height=130,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

@st.cache_data
def build_gantt(data: tuple) -> go.Figure:
    """data = tuple of tuple-of-pairs (hashable). Convierte a dicts internamente."""
    rows = [dict(row) for row in data]
    fig = go.Figure()
    for d in reversed(rows):
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["planificado"]-d["inicio"]], base=d["inicio"],
            orientation="h", marker=dict(color="#A8DDD8", line=dict(width=0)),
            showlegend=False, hovertemplate=f"{s(d['fase'])}: planificado {d['planificado']}%<extra></extra>",
        ))
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["completado"]-d["inicio"]], base=d["inicio"],
            orientation="h", marker=dict(color="#2AB5A3", line=dict(width=0)),
            showlegend=False, hovertemplate=f"{s(d['fase'])}: completado {d['completado']}%<extra></extra>",
        ))
    fig.update_layout(
        barmode="overlay",
        xaxis=dict(range=[0,100], tickvals=[0,25,50,75], ticktext=["0%","25%","50%","75%"],
                   showgrid=True, gridcolor="#E8EDF2", tickfont=dict(size=10,color="#8A9BB0")),
        yaxis=dict(showgrid=False, tickfont=dict(size=10,family="Inter",color="#4A5568")),
        margin=dict(t=6,b=20,l=10,r=10), height=212,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# ═══════════════════════════════════════════════════════════════
#  SELECTOR DE CLIENTE (sidebar — solo si hay más de uno)
# ═══════════════════════════════════════════════════════════════
nombres = list(CLIENTES.keys())
default_idx = nombres.index(CLIENTE_ACTIVO) if CLIENTE_ACTIVO in nombres else 0

if len(nombres) > 1:
    with st.sidebar:
        st.markdown("### 🏢 Cliente")
        sel = st.selectbox("Cliente", nombres, index=default_idx, label_visibility="collapsed")
else:
    sel = nombres[0]

D  = CLIENTES[sel]
KP = D["kpi"];  IMP = D["impacto"];  AUD = D["auditoria"]
IMPL = D["implementaciones"];  BIT = D["bitacora"]
INF  = D["informes"];          BKL = D["backlog"]
EMPRESA = sel
FECHA   = D["fecha_actualizacion"]

# Mostrar errores de validación
if ERRORES_VALIDACION:
    for e in ERRORES_VALIDACION:
        st.warning(f"⚠️ {e}", icon="⚠️")


# ═══════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="ldt-header">
  <div class="ldt-header-inner">
    <div class="ldt-logo-area">
      {logo_html}
      <span class="ldt-logo-name">Lidato</span>
    </div>
    <div class="ldt-center">
      <div class="ldt-empresa">{s(EMPRESA)}</div>
      <div class="ldt-portal">Client de Transparencia Portal</div>
    </div>
    <div class="ldt-user">👤 &nbsp;Usuario</div>
  </div>
  <div class="ldt-bar"></div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 1 — 4 KPI CARDS
# ═══════════════════════════════════════════════════════════════
c1, c2, c3, c4 = st.columns(4, gap="small")

with c1:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-title">Estabilidad de Implementación</div>', unsafe_allow_html=True)
    st.plotly_chart(build_gauge(KP["estabilidad"]["valor"]),
                    use_container_width=True, config={"displayModeBar":False})
    st.markdown(f"""<div style="text-align:center;margin-top:-10px;">
      <span class="status-dot"></span>
      <span style="font-size:11px;font-weight:700;color:#F5A623;">Status</span><br>
      <span class="kpi-sub">{s(KP["estabilidad"]["label"])}</span>
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    v = KP["progreso"]["valor"]
    st.markdown(f"""<div class="kpi-card">
      <div class="kpi-title">Progreso de Implementación Actual</div>
      <div style="text-align:center;padding:14px 0 6px;">
        <div class="kpi-num-orange" style="font-size:52px;">{v}%</div>
        <div class="prog-wrap"><div class="prog-fill" style="width:{v}%;"></div></div>
        <div class="kpi-sub">{s(KP["progreso"]["proyecto"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""<div class="kpi-card">
      <div class="kpi-title">Puntualidad de Informes (OTD)</div>
      <div style="text-align:center;padding:10px 0 6px;">
        <div class="otd-circle">
          <span style="font-size:26px;color:white;font-weight:900;line-height:1;">✓</span>
        </div>
        <div class="kpi-num-orange" style="font-size:48px;">{KP["otd"]["valor"]}%</div>
        <div class="kpi-sub">{s(KP["otd"]["label"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c4:
    n = str(KP["ajustes_tecnicos"]["valor"]).zfill(2)
    st.markdown(f"""<div class="kpi-card">
      <div class="kpi-title">Ajustes Técnicos Activos</div>
      <div style="text-align:center;padding:12px 0 6px;">
        <div class="kpi-num-dark" style="font-size:62px;">{n}</div>
        <div style="font-family:'Nunito',sans-serif;font-weight:700;font-size:13px;color:#4A5568;margin-top:4px;">Solicitudes</div>
        <div class="kpi-sub">{s(KP["ajustes_tecnicos"]["label"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 2 — GANTT + IMPACTO + AUDITORÍA
# ═══════════════════════════════════════════════════════════════
st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
cg, ci, ca = st.columns([2, 1.5, 1.5], gap="small")

with cg:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Track de Implementaciones Activas</div>', unsafe_allow_html=True)
    gantt_data = tuple(tuple(sorted(d.items())) for d in IMPL)
    st.plotly_chart(build_gantt(gantt_data), use_container_width=True, config={"displayModeBar":False})
    st.markdown("""<div class="g-legend">
      <div class="g-legend-item"><div class="g-dot g-teal"></div> Completado</div>
      <div class="g-legend-item"><div class="g-dot g-teal-l"></div> Planificado</div>
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with ci:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Impacto de Negocio y Valor Generado</div>', unsafe_allow_html=True)
    impacto_items = [
        ("⏰", IMP["horas_ahorradas"],        "hrs/mes",  "Horas Operativas<br>Ahorradas (Est. Mensual)"),
        ("⚙️", IMP["procesos_automatizados"], "procesos", "Procesos Manuales<br>Automatizados"),
        ("👥", f"{IMP['tasa_adopcion']}%",    "adoption", "Tasa de Adopción<br>del Sistema"),
    ]
    ci1, ci2, ci3 = st.columns(3)
    for col, (icon, val, unit, lbl) in zip([ci1, ci2, ci3], impacto_items):
        with col:
            st.markdown(f"""<div class="imp-wrap">
              <span class="imp-icon">{icon}</span>
              <div class="imp-num">{s(str(val))}</div>
              <div class="imp-unit">{s(unit)}</div>
              <div class="imp-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with ca:
    st.markdown(f"""<div class="sec-card">
      <div class="sec-title">Auditoría de Entregables
        <span class="sec-sub"> (Checklist Semanal/Mensual)</span>
      </div>
      <div class="aud-month">Currenté del mes</div>
      <div class="aud-grid">
        {aud_cell("Sem 1",        AUD["sem1"])}
        {aud_cell("Sem 2",        AUD["sem2"])}
        {aud_cell("Sem 3",        AUD["sem3"])}
        {aud_cell("Sem 4",        AUD["sem4"])}
        {aud_cell("Mensual KPIs", AUD["mensual_kpis"])}
        {aud_cell("Pendiente",    AUD["pendiente_extra"])}
      </div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 3 — TABS
# ═══════════════════════════════════════════════════════════════
st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["★  BITÁCORA", "REPOSITORIO", "BACKLOG"])

# ── BITÁCORA ─────────────────────────────────────────────────
with tab1:
    estados_b  = ["Todos"] + sorted({r["estado"] for r in BIT})
    solics     = ["Todos"] + sorted({r["solicitante"] for r in BIT})
    fb1, fb2, fb3 = st.columns([1, 1, 2])
    with fb1: f_est_b = st.selectbox("Estado", estados_b, key="b_est")
    with fb2: f_sol   = st.selectbox("Solicitante", solics, key="b_sol")

    data_b = [r for r in BIT
              if (f_est_b == "Todos" or r["estado"] == f_est_b)
              and (f_sol == "Todos" or r["solicitante"] == f_sol)]

    col_t, col_c = st.columns([3, 1], gap="small")
    with col_t:
        if not data_b:
            st.info("Sin registros con los filtros seleccionados.")
        else:
            rows = "".join(f"""<tr>
              <td><strong>{s(r["id"])}</strong></td>
              <td>{s(r["solicitante"])}</td>
              <td>{s(r["asunto"])}</td>
              <td>{bdg(r["estado"])}</td>
              <td style="font-family:monospace;font-size:12px;">{s(r["tiempo"])}</td>
            </tr>""" for r in data_b)
            st.markdown(tbl(["ID Ticket ▼","Solicitante","Asunto","Estado Actual","Tiempo Transcurrido"], rows),
                        unsafe_allow_html=True)
    with col_c:
        st.markdown(f"""<div class="cert-box">
          <span class="cert-title">Última Actualización y Certificación</span>
          Datos sincronizados en tiempo real.<br>
          Última validación aprobada el<br>
          <span class="cert-date">{s(FECHA)}</span>
        </div>""", unsafe_allow_html=True)

# ── REPOSITORIO ───────────────────────────────────────────────
with tab2:
    tipos      = ["Todos"] + sorted({r["tipo"] for r in INF})
    estados_i  = ["Todos"] + sorted({r["estado"] for r in INF})
    fi1, fi2, fi3 = st.columns([1, 1, 2])
    with fi1: f_tipo  = st.selectbox("Tipo",   tipos,     key="i_tip")
    with fi2: f_est_i = st.selectbox("Estado", estados_i, key="i_est")

    data_i = [r for r in INF
              if (f_tipo  == "Todos" or r["tipo"]   == f_tipo)
              and (f_est_i == "Todos" or r["estado"] == f_est_i)]

    if not data_i:
        st.info("Sin informes con los filtros seleccionados.")
    else:
        rows = "".join(f"""<tr>
          <td><strong>{s(r["id"])}</strong></td>
          <td>{s(r["titulo"])}</td>
          <td><span class="bdg bg-blue">{s(r["tipo"])}</span></td>
          <td>{s(r["fecha"])}</td>
          <td>{bdg(r["estado"])}</td>
          <td><a href="{s(r["enlace"])}" target="_blank" rel="noopener noreferrer"
              style="color:#2AB5A3;font-weight:700;font-size:12px;">Ver →</a></td>
        </tr>""" for r in data_i)
        st.markdown(tbl(["ID","Título","Tipo","Fecha","Estado","Acceso"], rows),
                    unsafe_allow_html=True)

# ── BACKLOG ───────────────────────────────────────────────────
with tab3:
    pris       = ["Todas"] + sorted({r["prioridad"] for r in BKL})
    sprints    = ["Todos"] + sorted({r["sprint"] for r in BKL})
    estados_k  = ["Todos"] + sorted({r["estado"] for r in BKL})
    fk1, fk2, fk3, fk4 = st.columns([1, 1, 1, 1])
    with fk1: f_pri  = st.selectbox("Prioridad", pris,     key="k_pri")
    with fk2: f_spr  = st.selectbox("Sprint",    sprints,  key="k_spr")
    with fk3: f_estk = st.selectbox("Estado",    estados_k,key="k_est")

    pri_cls = {"Alta":"bg-yellow","Media":"bg-blue","Baja":"bg-green"}
    data_k = [r for r in BKL
              if (f_pri  == "Todas" or r["prioridad"] == f_pri)
              and (f_spr  == "Todos" or r["sprint"]    == f_spr)
              and (f_estk == "Todos" or r["estado"]    == f_estk)]

    if not data_k:
        st.info("Sin tareas con los filtros seleccionados.")
    else:
        rows = "".join(f"""<tr>
          <td><strong>{s(r["id"])}</strong></td>
          <td>{s(r["tarea"])}</td>
          <td><span class="bdg {pri_cls.get(r["prioridad"],"bg-gray")}">{s(r["prioridad"])}</span></td>
          <td><span class="bdg bg-purple">{s(r["sprint"])}</span></td>
          <td>{s(r["asignado"])}</td>
          <td>{bdg(r["estado"])}</td>
        </tr>""" for r in data_k)
        st.markdown(tbl(["ID","Tarea","Prioridad","Sprint","Asignado","Estado"], rows),
                    unsafe_allow_html=True)
