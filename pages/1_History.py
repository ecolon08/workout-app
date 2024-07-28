import pandas as pd
import streamlit as st
import datetime
import gspread


def filter_by_date(df, dt):
    return df[df['date'] == dt]


def filter_by_exercise(df, ex):
    return df[df['exercise'] == ex]


def get_ex_df(df, dt):
    """
    Function to return dataframes for each unique exercise on a given date
    :param df: DataFrame with all exercises to be filtered by date
    :param dt: Date string to filter by
    :return: list of dataframes with unique exercises
    """
    fltrd_df = filter_by_date(df, dt)
    unique_exercises = fltrd_df['exercise'].unique()
    exercises = {}
    for ex in unique_exercises:
        exercises[ex] = filter_by_exercise(df, ex)[['reps', 'weight', 'time', 'superset', 'notes']]
    # return [filter_by_exercise(df, e) for e in unique_exercises]
    return exercises


# df_db = pd.read_csv('csv_db.csv')
# Create a connection object
creds = st.secrets['gspread']['gsheets_creds']
gc = gspread.service_account_from_dict(creds)
sh = gc.open('workout_db')
worksheet = sh.get_worksheet(0)

# print(sh.sheet1.get('A1'))
df_db = pd.DataFrame(worksheet.get_all_records())

# date filter
d = st.date_input("Exercise Date", datetime.date.today(), format="MM/DD/YYYY").strftime("%m/%d/%y")
st.write(d)
exercises = get_ex_df(df_db, d)

for e in exercises.keys():
    st.write(e)
    st.dataframe(exercises[e], hide_index=True)
