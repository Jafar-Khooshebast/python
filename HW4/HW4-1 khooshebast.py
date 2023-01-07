import pyfiglet
count = 0

def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print() 

def check_game1():
    announcement1 = pyfiglet.figlet_format("Player 1  is  Winner", font = "slant")

    if( game_board[0][0]==" X " and game_board[0][1]==" X " and game_board[0][2]==" X "):
        print (announcement1)

    elif(game_board[1][0]==" X " and game_board[1][1]==" X " and game_board[1][2]==" X "):
        print (announcement1)

    elif(game_board[2][0]==" X " and game_board[2][1]==" X " and game_board[2][2]==" X "):
        print (announcement1)

    elif(game_board[2][0]==" X " and game_board[1][1]==" X " and game_board[0][2]==" X "):
        print (announcement1)

    elif(game_board[0][0]==" X " and game_board[1][1]==" X " and game_board[2][2]==" X "):
        print (announcement1)

    elif(game_board[0][0]==" X " and game_board[1][0]==" X " and game_board[2][0]==" X "):
        print (announcement1)

    elif(game_board[0][1]==" X " and game_board[1][1]==" X " and game_board[2][1]==" X "):
        print (announcement1)

    elif(game_board[0][2]==" X " and game_board[1][2]==" X " and game_board[2][2]==" X "):
        print (announcement1)



def check_game2():
    announcement2 = pyfiglet.figlet_format("Player 2  is  Winner", font = "slant")

    if( game_board[0][0]==" O " and game_board[0][1]==" O " and game_board[0][2]==" O "):
        print (announcement2)

    elif(game_board[1][0]==" O " and game_board[1][1]==" O " and game_board[1][2]==" O "):
        print (announcement2)

    elif(game_board[2][0]==" O " and game_board[2][1]==" O " and game_board[2][2]==" O "):
        print (announcement2)

    elif(game_board[2][0]==" O " and game_board[1][1]==" O " and game_board[0][2]==" O "):
        print (announcement2)

    elif(game_board[0][0]==" O " and game_board[1][1]==" O " and game_board[2][2]==" O "):
        print (announcement2)

    elif(game_board[0][0]==" O " and game_board[1][0]==" O " and game_board[2][0]==" O "):
        print (announcement2)

    elif(game_board[0][1]==" O " and game_board[1][1]==" O " and game_board[2][1]==" O "):
        print (announcement2)

    elif(game_board[0][2]==" O " and game_board[1][2]==" O " and game_board[2][2]==" O "):
        print (announcement2)
      

game = pyfiglet.figlet_format("Tic Tac Toe", font = "digital")
print (game)

game_board = [[" - ", " - ", " - "],
               [" - ", " - ", " - "],
               [" - ", " - ", " - "]] 

show()

while True :

    print("player 1")
    while True:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        if 0 <= row <=2 and 0 <= col <= 2 :
        
            if game_board[row][col] == " - ":
                game_board[row][col] =" X "
                count = count +1
                show()
                break
            else:
                print("Select an other Cell. This Cell isn't Empty")
        else:
            print("row and col Limitation Eror. it must be between 0 and 2")

        check_game1()
   


    print ("player2")
    while True:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        if 0 <= row <=2 and 0 <= col <= 2 :        
            if game_board[row][col] == " - ":
                game_board[row][col] =" O "
                count = count +1
                show()
                break
            else:
                print("Select an other Cell. This Cell isn't Empty") 
        else:
            print("row and col Limitation Eror. it must be between 0 and 2")

        check_game2()
    
