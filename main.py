
# main.py

from src.countryFind import country_find

from src.crossbow import crossbow

from src.countrynamefind import countryNameGuess

# For Text Animation
from functions.smoothPrinting import smooth_printing,smooth_word_printing


def start_game():

    smooth_printing("--- Let's Go To Find The Treasure Located Country ---", delay=0.05)
    
    if country_find():
        smooth_printing("\n--- You Find The Country Where Treasure Is Located! ---\n",delay=0.05)
        if crossbow():
            smooth_printing("\n--- The Treasure Has been Dropped From The Roof... ---\n",delay=0.05)
            smooth_printing("\n--- The Treasure Is Encrepted, There Is Something On The Map ---\n",delay=0.05)
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