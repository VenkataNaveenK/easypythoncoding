import streamlit as st

def my_dataframe_notes():
    st.subheader('DataFrames')
    st.code("""
            # Bunch of Series object shares a same index.
            from numpy.random import randint
            np.random.seed(42)

            index = ['A','B','C','D','E']
            columns = ['w','x','y','z']
            data = randint(-100, 100,(5,4))
            df = pd.DataFrame(data, index, columns)
            '''
            output: 
                w   x   y   z
            A   2   79  88  -86
            B   6   -29 -26 -80
            C   2   21  -8  -13
            D   16  -1  3   51
            E   30  49  -48 -99
            '''
            # selection and indexing
            df['w']             # returns pandas.Series
            type(df['w'])       # pandas.core.series.Series
            type(df)            # pandas.core.frame.DataFrame

            # multiple columns
            df[['w','z']]       # if two or more Series combine, it will be dataframe
            type(df[['w','z']]) # pandas.core.frame.DataFrame

            # create a new column
            df['new'] = df['w'] + df['x']
            
            # Removing a column
            df.drop('new')      # gives us error b/c 'new' is not present in rows. default axis=0
            df.drop('new', axis=1) # removes the column and df will not be affected
            df.drop('new', axis=1, inplace=True) # df is affected

            # Rows
            df.loc['A']         # returns 'A' with all columns
            type(df.loc['A'])   # pandas.core.series.Series

            # multiple rows
            df.loc[['A', 'B', 'C']] # returns requested rows with all columns

            # Indexing with index value
            df.iloc[0]          # grabing the first row
            df.iloc[0:2]        # grabing two row values

            # Remove a row
            df.drop('A', axis=0, inplace=True)

            # Grab subset of rows & columns
            df.loc[['A', 'C'],['w','y']]

            # Conditional selection
            df[df>0]
            df[df['x']>0]
            df[(df['w']>0) & (df['y']>1)]   # here (df['w']>0) is condition1 and (df['y']>1) is condition2
            
            # Reset index
            df.reset_index()    # Reset the index to 0,1,2.. etc from labels 'A','B','C','D','E'
            df.reset_index(inplace=True) # To reset in the same df
            new_index = ['UP','MP','AP','TN','JK']
            df['new_index'] = new_index
            df.set_index('new_index')

            """)