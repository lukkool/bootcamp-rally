import streamlit as st
from modules.team_manager import get_teams

st.header("Teams list")
teams = get_teams()
st.table(teams)