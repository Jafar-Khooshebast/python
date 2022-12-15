# Dise game
# make a random number between 1 to 6
# if number = 6, you can do it again

import random

dise = random.randint(1, 6)
prize_dise = random.randint(1, 6)
while True:
    if dise != 6:
        print("Dise number= ", dise)
        break

    elif dise == 6:
        print("Dise number= ", dise)
        print("You win. as your prize you can dise again ")
        print("second Dise number= ", prize_dise)
        break