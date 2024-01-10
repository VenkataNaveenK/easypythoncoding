import streamlit as st 
from streamlit_option_menu import option_menu
from modules.streamlit.creating_streamlit_app import create_streamlit_app
from modules.pandas import creating_dataframe
from tools.git import git_commands
from modules.general.basics import general_modules
from modules.general.virtual_env import virtual_env_creation
from modules.pandas.base import base

# Page configuration
st.set_page_config(
    page_title='EasyPlotting',
    page_icon=':oncoming_automobile:',
    layout='centered'
)
with st.sidebar:
    selected = option_menu(
        menu_title='Essentials',
        options=['Virtual Env','Streamlit','Git commands', 'Pandas','Common libraries'],#,'stripplot','lmplot'],
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
elif selected == 'Pandas':
    base()
elif selected == 'Common libraries':
    general_modules()