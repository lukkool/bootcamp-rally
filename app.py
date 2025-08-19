import streamlit as st
from modules.car_manager import add_car
from modules.team_manager import get_teams, add_team
from modules.race_simulator import simulate_race


st.title("🏎️ Bootcamp Rally Racing")
tabs = st.tabs(["Cars", "Teams", "Race"])

# --- Cars tab ---
with tabs[0]:
    st.header("Add New Car")
    teams = get_teams()
    team_options = {row["TEAM_NAME"]: row["TEAM_ID"] for _, row in teams.iterrows()}
    with st.form("add_car"):
        car_name = st.text_input("Car Name")
        speed = st.number_input("Speed", 50, 400)
        durability = st.number_input("Durability", 0, 100)
        handling = st.number_input("Handling", 0, 100)
        team_choice = st.selectbox("Team", list(team_options.keys()))
        if st.form_submit_button("Add Car"):
            add_car(car_name, team_options[team_choice], speed, durability, handling)
            st.success(f"Car '{car_name}' added to '{team_choice}'!")

with tabs[1]:
    st.header("Add New Team")
    with st.form("add_team"):
        team_name = st.text_input("Team Name")
        budget = st.number_input("Budget", 10000, 10000000)
        members_input = st.text_area("Team Members (comma-separated)")  # Renamed for clarity
        if st.form_submit_button("Add Team"):
            members_list = [m.strip() for m in members_input.split(',') if m.strip()]
            add_team(team_name, members_list, budget)
            st.success(f"Team '{team_name}' added with budget of {budget}$!")

# --- Race tab ---
with tabs[2]:
    if st.button("Start Race!"):
        placeholder = st.empty()

        with placeholder.container():
            # Display the GIF
            st.markdown(
                f'<div style="text-align: center;"><img src="https://tenor.com/view/kitty-cat-driving-car-cute-gif-16109266.gif" width="400"></div>',
                unsafe_allow_html=True
            )
            st.markdown("<h3 style='text-align: center;'>The race is on! 🏎️💨</h3>", unsafe_allow_html=True)
            race_results, winning_team = simulate_race()

        placeholder.empty()

        st.subheader("🏁 Race Results")
        st.success(f"🏆 The winner is {winning_team}!")

        for pos, (team_id, _, car_name, team_name, time) in enumerate(race_results, start=1):
            st.write(f"{pos}. {team_name} - {car_name} | Time: {time:.2f}h")

