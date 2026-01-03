import streamlit as st
import os

# ----------------------------------------
# ESTILO
# ----------------------------------------
st.markdown("""
<style>

:root {
    --primaryColor: #C75B12;              /* naranja oscuro */
    --backgroundColor: #FAF7F0;           /* blanco hueso */
    --secondaryBackgroundColor: #A3A36F;  /* verde oliva */
    --textColor: #5A0010;                 /* bordo oscuro */
}

/* Fondo general */
body, .stApp {
    background-color: var(--backgroundColor);
    color: var(--textColor);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: var(--secondaryBackgroundColor);
}

/* Botones */
.stButton>button {
    background-color: var(--primaryColor);
    color: white;
    border-radius: 6px;
}

/* Selectbox */
.stSelectbox>div>div {
    color: var(--textColor);
}

/* Fuente: usar una estándar del sistema */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------------
# Función para cargar secciones del .md
# ----------------------------------------
def cargar_seccion(titulo):
    try:
        with open("documentacion.md", "r", encoding="utf-8") as f:
            contenido = f.read()

        secciones = contenido.split("## ")
        for sec in secciones:
            if sec.strip().startswith(titulo):
                return "## " + sec
        return "Sección no encontrada."
    except FileNotFoundError:
        return "El archivo documentacion.md no fue encontrado."


# ----------------------------------------
# Mostrar imagen 
# ----------------------------------------
def mostrar_imagen(ruta, titulo=None):
    if titulo:
        st.subheader(titulo)

    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True)
    else:
        st.warning(f"No se encontró la imagen: {ruta}")


# ----------------------------------------
# Interfaz principal
# ----------------------------------------
st.title("📊 Tienda Aurelion – Documentación Interactiva")

# HEADER VISUAL
st.markdown("""
<div style='padding: 15px; background-color:#f0f2f6; border-radius:10px; margin-bottom:20px;'>
<h3 style='color:#333; margin:0;'>📊 Análisis interactivo – Tienda Aurelion</h3>
<p style='color:#555; margin:0;'>Explorá el análisis, visualizaciones e insights del proyecto.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Elegí una sección:",
    [
        "Tema, problema y solución",
        "Información del dataset",
        "EDA",
        "Visualizaciones",
        "Estadísticas",
        "Insights",
        "Machine Learning",
        "Dashboard Power BI",
        "Sugerencias de Copilot"
    ]
)

# ----------------------------------------
# Mostrar contenido según opción
# ----------------------------------------

if opcion == "Tema, problema y solución":
    st.markdown(cargar_seccion("Tema, problema y solución"))

elif opcion == "Información del dataset":
    st.markdown(cargar_seccion("Fuente, definición, estructura, tipos y escala"))

elif opcion == "Estadísticas":
    st.markdown(cargar_seccion("Estadística"))

elif opcion == "Sugerencias de Copilot":
    st.markdown(cargar_seccion("Sugerencias de Copilot"))

# ----------------------------------------
# EDA
# ----------------------------------------
elif opcion == "EDA":
    st.header("Exploratory Data Analysis")
    st.divider()

    mostrar_imagen("graficos/corr_matrix.png", "Matriz de correlación")
    st.divider()

    mostrar_imagen("graficos/relacion_cant_precio_importe.png", "Relación cantidad – precio – importe")
    st.divider()

    mostrar_imagen("graficos/distribucion.png", "Distribución de variables")

# ----------------------------------------
# Visualizaciones
# ----------------------------------------
elif opcion == "Visualizaciones":
    st.header("Visualizaciones de Negocio")
    st.divider()

    mostrar_imagen("graficos/dist_temporal.png", "Distribución temporal de ventas")
    st.divider()

    mostrar_imagen("graficos/importe_promedio.png", "Importe promedio por categoría")
    st.divider()

    mostrar_imagen("graficos/dist_mediosP.png", "Distribución de medios de pago")
    st.divider()

    mostrar_imagen("graficos/dist_mediosP_boxplot.png", "Boxplot de medios de pago")
    st.divider()

    mostrar_imagen("graficos/ventas_ciudad.png", "Ventas por ciudad")

# ----------------------------------------
# Insights
# ----------------------------------------
elif opcion == "Insights":
    st.header("Insights del análisis")
    st.markdown(cargar_seccion("Insights"))
    st.divider()

    mostrar_imagen("graficos/ventas_mes.png", "Ventas por mes")
    st.divider()

    mostrar_imagen("graficos/dist_mediosP.png", "Distribución de medios de pago")
    st.divider()

    mostrar_imagen("graficos/ventas_ciudad.png", "Ventas por ciudad")

# ----------------------------------------
# Machine Learning
# ----------------------------------------
elif opcion == "Machine Learning":
    st.header("Modelos de Machine Learning")
    st.markdown(cargar_seccion("Aplicación de modelos de Machine Learning"))
    st.divider()

    mostrar_imagen("graficos/regresion_scatter.png", "Regresión Lineal – Valores reales vs predichos")
    st.divider()

    mostrar_imagen("graficos/regresion_coef.png", "Regresión Lineal – Coeficientes del modelo")
    st.divider()

    mostrar_imagen("graficos/RF_matriz.png", "Random Forest – Matriz de confusión")
    st.divider()

    mostrar_imagen("graficos/RF_featureImportance.png", "Random Forest – Importancia de variables")

# ----------------------------------------
# Dashboard Power BI
# ----------------------------------------
elif opcion == "Dashboard Power BI":
    st.header("Dashboard Power BI – Tienda Aurelion")
    st.divider()

    for i in range(1, 6):
        mostrar_imagen(f"graficos/pb{i}.png", f"Página {i}")
        st.divider()


# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Alumna: Lucía Páez Gayone<br>
Diciembre, 2025<br>
Programa Fundamentos en Inteligencia Artificial – IBM SkillsBuild & Guayerd
</p>
""", unsafe_allow_html=True)