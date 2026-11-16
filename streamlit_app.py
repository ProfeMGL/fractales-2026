import streamlit as st
import os
import matplotlib
matplotlib.use('Agg') # Evita que intente abrir ventanas
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Fractales 2026", page_icon="🌀")
st.title("Proyecto Fractales 2026 🌀")
st.write("Bienvenidos a la app del espacio EDI.")

# Creamos las 3 pestañas en el orden que pediste
tab_galeria, tab_ejecutar, tab_codigo = st.tabs(["🖼️ Galería", "🎨 Ejecutar", "💻 Ver Código"])

# --- PESTAÑA 1: GALERÍA (Izquierda) ---
with tab_galeria:
    st.header("Galería de Fractales")
    # Buscamos imágenes en la carpeta, ignorando el archivo temporal de resultados
    imagenes = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg')) and f != 'resultado.png']
    
    if imagenes:
        for img in imagenes:
            st.image(img, caption=img, use_container_width=True)
    else:
        st.info("Todavía no hay imágenes guardadas en el repositorio.")

# --- PESTAÑA 2: EJECUTAR (Centro) ---
with tab_ejecutar:
    st.header("Generador de Fractales")
    
    # Dividimos en dos columnas principales: controles (izquierda) y gráfico (derecha)
    col_controles, col_grafico = st.columns([1, 2]) 
    with col_controles:
        st.write("### Parámetros")
        # El slider con el valor de 20000
        iteraciones = st.slider("Iteraciones:", min_value=1000, max_value=50000, value=20000, step=1000)
        st.write("### Vértices del Triángulo")
        # Usamos dos columnas internas para los inputs (X e Y al costado)
        c1, c2 = st.columns(2)
        with c1:
            # Vértice 1: (5, 5)
            v1x = st.number_input("X1", value=5.0, step=0.1, format="%.1f")
            # Vértice 2: (-5, 5)
            v2x = st.number_input("X2", value=-5.0, step=0.1, format="%.1f")
            # Vértice 3: (0, 7)
            v3x = st.number_input("X3", value=0.0, step=0.1, format="%.1f")
        with c2:
            v1y = st.number_input("Y1", value=5.0, step=0.1, format="%.1f")
            v2y = st.number_input("Y2", value=5.0, step=0.1, format="%.1f")
            v3y = st.number_input("Y3", value=7.0, step=0.1, format="%.1f")
    
        # El botón al final de la columna de controles
        generar = st.button("▶️ Generar Fractal")

    with col_grafico:
        if generar:
            try:
                plt.clf() 
                vertx = [v1x, v2x, v3x]
                verty = [v1y, v2y, v3y]
                fx, fy = [], []
                p0x, p0y = 0.0, 0.0 # Punto inicial en el centro
                
                for _ in range(iteraciones):
                    v = random.randint(0, 2)
                    x = (p0x + vertx[v]) / 2
                    y = (p0y + verty[v]) / 2
                    fx.append(x)
                    fy.append(y)
                    p0x, p0y = x, y
                    
                plt.scatter(fx, fy, s=1, color="purple")
                plt.axis('equal')
                plt.axis('off')
                plt.tight_layout()
                plt.savefig("resultado.png")
                
                st.image("resultado.png", caption="Fractal Generado", use_column_width=True)
                st.success("¡Fractal generado!")
                
            except Exception as e:
                st.error("Hubo un error:")
                st.code(str(e))
        else:
            st.info("Ajustá los parámetros y hacé clic en Generar.")
# --- PESTAÑA 3: VER CÓDIGO (Derecha) ---
with tab_codigo:
    st.header("Código de los Fractales")
    
    # Usamos la misma lista de archivos de la pestaña anterior
    archivos_py = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']
    
    if not archivos_py:
        st.info("No se encontraron archivos de código.")
    else:
        for archivo in archivos_py:
            with st.expander(f"Ver código de {archivo}"):
                with open(archivo, "r", encoding="utf-8") as f:
                    codigo = f.read()
                st.code(codigo, language="python")
