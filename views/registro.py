import time
import streamlit as st
from auth import registrar_usuario

st.title("📝 Crear cuenta")

nombre = st.text_input("Nombre")
apellido = st.text_input("Apellido")
usuario = st.text_input("Usuario")
email = st.text_input("Correo electrónico")

password = st.text_input(
    "Contraseña",
    type="password"
)

confirmar = st.text_input(
    "Confirmar contraseña",
    type="password"
)

if st.button("Crear cuenta"):
    resultado = registrar_usuario(nombre, apellido, usuario, email, password)

    if resultado["success"]:
        st.success(resultado["message"])
        st.toast("Redirigiendo al login...", icon="🚀")

        time.sleep(1.2)

        st.switch_page("views/login.py")

    else:
        st.error(resultado["message"])