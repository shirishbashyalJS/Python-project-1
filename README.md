🗺️ AeroHunt: The Global Treasure Quest
AeroHunt is an immersive, text-based terminal adventure that challenges players to navigate the globe, solve physics-based projectile puzzles, and crack cryptographic codes to secure an ancient treasure.

📜 The Story
Deep within the frozen wilderness of Finland, an abandoned, ice-crusted cave has been unearthed. Inside, you stumbled upon a tattered, crumbling map. It is not an ordinary map; it is a traveler’s guide to a legendary hidden treasure. Your journey takes you across the world, where you must manage your resources, prove your intelligence, and outsmart the guardians of the treasure.

🎮 Game Phases
The quest is divided into three challenging levels:

Phase I: The Navigator

Travel across the globe to find the hidden destination country.

Manage your budget and fuel while calculating distances.

Follow clues and hints to avoid getting lost.

Phase II: The Archer

Locate the treasure key within the destination.

Predict the initial velocity of the arrow using patterns hidden in the map.

Test your physics intuition to hit the target.

Phase III: The Cryptographer

Decrypt the encrypted treasure box.

Guess the country name before your chances run out.

🛠️ Tech Stack
Language: Python 3.x

Database: MariaDB/MySQL

Libraries: geopy, python-dotenv, mariadb

🚀 Installation
Clone the repository:

Bash
git clone https://github.com/shirishbashyalJS/Python-project-1.git
cd Python-project-1
Install dependencies:

Bash
pip install geopy python-dotenv mariadb


⚙️ Environment Setup
To run this game locally, you need to configure your database credentials.

Create a file named .env inside the assets/ folder.

Copy the following template into your .env file and update it with your local MariaDB credentials:

DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=world_data

Security Warning: Never commit your .env file to GitHub. It is ignored by Git automatically in this project.

Run The Game:
Navigate to Python-project-1, and In terminal, Write 

python main.py


👥 Team

1. Karan
2. Chhabilal Bashyal
3. Nishan Khatiwada
4. Monika Tiwari


📜 MIT License

Copyright (c) 2026 Group 6,

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
