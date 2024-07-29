import streamlit as st
import pandas as pd
import gspread
from util import (
    check_password,
    filter_by_exercise,
    filter_by_date,
    load_gs_worksheet
)

if not check_password():
    st.stop()

worksheet = load_gs_worksheet()

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
