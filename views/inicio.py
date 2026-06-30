import streamlit as st

if not st.session_state.get("logged_in", False):
    st.warning("Debe iniciar sesión")
    st.stop()

st.title("Inicio")

st.write(f"Bienvenido, {st.session_state.usuario['nombre']}")

if st.button("Cerrar sesión"):
    st.session_state.clear()
    st.rerun()