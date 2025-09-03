-- Insert Teams
INSERT INTO Team (team_name, city, coach, captain, no_of_players, no_of_staff, no_of_wins)
VALUES 
('Chennai Super Kings', 'Chennai', 'Stephen Fleming', 'MS Dhoni', 25, 10, 5),
('Mumbai Indians', 'Mumbai', 'Mark Boucher', 'Rohit Sharma', 25, 12, 7),
('Royal Challengers Bangalore', 'Bengaluru', 'Andy Flower', 'Faf du Plessis', 25, 11, 0);

-- Insert Players
INSERT INTO Player (player_name, team_id, nationality, role, age, salary)
VALUES
('MS Dhoni', 1, 'India', 'Wicketkeeper-Batsman', 42, 15000000),
('Ravindra Jadeja', 1, 'India', 'All-Rounder', 34, 12000000),
('Rohit Sharma', 2, 'India', 'Batsman', 36, 14500000),
('Jasprit Bumrah', 2, 'India', 'Bowler', 30, 13000000),
('Virat Kohli', 3, 'India', 'Batsman', 36, 16000000),
('Glenn Maxwell', 3, 'Australia', 'All-Rounder', 35, 11000000);

-- Insert Stadiums
INSERT INTO Stadium (stadium_name, city, capacity, no_of_stands, home_team_id)
VALUES
('M. A. Chidambaram Stadium', 'Chennai', 50000, 5, 1),
('Wankhede Stadium', 'Mumbai', 45000, 4, 2),
('M. Chinnaswamy Stadium', 'Bengaluru', 40000, 4, 3);

-- Insert Matches
INSERT INTO Matches (match_date, team1_id, team2_id, venue, winner_team_id)
VALUES
('2025-03-31', 1, 2, 'M. A. Chidambaram Stadium', 1),
('2025-04-02', 2, 3, 'Wankhede Stadium', 2),
('2025-04-05', 3, 1, 'M. Chinnaswamy Stadium', 3);

-- Insert Player Stats
INSERT INTO PlayerStats (player_id, role, pl_matches, pl_runs, pl_wickets, pl50r, pl100r, pl5wi)
VALUES
(1, 'Wicketkeeper-Batsman', 250, 5000, 0, 23, 3, 0),
(2, 'All-Rounder', 200, 2500, 120, 10, 1, 5),
(3, 'Batsman', 220, 6000, 0, 40, 4, 0),
(4, 'Bowler', 150, 200, 180, 0, 0, 6),
(5, 'Batsman', 230, 7000, 0, 50, 5, 0),
(6, 'All-Rounder', 180, 3500, 70, 20, 2, 2);

-- Insert Match Stats
INSERT INTO MatchStats (match_id, player_id, runs, wickets, balls_faced)
VALUES
(1, 1, 50, 0, 35),
(1, 2, 30, 2, 25),
(2, 3, 70, 0, 40),
(2, 4, 10, 3, 12),
(3, 5, 80, 0, 45),
(3, 6, 45, 1, 30);
