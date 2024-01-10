import streamlit as st

def create_streamlit_app():
    st.header("Streamlit application creation")
    st.text("Open terminal and activate virtual environment")
    st.code("pip install streamlit==1.25.0")
    st.code("pip install streamlit_option_menu")
    st.code("""
            import streamlit as st 
            from streamlit_option_menu import option_menu

            # Page configuration
            st.set_page_config(
                page_title='EasyPlotting',
                page_icon=':oncoming_automobile:',
                layout='centered'
            )
            with st.sidebar:
                selected = option_menu(
                    menu_title='Essentials',
                    options=['Virtual Env','Streamlit','violinplot','stripplot','lmplot'],
                    icons=['house','file-earmark-text','body-text','chevron-bar-contract','cloud-check'],
                    menu_icon='diagram-3',
                    default_index=0
                )

            if selected == 'Virtual Env':
                virtual_env_creation()
            elif selected == 'Streamlit':
                create_streamlit_app()
            """)
    st.markdown("[streamlit cheat sheet](%s)" % "https://cheat-sheet.streamlit.app/")