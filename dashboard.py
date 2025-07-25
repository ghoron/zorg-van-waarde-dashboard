
import streamlit as st
import plotly.graph_objects as go
import datetime

st.set_page_config(layout="wide")
st.title("Zorg van Waarde Dashboard")

# Functie om gauges te maken
def klok(titel, waarde):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=waarde,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': titel},
        gauge={
            'axis': {'range': [0, 10]},
            'bar': {'color': "royalblue"},
            'steps': [
                {'range': [0, 4], 'color': "lightcoral"},
                {'range': [4, 7], 'color': "khaki"},
                {'range': [7, 10], 'color': "lightgreen"},
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

# Kolom 1 - Zorgverleners
st.header("👨‍⚕️ Zorgverleners - Welzijn")
col1, col2, col3 = st.columns(3)
with col1:
    klok("Zingeving", 8.2)
with col2:
    klok("Werkplezier", 7.9)
with col3:
    klok("Fitheid", 8.5)

# Emoji-poll alleen op werkdagen
st.header("📊 Hoe voel je je vandaag?")
dag = datetime.datetime.today().weekday()
if dag < 5:
    keuze = st.radio("Klik een emoji:", ["😄", "🙂", "😐", "🙁", "😫"], horizontal=True)
    if st.button("Verstuur"):
        st.success(f"Bedankt voor je reactie: {keuze}")
else:
    st.info("Vandaag is het weekend – geen poll actief.")

# Kolom 2 en 3 - Uitkomsten
st.header("📈 Zorgresultaten")
col4, col5, col6 = st.columns(3)
with col4:
    klok("Patiënttevredenheid", 8.4)
with col5:
    klok("Verwijzingen", 3.1)
with col6:
    klok("Chronisch zieken", 6.2)
