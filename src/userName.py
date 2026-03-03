

character_name = input("Enter Your Name To Start: ")

game_level_num = int(input("Which mode you want to play on: (\n 1 for Easy \n 2 for Medium \n 3 for Hard \n) \n Enter Level = "))

game_level = ""
if (game_level_num == 1):
    game_level = "easy"
elif (game_level_num == 2):
    game_level = "medium"
else:
    game_level = "hard"


print(f"Hello {character_name}, let's get started! ")






