🗺️ AeroHunt: The Map of Echoes
AeroHunt is an immersive, text-based terminal adventure that challenges players to navigate the globe, solve physics-based projectile puzzles, and crack cryptographic codes to secure an ancient treasure.



📜 The Story

The Backstory 📄

In the frigid, desolate wilderness of Finland, a solitary traveler named Elias sought shelter from a blizzard within the mouth of an ancient, forgotten cave. While scraping away frost from the limestone walls, he unearthed a hollowed-out stone containing a tattered, oil-stained map. It wasn't just a map; it was a riddle—a cryptic guide to a lost hoard of antiquities hidden by a nomadic civilization that vanished centuries ago. With the map whispering promises of fortune and glory, Elias decided to trade his quiet life for the thrill of the chase.


The Ultimate Aim 🎯
To navigate across the globe, survive the physical trials of the hunt, and ultimately decipher the final mechanism guarding the treasure to claim the lost artifacts.


The Setting and Environment
The journey begins in the stark, frozen landscapes of Finland. From there, the player must traverse various international borders, moving through diverse environments—from bustling, sun-drenched markets to dense, humid jungles—guided only by the elusive hints scribbled on the parchment. The final destination is a legendary, weathered temple tucked away in a remote corner of the world, where the treasure sits high upon a precarious rooftop.

The Characters 🦹‍♂️
Elias (The Player): A curious explorer whose bravery is tested by his limited resources and the unforgiving clock of his journey.

The Ancient Nomads (Background): The mysterious creators of the treasure, whose cryptic legacy still dictates the challenges of the hunt.

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

Folder Structure: 


Python-project-1/
├── Assects/               
│   ├── .env                     # Database credentials (locally created)
│   ├── countries.sql            # Database schema with data for countries
│   └── Patterns.sql             # Database schema with data for patterns
├── functions/                   # Utility scripts and helper functions
│   ├── databaseConnection.py    # Database credentials (locally created)
│   ├── smoothPrinting.py.sql    # Database schema with data for countries
├── src/                         # Core game logic and phase modules
│   ├── countryFind.py           # Phase I: Global Navigation logic
│   ├── crossbow.py              # Phase II: Physics-based challenges
│   ├── countrynamefind.py       # Phase III: Decryption logic
│   ├── story.py                 # Holds the story of the game
│   └── userName.py              # Ask for the username and level of the game
├── main.py                      # Main entry point to launch the game
├── .gitignore                   # Files to be excluded from version control
└── README.md                    # Project documentation


🚀 Installation
Clone the repository:

```bash
git clone https://github.com/shirishbashyalJS/Python-project-1.git
cd Python-project-1
Install dependencies:
```

```bash
pip install geopy python-dotenv mariadb
```

⚙️ Environment Setup
To run this game locally, you need to configure your database credentials.

Create a file named .env inside the assets/ folder.

Copy the following template into your .env file and update it with your local MariaDB credentials:

```text
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=world_data
```

Security Warning: Never commit your .env file to GitHub. It is ignored by Git automatically in this project.

Run The Game:
Navigate to Python-project-1, and In terminal, Write 

```bash
cd Python-project-1
```
Run the Main File:

```bash
python main.py
```


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
