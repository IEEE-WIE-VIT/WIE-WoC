# X-O Game
flag = False
print("Enter the row number followed by the column number, separated by a space")
print("Player1 : X \nPlayer2 : O")
Game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]


def check(game):
    # Vertical Check
    for counter in range(3):
        if game[0][counter] == "X" and game[1][counter] == "X" and game[2][counter] == "X":
            return True
        elif game[0][counter] == "O" and game[1][counter] == "O" and game[2][counter] == "O":
            return True
    # Horizontal check
    for counter in range(3):
        if game[counter][0] == "X" and game[counter][1] == "X" and game[counter][2] == "X":
            return True
        elif game[counter][0] == "O" and game[counter][1] == "O" and game[counter][2] == "O":
            return True
    # diagonal check
    if game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
        return True
    elif game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O":
        return True
    return False


def printer(game):
    for row_counter in range(3):
        for column_counter in range(3):
            print(game[row_counter][column_counter], end=" ")
        print()
    return


def player1():
    temp = input("Player1, your move : ").split()
    row = int(temp[0]) - 1
    column = int(temp[1]) - 1
    if Game[row][column] == "O":
        print("Invalid Input, There is already an O at that position")
        player1()
    elif Game[row][column] == "X":
        print("Invalid Input, There is already a X at that position")
        player1()
    Game[row][column] = "X"
    # counting += 1
    printer(Game)
    flag = check(Game)
    if flag:
        print("Player1 WINS!!!")
        return
    fl_ag = False
    for row_counter in range(3):
        for column_counter in range(3):
            if Game[row_counter][column_counter] == "_":
                fl_ag = True
                break
    if not fl_ag:
        print("Draw Match")
        return
    if not flag:
        player2()


def player2():
    temp = input("Player2, your move : ").split()
    row = int(temp[0]) - 1
    column = int(temp[1]) - 1
    if Game[row][column] == "X":
        print("Invalid Input, There is already a X at that position")
        player2()
    elif Game[row][column] == "O":
        print("Invalid Input, There is already a O at that position")
        player2()
    Game[row][column] = "O"
    printer(Game)
    flag = check(Game)
    if flag:
        print("Player2 WINS!!!")
        return
    else:
        player1()


player1()
