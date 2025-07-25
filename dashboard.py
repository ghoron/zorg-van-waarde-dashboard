# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
import datetime

st.set_page_config(layout="wide")
st.title("Zorg van Waarde Dashboard")

DATA_DIR = Path(__file__).parent / "data"

def safe_read_csv(filename):
    """Lees CSV-bestand als het bestaat, anders None."""
    file_path = DATA_DIR / filename
    if file_path.exists():
        return pd.read_csv(file_path)
    return None

def klok(titel, waarde, maxwaarde=10):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=waarde,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': titel},
        gauge={
            'axis': {'range': [0, maxwaarde]},
            'bar': {'color': "royalblue"},
            'steps': [
                {'range': [0, maxwaarde*0.4], 'color': "lightcoral"},
                {'range': [maxwaarde*0.4, maxwaarde*0.7], 'color': "khaki"},
                {'range': [maxwaarde*0.7, maxwaarde], 'color': "lightgreen"},
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

# --- 1. Zorgverleners ---
st.header("👨‍⚕️ Welzijn zorgverleners")
col1, col2, col3 = st.columns(3)
with col1: klok("Zingeving", 8.2)
with col2: klok("Werkplezier", 7.9)
with col3: klok("Fitheid", 8.5)

# --- 2. Poll zorgverleners ---
st.header("📊 Hoe voel je je vandaag?")
dag = datetime.datetime.today().weekday()
if dag < 5:
    keuze = st.radio("Klik een emoji:", ["😄", "🙂", "😐", "🙁", "😫"], horizontal=True)
    if st.button("Verstuur"):
        st.success(f"Bedankt voor je reactie: {keuze}")
else:
    st.info("Vandaag is het weekend - geen poll actief.")

# --- 3. CSV-data inladen ---
st.header("📂 Data uit CSV-bestanden")

# Verwijzingen
verwijzingen = safe_read_csv("Verwijzingen 2024.csv")
if verwijzingen is not None:
    st.subheader("Verwijzingen")
    st.dataframe(verwijzingen.head())
else:
    st.info("Nog geen data geupload voor verwijzingen")

# Medicatie
medicatie = safe_read_csv("Medicatie Q1-2025.csv")
if medicatie is not None:
    st.subheader("Medicatie")
    st.dataframe(medicatie.head())
else:
    st.info("Nog geen data geupload voor medicatie")

# Leeftijden
leeftijden = safe_read_csv("Leeftijden Q1-2025.csv")
if leeftijden is not None:
    st.subheader("Leeftijden")
    st.dataframe(leeftijden.head())
else:
    st.info("Nog geen data geupload voor leeftijden")

# Positieve Gezondheid
pg = safe_read_csv("PG juni 2025.csv")
if pg is not None:
    st.subheader("Positieve Gezondheid")
    st.dataframe(pg.head())
else:
    st.info("Nog geen data geupload voor Positieve Gezondheid")

# Chronische aandoeningen (HVZ / CVRM / DM2)
hvz = safe_read_csv("HVZ Q2 2025.csv")
cvrm = safe_read_csv("CVRM Q2 2025.csv")
dm2 = safe_read_csv("Diabetes Mellitus II Q2 2025.csv")

if hvz is not None or cvrm is not None or dm2 is not None:
    st.subheader("Chronische aandoeningen")
    if hvz is not None:
        st.write("**HVZ**")
        st.dataframe(hvz.head())
    if cvrm is not None:
        st.write("**CVRM**")
        st.dataframe(cvrm.head())
    if dm2 is not None:
        st.write("**Diabetes type II**")
        st.dataframe(dm2.head())
else:
    st.info("Nog geen data geupload voor chronische aandoeningen")
