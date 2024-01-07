import streamlit as st 
from streamlit_option_menu import option_menu
from utils.essentials import (virtual_env_creation, 
                              create_streamlit_app,
                              git_commands
                              )

# Page configuration
st.set_page_config(
    page_title='EasyPlotting',
    page_icon=':oncoming_automobile:',
    layout='centered'
)
with st.sidebar:
    selected = option_menu(
        menu_title='Essentials',
        options=['Virtual Env','Streamlit','Git commands','stripplot','lmplot'],
        icons=['house','file-earmark-text','body-text','chevron-bar-contract','cloud-check'],
        menu_icon='diagram-3',
        default_index=0
    )

if selected == 'Virtual Env':
    virtual_env_creation()
elif selected == 'Streamlit':
    create_streamlit_app()
elif selected == 'Git commands':
    git_commands()