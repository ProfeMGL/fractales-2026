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
