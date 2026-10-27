import streamlit as st

st.set_page_config(
    page_title="API Security",
    page_icon="🔐",
)

st.title("API security")

with st.sidebar:
    st.header("Configuration")
    api_url = st.text_input("URL de l'API", "http://localhost:8000/endpoint").rstrip("/")
    username= st.text_input("User", "admin")
    password = st.text_input("Mot de passe", type="password")
    