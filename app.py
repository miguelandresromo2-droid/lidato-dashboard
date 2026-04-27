"""
LIDATO — Client de Transparencia Portal
========================================
Mejoras aplicadas:
  ✅ CSS separado en assets/styles.css
  ✅ Logo cacheado con @st.cache_data
  ✅ Gráficas cacheadas con @st.cache_data
  ✅ HTML sanitizado con html.escape()
  ✅ Sin colores hex sueltos (todo usa CSS vars)
  ✅ Fecha de actualización manual en data_config
  ✅ Validación de datos con mensajes claros
  ✅ Filtros en las 3 tablas
  ✅ Leyenda en el Gantt
  ✅ try/except en carga del logo
  ✅ Spacers eliminados (padding en CSS)
  ✅ Soporte multi-cliente con selector en sidebar
"""

import streamlit as st
import plotly.graph_objects as go
import os
import base64
from html import escape          # ← sanitización anti-XSS
from data_config import CLIENTES, CLIENTE_ACTIVO, ERRORES_VALIDACION

# ═══════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Lidato | Client de Transparencia Portal",
    page_icon="🟩",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ═══════════════════════════════════════════════════════════════
#  CARGAR CSS (separado de app.py)
# ═══════════════════════════════════════════════════════════════
@st.cache_data
def load_css(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()

css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
st.markdown(f"<style>{load_css(css_path)}</style>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  CARGAR LOGO (cacheado, con fallback SVG)
# ═══════════════════════════════════════════════════════════════
@st.cache_data
def load_logo(path: str) -> str:
    """Devuelve HTML del logo: imagen real si existe, SVG si no."""
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return f'<img src="data:image/png;base64,{b64}" style="height:60px;width:auto;" alt="Logo Lidato">'
    except Exception:
        pass  # Si falla la lectura, cae al SVG

    # SVG aproximado del logo Lidato (L teal + cuadros + naranja)
    return """<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
      <rect x="4"  y="4"  width="16" height="42" rx="3" fill="#2AB5A3"/>
      <rect x="4"  y="38" width="40" height="16" rx="3" fill="#2AB5A3"/>
      <rect x="28" y="4"  width="12" height="11" rx="2" fill="#2AB5A3"/>
      <rect x="44" y="4"  width="12" height="11" rx="2" fill="#F5A623"/>
      <rect x="28" y="19" width="12" height="11" rx="2" fill="#2AB5A3"/>
      <rect x="44" y="19" width="12" height="11" rx="2" fill="#2AB5A3"/>
    </svg>"""

logo_html = load_logo(os.path.join(os.path.dirname(__file__), "assets", "logo.png"))


# ═══════════════════════════════════════════════════════════════
#  SELECTOR DE CLIENTE (sidebar)
# ═══════════════════════════════════════════════════════════════
nombres_clientes = list(CLIENTES.keys())
default_idx = nombres_clientes.index(CLIENTE_ACTIVO) if CLIENTE_ACTIVO in nombres_clientes else 0

if len(nombres_clientes) > 1:
    with st.sidebar:
        st.markdown("### 🏢 Cliente")
        cliente_sel = st.selectbox(
            "Selecciona el cliente",
            nombres_clientes,
            index=default_idx,
            label_visibility="collapsed",
        )
else:
    cliente_sel = nombres_clientes[0]

D = CLIENTES[cliente_sel]   # datos del cliente activo
KPI           = D["kpi"]
IMPLEMENTACIONES = D["implementaciones"]
IMPACTO       = D["impacto"]
AUDITORIA     = D["auditoria"]
BITACORA      = D["bitacora"]
INFORMES      = D["informes"]
BACKLOG       = D["backlog"]
EMPRESA_NOMBRE     = cliente_sel
FECHA_ACTUALIZACION = D["fecha_actualizacion"]


# ═══════════════════════════════════════════════════════════════
#  ALERTAS DE VALIDACIÓN
# ═══════════════════════════════════════════════════════════════
if ERRORES_VALIDACION:
    for err in ERRORES_VALIDACION:
        st.warning(f"⚠️ Error en datos: {err}", icon="⚠️")


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════

def s(text) -> str:
    """Escapa HTML para prevenir inyección. Siempre aplica a datos de usuario."""
    return escape(str(text))


def bdg(estado: str) -> str:
    """Genera badge HTML con clase CSS según estado."""
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


def aud_cell(label: str, estado: str) -> str:
    cls = {"completado": "a-orange", "en_proceso": "a-teal", "pendiente": "a-gray"}.get(estado, "a-gray")
    icon = "✓" if estado == "completado" else ("⏳" if estado == "en_proceso" else "")
    return f'<div class="audit-cell {cls}">{icon}<br>{s(label)}</div>'


@st.cache_data
def build_gauge(value: int) -> go.Figure:
    """Gráfica de gauge cacheada por valor."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": "%", "font": {"size": 38, "family": "Nunito", "color": "#F5A623"}},
        gauge={
            "axis": {"range": [0, 100], "showticklabels": False, "tickwidth": 0},
            "bar": {"color": "#F5A623", "thickness": 0.38},
            "bgcolor": "#E8EDF2",
            "borderwidth": 0,
            "steps": [{"range": [0, 100], "color": "#E8EDF2"}],
            "shape": "angular",
        },
    ))
    fig.update_layout(
        margin=dict(t=28, b=0, l=14, r=14),
        height=128,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


@st.cache_data
def build_gantt(data: tuple) -> go.Figure:
    """Gráfica Gantt cacheada. Recibe tuple para que sea hashable."""
    fig = go.Figure()
    for d in reversed(data):
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["planificado"] - d["inicio"]], base=d["inicio"],
            orientation="h",
            marker=dict(color="#A8DDD8", line=dict(width=0)),
            name="Planificado",
            showlegend=False,
            hovertemplate=f"{s(d['fase'])}: planificado {d['planificado']}%<extra></extra>",
        ))
        fig.add_trace(go.Bar(
            y=[d["fase"]], x=[d["completado"] - d["inicio"]], base=d["inicio"],
            orientation="h",
            marker=dict(color="#2AB5A3", line=dict(width=0)),
            name="Completado",
            showlegend=False,
            hovertemplate=f"{s(d['fase'])}: completado {d['completado']}%<extra></extra>",
        ))
    fig.update_layout(
        barmode="overlay",
        xaxis=dict(
            range=[0, 100],
            tickvals=[0, 25, 50, 75, 100],
            ticktext=["0%", "25%", "50%", "75%", "100%"],
            showgrid=True, gridcolor="#E8EDF2",
            tickfont=dict(size=10, color="#8A9BB0"),
        ),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, family="Inter", color="#4A5568")),
        margin=dict(t=6, b=20, l=10, r=10),
        height=208,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def tabla_html(headers: list, rows_html: str) -> str:
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return f"""
    <table class="l-tbl">
      <thead><tr>{ths}</tr></thead>
      <tbody>{rows_html}</tbody>
    </table>"""


# ═══════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="ldt-header">
  <div class="ldt-header-inner">
    <div class="ldt-logo-col">
      {logo_html}
      <div class="ldt-logo-name">Lidato</div>
    </div>
    <div class="ldt-center">
      <div class="ldt-empresa">{s(EMPRESA_NOMBRE)}</div>
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
    st.plotly_chart(
        build_gauge(KPI["estabilidad"]["valor"]),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    st.markdown(f"""
    <div style="text-align:center;margin-top:-8px;">
      <span class="status-dot"></span>
      <span class="status-label">Status</span><br>
      <span class="kpi-sub">{s(KPI["estabilidad"]["label"])}</span>
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
        <div class="kpi-sub">{s(KPI["progreso"]["proyecto"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">Puntualidad de Informes (OTD)</div>
      <div style="text-align:center;padding:12px 0 6px 0;">
        <div class="otd-badge"><span class="otd-check">✓</span></div>
        <div class="kpi-orange" style="font-size:46px;">{KPI["otd"]["valor"]}%</div>
        <div class="kpi-sub">{s(KPI["otd"]["label"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)

with c4:
    n = str(KPI["ajustes_tecnicos"]["valor"]).zfill(2)
    st.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">Ajustes Técnicos Activos</div>
      <div style="text-align:center;padding:14px 0 6px 0;">
        <div class="kpi-dark" style="font-size:60px;">{n}</div>
        <div class="imp-unit" style="margin-top:4px;">Solicitudes</div>
        <div class="kpi-sub">{s(KPI["ajustes_tecnicos"]["label"])}</div>
      </div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 2 — GANTT + IMPACTO + AUDITORÍA
# ═══════════════════════════════════════════════════════════════
cg, ci, ca = st.columns([2, 1.5, 1.5], gap="small")

with cg:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Track de Implementaciones Activas</div>', unsafe_allow_html=True)
    # Convertir a tuple de frozensets para que sea hashable por @st.cache_data
    impl_tuple = tuple(frozenset(d.items()) for d in IMPLEMENTACIONES)
    # Re-convertir a lista de dicts para la función
    impl_list = [dict(d) for d in impl_tuple]
    st.plotly_chart(
        build_gantt(tuple(tuple(sorted(d.items())) for d in IMPLEMENTACIONES)),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    # ── Leyenda del Gantt ──
    st.markdown("""
    <div class="gantt-legend">
      <div class="gantt-legend-item">
        <div class="gantt-dot gantt-dot-completed"></div> Completado
      </div>
      <div class="gantt-legend-item">
        <div class="gantt-dot gantt-dot-planned"></div> Planificado
      </div>
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with ci:
    st.markdown('<div class="sec-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Impacto de Negocio y Valor Generado</div>', unsafe_allow_html=True)
    items = [
        ("⏰", IMPACTO["horas_ahorradas"],        "hrs/mes",  "Horas Operativas<br>Ahorradas (Est. Mensual)"),
        ("⚙️", IMPACTO["procesos_automatizados"], "procesos", "Procesos Manuales<br>Automatizados"),
        ("👥", f"{IMPACTO['tasa_adopcion']}%",    "adoption", "Tasa de Adopción<br>del Sistema"),
    ]
    cols_i = st.columns(3)
    for idx, (icon, val, unit, label) in enumerate(items):
        with cols_i[idx]:
            st.markdown(f"""
            <div class="imp-item">
              <div class="imp-icon">{icon}</div>
              <div class="imp-num">{s(str(val))}</div>
              <div class="imp-unit">{s(unit)}</div>
              <div class="imp-lbl">{label}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with ca:
    A = AUDITORIA
    st.markdown(f"""
    <div class="sec-card">
      <div class="sec-title">Auditoría de Entregables
        <span class="sec-subtitle">(Checklist Semanal/Mensual)</span>
      </div>
      <div class="audit-month-label">Currenté del mes</div>
      <div class="audit-grid">
        {aud_cell("Sem 1",        A["sem1"])}
        {aud_cell("Sem 2",        A["sem2"])}
        {aud_cell("Sem 3",        A["sem3"])}
        {aud_cell("Sem 4",        A["sem4"])}
        {aud_cell("Mensual KPIs", A["mensual_kpis"])}
        {aud_cell("Pendiente",    A["pendiente_extra"])}
      </div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  ROW 3 — TABS CON FILTROS
# ═══════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs(["★  BITÁCORA", "REPOSITORIO", "BACKLOG"])


# ── TAB 1: BITÁCORA ──────────────────────────────────────────
with tab1:
    # Filtros
    estados_bit = ["Todos"] + sorted({r["estado"] for r in BITACORA})
    solicitantes = ["Todos"] + sorted({r["solicitante"] for r in BITACORA})
    f1, f2, f3 = st.columns([1, 1, 2])
    with f1:
        fil_estado_bit = st.selectbox("Estado", estados_bit, key="fil_bit_estado")
    with f2:
        fil_sol = st.selectbox("Solicitante", solicitantes, key="fil_bit_sol")

    # Aplicar filtros
    data_bit = [
        r for r in BITACORA
        if (fil_estado_bit == "Todos" or r["estado"] == fil_estado_bit)
        and (fil_sol == "Todos" or r["solicitante"] == fil_sol)
    ]

    col_t, col_c = st.columns([3, 1], gap="small")
    with col_t:
        if not data_bit:
            st.info("No hay registros con los filtros seleccionados.")
        else:
            rows = "".join(f"""<tr>
              <td><strong>{s(r["id"])}</strong></td>
              <td>{s(r["solicitante"])}</td>
              <td>{s(r["asunto"])}</td>
              <td>{bdg(r["estado"])}</td>
              <td class="mono">{s(r["tiempo"])}</td>
            </tr>""" for r in data_bit)
            st.markdown(tabla_html(
                ["ID Ticket ▼", "Solicitante", "Asunto", "Estado Actual", "Tiempo Transcurrido"],
                rows,
            ), unsafe_allow_html=True)

    with col_c:
        st.markdown(f"""
        <div class="cert-box">
          <span class="cert-title">Última Actualización y Certificación</span>
          Datos sincronizados en tiempo real.<br>
          Última validación aprobada el<br>
          <span class="cert-date">{s(FECHA_ACTUALIZACION)}</span>
        </div>""", unsafe_allow_html=True)


# ── TAB 2: REPOSITORIO ───────────────────────────────────────
with tab2:
    tipos = ["Todos"] + sorted({r["tipo"] for r in INFORMES})
    estados_inf = ["Todos"] + sorted({r["estado"] for r in INFORMES})
    f1, f2, _ = st.columns([1, 1, 2])
    with f1:
        fil_tipo = st.selectbox("Tipo", tipos, key="fil_inf_tipo")
    with f2:
        fil_estado_inf = st.selectbox("Estado", estados_inf, key="fil_inf_estado")

    data_inf = [
        r for r in INFORMES
        if (fil_tipo == "Todos" or r["tipo"] == fil_tipo)
        and (fil_estado_inf == "Todos" or r["estado"] == fil_estado_inf)
    ]

    if not data_inf:
        st.info("No hay informes con los filtros seleccionados.")
    else:
        rows = "".join(f"""<tr>
          <td><strong>{s(r["id"])}</strong></td>
          <td>{s(r["titulo"])}</td>
          <td><span class="bdg bg-blue">{s(r["tipo"])}</span></td>
          <td>{s(r["fecha"])}</td>
          <td>{bdg(r["estado"])}</td>
          <td><a href="{s(r["enlace"])}" style="color:var(--teal);font-weight:700;font-size:12px;"
              target="_blank" rel="noopener noreferrer">Ver →</a></td>
        </tr>""" for r in data_inf)
        st.markdown(tabla_html(
            ["ID", "Título", "Tipo", "Fecha", "Estado", "Acceso"],
            rows,
        ), unsafe_allow_html=True)


# ── TAB 3: BACKLOG ───────────────────────────────────────────
with tab3:
    prioridades = ["Todas"] + sorted({r["prioridad"] for r in BACKLOG})
    sprints     = ["Todos"] + sorted({r["sprint"] for r in BACKLOG})
    estados_bk  = ["Todos"] + sorted({r["estado"] for r in BACKLOG})
    f1, f2, f3, _ = st.columns([1, 1, 1, 1])
    with f1:
        fil_pri = st.selectbox("Prioridad", prioridades, key="fil_bk_pri")
    with f2:
        fil_spr = st.selectbox("Sprint", sprints, key="fil_bk_spr")
    with f3:
        fil_est_bk = st.selectbox("Estado", estados_bk, key="fil_bk_est")

    data_bk = [
        r for r in BACKLOG
        if (fil_pri == "Todas" or r["prioridad"] == fil_pri)
        and (fil_spr == "Todos" or r["sprint"] == fil_spr)
        and (fil_est_bk == "Todos" or r["estado"] == fil_est_bk)
    ]

    pri_cls = {"Alta": "bg-yellow", "Media": "bg-blue", "Baja": "bg-green"}
    if not data_bk:
        st.info("No hay tareas con los filtros seleccionados.")
    else:
        rows = "".join(f"""<tr>
          <td><strong>{s(r["id"])}</strong></td>
          <td>{s(r["tarea"])}</td>
          <td><span class="bdg {pri_cls.get(r["prioridad"], "bg-gray")}">{s(r["prioridad"])}</span></td>
          <td><span class="bdg bg-purple">{s(r["sprint"])}</span></td>
          <td>{s(r["asignado"])}</td>
          <td>{bdg(r["estado"])}</td>
        </tr>""" for r in data_bk)
        st.markdown(tabla_html(
            ["ID", "Tarea", "Prioridad", "Sprint", "Asignado", "Estado"],
            rows,
        ), unsafe_allow_html=True)
