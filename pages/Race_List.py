import streamlit as st
from modules.race_simulator import get_race_history

st.header("Race History")
history = get_race_history()
st.table(history)