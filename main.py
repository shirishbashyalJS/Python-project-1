
# main.py
from src.countryFind import country_find
from src.crossbow import crossbow
from src.countrynamefind import countryNameGuess
from functions.smoothPrinting import smooth_printing

def start_game():
    smooth_printing("--- WELCOME TO THE ADVENTURE ---")

    
    if country_find():
        print("\n--- Level 1 Complete! Moving to Level 2 ---\n")
        if crossbow():
            print("\n--- Level 2 Complete! Final Challenge... ---\n")
            if countryNameGuess():
                print("\nCONGRATULATIONS! You have won the whole game! 🏆")
            else:
                print("\nSo close! You failed at the final hurdle.")
        else:
            print("\nGame Over at the Crossbow challenge.")
    else:
        print("\nBetter luck next time. Thank you for participating!")
        


if __name__ == "__main__":
    start_game()