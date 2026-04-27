# =============================================================
#  LIDATO — CONFIGURACIÓN DE DATOS DEL DASHBOARD
#  Edita SOLO este archivo cada vez que actualices datos.
#  El dashboard carga todo desde aquí automáticamente.
# =============================================================

# ── MULTI-CLIENTE ─────────────────────────────────────────────
# Para agregar un cliente nuevo, duplica este bloque y cambia
# el nombre en CLIENTES. El selector aparece en la barra lateral.
# El cliente activo por defecto es el primero de la lista.
CLIENTE_ACTIVO = "Empresa Cliente A"   # ← cambia esto para el default

CLIENTES = {

    # ════════════════════════════════
    "Empresa Cliente A": {

        # ── FECHA MANUAL (controlas tú cuándo se muestra "actualizado") ──
        # Formato: "DD/MM/YYYY"
        "fecha_actualizacion": "26/04/2026",

        # ── KPIs PRINCIPALES ─────────────────────────────────────────────
        "kpi": {
            "estabilidad": {
                "valor": 99,          # int 0-100
                "label": "% de tiempo sin errores de flujo",
            },
            "progreso": {
                "valor": 65,          # int 0-100
                "proyecto": "Integración de IA y Automatizaciones",
            },
            "otd": {
                "valor": 100,         # int 0-100
                "label": "A Tiempo y Validados",
            },
            "ajustes_tecnicos": {
                "valor": 5,           # int >= 0
                "label": "Solicitudes de Ajuste / Bloqueos",
            },
        },

        # ── TRACK DE IMPLEMENTACIONES ─────────────────────────────────────
        # inicio, completado, planificado: valores 0-100 (% en el eje X)
        "implementaciones": [
            {"fase": "Levantamiento",      "inicio": 0,  "completado": 50, "planificado": 60},
            {"fase": "Configuración",      "inicio": 20, "completado": 55, "planificado": 70},
            {"fase": "Capacitación",       "inicio": 45, "completado": 55, "planificado": 65},
            {"fase": "Pruebas de Sistema", "inicio": 50, "completado": 70, "planificado": 80},
            {"fase": "Documentación",      "inicio": 60, "completado": 85, "planificado": 90},
            {"fase": "Entrega Final",      "inicio": 70, "completado": 90, "planificado": 100},
        ],

        # ── IMPACTO DE NEGOCIO ────────────────────────────────────────────
        "impacto": {
            "horas_ahorradas":       45,   # int
            "procesos_automatizados": 12,  # int
            "tasa_adopcion":         92,   # int 0-100
        },

        # ── AUDITORÍA SEMANAL/MENSUAL ─────────────────────────────────────
        # Valores válidos: "completado" | "en_proceso" | "pendiente"
        "auditoria": {
            "sem1":          "completado",
            "sem2":          "completado",
            "sem3":          "completado",
            "sem4":          "completado",
            "mensual_kpis":  "completado",
            "pendiente_extra": "pendiente",
        },

        # ── BITÁCORA DE AJUSTES ───────────────────────────────────────────
        # estado válido: "Aprobado" | "En Proceso" | "Pendiente"
        "bitacora": [
            {"id": "1001", "solicitante": "Marta Desk", "asunto": "Ajuste Webhook Albato-Zoho CRM",    "estado": "Aprobado",  "tiempo": "23.5s"},
            {"id": "1002", "solicitante": "Marta Desk", "asunto": "Corrección Flujo Power BI Ventas", "estado": "En Proceso","tiempo": "23.5s"},
            {"id": "1003", "solicitante": "Marta Desk", "asunto": "Integración IA (Revisión)",        "estado": "Pendiente", "tiempo": "18.5s"},
            {"id": "1004", "solicitante": "Carlos R.",  "asunto": "Configuración API HubSpot",        "estado": "Aprobado",  "tiempo": "12.0s"},
        ],

        # ── REPOSITORIO DE INFORMES ───────────────────────────────────────
        # estado válido: "Publicado" | "Pendiente"
        # enlace: URL real a PDF en Drive, Notion, etc. (o "#" si no aplica)
        "informes": [
            {"id": "INF-001", "titulo": "Informe Mensual Abril 2026", "tipo": "Mensual",  "fecha": "01/04/2026", "estado": "Publicado", "enlace": "#"},
            {"id": "INF-002", "titulo": "Reporte KPIs Semana 1",      "tipo": "Semanal",  "fecha": "07/04/2026", "estado": "Publicado", "enlace": "#"},
            {"id": "INF-003", "titulo": "Reporte KPIs Semana 2",      "tipo": "Semanal",  "fecha": "14/04/2026", "estado": "Publicado", "enlace": "#"},
            {"id": "INF-004", "titulo": "Reporte KPIs Semana 3",      "tipo": "Semanal",  "fecha": "21/04/2026", "estado": "Publicado", "enlace": "#"},
            {"id": "INF-005", "titulo": "Reporte KPIs Semana 4",      "tipo": "Semanal",  "fecha": "28/04/2026", "estado": "Pendiente", "enlace": "#"},
        ],

        # ── BACKLOG DE IMPLEMENTACIÓN ─────────────────────────────────────
        # prioridad válida: "Alta" | "Media" | "Baja"
        # estado válido:    "Aprobado" | "En Proceso" | "Pendiente"
        "backlog": [
            {"id": "BK-001", "tarea": "Integrar módulo de reportes automáticos",    "prioridad": "Alta",  "sprint": "Sprint 3", "asignado": "Equipo Técnico", "estado": "En Proceso"},
            {"id": "BK-002", "tarea": "Configurar alertas de Slack para errores",   "prioridad": "Media", "sprint": "Sprint 3", "asignado": "Marta Desk",     "estado": "Pendiente"},
            {"id": "BK-003", "tarea": "Revisión y ajuste de dashboards Power BI",   "prioridad": "Alta",  "sprint": "Sprint 4", "asignado": "Carlos R.",      "estado": "Pendiente"},
            {"id": "BK-004", "tarea": "Documentación de procesos automatizados",    "prioridad": "Baja",  "sprint": "Sprint 4", "asignado": "Equipo Técnico", "estado": "Pendiente"},
        ],
    },

    # ════════════════════════════════
    # Para agregar Cliente B, copia el bloque anterior aquí:
    # "Empresa Cliente B": { ... },

}


