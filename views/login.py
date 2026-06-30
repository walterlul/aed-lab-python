import streamlit as st
from controllers.auth_controller import iniciar_sesion

st.title("Inicio de sesion")

usuario=st.text_input("Usuario")

password=st.text_input("Contraseña", type="password")

if st.button("Ingresar"):
    resultado=iniciar_sesion(usuario,password)

    if resultado["success"]:
        st.session_state["logged_in"]=True
        st.session_state["usuario"]=resultado["data"]

        st.success(resultado["message"])
        st.rerun()
    else:
        st.error(resultado["message"])