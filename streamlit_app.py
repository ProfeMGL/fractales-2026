import streamlit as st
import os
import matplotlib
matplotlib.use('Agg') # Evita que intente abrir ventanas
import matplotlib.pyplot as plt

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
# --- PESTAÑA 2: EJECUTAR (Centro) ---
with tab_ejecutar:
    st.header("Generador de Fractales")
    
    # 1. Controles interactivos (reemplazan al input de la consola)
    st.write("### Parámetros")
    iteraciones = st.slider("Cantidad de iteraciones:", min_value=1000, max_value=50000, value=10000, step=1000)
    
    st.write("### Vértices del Triángulo")
    col1, col2, col3 = st.columns(3)
    with col1:
        v1x = st.number_input("X1", value=0.0)
        v1y = st.number_input("Y1", value=2.0)
    with col2:
        v2x = st.number_input("X2", value=-1.73)
        v2y = st.number_input("Y2", value=-1.0)
    with col3:
        v3x = st.number_input("X3", value=1.73)
        v3y = st.number_input("Y3", value=-1.0)

    # 2. Botón para ejecutar el cálculo
    if st.button("▶️ Generar Fractal"):
        try:
            plt.clf() # Limpiamos gráficos anteriores
            # 3. Lógica del Juego del Caos (adaptada de tu código)
            vertx = [v1x, v2x, v3x]
            verty = [v1y, v2y, v3y]
            fx, fy = [], []
            p0x, p0y = 0.0, 0.0 # Punto de inicio en el centro
            
            for _ in range(iteraciones):
                v = random.randint(0, 2) # Sortea uno de los 3 vértices
                x = (p0x + vertx[v]) / 2
                y = (p0y + verty[v]) / 2
                fx.append(x)
                fy.append(y)
                p0x, p0y = x, y
                
            # 4. Dibujamos y guardamos la imagen
            plt.scatter(fx, fy, s=1, color="purple")
            plt.axis('equal')
            plt.axis('off') # Ocultamos los ejes
            plt.savefig("resultado.png")
            
            # 5. Mostramos en la web
            st.image("resultado.png", caption="Fractal Generado")
            st.success("¡Fractal generado con éxito!")
            
        except Exception as e:
            st.error("Hubo un error:")
            st.code(str(e))

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
