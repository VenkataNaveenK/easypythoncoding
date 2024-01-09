import streamlit as st
import os
import base64

def virtual_env_creation():
    st.header("Virtual environment creation")
    st.text("Create a project folder and open vscode inside it")
    st.code("pip install virtualenv")
    st.code("virtualenv venv")
    st.code(r"venv\Scripts\activate")

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

def git_commands():
    st.header("Git Commands")
    st.subheader("1. Username and email configuration:")
    st.code("git config --global user.name 'yourName'")
    st.code("git config --global user.email 'youremail@email.com'")

    st.subheader("2. To verify the configuration:")
    st.code("git config user.name")
    st.code("git config user.email")

    st.subheader("3. To intialize a new repository")
    st.code("git init")

    st.subheader("4. To get the changes in repository")
    st.code("git status")

    st.subheader("5. To get differences")
    st.code("git diff")
    st.text("or")
    st.code("git diff <filename>")

    st.subheader("6. To add the file changes to working tree")
    st.code("git add .")
    st.text("or")
    st.code("git add <filename>")

    st.subheader("7. To commit the changes to working tree")
    st.code("git commit -m 'meaningful message'")

    st.subheader("8. To check the list of commits")
    st.code("git log")
    st.text("or")
    st.code("git log --oneline")

    st.subheader("9. To reset to a particular commit")
    st.code("git reset --hard <commit id>")

    st.subheader("10. To delete last commit")
    st.code("git reset --hard HEAD^0")

    st.subheader("11. Creation of a branch in local")
    st.code("git branch <branch name>")

    st.subheader("12. List of local branches")
    st.code("git branch")

    st.subheader("13. Checkout a branch")
    st.code("git checkout <branchname>")

    st.subheader("14. Merging master branch(old) to dev branch(new)")
    st.code("git checkout master")
    st.code("git merge dev")

    st.subheader("15. To delete a branch")
    st.code("git branch -d <branch name>")

    st.subheader("16. Configuring remote repository to local branch")
    st.code("git remote add origin <url for remote repo>")
    st.code("git remote -v")

    st.subheader("17. Pushing changes to remote repository")
    st.code("git push origin master")

    st.subheader("18. Cloning a remote repository")
    st.code("git clone <remote repo url>")

    st.subheader("19. Pulling changes from remote repository")
    st.code("git pull origin master")

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

def show_os_module():
    st.code("""
            os.getcwd()  # current working directory
            os.listdir(path)  # lists all the files and directories in the 'path'
            os.remove(path)  # removes a file
            os.rmdir(directory_path)  # removes a directory if it is empty. To delete non-empty folder, use shutil module
            os.rename('old_name.txt','New_name.txt')  # renames the file name
            os.mkdir(directory_path, mode)  # mode = 0o666 --> create a directory
            os.makedirs(directory_path, mode)  # creates all directories missing in the mentioned directory_path
            # os.path
            os.path.exists("file_name")  # giving the name of the file as a parameter
            os.path.getsize("filename")  # give us the size of the file in bytes
            os.path.join(path1, file_name)  # joins paths according to operating system
            os.path.basename("/baz/foo")  # output: foo
            os.path.dirname("/baz/foo")  # output: /baz
            os.path.isabs("/baz/foo")  # output: True
            os.path.isdir("C:\\Users")  # output: True
            os.path.isfile("C:\\Users\foo.csv")  # output: True
            os.path.normcase("/BAz")  # output: '\\\\baz' --> normcase in windows
            """)

def show_glob_module():
    st.markdown("[Open 'glob' module article](%s)" % "https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/")

def show_subprocess_module():
    st.markdown("[Open 'subprocess' module article](%s)" % "https://www.geeksforgeeks.org/python-subprocess-module/")

def show_logging_module():
    st.markdown("[Open 'logging' module article](%s)" % "https://www.geeksforgeeks.org/logging-in-python/")

def show_datetime_module():
    st.markdown("[Open 'datetime' module article](%s)" % "https://www.geeksforgeeks.org/python-datetime-module/")

def show_pathlib_module():
    st.markdown("[Open 'pathlib' module article](%s)" % "https://www.geeksforgeeks.org/pathlib-module-in-python/")

def show_shutil_module():
    st.markdown("[Open 'shutil' module article](%s)" % "https://www.geeksforgeeks.org/shutil-module-in-python/")


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

    