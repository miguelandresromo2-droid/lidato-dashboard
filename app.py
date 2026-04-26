import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data_config import (
    EMPRESA_NOMBRE, FECHA_ACTUALIZACION,
    KPI, IMPLEMENTACIONES, IMPACTO, AUDITORIA,
    BITACORA, INFORMES, BACKLOG
)

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Lidato | Client de Transparencia Portal",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL CSS ────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');

  /* ── Reset & base ── */
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .main .block-container { padding: 1rem 2rem 2rem 2rem; max-width: 1400px; }

  /* ── Header ── */
  .lidato-header {
    display: flex; align-items: center; justify-content: space-between;
    background: white; border-bottom: 3px solid #E8EDF2;
    padding: 12px 24px; border-radius: 12px; margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }
  .lidato-header-left { display: flex; align-items: center; gap: 14px; }
  .lidato-logo-text {
    font-family: 'Montserrat', sans-serif; font-weight: 800;
    font-size: 22px; color: #0D47A1; letter-spacing: 1px;
  }
  .lidato-divider { color: #B0BEC5; font-size: 22px; }
  .lidato-portal-text {
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 14px; color: #37474F; letter-spacing: 2px; text-transform: uppercase;
  }

  /* ── Section title ── */
  .section-title {
    font-family: 'Montserrat', sans-serif; font-weight: 800;
    font-size: 20px; color: #212121; margin: 8px 0 16px 0; letter-spacing: 0.5px;
  }

  /* ── KPI Cards ── */
  .kpi-card {
    background: white; border-radius: 14px; padding: 20px 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07); border: 1px solid #E8EDF2;
    text-align: center; height: 100%;
  }
  .kpi-card-title {
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 12px; color: #455A64; text-transform: uppercase;
    letter-spacing: 0.8px; margin-bottom: 12px;
  }
  .kpi-big-number {
    font-family: 'Montserrat', sans-serif; font-weight: 800;
    font-size: 52px; color: #212121; line-height: 1;
  }
  .kpi-sub {
    font-size: 11px; color: #78909C; margin-top: 6px;
  }
  .kpi-otd-badge {
    background: #E8F5E9; border-radius: 50%; width: 70px; height: 70px;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 8px auto;
  }
  .status-dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 6px; }
  .dot-green  { background: #43A047; }

  /* ── Section cards ── */
  .section-card {
    background: white; border-radius: 14px; padding: 18px 18px 12px 18px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07); border: 1px solid #E8EDF2; height: 100%;
  }
  .section-card-title {
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 12px; color: #455A64; text-transform: uppercase;
    letter-spacing: 0.8px; margin-bottom: 14px;
  }

  /* ── Impacto ── */
  .impacto-item { text-align: center; padding: 10px 6px; }
  .impacto-num {
    font-family: 'Montserrat', sans-serif; font-weight: 800;
    font-size: 38px; color: #0D47A1;
  }
  .impacto-unit {
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 13px; color: #455A64;
  }
  .impacto-label { font-size: 11px; color: #78909C; margin-top: 4px; }
  .impacto-icon { font-size: 28px; margin-bottom: 4px; }

  /* ── Auditoría ── */
  .audit-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
  .audit-cell {
    border-radius: 10px; padding: 14px 8px; text-align: center;
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 13px; color: white;
  }
  .audit-green  { background: #43A047; }
  .audit-gray   { background: #B0BEC5; }
  .audit-yellow { background: #FFA000; }

  /* ── Tabs ── */
  .tab-container {
    background: white; border-radius: 14px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07); border: 1px solid #E8EDF2;
    overflow: hidden; margin-top: 16px;
  }

  /* Override Streamlit tab styling */
  .stTabs [data-baseweb="tab-list"] {
    background: #0D47A1; padding: 0; gap: 0; border-radius: 14px 14px 0 0;
  }
  .stTabs [data-baseweb="tab"] {
    background: transparent; color: rgba(255,255,255,0.7) !important;
    font-family: 'Montserrat', sans-serif; font-weight: 700;
    font-size: 12px; letter-spacing: 0.8px; text-transform: uppercase;
    padding: 14px 20px; border: none; border-radius: 0;
  }
  .stTabs [aria-selected="true"] {
    background: #1565C0 !important; color: white !important;
    border-bottom: 3px solid #FFD600;
  }
  .stTabs [data-baseweb="tab-panel"] {
    background: white; padding: 20px;
  }

  /* ── Table ── */
  .lidato-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .lidato-table th {
    background: #F5F7FA; font-family: 'Montserrat', sans-serif; font-weight: 700;
    color: #37474F; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px;
    padding: 10px 14px; text-align: left; border-bottom: 2px solid #E8EDF2;
  }
  .lidato-table td {
    padding: 10px 14px; border-bottom: 1px solid #F0F4F8; color: #37474F;
  }
  .lidato-table tr:last-child td { border-bottom: none; }
  .lidato-table tr:hover td { background: #F8FBFF; }

  /* ── Estado badges ── */
  .badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;
  }
  .badge-green  { background: #E8F5E9; color: #2E7D32; }
  .badge-yellow { background: #FFF8E1; color: #F57F17; }
  .badge-gray   { background: #ECEFF1; color: #546E7A; }
  .badge-blue   { background: #E3F2FD; color: #1565C0; }
  .badge-red    { background: #FFEBEE; color: #C62828; }

  /* ── Footer cert box ── */
  .cert-box {
    background: #F8FBFF; border: 1px solid #BBDEFB;
    border-radius: 10px; padding: 14px 16px; font-size: 12px; color: #37474F;
  }
  .cert-box strong { font-family: 'Montserrat', sans-serif; font-weight: 700; color: #0D47A1; }

  /* ── Priority badges ── */
  .pri-alta   { color: #C62828; font-weight: 700; }
  .pri-media  { color: #E65100; font-weight: 700; }
  .pri-baja   { color: #2E7D32; font-weight: 700; }

  /* ── Streamlit overrides ── */
  div[data-testid="column"] { padding: 0 6px; }
  .stMetric { display: none; }
  header[data-testid="stHeader"] { background: #F0F4F8; }
  .stAppViewContainer { background: #F0F4F8; }
  footer { display: none; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════

def badge(estado: str) -> str:
    mapa = {
        "Aprobado":   ("badge-green",  "●"),
        "En Proceso": ("badge-yellow", "●"),
        "Pendiente":  ("badge-gray",   "●"),
        "Publicado":  ("badge-blue",   "●"),
        "Alta":       ("badge-red",    ""),
        "Media":      ("badge-yellow", ""),
        "Baja":       ("badge-green",  ""),
    }
    cls, icon = mapa.get(estado, ("badge-gray", "●"))
    return f'<span class="badge {cls}">{icon} {estado}</span>'


def audit_cell(label: str, estado: str) -> str:
    cls = {"completado": "audit-green", "pendiente": "audit-gray", "en_proceso": "audit-yellow"}.get(estado, "audit-gray")
    check = "✓" if estado == "completado" else ("⏳" if estado == "en_proceso" else "")
    return f'<div class="audit-cell {cls}">{check}<br>{label}</div>'


def gauge_chart(value: int, color: str = "#43A047") -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": "%", "font": {"size": 36, "family": "Montserrat", "color": "#212121", "weight": "bold"}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 0, "tickcolor": "white", "showticklabels": False},
            "bar": {"color": color, "thickness": 0.35},
            "bgcolor": "#E8EDF2",
            "borderwidth": 0,
            "steps": [{"range": [0, 100], "color": "#E8EDF2"}],
            "threshold": {"line": {"color": color, "width": 4}, "thickness": 0.75, "value": value},
            "shape": "angular",
        },
    ))
    fig.update_layout(
        margin=dict(t=30, b=5, l=20, r=20),
        height=140, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def gantt_chart(data: list) -> go.Figure:
    fases = [d["fase"] for d in data]
    fig = go.Figure()

    for d in data:
        # Barra de fondo (planificado)
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["planificado"] - d["inicio"]],
            base=d["inicio"], orientation="h",
            marker=dict(color="#90CAF9", line=dict(width=0)),
            showlegend=False, hovertemplate=f"{d['fase']}: {d['planificado']}%<extra></extra>",
        ))
        # Barra completado
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["completado"] - d["inicio"]],
            base=d["inicio"], orientation="h",
            marker=dict(color="#1565C0", line=dict(width=0)),
            showlegend=False, hovertemplate=f"{d['fase']}: {d['completado']}% completado<extra></extra>",
        ))

    fig.update_layout(
        barmode="overlay",
        xaxis=dict(range=[0, 100], tickvals=[0, 25, 50, 75, 100],
                   ticktext=["0%", "25%", "50%", "75%", "100%"],
                   showgrid=True, gridcolor="#E8EDF2", tickfont=dict(size=10)),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, family="Inter")),
        margin=dict(t=10, b=20, l=10, r=10),
        height=220, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter"),
    )
    return fig


# ═══════════════════════════════════════════════════════════════
#  RENDER
# ═══════════════════════════════════════════════════════════════

# ── HEADER ───────────────────────────────────────────────────
st.markdown(f"""
<div class="lidato-header">
  <div class="lidato-header-left">
    <span style="font-size:26px;">🔷</span>
    <span class="lidato-logo-text">LIDATO</span>
    <span class="lidato-divider">|</span>
    <span class="lidato-portal-text">Client de Transparencia Portal</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:20px;">🔷</span>
    <span style="font-family:Montserrat;font-weight:800;color:#0D47A1;font-size:16px;">Lidato</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── EMPRESA TÍTULO ───────────────────────────────────────────
st.markdown(f'<div class="section-title">{EMPRESA_NOMBRE}</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  ROW 1 — KPI CARDS
# ═══════════════════════════════════════════════════════════════
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-card-title">Estabilidad de Implementación</div>', unsafe_allow_html=True)
    fig = gauge_chart(KPI["estabilidad"]["valor"], "#43A047")
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown(f"""
    <div style="text-align:center;margin-top:-10px;">
      <span class="status-dot dot-green"></span>
      <span style="font-size:11px;color:#43A047;font-weight:600;">Status</span><br>
      <span class="kpi-sub">{KPI["estabilidad"]["label"]}</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-card-title">Progreso de Implementación Actual</div>', unsafe_allow_html=True)
    v = KPI["progreso"]["valor"]
    st.markdown(f"""
    <div style="text-align:center;padding:24px 0 10px 0;">
      <div style="font-family:Montserrat;font-weight:800;font-size:44px;color:#212121;">{v}%</div>
      <div style="background:#E8EDF2;border-radius:8px;height:14px;margin:14px 8px 10px 8px;overflow:hidden;">
        <div style="background:linear-gradient(90deg,#1565C0,#42A5F5);width:{v}%;height:100%;border-radius:8px;transition:width 0.8s;"></div>
      </div>
      <div style="font-size:11px;color:#78909C;">{KPI["progreso"]["proyecto"]}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-card-title">Puntualidad de Informes (OTD)</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:center;padding:16px 0 10px 0;">
      <div style="background:#E8F5E9;border-radius:50%;width:64px;height:64px;
                  display:inline-flex;align-items:center;justify-content:center;margin-bottom:8px;">
        <span style="font-size:30px;">✅</span>
      </div><br>
      <div style="font-family:Montserrat;font-weight:800;font-size:44px;color:#212121;">{KPI["otd"]["valor"]}%</div>
      <div style="font-size:11px;color:#78909C;">{KPI["otd"]["label"]}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
    st.markdown('<div class="kpi-card-title">Ajustes Técnicos Activos</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:center;padding:20px 0 10px 0;">
      <div style="font-family:Montserrat;font-weight:800;font-size:64px;color:#212121;line-height:1;">
        {str(KPI["ajustes_tecnicos"]["valor"]).zfill(2)}
      </div>
      <div style="font-size:13px;color:#37474F;font-weight:600;margin-top:6px;">Solicitudes</div>
      <div style="font-size:11px;color:#78909C;">{KPI["ajustes_tecnicos"]["label"]}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  ROW 2 — MIDDLE SECTION
# ═══════════════════════════════════════════════════════════════
col_gantt, col_impacto, col_audit = st.columns([2, 1.5, 1.5], gap="small")

with col_gantt:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-card-title">Track de Implementaciones Activas</div>', unsafe_allow_html=True)
    fig_gantt = gantt_chart(IMPLEMENTACIONES)
    st.plotly_chart(fig_gantt, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

with col_impacto:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-card-title">Impacto de Negocio y Valor Generado</div>', unsafe_allow_html=True)
    items = [
        ("⏰", IMPACTO["horas_ahorradas"], "hrs/mes", "Horas Operativas<br>Ahorradas (Est. Mensual)"),
        ("⚙️", IMPACTO["procesos_automatizados"], "procesos", "Procesos Manuales<br>Automatizados"),
        ("👥", f"{IMPACTO['tasa_adopcion']}%", "adoption", "Tasa de Adopción<br>del Sistema"),
    ]
    cols_imp = st.columns(3)
    for i, (icon, val, unit, label) in enumerate(items):
        with cols_imp[i]:
            st.markdown(f"""
            <div class="impacto-item">
              <div class="impacto-icon">{icon}</div>
              <div class="impacto-num">{val}</div>
              <div class="impacto-unit">{unit}</div>
              <div class="impacto-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_audit:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-card-title">Auditoría de Entregables <span style="font-weight:400;font-size:10px;">(Checklist Semanal/Mensual)</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:Montserrat;font-weight:700;font-size:12px;color:#37474F;margin-bottom:10px;">
      Currenté del mes
    </div>
    """, unsafe_allow_html=True)
    A = AUDITORIA
    st.markdown(f"""
    <div class="audit-grid">
      {audit_cell("Sem 1", A["sem1"])}
      {audit_cell("Sem 2", A["sem2"])}
      {audit_cell("Sem 3", A["sem3"])}
      {audit_cell("Sem 4", A["sem4"])}
      {audit_cell("Mensual KPIs", A["mensual_kpis"])}
      {audit_cell("Pendiente", A["pendiente_extra"])}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  ROW 3 — TABS
# ═══════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs([
    "★ Bitácora de Ajustes de Implementación",
    "Repositorio de Informes",
    "Backlog de Implementación",
])

# ── TAB 1: BITÁCORA ──────────────────────────────────────────
with tab1:
    col_tabla, col_cert = st.columns([3, 1], gap="small")

    with col_tabla:
        rows_html = ""
        for r in BITACORA:
            rows_html += f"""
            <tr>
              <td><strong>{r["id"]}</strong></td>
              <td>{r["solicitante"]}</td>
              <td>{r["asunto"]}</td>
              <td>{badge(r["estado"])}</td>
              <td style="font-family:monospace;font-size:12px;">{r["tiempo"]}</td>
            </tr>"""
        st.markdown(f"""
        <table class="lidato-table">
          <thead><tr>
            <th>ID Ticket ▼</th><th>Solicitante</th><th>Asunto</th>
            <th>Estado Actual</th><th>Tiempo Transcurrido</th>
          </tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
        """, unsafe_allow_html=True)

    with col_cert:
        st.markdown(f"""
        <div class="cert-box">
          <strong>Última Actualización y Certificación</strong><br><br>
          Datos sincronizados en tiempo real.<br>
          Última validación aprobada el<br>
          <strong style="color:#1565C0;">{FECHA_ACTUALIZACION}</strong>
        </div>
        """, unsafe_allow_html=True)

# ── TAB 2: REPOSITORIO ───────────────────────────────────────
with tab2:
    rows_html = ""
    for r in INFORMES:
        rows_html += f"""
        <tr>
          <td><strong>{r["id"]}</strong></td>
          <td>{r["titulo"]}</td>
          <td><span style="font-size:11px;background:#E3F2FD;color:#1565C0;padding:2px 8px;border-radius:10px;font-weight:600;">{r["tipo"]}</span></td>
          <td>{r["fecha"]}</td>
          <td>{badge(r["estado"])}</td>
          <td><a href="{r["enlace"]}" style="color:#1565C0;font-size:12px;font-weight:600;">Ver →</a></td>
        </tr>"""
    st.markdown(f"""
    <table class="lidato-table">
      <thead><tr>
        <th>ID</th><th>Título</th><th>Tipo</th><th>Fecha</th><th>Estado</th><th>Acceso</th>
      </tr></thead>
      <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

# ── TAB 3: BACKLOG ───────────────────────────────────────────
with tab3:
    pri_cls = {"Alta": "pri-alta", "Media": "pri-media", "Baja": "pri-baja"}
    rows_html = ""
    for r in BACKLOG:
        cls = pri_cls.get(r["prioridad"], "")
        rows_html += f"""
        <tr>
          <td><strong>{r["id"]}</strong></td>
          <td>{r["tarea"]}</td>
          <td><span class="{cls}">{r["prioridad"]}</span></td>
          <td><span style="font-size:11px;background:#EDE7F6;color:#4527A0;padding:2px 8px;border-radius:10px;font-weight:600;">{r["sprint"]}</span></td>
          <td>{r["asignado"]}</td>
          <td>{badge(r["estado"])}</td>
        </tr>"""
    st.markdown(f"""
    <table class="lidato-table">
      <thead><tr>
        <th>ID</th><th>Tarea</th><th>Prioridad</th><th>Sprint</th><th>Asignado</th><th>Estado</th>
      </tr></thead>
      <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)
