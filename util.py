import streamlit as st
import hmac
import gspread
import datetime
import pytz


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


def filter_by_exercise(df, ex):
    return df[df['exercise'] == ex]


def filter_by_date(df, dt):
    return df[df['date'] == dt]


def load_gs_worksheet():
    creds = st.secrets['gspread']['gsheets_creds']
    gc = gspread.service_account_from_dict(creds)
    sh = gc.open('workout_db')
    worksheet = sh.get_worksheet(0)
    return worksheet


def set_todays_date():
    if 'today' not in st.session_state:
        tz = pytz.timezone('America/New_York')
        dt_ny = datetime.datetime.now(tz)
        st.session_state['today'] = dt_ny.today()