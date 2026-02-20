-- 1. Create the table with MariaDB compatible syntax
CREATE TABLE IF NOT EXISTS patterns (
    id INT NOT NULL AUTO_INCREMENT,
    sequence_text TEXT NOT NULL,
    hidden_velocity INT NOT NULL,
    difficulty_level VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- 2. Insert the data
INSERT INTO patterns (sequence_text, hidden_velocity, difficulty_level) VALUES
('2, 4, 6, 8, 10', 12, 'Easy'),
('5, 10, 15, 20, 25', 30, 'Easy'),
('10, 20, 30, 40, 50', 60, 'Easy'),
('100, 95, 90, 85, 80', 75, 'Easy'),
('3, 6, 9, 12, 15', 18, 'Easy'),
('1, 3, 5, 7, 9', 11, 'Easy'),

('2, 4, 8, 16, 32', 64, 'Medium'),
('1, 4, 9, 16, 25', 36, 'Medium'),
('10, 15, 25, 40, 60', 85, 'Medium'),
('81, 64, 49, 36, 25', 16, 'Medium'),
('1, 3, 6, 10, 15', 21, 'Medium'),
('7, 14, 21, 28, 35', 42, 'Medium'),
('100, 99, 97, 94, 90', 85, 'Medium'),

('2, 3, 5, 7, 11', 13, 'Hard'),
('1, 1, 2, 3, 5, 8', 13, 'Hard'),
('1, 8, 27, 64, 125', 216, 'Hard'),
('3, 9, 27, 81, 243', 729, 'Hard'),
('2, 6, 12, 20, 30', 42, 'Hard'),
('1, 2, 6, 24, 120', 720, 'Hard'),
('2, 5, 11, 23, 47', 95, 'Hard');