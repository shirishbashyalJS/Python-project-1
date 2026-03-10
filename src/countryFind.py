import random
from geopy.distance import geodesic
from functions.databaseConnection import *
from functions.smoothPrinting import smooth_printing,smooth_word_printing




def country_find():

    # Default starting location (Finland)
    temp_location = {
        "name": "Finland",
        "latitude": 61.924110,
        "longitude": 25.748151
    }

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

    def getMoney():
        if game_level == "easy":
            return 65000
        elif game_level == "medium":
            return 55000
        else:
            return 45000


    # Main Program
    
    # Maria DB Query has been stored in query variable as string
    query = "SELECT * FROM countries;"
    
    #Fetching data from database
    fetched_data = database_connection_for_fetching(query)


    # Show player's starting country

    print(f"You are currently in: {temp_location['name']}\n")

    # Player Money System
    money = getMoney()
    cost_per_km = 1

    smooth_printing(f"You have total {money} €", delay=0.1)

    # Show all available travelable countries
    smooth_printing("You can travel to the following countries:\n", 0.05)
    print("\n\t\t\t-------------------------------------------------")
    for country in fetched_data:
        smooth_word_printing(f"-> {country[1]}", 0.1, escape=False)

    print("\n\t\t\t-------------------------------------------------")

    # Pick random target country
    random_country_data = random.choice(fetched_data)

    # Show hint
    smooth_word_printing(f"\nHint for the country in map is: {random_country_data[5]}\n", delay=0.4)

    # Game Loop
    # Game Loop
    while True:
        print(f"\nCurrent Location: {temp_location['name']}")
        print(f"Money Left: {round(money, 2)} €")

        user_thought_country = input("Guess the country name: ").lower()
        new_loc = updating_location(user_thought_country, fetched_data)

        if new_loc is not None:
<<<<<<< HEAD
            # 1. Capture OLD coordinates, where the player is right now
            current_coords = (temp_location["latitude"], temp_location["longitude"])
            
            # 2. Capture NEW coordinates, where the player wants to go
=======
            # 1. Capture OLD coordinates (where the player is right now)
            current_coords = (temp_location["latitude"], temp_location["longitude"])
            
            # 2. Capture NEW coordinates (where the player wants to go)
>>>>>>> a1474feab29cc438fe0d15a499dbd7f4874c02db
            destination_coords = (new_loc["latitude"], new_loc["longitude"])

            # 3. Calculate distance from CURRENT to DESTINATION
            distance = geodesic(current_coords, destination_coords).km
            distance = round(distance, 2)

            # 4. Deduct money for this trip
            travel_cost = distance * cost_per_km
            money -= travel_cost

            # 5. Update the current location to the new country
            temp_location = new_loc

            print(f"You travelled {distance} km to {temp_location['name']}")
            print(f"Travel Cost: {round(travel_cost, 2)} €")

            # Check if money ran out after the flight
            if money <= 0:
                smooth_printing("You ran out of money during the flight!", delay=0.05)
                print(f"The correct country was: {random_country_data[1]}")
                return False

            # Check if this new location is the target
            if user_thought_country == random_country_data[1].lower():
                smooth_printing("\nCongratulations! You reached the correct country!", 0.05)
                print(f"Final Money Left: {round(money, 2)} €")
                return True
            else:
                print("Not the target country! Keep looking.")

        else:
            print("Country not found in the database. Try again.\n")