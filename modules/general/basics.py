import streamlit as st
from .utils import (show_os_module, 
                   show_glob_module, 
                   show_subprocess_module, 
                   show_logging_module,
                   show_datetime_module,
                   show_pathlib_module,
                   show_shutil_module
                   )

def general_modules():
    st.header("General modules")
    selected_lib = st.selectbox("Select a module",
                                [
                                    'os', 
                                    'glob', 
                                    'subprocess', 
                                    'logging',
                                    'datatime',
                                    'pathlib',
                                    'shutil',

                                ]
                            )
    if selected_lib == 'os':
        show_os_module()
    elif selected_lib == 'glob':
        show_glob_module()
    elif selected_lib == 'subprocess':
        show_subprocess_module()
    elif selected_lib == 'logging':
        show_logging_module()
    elif selected_lib == 'datatime':
        show_datetime_module()
    elif selected_lib == 'pathlib':
        show_pathlib_module()
    elif selected_lib == 'shutil':
        show_shutil_module()