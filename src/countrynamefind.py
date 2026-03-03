
import random
from functions.databaseConnection import *


def countryNameGuess():
    def getAttempts(length):
        if (game_level == "easy"):
            return length + 2
        if (game_level == "medium"):
            return length 
        if (game_level == "hard"):
            return length - 2


    def printPattern(random_country_name, user_guessed_letters):
        print("\n\t", end = "")
        for letter in random_country_name:
            if letter not in user_guessed_letters:
                print(" _ ", end="")
            else:
                print(f" {letter} ", end="")
        print("\n")


    query = "SELECT name FROM countries;"
    fetched_countries = database_connection_for_fetching(query)


    # Pick random target country
    random_country_name = random.choice(fetched_countries)[0].upper()




    country_name_sets= set(random_country_name)

    country_set_length = len(country_name_sets)

    attempts = getAttempts(country_set_length)


    print("\tGuess the country: ")

    user_guessed_letters = []

    printPattern(random_country_name, user_guessed_letters)


    while True:
        if attempts:
            guess = input((f"Guess the Letters (Remainig Attempts: {attempts}): ")).upper()
            if guess in country_name_sets:
                user_guessed_letters.append(guess)
            
            else:
                attempts -= 1
            
            printPattern(random_country_name, user_guessed_letters)

            if country_name_sets.issubset(set(user_guessed_letters)):
                print("You successfully decrepted the treasure!")
                return True
        else:
            return False