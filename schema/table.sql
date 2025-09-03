-- Create Team Table
CREATE TABLE Team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100),
    coach VARCHAR(100),
    captain VARCHAR(100),
    no_of_players INT,
    no_of_staff INT,
    no_of_wins INT DEFAULT 0
);

-- Create Player Table
CREATE TABLE Player (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    team_id INT,
    nationality VARCHAR(50),
    role VARCHAR(50),
    age INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

-- Create Stadium Table
CREATE TABLE Stadium (
    stadium_id INT AUTO_INCREMENT PRIMARY KEY,
    stadium_name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    capacity INT,
    no_of_stands INT,
    home_team_id INT,
    FOREIGN KEY (home_team_id) REFERENCES Team(team_id)
);

-- Create Match Table
CREATE TABLE Matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    match_date DATE NOT NULL,
    team1_id INT,
    team2_id INT,
    venue VARCHAR(100),
    winner_team_id INT,
    FOREIGN KEY (team1_id) REFERENCES Team(team_id),
    FOREIGN KEY (team2_id) REFERENCES Team(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES Team(team_id)
);

-- Create PlayerStats Table
CREATE TABLE PlayerStats (
    player_id INT PRIMARY KEY,
    role VARCHAR(50),
    pl_matches INT DEFAULT 0,
    pl_runs INT DEFAULT 0,
    pl_wickets INT DEFAULT 0,
    pl50r INT DEFAULT 0,
    pl100r INT DEFAULT 0,
    pl5wi INT DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);

-- Create MatchStats Table
CREATE TABLE MatchStats (
    match_id INT,
    player_id INT,
    runs INT DEFAULT 0,
    wickets INT DEFAULT 0,
    balls_faced INT DEFAULT 0,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id) REFERENCES Matches(match_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);
