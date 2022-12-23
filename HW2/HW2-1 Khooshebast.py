# make a game for guess the random number that pc generate
# repeat this code untill user enter correct number
# use while_True
# this code will show how many times did you try

import random

pc_number = random.randint(0, 20)
count = 0

while True:
    user_number = int(input('Enter number: '))

    if pc_number == user_number:
        print("Barande Shodi")
        count = count+1
        print("you tried for", count, "times")
        break

    elif pc_number > user_number:
        print("Boro Balatar")
        count = count+1

    elif pc_number < user_number:
        print("Boro Paiintar")
        count = count+1