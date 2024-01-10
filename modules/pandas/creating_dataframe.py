import streamlit as st

def create_dataframe():
    st.subheader('Creating Pandas Dataframe')
    st.code("""
            # initialize list of lists
            data = [['tom', 10], ['nick', 15], ['juli', 14]]
            
            # Create the pandas DataFrame
            df = pd.DataFrame(data, columns=['Name', 'Age'])
            """)

    st.code("""
            # initialize data of lists.
            data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
                    'Age': [20, 21, 19, 18]}
            
            # Create DataFrame
            df = pd.DataFrame(data)
            """)

    st.code("""
            # Initialize data to lists.
            data = [{'a': 1, 'b': 2, 'c': 3},
                    {'a': 10, 'b': 20, 'c': 30}]
            
            # Creates DataFrame.
            df = pd.DataFrame(data)
            """)
