from functions.smoothPrinting import smooth_printing,smooth_word_printing
from src.story import story, question

# This section will ask for the username and level of the game

# Print the Story
smooth_printing(story,delay=0.03)
smooth_printing(question,delay=0.1)

print("\n\n")


smooth_printing("\t -------------  WELCOME TO AEROHUNT  ---------------", delay=0.05)

character_name = input("Enter Your Name To Start: ")

game_level_num = (input("Which mode you want to play on: (\n 1 for Easy \n 2 for Medium \n 3 for Hard \n) \n Enter Level = "))
try:
    game_level_num = int(game_level_num)
except ValueError:
    smooth_word_printing("You Can Only Enter Corresponding Number. Starting The Default Hard Mode! ", 0.05)
game_level = ""
if (game_level_num == 1):
    game_level = "easy"
elif (game_level_num == 2):
    game_level = "medium"
else:
    game_level = "hard"

print("\t\t\t-----------------------------------------------")

smooth_word_printing(f"Hello {character_name}, let's get started! ", 0.05)






