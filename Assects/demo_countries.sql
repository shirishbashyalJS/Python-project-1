
CREATE DATABASE IF NOT EXISTS world_data;
USE world_data;

DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    area_km2 BIGINT,
    famous_for TEXT
);


INSERT INTO countries (name, latitude, longitude, area_km2, famous_for) VALUES
('United States', 37.090240, -95.712891, 9833520, 'World’s largest economy, Hollywood, Silicon Valley, global superpower'),
('China', 35.861660, 104.195397, 9596961, 'Great Wall, largest population, manufacturing powerhouse'),
('India', 20.593684, 78.962880, 3287263, 'Taj Mahal, yoga, Bollywood, second most populous country'),
('Japan', 36.204824, 138.252924, 377975, 'Technology innovation, anime, Mount Fuji'),
('Germany', 51.165691, 10.451526, 357022, 'Engineering excellence, BMW, Oktoberfest'),
('France', 46.227638, 2.213749, 551695, 'Eiffel Tower, fashion, wine and cuisine'),
('United Kingdom', 55.378051, -3.435973, 243610, 'Industrial Revolution, London, monarchy'),
('Brazil', -14.235004, -51.925280, 8515767, 'Amazon Rainforest, football, Carnival'),
('Italy', 41.871940, 12.567380, 301340, 'Roman Empire history, Vatican City, pizza and pasta'),
('Canada', 56.130366, -106.346771, 9984670, 'Second largest country by area, Niagara Falls, natural resources');
