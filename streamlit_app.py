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
    
    # 1. Diccionario con tus 4 archivos
    opciones_fractales = {
        "fractales_regulares.py": "Fractales en polígonos regulares (math)",
        "fractales_regulares_np.py": "Fractales en polígonos regulares (numpy)",
        "fractales_triangulos.py": "Fractales en triángulos de cualquier tipo",
        "fractales_cuadrado.py": "Fractales en cuadrados"
    }
    
    archivo_seleccionado = st.selectbox(
        "Elegí qué fractal querés generar:", 
        options=list(opciones_fractales.keys()),
        format_func=lambda x: opciones_fractales[x] 
    )
    
    col_controles, col_grafico = st.columns([1, 2]) 
    
    with col_controles:
        st.write("### Parámetros")
        iteraciones = st.slider("Iteraciones:", min_value=1000, max_value=50000, value=20000, step=1000)
        
        # --- LÓGICA CONDICIONAL SEGÚN EL ARCHIVO ELEGIDO ---
        
        # CASO 1: Polígonos regulares (math o numpy)
        if "regulares" in archivo_seleccionado:
            st.write("### Configuración del Polígono")
            lados = st.number_input("Cantidad de lados:", min_value=3, max_value=20, value=3, step=1)
            
            # Calculamos los vértices automáticamente
            import numpy as np
            angulos = np.linspace(0, 2 * np.pi, lados, endpoint=False)
            vertx = 2 * np.cos(angulos)
            verty = 2 * np.sin(angulos)
            
        # CASO 2: Triángulo de cualquier tipo (pide coordenadas)
        elif "triangulos" in archivo_seleccionado:
            st.write("### Vértices del Triángulo")
            c1, c2 = st.columns(2)
            with c1:
                v1x = st.number_input("X1", value=5.0, step=0.1, format="%.1f")
                v2x = st.number_input("X2", value=-5.0, step=0.1, format="%.1f")
                v3x = st.number_input("X3", value=0.0, step=0.1, format="%.1f")
            with c2:
                v1y = st.number_input("Y1", value=5.0, step=0.1, format="%.1f")
                v2y = st.number_input("Y2", value=5.0, step=0.1, format="%.1f")
                v3y = st.number_input("Y3", value=-5.0, step=0.1, format="%.1f")
            vertx = [v1x, v2x, v3x]
            verty = [v1y, v2y, v3y]
            lados = 3
            
        # CASO 3: Cuadrado (no pide nada más, solo usa el cuadrado por defecto)
        else:
            st.write("### Cuadrado Predefinido")
            st.write("El cuadrado ya está configurado con sus 4 vértices.")
            vertx = [1.0, 1.0, -1.0, -1.0]
            verty = [1.0, -1.0, -1.0, 1.0]
            lados = 4

        generar = st.button("▶️ Generar Fractal")

    with col_grafico:
        if generar:
            try:
                plt.clf() 
                fx, fy = [], []
                p0x, p0y = 0.0, 0.0
         ##################################################
                ultimo=random.radint(0,3)
        ###################################################
                 for _ in range(iteraciones):
                   elegido=random.radint(0,3)
                    while elegido==ultimo
                        elegido=random.randint(0,3)
                    ultimo=elegido
                    #v = random.randint(0, int(lados) - 1)
                    x = (p0x + vertx[ultimo]) / 2
                    y = (p0y + verty[ultimo]) / 2
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
