import streamlit as st
from .creating_dataframe import create_dataframe
from .notes import my_dataframe_notes

def base():
    st.header("Pandas")
    selected = st.selectbox('Select the topic', ['Creating DataFrame','Notes on DataFrames'])

    if selected == 'Creating DataFrame':
        create_dataframe()
    if selected == 'Notes on DataFrames':
        my_dataframe_notes()
    