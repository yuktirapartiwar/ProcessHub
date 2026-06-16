import streamlit as st

from database import initialize_database

initialize_database()

st.set_page_config(
    page_title="ProcessHub",
    page_icon="📋",
    layout="wide"
)

st.title("ProcessHub")

st.write("Workflow Management Platform")    