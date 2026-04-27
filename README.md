# 🔷 LIDATO — Client de Transparencia Portal v2

## 📁 Estructura del proyecto

```
lidato_dashboard/
├── app.py                ← Aplicación principal (no tocar)
├── data_config.py        ← TODOS LOS DATOS VAN AQUÍ
├── requirements.txt      ← Dependencias
└── assets/
    ├── styles.css        ← Todos los estilos (no tocar)
    ├── logo.png          ← 👈 SUBE TU LOGO AQUÍ
    └── README.md
```

---

## ✏️ Actualizar datos mensualmente

**Solo edita `data_config.py`**. Cambia los valores dentro del bloque de tu cliente:

```python
"fecha_actualizacion": "01/05/2026",       # ← fecha manual, tú la controlas
"kpi": {
    "progreso": { "valor": 80, ... },      # ← nuevo % de avance
    ...
},
"impacto": {
    "horas_ahorradas": 52,                 # ← nuevas horas
    ...
},
"auditoria": {
    "sem1": "completado",                  # ← marcar semanas
    "sem4": "en_proceso",
    ...
},
```

Si pones un valor inválido (texto en lugar de número, estado incorrecto, etc.) el dashboard muestra un **aviso amarillo** explicando exactamente qué hay que corregir.

---

## 🏢 Agregar un segundo cliente

En `data_config.py`, duplica el bloque dentro de `CLIENTES`:

```python
CLIENTES = {
    "Empresa Cliente A": { ... },   # ya existe
    "Empresa Cliente B": { ... },   # ← copia y pega, cambia los datos
}
```

El selector de cliente aparece automáticamente en la barra lateral.

---

## 🖼️ Subir tu logo real

1. En GitHub → carpeta `assets/` → **"Add file" → "Upload files"**
2. Sube el archivo con el nombre exacto: **`logo.png`**
3. Haz commit. Streamlit se actualiza solo.

Tamaño recomendado: 200×200 px, PNG con fondo transparente.

---

## 🚀 Deploy en Streamlit Cloud

```bash
# 1. Sube a GitHub
git init && git add . && git commit -m "Lidato Dashboard v2"
git remote add origin https://github.com/TU_USUARIO/lidato-dashboard.git
git push -u origin main

# 2. share.streamlit.io → Create app
#    Repository: TU_USUARIO/lidato-dashboard
#    Branch: main
#    Main file path: app.py
#    → Deploy ✅
```

---

## 💻 Correr localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎨 Cambiar colores globalmente

Edita las variables al inicio de `assets/styles.css`:

```css
:root {
  --teal:    #2AB5A3;   /* color principal */
  --orange:  #F5A623;   /* color de acento */
  --bg:      #EEF1F5;   /* fondo general */
}
```
Cambiar `--teal` y `--orange` actualiza toda la paleta del dashboard.
