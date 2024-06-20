from random import randint


def printBoard(board):
    index = 0
    p = ""

    for i in range(5):
        for j in range(5):
            if i % 2 == 1:
                p += "---"
            else:
                if j % 2 == 1:
                    p += " | "
                else:
                    p += f" {board[index]} "
                    index += 1
        p += "\n"

    print(p)


def checkIfWon(board):
    if board[0] == board[1] == board[2] == "o" or board[3] == board[4] == board[5] == "o" or board[6] == board[7] == \
            board[8] == "o" or board[0] == board[3] == board[6] == "o" or board[1] == board[4] == board[7] == "o" \
            or board[2] == board[5] == board[8] == "o" or board[0] == board[4] == board[8] == "o" or board[2] == \
            board[4] == board[6] == "o":

        print("Winner is 'o'")
        printBoard(board)
        quit(1123)

    elif board[0] == board[1] == board[2] == "x" or board[3] == board[4] == board[5] == "x" or board[6] == board[7] ==\
            board[8] == "x" or board[0] == board[3] == board[6] == "x" or board[1] == board[4] == board[7] == "x" or \
            board[2] == board[5] == board[8] == "x" or board[0] == board[4] == board[8] == "x" or board[2] == board[4] \
            == board[6] == "x":

        print("Winner is 'x'")
        printBoard(board)
        quit(5813)

    else:
        draw = False
        for i in range(9):
            if board[i] == i+1:
                draw = False
                break
            else:
                draw = True
        if draw:
            print("Draw")
            printBoard(board)
            quit(2134)


def multiplayer(board):
    printBoard(board)
    symbol = "o"

    while True:
        ind = input(f"{symbol} Insert 1-9: ")
        ok = False
        try:
            ind = int(ind)
            for i in range(len(board)):
                if ind == board[i]:
                    board[i] = symbol
                    ok = True
                    break
            if ok:
                checkIfWon(board)
                if symbol == "o":
                    symbol = "x"
                else:
                    symbol = "o"
            else:
                print("Incorrect value")
        except ValueError:
            print(":(")

        printBoard(board)


def singleplayer(board):
    print("In progress")


# main
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    mode = input("1-single player; 2-two players; 3-quit:\n> ")

    try:
        mode = int(mode)
        if mode == 1:
            singleplayer(board)
        elif mode == 2:
            multiplayer(board)
        elif mode == 3:
            quit(0)
        else:
            print("Incorrect value")
    except ValueError:
        print("Insert '1' or '2'")
