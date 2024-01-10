import streamlit as st

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
