import streamlit as st
import os
import base64

def pandas_basics():
    st.header('Pandas')
    # Opening file from file path
    file = os.path.join(os.getcwd(),os.path.join('assets', 'Pandas_Cheat_Sheet.pdf'))
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)