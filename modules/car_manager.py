from modules import db

def add_car(name, team_id, speed, durability, handling):
    db.execute(
        "INSERT INTO CARS_SCHEMA.CARS (CAR_NAME, TEAM_ID, SPEED, DURABILITY, HANDLING) VALUES (%s,%s,%s,%s,%s)",
        (name, team_id, speed, durability, handling)
    )

def get_cars():
    return db.query("SELECT C.CAR_ID, C.CAR_NAME, C.SPEED, C.DURABILITY, C.HANDLING, T.TEAM_NAME "
                    "FROM CARS_SCHEMA.CARS C JOIN TEAMS_SCHEMA.TEAMS T ON C.TEAM_ID=T.TEAM_ID")