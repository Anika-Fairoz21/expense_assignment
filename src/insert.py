import os
import streamlit as st
import pandas as pd

from src.db_ops import show_data, edit_data, delete_data


def parameter_listing(cursor, db):
    st.header('💸 INSERT YOUR FIELD')
    # st.write(st.session_state)
    if 'flag' not in st.session_state:
        st.session_state.flag = 0

    with st.form(key='expense_submit_form', clear_on_submit=False, border=True):
        datatype_catagory = ['Select datatype', 'Numerical Data', 'Text data', 'password', 'Others']

        purpose = st.text_input('Purpose')
        datatype = st.selectbox('Type of data*', datatype_catagory)
        if st.form_submit_button(label='Submit'):
            if not(purpose and datatype):
                st.error('Please fill all the * fields')
            else:
                st.session_state.flag = 1

    if st.session_state.flag:
    # st.write(final_parameter_calculation)
        with st.form(key='final', clear_on_submit=True, border=True):
            # st.write(final_parameter_calculation)


            if st.form_submit_button('Are you Sure?'):
                # st.write(final_parameter_calculation)
                st.session_state.flag = 0
                
                query = '''Insert into parameters (purpose, datatype) 
                        VALUES (%s, %s)
                        '''
                values = (purpose,datatype)
                # st.write(query, values)
                cursor.execute(query, values)
                db.commit()
                st.success("Expense Record Inserted Successfully!")
                st.balloons()

            else:
                st.write("Click above button If you are Sure")
    else:
        st.warning("Please fill up above form")

    df = pd.read_sql('''SELECT purpose, datatype FROM parameters''', con=db)
 
    # st.dataframe(df)

    # select the columns you want the users to see
    columns = [
               'purpose',
                'datatype'
                ]
                   
    # st.dataframe(df[columns])
    show_data(df, columns)
    edit_data(cursor, db, df, columns, 'Edit Expenses', 'parameters')
    delete_data(cursor, db, df, columns, 'Delete Expenses', 'parameters')
    