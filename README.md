# 🔷 LIDATO — Client de Transparencia Portal

Dashboard interactivo de transparencia para clientes, replicable mensualmente.

## 📁 Estructura de archivos

```
lidato_dashboard/
├── app.py            ← Aplicación principal (no tocar)
├── data_config.py    ← DATOS DEL DASHBOARD (editar aquí cada mes)
├── requirements.txt  ← Dependencias
└── README.md
```

---

## ✏️ Cómo actualizar los datos mensualmente

**Solo edita `data_config.py`**. Los cambios se reflejan automáticamente.

### Cambios más comunes:

| Sección | Qué editar |
|---|---|
| `KPI["estabilidad"]["valor"]` | % tiempo sin errores |
| `KPI["progreso"]["valor"]` | % avance del proyecto |
| `KPI["otd"]["valor"]` | % puntualidad informes |
| `KPI["ajustes_tecnicos"]["valor"]` | Nro de solicitudes activas |
| `IMPACTO` | Horas ahorradas, procesos, adopción |
| `AUDITORIA` | Estado semanal (`"completado"`, `"pendiente"`, `"en_proceso"`) |
| `BITACORA` | Agregar/editar tickets |
| `INFORMES` | Agregar nuevos informes al repositorio |
| `BACKLOG` | Tareas del backlog de implementación |

---

## 🚀 Deploy en Streamlit Cloud (desde GitHub)

### Paso 1 — Subir a GitHub
```bash
git init
git add .
git commit -m "Lidato Dashboard v1"
git remote add origin https://github.com/TU_USUARIO/lidato-dashboard.git
git push -u origin main
```

### Paso 2 — Publicar en Streamlit Cloud
1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Conecta tu cuenta de GitHub
3. Selecciona el repositorio `lidato-dashboard`
4. **Main file path:** `app.py`
5. Clic en **Deploy** ✅

### Paso 3 — Actualizar datos cada mes
1. Edita `data_config.py` en GitHub (o localmente y haz `git push`)
2. Streamlit Cloud se actualiza automáticamente

---

## 💻 Correr localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎨 Paleta de colores
| Color | Uso |
|---|---|
| `#0D47A1` | Azul oscuro (headers, logo) |
| `#1565C0` | Azul medio (tabs, botones) |
| `#43A047` | Verde (completado, aprobado) |
| `#FFA000` | Amarillo (en proceso) |
| `#B0BEC5` | Gris (pendiente) |
