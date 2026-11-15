import streamlit as st
import os

st.set_page_config(page_title="Fractales 2026", page_icon="🌀")

st.title("Proyecto Fractales 2026 🌀")
st.write("Bienvenidos a la app del espacio EDI.")

st.header("Galería de Fractales")
imagenes = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg'))]

if imagenes:
    for img in imagenes:
        st.image(img, caption=f"Imagen: {img}", use_container_width=True)
else:
    st.info("No se encontraron imágenes en el repositorio.")

st.header("Código de los Fractales")
archivos_py = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']

for archivo in archivos_py:
    with st.expander(f"Ver código de {archivo}"):
        with open(archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
        st.code(codigo, language="python")

st.divider()
st.header("🎨 Prueba interactiva")
st.write("Elegí un archivo de tu repositorio para ejecutarlo en vivo:")

# Buscamos los archivos .py
archivos = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']

if archivos:
    # 1. Menú desplegable
    opcion = st.selectbox("Elegí el código que querés ejecutar:", archivos)
    
    # 2. Botón para ejecutar
    if st.button("▶️ Ejecutar código"):
        st.info(f"Ejecutando {opcion}...")
        try:
            import subprocess
            # Ejecuta el archivo de Python
            resultado = subprocess.run(["python", opcion], capture_output=True, text=True)
            if resultado.returncode == 0:
                st.success("¡El código se ejecutó sin errores!")
            else:
                st.error("El código se ejecutó pero devolvió este error:")
                st.code(resultado.stderr)
        except Exception as e:
            st.error(f"Error al intentar ejecutar: {e}")
