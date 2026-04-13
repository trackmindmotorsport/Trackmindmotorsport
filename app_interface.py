import streamlit as st
import pandas as pd
import plotly.express as px

# --- SEGURIDAD ---
def check_password():
    if "password_correct" not in st.session_state:
        st.title("🔒 Trackmind APEX v11.0")
        pwd = st.text_input("Introduce la clave estratégica", type="password")
        if st.button("Acceder"):
            if pwd == "Apex2026":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Clave incorrecta")
        return False
    return True

# --- CONTENIDO PRINCIPAL ---
if check_password():
    st.set_page_config(page_title="Trackmind APEX", layout="wide")
    st.title("🏎️ Centro de Estrategia APEX")
    
    # LISTA DE LOS 22 PILOTOS (Parrilla 2026)
    lista_pilotos = [
        "K. Antonelli", "M. Verstappen", "L. Norris", "O. Piastri", 
        "G. Russell", "L. Hamilton", "C. Leclerc", "C. Sainz",
        "F. Alonso", "L. Stroll", "P. Gasly", "E. Ocon", 
        "N. Hülkenberg", "O. Bearman", "Y. Tsunoda", "L. Lawson",
        "A. Albon", "F. Colapinto", "G. Zhou", "V. Bottas",
        "J. Doohan", "B. Bortoleto"
    ]
    
    st.sidebar.header("Panel de Control")
    piloto = st.sidebar.selectbox("Seleccionar Operador:", lista_pilotos)
    
    # Simulación de datos para que todos tengan algo que mostrar
    # (En el futuro esto se puede conectar a datos reales)
    import random
    prob_victoria = round(random.uniform(5.0, 45.0), 1)
    estados = ["Óptimo", "Estable", "Riesgo Motor", "Desgaste Neumáticos"]
    estado_actual = random.choice(estados)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"Piloto: {piloto}")
        st.metric("Probabilidad de Victoria", f"{prob_victoria}%")
        st.info(f"Estado del Sistema: {estado_actual}")

    with col2:
        # Gráfico de rendimiento simulado
        df = pd.DataFrame({
            "Sector": ["S1", "S2", "S3"], 
            "Rendimiento": [random.randint(80, 98) for _ in range(3)]
        })
        fig = px.line(df, x="Sector", y="Rendimiento", title=f"Telemetría: {piloto}")
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.caption("Trackmind APEX v11.0 | Parrilla Completa 2026")
