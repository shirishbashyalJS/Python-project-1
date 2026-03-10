
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
('United States', 37.090240, -95.712891, 9833520, 'World’s largest economy, Hollywood, Silicon Valley'),
('China', 35.861660, 104.195397, 9596961, 'Great Wall, largest population, manufacturing powerhouse'),
('India', 20.593684, 78.962880, 3287263, 'Taj Mahal, yoga, Bollywood'),
('Japan', 36.204824, 138.252924, 377975, 'Technology innovation, anime, Mount Fuji'),
('Germany', 51.165691, 10.451526, 357022, 'Engineering excellence, BMW, Oktoberfest'),
('France', 46.227638, 2.213749, 551695, 'Eiffel Tower, fashion, wine and cuisine'),
('United Kingdom', 55.378051, -3.435973, 243610, 'Industrial Revolution, London, monarchy'),
('Brazil', -14.235004, -51.925280, 8515767, 'Amazon Rainforest, football, Carnival'),
('Italy', 41.871940, 12.567380, 301340, 'Roman Empire history, Vatican City, pizza and pasta'),
('Canada', 56.130366, -106.346771, 9984670, 'Second largest country by area, Niagara Falls'),
('Australia', -25.274398, 133.775136, 7692024, 'The Great Barrier Reef, Kangaroos, and the Outback'),
('Russia', 61.524010, 105.318756, 17098242, 'Largest country in the world, Kremlin, Red Square'),
('South Korea', 35.907757, 127.766922, 100210, 'K-Pop, Samsung, and high-speed internet'),
('Mexico', 23.634501, -102.552784, 1964375, 'Chichen Itza, Day of the Dead, and Tacos'),
('Egypt', 26.820553, 30.802498, 1001450, 'The Great Pyramids, Sphinx, and the Nile River'),
('South Africa', -30.559482, 22.937506, 1221037, 'Safari wildlife, Table Mountain, and Nelson Mandela'),
('Spain', 40.463667, -3.749220, 505992, 'Flamenco dance, Paella, and Sagrada Familia'),
('Turkey', 38.963745, 35.243322, 783562, 'Hot air balloons in Cappadocia and the Hagia Sophia'),
('Argentina', -38.416097, -63.616672, 2780400, 'Tango dance, Lionel Messi, and Patagonia'),
('Thailand', 15.870032, 100.992541, 513120, 'Tropical beaches, ornate temples, and street food'),
('Greece', 39.074208, 21.824312, 131957, 'Birthplace of democracy, Parthenon, and beautiful islands'),
('Switzerland', 46.818188, 8.227512, 41285, 'The Alps, chocolate, luxury watches, and neutrality'),
('Norway', 60.472024, 8.468946, 323802, 'Breathtaking Fjords, Midnight Sun, and Vikings'),
('Sweden', 60.128161, 18.643501, 450295, 'ABBA, IKEA, and the Nobel Prize'),
('Netherlands', 52.132633, 5.291266, 41543, 'Tulips, windmills, and massive cycling culture'),
('Portugal', 39.399872, -8.224454, 92212, 'Fado music, Port wine, and Vasco da Gama'),
('New Zealand', -40.900557, 174.885971, 268021, 'Lord of the Rings landscapes, Haka, and Kiwis'),
('Iceland', 64.963051, -19.020835, 103000, 'Blue Lagoon, Northern Lights, and volcanoes'),
('Poland', 51.919438, 19.145136, 312685, 'Pierogi, medieval architecture, and Marie Curie'),
('Vietnam', 14.058324, 108.277199, 331210, 'Ha Long Bay, Pho soup, and motorbikes'),
('Indonesia', -0.789275, 113.921327, 1904569, 'Bali beaches, Komodo dragons, and 17,000 islands'),
('Saudi Arabia', 23.885942, 45.079162, 2149690, 'The Mecca, vast deserts, and oil reserves'),
('Kenya', -1.286389, 36.817223, 580367, 'The Maasai Mara, long-distance runners, and coffee'),
('Morocco', 31.791702, -7.092620, 446550, 'Marrakesh markets, Atlas Mountains, and Sahara Desert'),
('Peru', -9.189967, -75.015152, 1285216, 'Machu Picchu, Incan Empire, and Ceviche'),
('Chile', -35.675147, -71.542969, 756102, 'Easter Island, Atacama Desert, and fine wine'),
('Austria', 47.516231, 14.550072, 83871, 'Classical music, Mozart, and mountain skiing'),
('United Arab Emirates', 23.424076, 53.847818, 83600, 'Burj Khalifa, luxury shopping, and desert safaris'),
('Singapore', 1.352083, 103.819836, 728, 'Garden City, Marina Bay Sands, and strict laws'),
('Malaysia', 4.210484, 101.975766, 330803, 'Petronas Towers, Batu Caves, and rainforests'),
('Pakistan', 30.375321, 69.345116, 796095, 'K2 mountain, ancient Indus Valley, and cricket'),
('Nigeria', 9.081999, 8.675277, 923768, 'Nollywood film industry, diverse tribes, and oil'),
('Ukraine', 48.379433, 31.165580, 603628, 'Sunflowers, Chernobyl history, and Carpathian Mountains'),
('Colombia', 4.570868, -74.297333, 1141748, 'Superior coffee, emeralds, and Shakira'),
('Belgium', 50.503887, 4.469936, 30528, 'Waffles, chocolate, and the European Union HQ'),
('Denmark', 56.263920, 9.501785, 43094, 'LEGO, Hans Christian Andersen, and cycling'),
('Ireland', 53.142367, -7.692054, 70273, 'Emerald Isle, St. Patrick’s Day, and Guinness'),
('Philippines', 12.879721, 121.774017, 300000, 'Stunning lagoons, Boracay, and 7,107 islands'),
('Israel', 31.046051, 34.851612, 22145, 'The Dead Sea, Silicon Wadi, and ancient history');