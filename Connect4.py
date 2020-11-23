from termcolor import colored
from random import randint
from time import sleep

board = []
players = {
    1: colored("O", "red"),
    2: "O",
}
full_columns = set()
columns = "1234567"

for i in range(6):
    board.append([" "] * 7)

def DrawBoard(board):
    print(colored(" | ", "blue").join(columns))
    print(colored("--------------------------", "blue"))
    for i in range(6):
        print(colored(" | ", "blue").join(board[i]))
        print(colored("--------------------------", "blue"))
    print()

def ChosingMove():
    while True:
        try:
            next_move = int(input("Choose a column: "))
            if 1 <= next_move <= 7 and next_move not in full_columns:
                break
        except:
            continue
    return next_move

def ColumnChecking(move):
    i = 5
    next_move = move
    while board[i][next_move - 1] in [colored("O", "red"), "O"]:
        i -= 1
        if i < 0:
            print("This column is full!")
            full_columns.add(next_move)
            next_move = ChosingMove()
            ColumnChecking(next_move)
    return i, next_move

def CheckWin(board):
    for i in range(3):  # Checking rows
        for j in range(7):
            if board[i][j] not in [colored("O", "red"), "O"]:
                continue
            if (board[i][j] == board[i+1][j] and
                    board[i+1][j] == board[i+2][j] and
                    board[i+2][j] == board[i+3][j]):
                print(f"Winner is {board[i][j]} with row")
                return True

    for i in range(6):  # Checking for columns
        for j in range(4):
            if board[i][j] not in [colored("O", "red"), "O"]:
                continue
            if (board[i][j] == board[i][j+1] and
                    board[i][j+1] == board[i][j+2] and
                    board[i][j+2] == board[i][j+3]):
                print(f"Winner is {board[i][j]} with column")
                return True

    for i in range(3):  # Checking for main diagonals
        for j in range(4):
            if board[i][j] not in [colored("O", "red"), "O"]:
                continue
            if (board[i][j] == board[i+1][j+1] and
                    board[i+1][j+1] == board[i+2][j+2] and
                    board[i+2][j+2] == board[i+3][j+3]):
                print(f"Winner is {board[i][j]} with main diagonal")
                return True

    for i in range(3, 6):  # Checking for side diagonals
        for j in range(4):
            if board[i][j] not in [colored("O", "red"), "O"]:
                continue
            if (board[i][j] == board[i-1][j+1] and
                    board[i-1][j+1] == board[i-2][j+2] and
                    board[i-2][j+2] == board[i-3][j+3]):
                print(f"Winner is {board[i][j]} with side diagonal")
                return True
    k = 0
    for i in range(6):  # Checking for pat
        for j in range(7):
            if board[i][j] in [colored("O", "red"), "O"]:
                k += 1
    if k == 42:
        print("Pat")
        return True
    return False

DrawBoard(board)
player = 1
while True:
    print(f"Now turn of {players[player]}\n")
    i, move = ColumnChecking(ChosingMove())
    if player == 1:
        board[i][move - 1] = colored("O", "red")
        player = 2
    else:
        board[i][move - 1] = "O"
        player = 1
    DrawBoard(board)
    if CheckWin(board):
        break
