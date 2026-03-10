
# main.py

# Import The First Part Of The Game To Find The Country Where Treasure Is Located
from src.countryFind import country_find

# Import The Second Part To Find Velocity
from src.crossbow import crossbow

# Import The Third Part To Decript The Treasure
from src.countrynamefind import countryNameGuess

# For Text Animation
# smooth_printing Function accepts 2 parameter and First One Is Text and another is Delay
from functions.smoothPrinting import smooth_printing,smooth_word_printing


def start_game():

    smooth_printing("--- Let's Go To Find The Treasure Located Country ---", delay=0.05)
    
    if country_find():
        # If They Pass Country Finding Task
        smooth_printing("\n--- You Find The Country Where Treasure Is Located! ---\n",delay=0.05)
        
        if crossbow():
            # If they pass Crossbow
            smooth_printing("\n--- The Treasure Has been Dropped From The Roof... ---\n",delay=0.05)
            smooth_printing("\n--- The Treasure Is Encrepted, There Is Something On The Map ---\n",delay=0.05)
            if countryNameGuess():
                # If they pass the final challange of Guessing Letter
                smooth_printing("\nCONGRATULATIONS! You have won the whole game! 🏆",delay=0.05)
            else:
                smooth_printing("\nSo close! You failed at the final hurdle.",delay=0.05)
        else:
            smooth_printing("\nGame Over at the Crossbow challenge.",delay=0.05)
    else:
        smooth_printing("\nBetter luck next time. Thank you for participating!",delay=0.05)
        


# First Execute the Main Function
if __name__ == "__main__":
    start_game()