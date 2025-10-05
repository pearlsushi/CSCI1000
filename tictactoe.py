def printBoard(board):
    for p in range(3):
        print(board[p])

def reset(board):
    board.clear()
    for x in range(3):
        temp = []
        for z in range(3):
            temp.append("_")
        board.append(temp)
    return board



running = True
tie = 0
player = "x"
b = [] 
for x in range(3):
    temp = []
    for z in range(3):
        temp.append(" ")
    b.append(temp)

while running == True:
    printBoard(b)
    while True:
        row = int(input("Enter a row (1-3): \n"))
        column = int(input("Enter a column (1-3): \n"))
        if row < 4 and row > 0 and column < 4 and column > 0:
            if b[row-1][column-1] == " ":
                b[row-1][column-1] = player
                tie+=1
                False
                break
            else:
                print("Try again")
                True
        else:
            print("Row or Column selection is out of range. Pick Again.")
            True

    for s in range(3):
        if b[s][0] == player and b[s][1] == player and b[s][2] == player:
            printBoard(b)
            print("Player:", player, " wins!")
            running = False
            x = input("Would you like to play again?\n")
            if x.lower() == "yes":
                running = True
                reset(b)
        if b[0][s] == player and b[1][s] == player and b[2][s] == player:
            printBoard(b)
            print("Player: ", player, " wins!") 
            running = False
            x = input("Would you like to play again?\n")
            if x.lower() == "yes":
                running = True
                reset(b)
    if b[0][0] == player and b [1][1] == player and b[2][2] == player:
        printBoard(b)
        print("Player:", player, " wins!")
        running = False
        x = input("Would you like to play again?\n")
        if x.lower() == "yes":
            running = True
            reset(b)
    if b[2][0] == player and b[1][1] == player and b[2][0] == player:
        printBoard(b)
        print("Player:", player, " wins!")
        running = False
        x = input("Would you like to play again?\n")
        if x.lower() == "yes":
            running = True
            reset(b)
    if tie == 9:
        printBoard(b)
        print("Game Over. It is a tie")
        running = False
        x = input("Would you like to play again?\n")
        if x.lower() == "yes":
            running = True
            reset(b)

    if player == "x":
        player = "o"
    elif player == "o":
        player = "x"