import streamlit as st
import pandas as pd
import gspread


def filter_by_exercise(df, ex):
    return df[df['exercise'] == ex]


def filter_by_date(df, dt):
    return df[df['date'] == dt]


# read database
# df_db = pd.read_csv('csv_db.csv')
# Create a connection object

creds = st.secrets['gspread']['gsheets_creds']
gc = gspread.service_account_from_dict(creds)
sh = gc.open('workout_db')
worksheet = sh.get_worksheet(0)

# print(sh.sheet1.get('A1'))
df_db = pd.DataFrame(worksheet.get_all_records())

# filter by Exercise
unique_exercises = df_db['exercise'].unique()

ex_option = st.selectbox('Exercise', unique_exercises)

# First filter by exercise and then display by date
ex_df = filter_by_exercise(df_db, ex_option)

# get unique dates
unique_dates = ex_df['date'].unique()

for d in unique_dates:
    st.write(d)
    st.dataframe(
        filter_by_date(ex_df, d),
        hide_index=True
    )
