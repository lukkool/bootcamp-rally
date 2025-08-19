CREATE OR REPLACE SCHEMA teams_schema;
CREATE OR REPLACE SCHEMA cars_schema;
CREATE OR REPLACE SCHEMA races_schema;

CREATE OR REPLACE TABLE teams_schema.teams (
    team_id INT AUTOINCREMENT PRIMARY KEY,
    team_name STRING NOT NULL,
    members STRING,
    budget FLOAT DEFAULT 10000
);

INSERT INTO teams_schema.teams (team_name, members, budget) VALUES
('Speedsters', 'Alice,Bob', 10000),
('Turbo Kings', 'Charlie,David', 10000),
('Rapid Racers', 'Eve,Frank', 10000);


CREATE OR REPLACE TABLE cars_schema.cars (
    car_id INT AUTOINCREMENT PRIMARY KEY,
    car_name STRING NOT NULL,
    team_id INT REFERENCES teams_schema.teams(team_id),
    speed FLOAT,
    durability FLOAT,
    handling FLOAT
);


INSERT INTO cars_schema.cars (car_name, team_id, speed, durability, handling) VALUES
('Flash', 1, 180, 90, 80),
('Lightning', 2, 175, 85, 90),
('Storm', 3, 190, 80, 85);


CREATE OR REPLACE TABLE races_schema.racing_history (
    race_id INT AUTOINCREMENT PRIMARY KEY,
    race_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    team_id INT REFERENCES teams_schema.teams(team_id),
    car_id INT REFERENCES cars_schema.cars(car_id),
    time FLOAT,
    prize FLOAT
);


