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
with tab_ejecutar:
    st.header("Generador de Fractales")
    
    # Filtramos los archivos .py del repositorio
    archivos_py = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']
    
    if archivos_py:
        opcion = st.selectbox("Elegí qué fractal querés generar:", archivos_py)
        
        if st.button("▶️ Generar Fractal"):
            try:
                plt.clf() # Limpiamos gráficos anteriores
                
                # Ejecutamos el código del fractal elegido
                with open(opcion, "r", encoding="utf-8") as f:
                    codigo = f.read()
                exec(codigo)
                
                # Guardamos el dibujo y lo mostramos
                plt.savefig("resultado.png")
                st.image("resultado.png", caption=f"Fractal: {opcion}")
                st.success("¡Fractal generado con éxito!")
                
            except Exception as e:
                st.error("Hubo un error al ejecutar el archivo:")
                st.code(str(e)) # Muestra el error exacto si falla
    else:
        st.warning("No se encontraron archivos de código (.py).")

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
