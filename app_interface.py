import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import numpy as np

# --- 1. CONFIGURACIÓN TÉCNICA ---
st.set_page_config(
    page_title="APEX F1 Strategy | Terminal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS DE ALTO IMPACTO (Auditoría Visual) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'SF Pro Display', sans-serif; }
    .tech-header {
        font-family: 'JetBrains Mono', monospace;
        color: #586069;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 15px;
        border-bottom: 1px solid #161B22;
        padding-bottom: 5px;
    }
    /* Estilo Sliders */
    .stSlider > div > div > div > div { background-color: #00E6FF; }
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. SEGURIDAD ---
if "password_correct" not in st.session_state:
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>🔒 APEX SECURE ACCESS</h1>", unsafe_allow_html=True)
    pwd = st.text_input("STRATEGIC KEY CODE:", type="password")
    if st.button("AUTHORIZE"):
        if pwd == "Apex2026":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("ACCESS DENIED")
else:
    # --- 4. SELECCIÓN DE OPERADOR ---
    st.sidebar.markdown("### PANEL DE CONTROL")
    lista_pilotos = ["K. Antonelli", "M. Verstappen", "L. Norris", "O. Piastri", "F. Alonso", "F. Colapinto", "B. Bortoleto"]
    piloto = st.sidebar.selectbox("OPERATOR:", lista_pilotos, index=5) # Colapinto default

    # --- 5. ENCABEZADO PRO ---
    st.markdown(f"<h1 style='margin-bottom:0;'>{piloto} | <span style='color:#586069;'>2026 STRATEGY</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00E6FF; font-family:monospace;'>TERMINAL STATUS: ACTIVE | MONTE CARLO ITERATIONS: 5000</p>", unsafe_allow_html=True)
    st.divider()

    # --- 6. FILA DE DIALES (Inspirado en Imagen 1) ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='tech-header'>Chaos Intensity Meter</div>", unsafe_allow_html=True)
        ch_val = random.randint(30, 95)
        fig_ch = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = ch_val,
            number = {'suffix': "%", 'font': {'color': "#FFFFFF", 'size': 60}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#586069"},
                'bar': {'color': "#FFFFFF"},
                'bgcolor': "#161B22",
                'steps': [
                    {'range': [0, 40], 'color': "#238636"},
                    {'range': [40, 70], 'color': "#D29922"},
                    {'range': [70, 100], 'color': "#DA3633"}]
            }
        ))
        fig_ch.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20,r=20,t=20,b=20))
        st.plotly_chart(fig_ch, use_container_width=True)

    with col2:
        st.markdown("<div class='tech-header'>Top 10 Prediction Confidence</div>", unsafe_allow_html=True)
        prob_val = random.randint(65, 98)
        fig_p = go.Figure(data=[go.Pie(labels=['T10', 'OUT'], values=[prob_val, 100-prob_val], hole=.75, marker_colors=['#00E6FF', '#161B22'])])
        fig_p.update_layout(height=300, showlegend=False, paper_bgcolor='rgba(0,0,0,0)', 
                            margin=dict(l=10,r=10,t=10,b=10),
                            annotations=[dict(text=f'{prob_val}%', x=0.5, y=0.5, font_size=45, font_color="#FFFFFF", showarrow=False)])
        st.plotly_chart(fig_p, use_container_width=True)

    st.divider()

    # --- 7. SIMULADOR Y CONTROLES ---
    st.markdown("<div class='tech-header'>Scenario Simulation Inputs</div>", unsafe_allow_html=True)
    c3, c4 = st.columns([2, 1])
    
    with c3:
        st.slider("RAIN PROBABILITY (%)", 0, 100, 15)
        st.slider("TRACK TEMP (°C)", 15, 55, 32)
        st.slider("FUEL LOAD (kg)", 5, 110, 65)

    with c4:
        st.markdown("<p style='font-size:0.8rem; color:#586069;'>ACTIVE AERO MODES</p>", unsafe_allow_html=True)
        st.button("MODE X (LOW DRAG)", use_container_width=True)
        st.button("MODE Z (HIGH DOWNFORCE)", use_container_width=True)

    st.divider()

    # --- 8. TELEMETRÍA Y TABLA (Imagen 5) ---
    st.markdown("<div class='tech-header'>Inferred Telemetry & Risk Analysis</div>", unsafe_allow_html=True)
    
    t_col1, t_col2, t_col3 = st.columns(3)
    with t_col1:
        st.write("🔋 Battery SoC")
        st.progress(0.88)
    with t_col2:
        st.write("🛞 Tyre Life")
        st.progress(0.62)
    with t_col3:
        st.write("📉 Fuel Delta")
        st.markdown("<h3 style='color:#00ff41;'>+0.18kg</h3>", unsafe_allow_html=True)

    # Tabla Técnica
    data = {
        'Driver': ['1. Verstappen', '2. Norris', f'3. {piloto}'],
        'Win Prob': ['68.4%', '18.2%', '7.5%'],
        'Energy Status': ['OPTIMAL', 'STABLE', 'STABLE'],
        'Risk Level': ['LOW', 'LOW', 'WARNING']
    }
    df = pd.DataFrame(data)
    
    def style_risk(val):
        color = '#DA3633' if val == 'WARNING' else '#238636' if val == 'LOW' else '#FFFFFF'
        return f'color: {color}; font-weight: bold'

    st.table(df.style.applymap(style_risk, subset=['Risk Level']))

    st.caption("APEX 2026 Strategy | Santo Domingo Terminal | v11.0.4")
