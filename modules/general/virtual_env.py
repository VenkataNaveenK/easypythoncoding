import streamlit as st


def virtual_env_creation():
    st.header("Virtual environment creation")
    st.text("Create a project folder and open vscode inside it")
    st.code("pip install virtualenv")
    st.code("virtualenv venv")
    st.code(r"venv\Scripts\activate")