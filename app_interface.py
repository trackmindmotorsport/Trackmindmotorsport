import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

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

if check_password():
    st.set_page_config(page_title="Trackmind APEX", layout="wide")
    
    lista_pilotos = [
        "K. Antonelli", "M. Verstappen", "L. Norris", "O. Piastri", 
        "G. Russell", "L. Hamilton", "C. Leclerc", "C. Sainz",
        "F. Alonso", "L. Stroll", "P. Gasly", "E. Ocon", 
        "N. Hülkenberg", "O. Bearman", "Y. Tsunoda", "L. Lawson",
        "A. Albon", "F. Colapinto", "G. Zhou", "V. Bottas",
        "J. Doohan", "B. Bortoleto"
    ]
    
    st.title("🏎️ Centro de Estrategia APEX")
    
    st.sidebar.header("Panel de Control")
    piloto = st.sidebar.selectbox("Seleccionar Operador:", lista_pilotos)
    
    # --- SIMULACIÓN DE PREDICCIÓN ---
    prob_top10 = random.randint(30, 99)
    prob_victoria = round(prob_top10 * 0.4, 1) # La victoria siempre es más difícil que el top 10

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Probabilidad de Victoria", f"{prob_victoria}%")
    with col2:
        st.write(f"**Probabilidad de Top 10:** {prob_top10}%")
        st.progress(prob_top10 / 100) # Barra de progreso visual

    st.divider()

    # --- GRÁFICO DE RADAR ---
    st.subheader(f"Análisis de Rendimiento: {piloto}")
    categorias = ['Velocidad', 'Neumáticos', 'Adelantamientos', 'Estrategia', 'Salida']
    valores = [random.randint(75, 100) if prob_top10 > 70 else random.randint(50, 85) for _ in range(5)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=valores + [valores[0]],
          theta=categorias + [categorias[0]],
          fill='toself',
          name=piloto,
          line_color='#00ff41' # Verde tecnológico
    ))

    fig.update_layout(
      polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
      template="plotly_dark",
      showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Los datos se recalculan en cada sesión de simulación.")
