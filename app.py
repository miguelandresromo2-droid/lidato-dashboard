import streamlit as st
import plotly.graph_objects as go
import os, base64
from data_config import (
    EMPRESA_NOMBRE, FECHA_ACTUALIZACION,
    KPI, IMPLEMENTACIONES, IMPACTO, AUDITORIA,
    BITACORA, INFORMES, BACKLOG
)

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Lidato | Client de Transparencia Portal",
    page_icon="🟩",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL CSS ────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap');

  :root {
    --teal:        #2AB5A3;
    --teal-dark:   #1E9285;
    --teal-light:  #D6F2EF;
    --orange:      #F5A623;
    --orange-lt:   #FEF3DC;
    --bg:          #EEF1F5;
    --card:        #FFFFFF;
    --txt-dark:    #1A2B3C;
    --txt-mid:     #4A5568;
    --txt-lt:      #8A9BB0;
    --border:      #E2E8F0;
  }

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .main .block-container { padding: 0 1.6rem 2rem 1.6rem; max-width: 1440px; }

  /* ── HEADER ── */
  .ldt-header {
    background: white;
    border-radius: 0 0 16px 16px;
    box-shadow: 0 3px 16px rgba(0,0,0,0.09);
    margin-bottom: 18px;
    overflow: hidden;
  }
  .ldt-header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 24px 12px 18px;
  }
  .ldt-logo-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    min-width: 110px;
  }
  .ldt-logo-name {
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    font-size: 17px;
    color: var(--teal);
    letter-spacing: 0.5px;
  }
  .ldt-center { text-align: center; flex: 1; }
  .ldt-empresa {
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    font-size: 26px;
    color: var(--txt-dark);
    letter-spacing: 0.3px;
  }
  .ldt-portal {
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 14px;
    color: var(--teal);
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }
  .ldt-user {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--teal-light);
    border: 1.5px solid var(--teal);
    border-radius: 24px;
    padding: 7px 16px;
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 13px;
    color: var(--teal-dark);
    min-width: 100px;
    justify-content: center;
  }
  .ldt-accent-bar {
    height: 5px;
    background: linear-gradient(90deg, var(--teal) 0%, var(--teal) 68%, var(--orange) 100%);
  }

  /* ── KPI CARDS ── */
  .kpi-card {
    background: white;
    border-radius: 14px;
    padding: 16px 14px 12px 14px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1px solid var(--border);
    border-top: 3px solid var(--teal);
    height: 100%;
  }
  .kpi-title {
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 11px;
    color: var(--txt-mid);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
  }
  .kpi-orange {
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    color: var(--orange);
    line-height: 1;
  }
  .kpi-dark {
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    color: var(--txt-dark);
    line-height: 1;
  }
  .kpi-sub { font-size: 11px; color: var(--txt-lt); margin-top: 5px; }

  .prog-wrap {
    background: #E8EDF2;
    border-radius: 8px;
    height: 13px;
    margin: 12px 0 8px 0;
    overflow: hidden;
  }
  .prog-fill {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, var(--orange) 0%, #F7C05A 100%);
  }
  .otd-badge {
    background: var(--orange);
    border-radius: 50%;
    width: 56px; height: 56px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 6px;
  }

  /* ── SECTION CARDS ── */
  .sec-card {
    background: white;
    border-radius: 14px;
    padding: 16px 14px 12px 14px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1px solid var(--border);
    height: 100%;
  }
  .sec-title {
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 11px;
    color: var(--txt-dark);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 12px;
  }

  /* ── IMPACTO ── */
  .imp-item { text-align: center; padding: 6px 2px; }
  .imp-icon { font-size: 26px; margin-bottom: 4px; }
  .imp-num  { font-family: 'Nunito', sans-serif; font-weight: 900; font-size: 36px; color: var(--orange); line-height: 1; }
  .imp-unit { font-family: 'Nunito', sans-serif; font-weight: 700; font-size: 12px; color: var(--txt-mid); }
  .imp-lbl  { font-size: 10px; color: var(--txt-lt); margin-top: 3px; line-height: 1.3; }

  /* ── AUDITORÍA ── */
  .audit-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 7px; }
  .audit-cell {
    border-radius: 9px; padding: 11px 4px;
    text-align: center;
    font-family: 'Nunito', sans-serif; font-weight: 800;
    font-size: 12px; color: white; line-height: 1.4;
  }
  .a-orange { background: var(--orange); }
  .a-teal   { background: var(--teal); }
  .a-gray   { background: #B8C5D0; }

  /* ── TABS ── */
  .stTabs [data-baseweb="tab-list"] {
    background: var(--teal-dark) !important;
    padding: 0; gap: 0;
    border-radius: 12px 12px 0 0;
  }
  .stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(255,255,255,0.6) !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: 12px !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    padding: 13px 22px !important;
    border: none !important;
    border-radius: 0 !important;
  }
  .stTabs [aria-selected="true"] {
    background: var(--orange) !important;
    color: white !important;
    border-radius: 10px 10px 0 0 !important;
  }
  .stTabs [data-baseweb="tab-panel"] {
    background: white !important;
    padding: 20px !important;
    border-radius: 0 0 14px 14px !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
  }

  /* ── TABLE ── */
  .l-tbl { width: 100%; border-collapse: collapse; font-size: 13px; }
  .l-tbl th {
    background: #F7F9FB;
    font-family: 'Nunito', sans-serif; font-weight: 800;
    color: var(--txt-mid); font-size: 11px;
    text-transform: uppercase; letter-spacing: 0.8px;
    padding: 10px 14px; text-align: left;
    border-bottom: 2px solid var(--border);
  }
  .l-tbl td { padding: 10px 14px; border-bottom: 1px solid #F0F4F8; color: var(--txt-dark); }
  .l-tbl tr:last-child td { border-bottom: none; }
  .l-tbl tr:hover td { background: #FAFCFF; }

  /* ── BADGES ── */
  .bdg {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 3px 11px; border-radius: 20px;
    font-size: 11px; font-weight: 700;
  }
  .bg-green  { background: #E6F9F1; color: #1A7F4B; }
  .bg-yellow { background: var(--orange-lt); color: #B07309; }
  .bg-gray   { background: #EDF0F3; color: #607080; }
  .bg-blue   { background: #E3F0FF; color: #1A5FAB; }
  .bg-purple { background: #EDE7F6; color: #4527A0; }

  /* ── CERT BOX ── */
  .cert-box {
    background: var(--teal-light);
    border: 1.5px solid var(--teal);
    border-radius: 12px;
    padding: 16px;
    font-size: 12px;
    color: var(--txt-mid);
    line-height: 1.7;
  }
  .cert-box strong { color: var(--teal-dark); font-family:'Nunito',sans-serif; font-weight:800; }

  /* ── Overrides ── */
  div[data-testid="column"] { padding: 0 5px; }
  .stAppViewContainer { background: var(--bg) !important; }
  header[data-testid="stHeader"] { background: transparent !important; }
  footer { display: none; }
  [data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════

def bdg(estado: str) -> str:
    m = {
        "Aprobado":   ("bg-green",  "●"),
        "En Proceso": ("bg-yellow", "●"),
        "Pendiente":  ("bg-gray",   "●"),
        "Publicado":  ("bg-blue",   "●"),
        "Alta":       ("bg-yellow", "▲"),
        "Media":      ("bg-blue",   "►"),
        "Baja":       ("bg-green",  "▼"),
    }
    c, i = m.get(estado, ("bg-gray", "●"))
    return f'<span class="bdg {c}">{i} {estado}</span>'

def aud(label, estado):
    cls = {"completado": "a-orange", "en_proceso": "a-teal", "pendiente": "a-gray"}.get(estado, "a-gray")
    ico = "✓" if estado == "completado" else ("⏳" if estado == "en_proceso" else "")
    return f'<div class="audit-cell {cls}">{ico}<br>{label}</div>'

def gauge(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=value,
        number={"suffix": "%", "font": {"size": 38, "family": "Nunito", "color": "#F5A623"}},
        gauge={
            "axis": {"range": [0, 100], "showticklabels": False, "tickwidth": 0},
            "bar": {"color": "#F5A623", "thickness": 0.38},
            "bgcolor": "#E8EDF2", "borderwidth": 0,
            "steps": [{"range": [0, 100], "color": "#E8EDF2"}],
            "shape": "angular",
        },
    ))
    fig.update_layout(margin=dict(t=28, b=0, l=14, r=14), height=128,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def gantt(data):
    fig = go.Figure()
    for d in reversed(data):
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["planificado"] - d["inicio"]], base=d["inicio"],
            orientation="h", marker=dict(color="#A8DDD8", line=dict(width=0)),
            showlegend=False,
            hovertemplate=f"{d['fase']}: planificado {d['planificado']}%<extra></extra>",
        ))
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["completado"] - d["inicio"]], base=d["inicio"],
            orientation="h", marker=dict(color="#2AB5A3", line=dict(width=0)),
            showlegend=False,
            hovertemplate=f"{d['fase']}: completado {d['completado']}%<extra></extra>",
        ))
    fig.update_layout(
        barmode="overlay",
        xaxis=dict(range=[0, 100], tickvals=[0, 25, 50, 75],
                   ticktext=["0%", "25%", "50%", "75%"],
                   showgrid=True, gridcolor="#E8EDF2",
                   tickfont=dict(size=10, color="#8A9BB0")),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, family="Inter", color="#4A5568")),
        margin=dict(t=6, b=20, l=10, r=10),
        height=208, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# ═══════════════════════════════════════════════════════════════
#  LOGO (carga desde assets/logo.png si existe)
# ═══════════════════════════════════════════════════════════════
LOGO_PATH = "assets/logo.png"
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    logo_img = f'<img src="data:image/png;base64,{b64}" style="height:60px;width:auto;" alt="Logo Lidato">'
else:
    # SVG aproximado del logo Lidato (L teal + cuadros + naranja)
    logo_img = """<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
      <rect x="4"  y="4"  width="16" height="42" rx="3" fill="#2AB5A3"/>
      <rect x="4"  y="38" width="40" height="16" rx="3" fill="#2AB5A3"/>
      <rect x="28" y="4"  width="12" height="11" rx="2" fill="#2AB5A3"/>
      <rect x="44" y="4"  width="12" height="11" rx="2" fill="#F5A623"/>
      <rect x="28" y="19" width="12" height="11" rx="2" fill="#2AB5A3"/>
      <rect x="44" y="19" width="12" height="11" rx="2" fill="#2AB5A3"/>
    </svg>"""


# ═══════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="ldt-header">
  <div class="ldt-header-inner">
    <div class="ldt-logo-col">
      {logo_img}
      <div class="ldt-logo-name">Lidato</div>
    </div>
    <div class="ldt-center">
      <div class="ldt-empresa">{EMPRESA_NOMBRE}</div>
      <div class="ldt-portal">Client de Transparencia Portal</div>
    </div>
    <div class="ldt-user">👤 &nbsp;Usuario</div>
  </div>
  <div class="ldt-accent-bar"></div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 1 — KPI CARDS
# ═══════════════════════════════════════════════════════════════
c1, c2, c3, c4 = st.columns(4, gap="small")

with c1:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-title">Estabilidad de Implementación</div>', unsafe_allow_html=True)
    st.plotly_chart(gauge(KPI["estabilidad"]["valor"]), use_container_width=True, config={"displayModeBar": False})
    st.markdown(f"""
    <div style="text-align:center;margin-top:-8px;">
      <span style="display:inline-block;width:9px;height:9px;border-radius:50%;
                   background:#F5A623;margin-right:5px;"></span>
      <span style="font-size:11px;font-weight:700;color:#F5A623;">Status</span><br>
      <span class="kpi-sub">{KPI["estabilidad"]["label"]}</span>
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    v = KPI["progreso"]["valor"]
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">Progreso de Implementación Actual</div>
      <div style="text-align:center;padding:16px 0 6px 0;">
        <div class="kpi-orange" style="font-size:50px;">{v}%</div>
        <div class="prog-wrap"><div class="prog-fill" style="width:{v}%;"></div></div>
        <div class="kpi-sub">{KPI["progreso"]["proyecto"]}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">Puntualidad de Informes (OTD)</div>
      <div style="text-align:center;padding:12px 0 6px 0;">
        <div class="otd-badge"><span style="font-size:24px;color:white;font-weight:900;">✓</span></div>
        <div class="kpi-orange" style="font-size:46px;">{KPI["otd"]["valor"]}%</div>
        <div class="kpi-sub">{KPI["otd"]["label"]}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c4:
    n = str(KPI["ajustes_tecnicos"]["valor"]).zfill(2)
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">Ajustes Técnicos Activos</div>
      <div style="text-align:center;padding:14px 0 6px 0;">
        <div class="kpi-dark" style="font-size:60px;">{n}</div>
        <div style="font-size:13px;color:#4A5568;font-weight:700;margin-top:4px;">Solicitudes</div>
        <div class="kpi-sub">{KPI["ajustes_tecnicos"]["label"]}</div>
      </div>
    </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  ROW 2 — GANTT + IMPACTO + AUDITORÍA
# ═══════════════════════════════════════════════════════════════
cg, ci, ca = st.columns([2, 1.5, 1.5], gap="small")

with cg:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Track de Implementaciones Activas</div>', unsafe_allow_html=True)
    st.plotly_chart(gantt(IMPLEMENTACIONES), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

with ci:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Impacto de Negocio y Valor Generado</div>', unsafe_allow_html=True)
    items = [
        ("⏰", IMPACTO["horas_ahorradas"], "hrs/mes", "Horas Operativas<br>Ahorradas (Est. Mensual)"),
        ("⚙️", IMPACTO["procesos_automatizados"], "procesos", "Procesos Manuales<br>Automatizados"),
        ("👥", f"{IMPACTO['tasa_adopcion']}%", "adoption", "Tasa de Adopción<br>del Sistema"),
    ]
    cols_i = st.columns(3)
    for idx, (icon, val, unit, label) in enumerate(items):
        with cols_i[idx]:
            st.markdown(f"""
            <div class="imp-item">
              <div class="imp-icon">{icon}</div>
              <div class="imp-num">{val}</div>
              <div class="imp-unit">{unit}</div>
              <div class="imp-lbl">{label}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with ca:
    A = AUDITORIA
    st.markdown(f"""
    <div class="sec-card">
      <div class="sec-title">Auditoría de Entregables
        <span style="font-weight:600;text-transform:none;font-size:10px;">
          (Checklist Semanal/Mensual)
        </span>
      </div>
      <div style="font-family:'Nunito',sans-serif;font-weight:700;font-size:12px;
                  color:#4A5568;margin-bottom:10px;">Currenté del mes</div>
      <div class="audit-grid">
        {aud("Sem 1",        A["sem1"])}
        {aud("Sem 2",        A["sem2"])}
        {aud("Sem 3",        A["sem3"])}
        {aud("Sem 4",        A["sem4"])}
        {aud("Mensual KPIs", A["mensual_kpis"])}
        {aud("Pendiente",    A["pendiente_extra"])}
      </div>
    </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  ROW 3 — TABS
# ═══════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs(["★  BITÁCORA", "REPOSITORIO", "BACKLOG"])

# ── BITÁCORA ─────────────────────────────────────────────────
with tab1:
    col_t, col_c = st.columns([3, 1], gap="small")
    with col_t:
        rows = "".join(f"""<tr>
          <td><strong>{r["id"]}</strong></td>
          <td>{r["solicitante"]}</td>
          <td>{r["asunto"]}</td>
          <td>{bdg(r["estado"])}</td>
          <td style="font-family:monospace;font-size:12px;">{r["tiempo"]}</td>
        </tr>""" for r in BITACORA)
        st.markdown(f"""
        <table class="l-tbl">
          <thead><tr>
            <th>ID Ticket ▼</th><th>Solicitante</th><th>Asunto</th>
            <th>Estado Actual</th><th>Tiempo Transcurrido</th>
          </tr></thead><tbody>{rows}</tbody>
        </table>""", unsafe_allow_html=True)
    with col_c:
        st.markdown(f"""
        <div class="cert-box">
          <strong>Última Actualización y Certificación</strong><br><br>
          Datos sincronizados en tiempo real.<br>
          Última validación aprobada el<br>
          <strong style="color:#1E9285;font-size:13px;">{FECHA_ACTUALIZACION}</strong>
        </div>""", unsafe_allow_html=True)

# ── REPOSITORIO ───────────────────────────────────────────────
with tab2:
    rows = "".join(f"""<tr>
      <td><strong>{r["id"]}</strong></td>
      <td>{r["titulo"]}</td>
      <td><span class="bdg bg-blue">{r["tipo"]}</span></td>
      <td>{r["fecha"]}</td>
      <td>{bdg(r["estado"])}</td>
      <td><a href="{r["enlace"]}" style="color:#2AB5A3;font-weight:700;font-size:12px;">Ver →</a></td>
    </tr>""" for r in INFORMES)
    st.markdown(f"""
    <table class="l-tbl">
      <thead><tr>
        <th>ID</th><th>Título</th><th>Tipo</th><th>Fecha</th><th>Estado</th><th>Acceso</th>
      </tr></thead><tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)

# ── BACKLOG ───────────────────────────────────────────────────
with tab3:
    pri_map = {"Alta": "bg-yellow", "Media": "bg-blue", "Baja": "bg-green"}
    rows = "".join(f"""<tr>
      <td><strong>{r["id"]}</strong></td>
      <td>{r["tarea"]}</td>
      <td><span class="bdg {pri_map.get(r["prioridad"], "bg-gray")}">{r["prioridad"]}</span></td>
      <td><span class="bdg bg-purple">{r["sprint"]}</span></td>
      <td>{r["asignado"]}</td>
      <td>{bdg(r["estado"])}</td>
    </tr>""" for r in BACKLOG)
    st.markdown(f"""
    <table class="l-tbl">
      <thead><tr>
        <th>ID</th><th>Tarea</th><th>Prioridad</th><th>Sprint</th><th>Asignado</th><th>Estado</th>
      </tr></thead><tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)
