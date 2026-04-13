import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import numpy as np

# --- CONFIGURACIÓN DE PÁGINA (UI Premium) ---
st.set_page_config(page_title="APEX F1 | Strategy Terminal", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: ESTILO INSPIRADO EN TU PRIMERA IMAGEN ---
st.markdown("""
<style>
    .stApp { background-color: #05070A; color: #FFFFFF; }
    
    /* Tarjetas de métricas */
    .metric-card {
        background-color: #0D1117;
        border-radius: 8px;
        padding: 20px;
        border-left: 5px solid #00E6FF;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Headers estilo Telemetría */
    .tech-header {
        font-family: 'JetBrains Mono', monospace;
        color: #586069;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    /* Forzar modo oscuro en inputs */
    .stSelectbox div[data-baseweb="select"] { background-color: #0D1117; border-color: #30363D; }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE SEGURIDAD ---
if "password_correct" not in st.session_state:
    st.title("🔒 APEX STRATEGY ACCESS")
    pwd = st.text_input("ENTER KEY CODE:", type="password")
    if st.button("LOGIN"):
        if pwd == "Apex2026":
            st.session_state["password_correct"] = True
            st.rerun()
else:
    # --- CABECERA ---
    col_t1, col_t2 = st.columns([4, 1])
    with col_t1:
        st.markdown("<h1 style='margin-bottom:0;'>STRATEGY SIMULATOR 2026</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#586069;'>Real-time Predictive Analytics | v11.0</p>", unsafe_allow_html=True)
    
    # --- SELECCIÓN DE PILOTO ---
    lista_pilotos = ["K. Antonelli", "M. Verstappen", "L. Norris", "O. Piastri", "F. Alonso", "F. Colapinto", "B. Bortoleto"]
    piloto = st.sidebar.selectbox("SELECT OPERATOR:", lista_pilotos, index=5)

    st.divider()

    # --- FILA 1: DIALES (Inspirado en Imagen 1) ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='tech-header'>Chaos Intensity</div>", unsafe_allow_html=True)
        chaos_val = random.randint(30, 90)
        fig_chaos = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = chaos_val,
            number = {'suffix': "%", 'font': {'color': "#FFFFFF"}},
            gauge = {
                'axis': {'range': [0, 100], 'tickcolor': "#586069"},
                'bar': {'color': "#FF3E3E" if chaos_val > 70 else "#F1C40F"},
                'bgcolor': "#161B22",
                'steps': [
                    {'range': [0, 40], 'color': "#238636"},
                    {'range': [40, 70], 'color': "#D29922"},
                    {'range': [70, 100], 'color': "#DA3633"}]
            }
        ))
        fig_chaos.update_layout(height=250, margin=dict(l=20,r=20,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_chaos, use_container_width=True)

    with c2:
        st.markdown("<div class='tech-header'>Top 10 Probability</div>", unsafe_allow_html=True)
        prob_t10 = random.randint(60, 98)
        fig_t10 = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prob_t10,
            number = {'suffix': "%", 'font': {'color': "#00E6FF"}},
            gauge = {
                'axis': {'range': [0, 100], 'tickcolor': "#586069"},
                'bar': {'color': "#00E6FF"},
                'bgcolor': "#161B22",
                'steps': [{'range': [0, 100], 'color': "rgba(0, 230, 255, 0.1)"}]
            }
        ))
        fig_t10.update_layout(height=250, margin=dict(l=20,r=20,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_t10, use_container_width=True)

    with c3:
        st.markdown("<div class='tech-header'>Strategy Selection</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        mode = st.radio("SELECT ACCURATE MODEL:", ["Standard (Safety First)", "AI Optimized (Recommended)", "Aggressive (High Risk)"], index=1)
        if mode == "AI Optimized (Recommended)":
            st.success("Target: P7-P9 Confirmed")
        else:
            st.warning("Alternative simulation active")

    st.divider()

    # --- FILA 2: BARRAS DE PROGRESO Y STATUS ---
    st.markdown("<div class='tech-header'>Live System Status</div>", unsafe_allow_html=True)
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    
    with col_stat1:
        st.write("🔋 Battery SoC (Energy)")
        val_ers = random.randint(70, 95)
        st.progress(val_ers / 100)
        st.caption(f"Status: {val_ers}% - Optimal Deployment")

    with col_stat2:
        st.write("🛞 Tyre Life (Median)")
        val_tyre = random.randint(40, 80)
        st.progress(val_tyre / 100)
        st.caption(f"Status: {val_tyre}% - Window Open")

    with col_stat3:
        st.write("📉 Fuel Delta")
        st.markdown("<h2 style='color:#00ff41;'>+0.12kg</h2>", unsafe_allow_html=True)
        st.caption("Status: Safe for Finish")

    st.divider()

    # --- FILA 3: MONTE CARLO (ESTILO LIMPIO) ---
    st.markdown("<div class='tech-header'>Monte Carlo Path Invariance</div>", unsafe_allow_html=True)
    
    laps = np.arange(0, 25)
    fig_mc = go.Figure()
    # Línea principal
    fig_mc.add_trace(go.Scatter(x=laps, y=np.random.normal(10, 1, 25), mode='lines+markers', name='Predicted Path', line=dict(color='#00E6FF', width=3)))
    # Nube de incertidumbre
    fig_mc.add_trace(go.Scatter(x=laps, y=np.random.normal(10, 2, 25), fill='toself', fillcolor='rgba(0, 230, 255, 0.1)', line_color='rgba(255,255,255,0)', name='Probability Cloud'))
    
    fig_mc.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                         xaxis=dict(gridcolor='#161B22'), yaxis=dict(gridcolor='#161B22', range=[20, 1]))
    st.plotly_chart(fig_mc, use_container_width=True)

    st.caption("Data Terminal: Santo Domingo | APEX High-Performance Computing")
