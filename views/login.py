import streamlit as st

st.title("🚲 Bike Rental")

usuario = st.text_input("Usuario")

password = st.text_input(
    "Contraseña",
    type="password"
)

st.button("Ingresar")