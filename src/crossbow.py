import random
from functions.databaseConnection import *
from functions.smoothPrinting import smooth_printing,smooth_word_printing

# Second Part of the game to throw the crossbow and User need to guess the initial velocity for that


def crossbow():

    # Setting up the query for fetching the data
    query = "SELECT * FROM Patterns WHERE difficulty_level = ?;"

    # Call the database function for fetching the data and stored in the variable
    fetched_pattern = database_connection_for_fetching(query)

    smooth_word_printing("  Hey, Treasure Is On The Roof Of The Temple! ", delay=0.1)
    smooth_word_printing("  You Have An Arrow To Throw To Drop It Down, You Have Only One Attempt! ", delay=0.1)
    smooth_word_printing("  Oh! 😮, There Is A Pattern In The Map, ", delay=0.1)

    # store the randomly selected pattern on a variable
    random_pattern_data = random.choice(fetched_pattern)

    print ("Pattern :",random_pattern_data[1])
    
    # Get the velocity thought by user
    user_choice = int(input("\nWhat Is The Initial Velocity : "  ))

    # If user thought velocity equals to random pattern 2 nd index data
    if user_choice == random_pattern_data[2]:
        smooth_printing("\nYou Got The Right Initial Velocity!",0.09)
        return True
    else:
        print("You are wrong!")
        return False


