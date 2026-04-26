# =============================================================
#  LIDATO - CONFIGURACIÓN DE DATOS DEL DASHBOARD
#  Edita este archivo cada vez que necesites actualizar datos
#  mensuales, quincenales o semanales.
# =============================================================

from datetime import date

# ── INFORMACIÓN GENERAL ──────────────────────────────────────
EMPRESA_NOMBRE = "EMPRESA CLIENTE A"
FECHA_ACTUALIZACION = date.today().strftime("%d/%m/%Y")

# ── KPIs PRINCIPALES (tarjetas superiores) ───────────────────
KPI = {
    "estabilidad": {
        "valor": 99,          # % de tiempo sin errores de flujo
        "label": "% de tiempo sin errores de flujo",
    },
    "progreso": {
        "valor": 65,          # % de avance del proyecto actual
        "proyecto": "Integración de IA y Automatizaciones",
    },
    "otd": {
        "valor": 100,         # % puntualidad de informes
        "label": "A Tiempo y Validados",
    },
    "ajustes_tecnicos": {
        "valor": 5,           # número de solicitudes activas
        "label": "Solicitudes de Ajuste / Bloqueos",
    },
}

# ── TRACK DE IMPLEMENTACIONES (gráfico de barras Gantt) ──────
# Cada fila: [nombre, inicio%, fin_completado%, fin_planificado%]
IMPLEMENTACIONES = [
    {"fase": "Levantamiento",       "inicio": 0,  "completado": 50, "planificado": 60},
    {"fase": "Configuración",       "inicio": 20, "completado": 55, "planificado": 70},
    {"fase": "Capacitación",        "inicio": 45, "completado": 55, "planificado": 65},
    {"fase": "Pruebas de Sistema",  "inicio": 50, "completado": 70, "planificado": 80},
    {"fase": "Documentación",       "inicio": 60, "completado": 85, "planificado": 90},
    {"fase": "Entrega Final",       "inicio": 70, "completado": 90, "planificado": 100},
]

# ── IMPACTO DE NEGOCIO ────────────────────────────────────────
IMPACTO = {
    "horas_ahorradas": 45,         # hrs/mes
    "procesos_automatizados": 12,  # número de procesos
    "tasa_adopcion": 92,           # % adopción del sistema
}

# ── AUDITORÍA DE ENTREGABLES (checklist semanal/mensual) ──────
# Estado: "completado", "pendiente", "en_proceso"
AUDITORIA = {
    "sem1": "completado",
    "sem2": "completado",
    "sem3": "completado",
    "sem4": "completado",
    "mensual_kpis": "completado",
    "pendiente_extra": "pendiente",   # última celda (gris si no aplica)
}

# ── BITÁCORA DE AJUSTES ───────────────────────────────────────
BITACORA = [
    {
        "id": "1001",
        "solicitante": "Marta Desk",
        "asunto": "Ajuste Webhook Albato-Zoho CRM",
        "estado": "Aprobado",
        "tiempo": "23.5s",
    },
    {
        "id": "1002",
        "solicitante": "Marta Desk",
        "asunto": "Corrección Flujo Power BI Ventas",
        "estado": "En Proceso",
        "tiempo": "23.5s",
    },
    {
        "id": "1003",
        "solicitante": "Marta Desk",
        "asunto": "Integración IA (Revisión)",
        "estado": "Pendiente",
        "tiempo": "18.5s",
    },
    {
        "id": "1004",
        "solicitante": "Carlos R.",
        "asunto": "Configuración API HubSpot",
        "estado": "Aprobado",
        "tiempo": "12.0s",
    },
]

# ── REPOSITORIO DE INFORMES ───────────────────────────────────
INFORMES = [
    {
        "id": "INF-001",
        "titulo": "Informe Mensual Abril 2025",
        "tipo": "Mensual",
        "fecha": "01/04/2025",
        "estado": "Publicado",
        "enlace": "#",
    },
    {
        "id": "INF-002",
        "titulo": "Reporte KPIs Semana 1",
        "tipo": "Semanal",
        "fecha": "07/04/2025",
        "estado": "Publicado",
        "enlace": "#",
    },
    {
        "id": "INF-003",
        "titulo": "Reporte KPIs Semana 2",
        "tipo": "Semanal",
        "fecha": "14/04/2025",
        "estado": "Publicado",
        "enlace": "#",
    },
    {
        "id": "INF-004",
        "titulo": "Reporte KPIs Semana 3",
        "tipo": "Semanal",
        "fecha": "21/04/2025",
        "estado": "Publicado",
        "enlace": "#",
    },
    {
        "id": "INF-005",
        "titulo": "Reporte KPIs Semana 4",
        "tipo": "Semanal",
        "fecha": "28/04/2025",
        "estado": "Pendiente",
        "enlace": "#",
    },
]

# ── BACKLOG DE IMPLEMENTACIÓN ─────────────────────────────────
BACKLOG = [
    {
        "id": "BK-001",
        "tarea": "Integrar módulo de reportes automáticos",
        "prioridad": "Alta",
        "sprint": "Sprint 3",
        "asignado": "Equipo Técnico",
        "estado": "En Proceso",
    },
    {
        "id": "BK-002",
        "tarea": "Configurar alertas de Slack para errores",
        "prioridad": "Media",
        "sprint": "Sprint 3",
        "asignado": "Marta Desk",
        "estado": "Pendiente",
    },
    {
        "id": "BK-003",
        "tarea": "Revisión y ajuste de dashboards Power BI",
        "prioridad": "Alta",
        "sprint": "Sprint 4",
        "asignado": "Carlos R.",
        "estado": "Pendiente",
    },
    {
        "id": "BK-004",
        "tarea": "Documentación de procesos automatizados",
        "prioridad": "Baja",
        "sprint": "Sprint 4",
        "asignado": "Equipo Técnico",
        "estado": "Pendiente",
    },
]
