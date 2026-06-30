import streamlit as st
from database import Base, engine
import models

st.set_page_config(
    page_title="Bike Rental",
    page_icon="🚲",
    layout="centered"
)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Inicializar la sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Páginas públicas
login = st.Page("views/login.py", title="Iniciar sesión", icon="🔐")
registro = st.Page("views/registro.py", title="Registrarse", icon="📝")

# Páginas privadas
inicio = st.Page("views/inicio.py", title="Inicio", icon="🏠")
bicicletas = st.Page("views/bicicletas.py", title="Bicicletas", icon="🚲")
alquileres = st.Page("views/alquileres.py", title="Alquileres", icon="📋")
perfil = st.Page("views/perfil.py", title="Perfil", icon="👤")

# Elegir navegación según la sesión
if st.session_state.logged_in:
    pg = st.navigation(
        [inicio, bicicletas, alquileres, perfil]
    )
else:
    pg = st.navigation(
        [login, registro]
    )

pg.run()