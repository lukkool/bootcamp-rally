from modules import db

def add_team(name, members, budget=10000):
    members_str = ", ".join(members)
    db.execute(
        "INSERT INTO TEAMS_SCHEMA.TEAMS (TEAM_NAME, MEMBERS, BUDGET) VALUES (%s,%s,%s)",
        (name, members_str, budget)
    )


def get_teams():
    return db.query("SELECT TEAM_ID, TEAM_NAME, MEMBERS, BUDGET FROM TEAMS_SCHEMA.TEAMS")