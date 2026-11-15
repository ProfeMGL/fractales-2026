import streamlit as st
import os
import subprocess

st.set_page_config(page_title="Fractales 2026", page_icon="🌀")

st.title("Proyecto Fractales 2026 🌀")
st.write("Bienvenidos a la app del espacio EDI.")

tab1, tab2 = st.tabs(["🎨 Generar Fractal", "💻 Ver Código"])

with tab2:
    st.header("Código de los Fractales")
    archivos_py = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']
    for archivo in archivos_py:
        with st.expander(f"Ver código de {archivo}"):
            with open(archivo, "r", encoding="utf-8") as f:
                codigo = f.read()
            st.code(codigo, language="python")

with tab1:
    st.header("Generador de Fractales")
    archivos_py = [f for f in os.listdir('.') if f.endswith('.py') and f != 'streamlit_app.py']
    
    if archivos_py:
        opcion = st.selectbox("Elegí qué fractal querés generar:", archivos_py)
        
        if st.button("▶️ Generar Fractal"):
            st.info(f"Ejecutando {opcion}...")
            try:
                resultado = subprocess.run(["python", opcion], capture_output=True, text=True)
                if resultado.returncode == 0:
                    st.success("¡Código ejecutado correctamente!")
                else:
                    st.error("Hubo un error al ejecutar el código:")
                    st.code(resultado.stderr)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("No hay archivos .py en el repositorio para ejecutar.")
