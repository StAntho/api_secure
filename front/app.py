import streamlit as st
import os, httpx
from dotenv import load_dotenv

st.set_page_config(
    page_title="API Security",
    page_icon="🔐",
    layout="wide"
)

st.title("API security")

load_dotenv()
API_URL = os.getenv("STREAMLIT_URL_API")

with st.sidebar:
    st.header("Configuration")
    api_url = st.text_input("URL de l'API", "http://localhost:8000/endpoint").rstrip("/")
    username= st.text_input("User", "admin")
    password = st.text_input("Mot de passe", type="password")


endpoints = ['/public_data/info', '/private_data/info', '/private_data/health']
col_request, col_response = st.columns(2)

with col_request:
    path = st.selectbox("Données de:", endpoints)
    send = st.button("Envoyer", type="primary")

with col_response:
    if send:
        st.markdown("**Response**")
        res = httpx.get(
            API_URL+path,
            timeout=60.0,
        )
        st.write(res.json())