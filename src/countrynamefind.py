
import random
from functions.databaseConnection import *
from functions.smoothPrinting import smooth_printing,smooth_word_printing

# Third phase of the game for country name guessing

def countryNameGuess():
    # Get the number of attempts users can try to guess the letter according to selected level
    def getAttempts(length):
        if (game_level == "easy"):
            return length + 2
        if (game_level == "medium"):
            return length 
        if (game_level == "hard"):
            return length - 2

    # Print the pattern on the terminal like " _ " if letter is not guessed and " A " if A is guessed
    def printPattern(random_country_name, user_guessed_letters):
        print("\n\t", end = "")
        for letter in random_country_name:
            if letter not in user_guessed_letters:
                print(" _ ", end="")
            else:
                print(f" {letter} ", end="")
        print("\n")


    # Set the query to fetch the data
    query = "SELECT name FROM countries;"
    # Fetch the data from database by calling the fetching function
    fetched_countries = database_connection_for_fetching(query)


    # Pick random target country
    random_country_name = random.choice(fetched_countries)[0].upper()



    # Convert the randomly choosed country to set for making the letters unique helps for compairing the letters of user choosed with it
    country_name_sets= set(random_country_name)

    # Getting the country set length
    country_set_length = len(country_name_sets)

    # Get the attempts as returned from the getAttempts function according to game level
    attempts = getAttempts(country_set_length)


    smooth_word_printing("\t'_' is the placeholder for each country letter. Guess the country's Letters: ", delay=0.3)

    # Setting the user guessed letter as empty array initially
    user_guessed_letters = []

    printPattern(random_country_name, user_guessed_letters)

    # Run the program until user gussed all the letter or chances are finnished

    while True:

        # If any attempts
        if attempts:
            guess = input((f"Guess the Letters (Remainig Attempts: {attempts}): ")).upper()

            # Checks if the guess exist in the country name set
            if guess in country_name_sets:
                # if exist then add the letter to guessed letter by user
                user_guessed_letters.append(guess)
            
            else:
                # if doesnot exist, attempts decrease
                attempts -= 1
            
            printPattern(random_country_name, user_guessed_letters)

            # If all the element of country name set is in user guessed array's set then,
            if country_name_sets.issubset(set(user_guessed_letters)):
                print("You successfully decrepted the treasure!")
                return True
        else:
            return False