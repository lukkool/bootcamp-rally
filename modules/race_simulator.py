import random
from modules import db

RACE_FEE = 1000
PRIZE = 5000
RACE_DISTANCE = 100  # km


def simulate_race():
    cars = db.query("""
                    SELECT C.CAR_ID,
                           C.CAR_NAME,
                           C.SPEED,
                           C.DURABILITY,
                           C.HANDLING,
                           C.TEAM_ID,
                           T.BUDGET,
                           T.TEAM_NAME
                    FROM CARS_SCHEMA.CARS C
                             JOIN TEAMS_SCHEMA.TEAMS T ON C.TEAM_ID = T.TEAM_ID
                    """)

    results = []

    for _, car in cars.iterrows():
        new_budget = car['BUDGET'] - RACE_FEE
        db.execute("UPDATE TEAMS_SCHEMA.TEAMS SET BUDGET=%s WHERE TEAM_ID=%s",
                   (new_budget, car['TEAM_ID']))

        # Simulate race time
        speed_factor = car['SPEED'] * random.uniform(0.8, 1.2)
        durability_factor = car['DURABILITY'] / 100
        handling_factor = car['HANDLING'] / 100
        time = RACE_DISTANCE / (speed_factor * durability_factor * handling_factor)
        results.append((car['TEAM_ID'], car['CAR_ID'], car['CAR_NAME'], car['TEAM_NAME'], time))

    results.sort(key=lambda x: x[4])  # sort by time
    winner_team_id, winner_car_id, winner_car_name, winner_team_name, winner_time = results[0]

    db.execute("UPDATE TEAMS_SCHEMA.TEAMS SET BUDGET=BUDGET+%s WHERE TEAM_ID=%s",
               (PRIZE, winner_team_id))

    db.execute("""
               INSERT INTO RACES_SCHEMA.RACING_HISTORY (team_id, car_id, time, prize)
               VALUES (%s, %s, %s, %s)
               """, (winner_team_id, winner_car_id, winner_time, PRIZE))

    return results, winner_team_name


def get_race_history():
    return db.query("""
        SELECT RH.race_id, RH.race_date, T.TEAM_NAME, C.CAR_NAME, RH.time, RH.prize
        FROM RACES_SCHEMA.RACING_HISTORY RH
        JOIN TEAMS_SCHEMA.TEAMS T ON RH.team_id = T.TEAM_ID
        JOIN CARS_SCHEMA.CARS C ON RH.car_id = C.CAR_ID
        ORDER BY RH.race_date DESC
    """)