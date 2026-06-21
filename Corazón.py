import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="❤️ Página de Amor ❤️",
    page_icon="❤️",
    layout="centered"
)

# Título
st.title("❤️ Para la Persona que Amo ❤️")

# Cargar imagen
imagen = Image.open("foto.png")  # Cambia por el nombre de tu foto
st.image(imagen, caption="Nuestro recuerdo favorito ❤️", use_container_width=True)

# Mensaje
st.markdown("""
# 💕 Te Amo 💕

Cada momento a tu lado es especial.

Gracias por existir y por llenar mi vida de felicidad.

❤️ Eres mi persona favorita ❤️
""")

# Botón sorpresa
if st.button("💖 Haz clic aquí 💖"):
    st.balloons()
    st.success("¡Te amo mucho! ❤️")