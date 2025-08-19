import streamlit as st
from modules.car_manager import get_cars

st.header("Cars list")
cars = get_cars()
st.table(cars)