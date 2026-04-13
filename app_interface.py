import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="APEX F1 Terminal", layout="wide", initial_sidebar_state="collapsed")

# --- ESTILO VISUAL (Auditoría Imagen 1) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .tech-header {
        font-family: monospace; color: #586069; font-size: 0.7rem;
        text-transform: uppercase; letter-spacing: 2px;
        border-bottom: 1px solid #161B22; padding-bottom: 5px; margin-bottom: 20px;
    }
    .stSlider > div > div > div > div { background-color: #00E6FF; }
</style>
""", unsafe_allow_html=True)

# --- SEGURIDAD ---
if "password_correct" not in st.session_state:
    st.title("🔒 APEX STRATEGY")
    pwd = st.text_input("ACCESS KEY:", type="password")
    if st.button("LOGIN"):
        if pwd == "Apex2026":
            st.session_state["password_correct"] = True
            st.rerun()
else:
    # --- CABECERA ---
    st.markdown("<h1>CHASIS & STRATEGY <span style='color:#586069;'>v11.0</span></h1>", unsafe_allow_html=True)
    
    # --- FILA 1: DIALES (IMAGEN 1) ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='tech-header'>Chaos Meter</div>", unsafe_allow_html=True)
        val = random.randint(40, 90)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number", value = val,
            number = {'suffix': "%", 'font': {'size': 50}},
            gauge = {
                'axis': {'range': [0, 100], 'tickcolor': "#586069"},
                'bar': {'color': "#FFFFFF"},
                'steps': [
                    {'range': [0, 40], 'color': "#238636"},
                    {'range': [40, 70], 'color': "#D29922"},
                    {'range': [70, 100], 'color': "#DA3633"}]
            }
        ))
        fig.update_layout(height=280, paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20,r=20,t=20,b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("<div class='tech-header'>Top 10 Prediction</div>", unsafe_allow_html=True)
        prob = random.randint(70, 99)
        fig_p = go.Figure(data=[go.Pie(labels=['T10', 'OUT'], values=[prob, 100-prob], hole=.8, marker_colors=['#00E6FF', '#161B22'])])
        fig_p.update_layout(height=280, showlegend=False, paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0))
        fig_p.add_annotation(text=f"{prob}%", x=0.5, y=0.5, font_size=40, showarrow=False)
        st.plotly_chart(fig_p, use_container_width=True)

    st.divider()

    # --- FILA 2: SIMULADOR (IMAGEN 1) ---
    st.markdown("<div class='tech-header'>Scenario Simulator</div>", unsafe_allow_html=True)
    c3, c4 = st.columns([2, 1])
    with c3:
        st.slider("RAIN PROBABILITY", 0, 100, 15)
        st.slider("FUEL LOAD", 0, 110, 65)
    with c4:
        st.button("MODE X (DRS+)", use_container_width=True)
        st.button("MODE Z (BASE)", use_container_width=True)

    st.divider()

    # --- FILA 3: TABLA (ELIMINANDO EL ERROR) ---
    st.markdown("<div class='tech-header'>Inferred Telemetry Risk</div>", unsafe_allow_html=True)
    
    df = pd.DataFrame({
        'Driver': ['Verstappen', 'Norris', 'Colapinto'],
        'Status': ['OPTIMAL', 'STABLE', 'WARNING'],
        'Energy': ['92%', '85%', '60%']
    })

    # Solución al AttributeError: Usamos st.dataframe directo o estilos compatibles
    def color_risk(val):
        color = '#DA3633' if val == 'WARNING' else '#238636'
        return f'color: {color}'

    # Usamos .style.map (la versión moderna que no da error)
    st.dataframe(df.style.map(color_risk, subset=['Status']), use_container_width=True)
