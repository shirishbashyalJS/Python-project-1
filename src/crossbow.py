import random
from functions.databaseConnection import *

def crossbow():

    query = "SELECT * FROM Patterns WHERE difficulty_level = ?;"
    fetched_pattern = database_connection_for_fetching(query)

    random_pattern_data = random.choice(fetched_pattern)
    print (random_pattern_data[1])
    user_choice = int(input("what is the next value : "  ))

    if user_choice == random_pattern_data[2]:
        print("\nYou Got The Right Initial Velocity!")
        return True
    else:
        print("you are wrong")
        return False


