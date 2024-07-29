import streamlit as st
import hmac
from util import check_password

st.title('Workout Tracking App')

if not check_password():
    st.stop()

# Main Streamlit app starts here
st.write("Here goes your normal Streamlit app...")
st.button("Click me")
