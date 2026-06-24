import streamlit as st
import time
import streamlit as st
import time

# Configuración de la página con temática romántica
st.set_page_config(page_title="Un mensaje el amor de mi vida ♥", page_icon="💖", layout="centered")

# Estilos personalizados para fondo rosa, texto legible y animación de corazones
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
    /* Estilos para la lluvia de corazones */
    @keyframes heart-fall {
        0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(105vh) translateX(100px) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        top: -10vh;
        font-size: 24px;
        color: #ff4d94;
        user-select: none;
        pointer-events: none;
        animation: heart-fall 4s linear infinite;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='titulo'>Para mi amor bonito (:flor:) 🌼☀️✨</h1>", unsafe_allow_html=True)
st.write("")

# Texto de la carta
texto = """Mi amorcito bello,

Compartir mis dias contigo ha sido lo mas hermoso de mi vida
los viajes, aventuras, rutas y salidas ahora son especiales y perfectas 
porque estas a mi lado.
🏖️✈️⛰️🏍️

Me siento feliz y afortunado de tener un amor tan bonito, 
que Dios nos bendiga siempre 🙏

Gracias por regalarme tus dias, tu amor, tus abrazos, tus besos.
Te amo hoy, mañana y siempre. ♥"""

# Botón para iniciar la animación
if st.button("💖 Haz clic aquí para leer tu mensaje"):
    placeholder = st.empty()
    texto_animado = ""
    
    # Bucle para simular la máquina de escribir
    for caracter in texto:
        texto_animado += caracter
        placeholder.markdown(f"<div class='carta'>{texto_animado}</div>", unsafe_allow_html=True)
        time.sleep(0.05)
    
    # NUEVO: Inyección de HTML para generar la lluvia de corazones en posiciones aleatorias
    corazones_html = "".join([
        f"<div class='heart' style='left: {i * 7}vw; animation-delay: {i * 0.2}s; animation-duration: {3 + (i % 3)}s;'>❤️</div>"
        for i in range(15)
    ])
    st.markdown(corazones_html, unsafe_allow_html=True)



