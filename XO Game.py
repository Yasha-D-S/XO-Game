def createboard():
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def printboard(board):
    rows = len(board)
    print("|___|___|___|")
    for r in range(rows):
        print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
        print("|___|___|___|")
    return board

def selectsymbol():
    sym1 = input("Player 1, do you want to be X or O? ")
    if sym1 == "X":
        sym2 = "O"
        print("Player 2, you are O. ")
    else:
        sym2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return (sym1, sym2)


def startGame(board, sym1, sym2, count):
    if count % 2 == 0:
        player = sym1
    elif count % 2 == 1:
        player = sym2

    print("Player " + player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    # out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        print("Out of boarder. Pick another one. ")
        row = int(input("Pick a row:"
                        "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    # filled
    while (board[row][column] == sym1) or (board[row][column] == sym2):
        print("The square you picked is already filled. Pick another one.")
        row = int(input("Pick a row:"
                        "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))


    if player == sym1:
        board[row][column] = sym1

    else:
        board[row][column] = sym2

    return board


def checkwinner(board, sym1, sym2):
    winner = True
    #rows
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == sym1:
            winner = False
            print("Player " + sym1 + " won!")

        elif board[row][0] == board[row][1] == board[row][2] == sym2:
            winner = False
            print("Player " + sym2 + " won!")

    #columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == sym1:
            winner = False
            print("Player " + sym1 + " won!")
        elif board[0][col] == board[1][col] == board[2][col] == sym2:
            winner = False
            print("Player " + sym2 + " won!")

    # diagnoals
    if board[0][0] == board[1][1] == board[2][2] == sym1:
        winner = False
        print("Player " + sym1 + " won!")

    elif board[0][0] == board[1][1] == board[2][2] == sym2:
        winner = False
        print("Player " + sym2 + " won!")

    elif board[0][2] == board[1][1] == board[2][0] == sym1:
        winner = False
        print("Player " + sym1 + " won!")

    elif board[0][2] == board[1][1] == board[2][0] == sym2:
        winner = False
        print("Player " + sym2 + " won!")

    return winner

def full(board, sym1, sym2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        startGame(board, sym1, sym2, count)
        printboard(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner:
                print("There is a tie. ")

        winner = checkwinner(board, sym1, sym2)
        count += 1

    if not winner:
        print("Game over.")

def main():
    board = createboard()
    printboard(board)
    sym1, sym2 = selectsymbol()
    full(board, sym1, sym2)

main()
