
# main.py
from src.countryFind import country_find
from src.crossbow import crossbow
from src.countrynamefind import countryNameGuess
from functions.smoothPrinting import smooth_printing,smooth_word_printing

def start_game():

    smooth_printing("--- Let's Go To Find The Treasure Located Country ---", delay=0.05)
    
    if country_find():
        smooth_printing("\n--- You Find The Country Where Treasure Is Located! ---\n",delay=0.05)
        if crossbow():
            smooth_printing("\n--- Level 2 Complete! Final Challenge... ---\n",delay=0.05)
            if countryNameGuess():
                smooth_printing("\nCONGRATULATIONS! You have won the whole game! 🏆",delay=0.05)
            else:
                smooth_printing("\nSo close! You failed at the final hurdle.",delay=0.05)
        else:
            smooth_printing("\nGame Over at the Crossbow challenge.",delay=0.05)
    else:
        smooth_printing("\nBetter luck next time. Thank you for participating!",delay=0.05)
        


if __name__ == "__main__":
    start_game()