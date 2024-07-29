import streamlit as st
import pandas as pd
from util import (
    check_password,
    load_gs_worksheet
)


if not check_password():
    st.stop()

worksheet = load_gs_worksheet()

df_db = pd.DataFrame(worksheet.get_all_records())

# filter by Exercise
unique_exercises = pd.DataFrame(df_db['exercise'].unique(), columns=['exercise'])
# print(type(unique_exercises))
st.dataframe(unique_exercises, hide_index=True)

# ex_option = st.selectbox('Exercise', unique_exercises)
