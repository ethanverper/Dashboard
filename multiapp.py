"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        st.sidebar.title("Kardex Informativo")
        st.sidebar.subheader("by Nuevo Amanecer")
        st.session_state.gs_URL = st.sidebar.text_input("Privarte Nuevo Amanecer URL:","https://docs.google.com/spreadsheets/d/1mnqBzFI2doEicBFj3aOS0sN1lX_Sn5TaJw4MYQynEGc/edit?usp=sharing") 
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()