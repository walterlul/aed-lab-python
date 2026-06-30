import streamlit as st

if not st.session_state.get("logged_in", False):
    st.warning("Debe iniciar sesión")
    st.stop()


st.title("Perfil")