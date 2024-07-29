import pandas as pd
import streamlit as st
import datetime
import pytz
import gspread
from util import (
    check_password,
    filter_by_date,
    filter_by_exercise,
    load_gs_worksheet,
    set_todays_date
)


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

    return exercises


if not check_password():
    st.stop()

worksheet = load_gs_worksheet()

df_db = pd.DataFrame(worksheet.get_all_records())

# date filter
tz = pytz.timezone('America/New_York')
dt_ny = datetime.datetime.now(tz)
d = st.date_input("Exercise Date", dt_ny.date(), format="MM/DD/YYYY").strftime("%m/%d/%y")
st.write(d)

exercises = get_ex_df(df_db, d)

for e in exercises.keys():
    st.write(e)
    st.dataframe(exercises[e], hide_index=True)
