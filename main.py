import streamlit as st
import datetime
import pytz
from util import (
    check_password,
    load_gs_worksheet,
    set_todays_date
)

st.title('Workout Tracking App')

if not check_password():
    st.stop()

# Get today's date and set as session's variable

set_todays_date()
# if 'today' not in st.session_state:
#     tz = pytz.timezone('America/New_York')
#     dt_ny = datetime.datetime.now(tz)
#     d = st.date_input("Exercise Date", dt_ny.today(), format="MM/DD/YYYY").strftime("%m/%d/%y")
#     st.session_state['today'] = d

# d = st.date_input("Exercise Date", dt_ny.today(), format="MM/DD/YYYY").strftime("%m/%d/%y")

worksheet = load_gs_worksheet()

# st.button("Click me")

st.write("Log a new set")

with st.form(key='new_set'):
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        exercise = st.text_input('Exercise', value='')

    with col2:
        reps = st.text_input('Reps', value='')

    with col3:
        weight = st.text_input('Weight', value='')

    with col4:
        time = st.text_input('Time', value='')

    with col5:
        superset = st.text_input('Superset', value='')

    with col6:
        notes = st.text_input('Notes', value='')

    submit_bttn = st.form_submit_button('Submit')


# append to database
if submit_bttn:
    data = [st.session_state['today'], exercise, reps, weight, time, superset, notes]
    worksheet.append_row(data, value_input_option='USER_ENTERED')