# ═══════════════════════════════════════════════════════════════
#  VALIDACIÓN AUTOMÁTICA
#  No edites esta sección. Se ejecuta al importar el módulo
#  y avisa con mensajes claros si hay errores en los datos.
# ═══════════════════════════════════════════════════════════════

ESTADOS_VALIDOS_BITACORA  = {"Aprobado", "En Proceso", "Pendiente"}
ESTADOS_VALIDOS_AUDITORIA = {"completado", "en_proceso", "pendiente"}
ESTADOS_VALIDOS_INFORMES  = {"Publicado", "Pendiente"}
PRIORIDADES_VALIDAS       = {"Alta", "Media", "Baja"}


def _validar_cliente(nombre: str, datos: dict):
    kpi = datos.get("kpi", {})
    imp = datos.get("impacto", {})
    aud = datos.get("auditoria", {})
    ctx = f"[Cliente: {nombre}]"

    # KPI numéricos entre 0 y 100
    for campo in ("estabilidad", "progreso", "otd"):
        v = kpi.get(campo, {}).get("valor")
        assert isinstance(v, (int, float)),        f"{ctx} kpi.{campo}.valor debe ser número, recibido: {v!r}"
        assert 0 <= v <= 100,                      f"{ctx} kpi.{campo}.valor debe estar entre 0 y 100, recibido: {v}"

    # Ajustes técnicos >= 0
    at = kpi.get("ajustes_tecnicos", {}).get("valor")
    assert isinstance(at, int) and at >= 0,        f"{ctx} kpi.ajustes_tecnicos.valor debe ser entero >= 0"

    # Impacto
    assert isinstance(imp.get("horas_ahorradas"), (int, float)),        f"{ctx} impacto.horas_ahorradas debe ser número"
    assert isinstance(imp.get("procesos_automatizados"), int),           f"{ctx} impacto.procesos_automatizados debe ser entero"
    ta = imp.get("tasa_adopcion")
    assert isinstance(ta, (int, float)) and 0 <= ta <= 100,             f"{ctx} impacto.tasa_adopcion debe estar entre 0 y 100"

    # Auditoría
    for clave, val in aud.items():
        assert val in ESTADOS_VALIDOS_AUDITORIA, \
            f"{ctx} auditoria.{clave}='{val}' inválido. Usa: {ESTADOS_VALIDOS_AUDITORIA}"

    # Implementaciones
    for row in datos.get("implementaciones", []):
        for campo in ("inicio", "completado", "planificado"):
            assert isinstance(row[campo], (int, float)) and 0 <= row[campo] <= 100, \
                f"{ctx} implementaciones[{row['fase']}].{campo} debe ser 0-100"

    # Bitácora
    for row in datos.get("bitacora", []):
        assert row["estado"] in ESTADOS_VALIDOS_BITACORA, \
            f"{ctx} bitacora[{row['id']}].estado='{row['estado']}' inválido. Usa: {ESTADOS_VALIDOS_BITACORA}"

    # Informes
    for row in datos.get("informes", []):
        assert row["estado"] in ESTADOS_VALIDOS_INFORMES, \
            f"{ctx} informes[{row['id']}].estado='{row['estado']}' inválido. Usa: {ESTADOS_VALIDOS_INFORMES}"

    # Backlog
    for row in datos.get("backlog", []):
        assert row["prioridad"] in PRIORIDADES_VALIDAS, \
            f"{ctx} backlog[{row['id']}].prioridad='{row['prioridad']}' inválido. Usa: {PRIORIDADES_VALIDAS}"
        assert row["estado"] in ESTADOS_VALIDOS_BITACORA, \
            f"{ctx} backlog[{row['id']}].estado='{row['estado']}' inválido. Usa: {ESTADOS_VALIDOS_BITACORA}"


# Ejecutar validación en el momento de importar
_errores = []
for _nombre, _datos in CLIENTES.items():
    try:
        _validar_cliente(_nombre, _datos)
    except AssertionError as e:
        _errores.append(str(e))

ERRORES_VALIDACION = _errores  # app.py los muestra como warnings
