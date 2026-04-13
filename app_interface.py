import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import numpy as np

# --- 1. CONFIGURACIÓN DE PÁGINA (Estilo FIA Engineering) ---
st.set_page_config(
    page_title="APEX F1 Strategy | Terminal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS PERSONALIZADO (Híper Realismo Visual) ---
# Forzamos modo oscuro puro, fuentes técnicas y colores neón.
st.markdown("""
<style>
    /* Fondo y texto general */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'SF Pro Display', sans-serif;
    }
    
    /* Headers estilo telemetría (Imagen 1) */
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

    /* Estilo para tarjetas de métricas */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] {
        background-color: #0D1117;
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #161B22;
    }

    /* Sliders estilo Imagen 1 */
    .stSlider > div > div > div > div {
        background-color: #00E6FF; /* Cian Neón */
    }

    /* Forzar ocultar menú Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. SEGURIDAD ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>🔒 APEX Secure Terminal</h1>", unsafe_allow_html=True)
        pwd = st.text_input("Enter Strategic Access Key:", type="password")
        if st.button("Access"):
            if pwd == "Apex2026":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Invalid Key")
        return False
    return True

if check_password():
    # --- 4. LÓGICA DE SIMULACIÓN Y SELECCIÓN ---
    lista_pilotos = ["K. Antonelli", "M. Verstappen", "L. Norris", "O. Piastri", "F. Alonso", "F. Colapinto", "B. Bortoleto"]
    piloto = st.sidebar.selectbox("OPERATOR:", lista_pilotos, index=1)
    
    # Datos simulados base
    base_probs = {"Antonelli": 35, "Verstappen": 92, "Norris": 78, "Piastri": 65, "Alonso": 60, "Colapinto": 45, "Bortoleto": 30}
    
    # Encabezado (Logo F1 opcional)
    st.markdown("<div style='text-align: right;'><img src='https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg' width='60'></div>", unsafe_allow_html=True)
    st.markdown(f"<h1>{piloto} | <span style='color:#586069;'>2026 Strategy</span></h1>", unsafe_allow_html=True)
    
    st.divider()

    # --- 5. FILA 1: DIALES PRINCIPALES (Look Imagen 1) ---
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='tech-header'>Chaos Intensity Meter</div>", unsafe_allow_html=True)
        chaos_val = random.randint(30, 95)
        # Dial tipo Gauge (Imagen 1)
        fig_chaos = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = chaos_val,
            number = {'suffix': "%", 'font': {'color': "#FFFFFF", 'size': 50}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#586069"},
                'bar': {'color': "#FF0000" if chaos_val > 70 else "#F1C40F"}, # Aguja Roja/Amarilla
                'bgcolor': "#161B22",
                'borderwidth': 1,
                'bordercolor': "#30363D",
                'steps': [
                    {'range': [0, 40], 'color': "#238636"},   # Verde
                    {'range': [40, 70], 'color': "#D29922"},  # Amarillo
                    {'range': [70, 100], 'color': "#DA3633"}  # Rojo
                ],
            }
        ))
        fig_chaos.update_layout(height=280, paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_chaos, use_container_width=True)

    with col2:
        st.markdown("<div class='tech-header'>Top 10 Probability (Live)</div>", unsafe_allow_html=True)
        prob_t10 = base_probs.get(piloto.split(". ")[1], 50) + random.randint(-5, 5)
        # Dial tipo Donut (Híbrido)
        fig_win = go.Figure(data=[go.Pie(labels=['Top 10', 'Outside'], values=[prob_t10, 100-prob_t10], hole=.75, marker_colors=['#00E6FF', '#161B22'])])
        fig_win.update_layout(
            height=280, paper_bgcolor='rgba(0,0,0,0)', showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10),
            annotations=[dict(text=f'{prob_t10}%', x=0.5, y=0.5, font_size=40, font_color="#FFFFFF", showarrow=False)]
        )
        st.plotly_chart(fig_win, use_container_width=True)

    st.divider()

    # --- 6. FILA 2: SIMULADOR DE ESCENARIOS (Controles Imagen 1) ---
    st.markdown("<div class='tech-header'>Scenario Simulator & Active Aero</div>", unsafe_allow_html=True)
    col3, col4 = st.columns([2, 1])
    
    with col3:
        # Sliders (Imagen 1)
        rain_prob = st.slider("RAIN PROBABILITY", 0, 100, 20, format="%d%%")
        track_temp = st.slider("TRACK TEMP (°C)", 10, 50, 28)
        fuel_load = st.slider("FUEL LOAD (kg)", 10, 110, 70)
        
        # Afectar probabilidades con sliders
        if rain_prob > 50: prob_t10 += random.randint(5, 15); st.info("Wet conditions simulation active.")

    with col4:
        # Toggles de Active Aero (Imagen 5)
        st.write("**ACTIVE AERO TOGGLE**")
        st.button("MODE X (Low Drag)", key="modeX")
        st.button("MODE Z (High Downforce)", key="modeZ")
        st.caption("Targeting: P7-P9 for Top 10.")

    st.divider()

    # --- 7. FILA 3: STATUS & TELEMETRÍA INFERIDA (Imagen 5) ---
    st.markdown("<div class='tech-header'>Live System Status & Inferred Data</div>", unsafe_allow_html=True)
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.write("🔋 Battery SoC")
        val_ers = random.randint(75, 98)
        st.progress(val_ers / 100)
        st.caption(f"Status: {val_ers}% - Deployment Stable")

    with col6:
        st.write("🛞 Tyre Life (Median)")
        val_tyre = random.randint(50, 85)
        st.progress(val_tyre / 100)
        st.caption(f"Status: {val_tyre}% - Window Open")

    with col7:
        st.write("📉 Fuel Delta")
        st.markdown("<h2 style='color:#00ff41;'>+0.15kg</h2>", unsafe_allow_html=True)
        st.caption("Status: Fuel Safe")

    st.divider()

    # Tabla Técnica (Imagen 5)
    st.markdown("<div class='tech-header'>Tabla de Telemetría Inferida</div>", unsafe_allow_html=True)
    inf_data = {
        'Driver': ['1. Verstappen', '2. Norris', f'3. {piloto}'],
        'Expected P1': ['72.1%', '15.5%', '8.2%'],
        'Energy Risk': ['[========= ] 90%', '[=======   ] 70%', '[======    ] 60%'],
        'Derating Risk': ['LOW', 'STABLE', 'WARNING'],
        'Strategy': ['Plan A', 'Plan A', 'Plan B: Alt']
    }
    df_inf = pd.DataFrame(inf_data)
    
    # Estilo condicional para la tabla
    def color_risk(val):
        if val == 'WARNING': color = '#DA3633' # Rojo
        elif val == 'LOW': color = '#238636' # Verde
        else: color = '#FFFFFF'
        return f'color: {color}; font-weight: bold;'

    st.dataframe(df_inf.style.applymap(color_risk, subset=['Derating Risk']), use_container_width=True, hide_index=True)

    st.divider()
    st.caption("APEX Strategy Engine v11.0 Pro | FIA 2026 Specs | Santo Domingo Terminal")
