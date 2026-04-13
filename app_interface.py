import streamlit as st
import pandas as pd
import plotly.express as px

# SEGURIDAD (Tu llave de acceso)
def check_password():
    def password_entered():
        if st.session_state["password"] == "Apex2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.title("🔒 Trackmind APEX v11.0")
        st.text_input("Introduce la clave estratégica", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Clave incorrecta", type="password", on_change=password_entered, key="password")
        st.error("Acceso denegado")
        return False
    return True

# CONTENIDO DE LA APP
if check_password():
    st.set_page_config(page_title="Trackmind APEX", layout="wide")
    st.title("🏎️ Centro de Estrategia APEX")
    
    piloto = st.sidebar.selectbox("Operador", ["K. Antonelli", "M. Verstappen", "L. Norris"])
    
    col1, col2 = st.columns(2)
    
    datos = {
        "K. Antonelli": {"prob": 44.2, "status": "Óptimo"},
        "M. Verstappen": {"prob": 9.6, "status": "Riesgo Motor"},
        "L. Norris": {"prob": 28.1, "status": "Estable"}
    }

    with col1:
        st.metric("Probabilidad de Victoria", f"{datos[piloto]['prob']}%")
        st.info(f"Estado: {datos[piloto]['status']}")

    with col2:
        df = pd.DataFrame({"Sector": ["S1", "S2", "S3"], "Rendimiento": [95, 88, 92]})
        fig = px.line(df, x="Sector", y="Rendimiento", title="Telemetría Proyectada")
        st.plotly_chart(fig, use_container_width=True)
