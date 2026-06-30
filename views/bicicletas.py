import streamlit as st
from controllers.bike_controller import registrar_bicicleta


if not st.session_state.get("logged_in", False):
    st.warning("Debe iniciar sesión")
    st.stop()

st.title("Bicicletas")


@st.dialog("Registrar bicicleta")
def dialogo_registro():

    marca = st.text_input("Marca")

    modelo = st.text_input("Modelo")

    color = st.selectbox(
        "Color",
        [
            "Negro",
            "Blanco",
            "Gris",
            "Rojo",
            "Azul",
            "Verde",
            "Amarillo",
            "Naranja",
            "Violeta",
            "Rosa"
        ]
    )

    tipo = st.selectbox(
        "Tipo",
        [
            "Urbana",
            "Mountain Bike",
            "Ruta",
            "Eléctrica"
        ]
    )

    precio = st.number_input(
        "Precio por hora",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Registrar"):

        resultado = registrar_bicicleta(
            marca,
            modelo,
            color,
            tipo,
            precio
        )

        if resultado["success"]:
            st.success(resultado["message"])
            st.rerun()

        else:
            st.error(resultado["message"])


if st.button("Registrar bicicleta"):
    dialogo_registro()

st.divider()

st.write("Aquí se mostrará la tabla de bicicletas.")