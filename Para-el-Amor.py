import streamlit as st
import time

# Configuración de la página con temática romántica
st.set_page_config(page_title="Un mensaje para ti ♥", page_icon="💖", layout="centered")

# Estilos personalizados para fondo rosa y texto legible
st.markdown("""
    <style>
    .stApp {
        background-color: #ffe6f2;
    }
    .titulo {
        color: #ff4d94;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .carta {
        font-size: 20px;
        color: #4a4a4a;
        line-height: 1.6;
        font-family: 'Courier New', Courier, monospace;
        white-space: pre-wrap;
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='titulo'>Para el regalo que Dios me prometio ✨</h1>", unsafe_allow_html=True)
st.write("")

# Texto de la carta
texto = """Mi amorcito bello,

me siento el hombre mas afortunado del universo 
por tener el privilegio de compartir contigo;

te amo, vida hermosa. ♥"""

# Botón para iniciar la animación
if st.button("💖 Haz clic aquí para leer tu mensaje"):
    # Contenedor vacío donde se irá escribiendo el texto
    placeholder = st.empty()
    texto_animado = ""
    
    # Bucle para simular la máquina de escribir
    for caracter in texto:
        texto_animado += caracter
        # Renderizamos el texto dentro de una caja estilizada de HTML
        placeholder.markdown(f"<div class='carta'>{texto_animado}</div>", unsafe_allow_html=True)
        time.sleep(0.05) # Velocidad de la escritura
    
    # Efecto de globos al terminar
    st.balloons()
