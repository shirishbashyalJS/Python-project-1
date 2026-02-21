import mariadb
import random
from geopy.distance import geodesic
import os
from dotenv import load_dotenv

# This looks for a .env file in the current directory
load_dotenv()

# Default starting location (Finland)
temp_location = {
    "name": "Finland",
    "latitude": 61.924110,
    "longitude": 25.748151
}


# Function to connect database

def database_connection():

    config = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", 3306)), # Cast to int; 3306 is the fallback
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

    try:
        conn = mariadb.connect(**config)
        print("Server Loaded!\n")

        cur = conn.cursor()

        query = "SELECT * FROM countries;"
        cur.execute(query)

        fetched_data = cur.fetchall()

        return fetched_data

    except mariadb.Error as e:
        print(f"Error in MariaDB: {e}")
        return []


# Function to get full tuple using country name

def get_country_tuple(country_name, fetched_data):
    for country in fetched_data:
        if country[1].lower() == country_name.lower():
            return country
    return None


# Function to update user's current location

def updating_location(user_thought_country, fetched_data):

    country = get_country_tuple(user_thought_country, fetched_data)

    if country is not None:
        new_location = {
            "name": country[1],
            "latitude": float(country[2]),
            "longitude": float(country[3])
        }
        return new_location
    else:
        return None


# Main Program

fetched_data = database_connection()

# Show player's starting country

print(f"You are currently in: {temp_location['name']}\n")

# Show all available travelable countries
print("You can travel to the following countries:\n")
for country in fetched_data:
    print("-", country[1])

print("\n--------------------------------------")

# Pick random target country
random_country_data = random.choice(fetched_data)

# Show hint
print(f"\nHint for the country is: {random_country_data[5]}\n")

# Player Money System
money = 65000
cost_per_km = 1

# Game Loop
while True:

    print(f"Current Location: {temp_location['name']}")
    print(f"Money Left: {round(money,2)} €")

    user_thought_country = input("Guess the country name: ").lower()

    # If correct guess
    if user_thought_country == random_country_data[1].lower():
        print("\nYou reached the correct country!")
        print(f"Money Left: {round(money,2)} €")
        break

    new_loc = updating_location(user_thought_country, fetched_data)

    if new_loc is not None:

        temp_location = new_loc

        user_coords = (
            temp_location["latitude"],
            temp_location["longitude"]
        )

        target_coords = (
            float(random_country_data[2]),
            float(random_country_data[3])
        )

        # calculate distance
        distance = geodesic(user_coords, target_coords).km
        distance = round(distance, 2)

        print(f"You travelled {distance} km")

        # calculate travel cost
        travel_cost = distance * cost_per_km
        money -= travel_cost

        print(f"Travel Cost: {round(travel_cost,2)} €")
        print(f"Money Remaining: {round(money,2)} €\n")

        # check if money finished
        if money <= 0:
            print("You ran out of money!")
            print("Game Over!")
            print(f"The correct country was: {random_country_data[1]}")
            break

    else:
        print("Country not found in the database.\n")