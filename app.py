import streamlit as st

# Simulamos usuarios con sus roles (en la vida real viene de la base de datos)
usuarios = {
    "vendedor1": {"password": "1234", "rol": "vendedor"},
    "admin1": {"password": "adminpass", "rol": "administracion"},
    "prog1": {"password": "progpass", "rol": "programador"}
}

def login():
    st.title("Login")
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["password"] == clave:
            st.session_state["usuario"] = usuario
            st.session_state["rol"] = usuarios[usuario]["rol"]
            st.success(f"Bienvenido {usuario} - Rol: {usuarios[usuario]['rol']}")
        else:
            st.error("Usuario o contraseña incorrectos")

def app_principal():
    st.title(f"Panel de {st.session_state['rol'].capitalize()}")
    rol = st.session_state["rol"]

    if rol == "vendedor":
        st.write("Funcionalidades para vendedor")
        # Aquí va formulario para cargar pedidos, clientes, etc.

    elif rol == "administracion":
        st.write("Funcionalidades para administración")
        # Aquí va gestión de usuarios, reportes, etc.

    elif rol == "programador":
        st.write("Funcionalidades para programador")
        # Aquí va configuración, conexiones API, etc.

    if st.button("Cerrar sesión"):
        st.session_state.clear()
        st.experimental_rerun()

if "usuario" not in st.session_state:
    login()
else:
    app_principal()
