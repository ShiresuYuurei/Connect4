from termcolor import colored

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

def DrawBoard(board):
    for i in range(3):
        print(colored(" | ", "blue").join(board[i]))
        if i != 2:
            print(colored("---------", "blue"))
    print()

def CheckWinner(board):
    k = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] in "123456789":
                return False
            else:
                k += 1
    if k == 9:
        print("Pat")
        return True
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):  # Checking main diagonal
        print(f"Winner is {board[0][0]}")
        return True
    elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):  # Checking side diagonal
        print(f"Winner is {board[0][2]}")
        return True
    else:
        for k in range(3):
            if (board[k][0] == board[k][1]) and (board[k][1] == board[k][2]):  # Checking rows
                print(f"Winner is {board[k][0]}")
                return True
            elif (board[0][k] == board[1][k]) and (board[1][k] == board[2][k]):  # Checking Columns
                print(f"Winner is {board[0][k]}")
                return True
    return False

player = 1
DrawBoard(board)
while True:
    while True:
        try:
            move = int(input("Choose a cell: "))
            if 1 <= move <= 9:
                break
        except ValueError:
            print("Enter a number!")
            continue

    while board[(move - 1) // 3][move % 3 - 1] in [colored("X", "red", attrs=["bold"]),
                                                   colored("O", "green", attrs=["bold"])]:
        move = int(input("This cell already occupied, please enter another: "))
    if player == 1:
        board[(move - 1) // 3][move % 3 - 1] = colored("X", "red", attrs=["bold"])
        player = 2
    else:
        board[(move - 1) // 3][move % 3 - 1] = colored("O", "green", attrs=["bold"])
        player = 1
    DrawBoard(board)
    if CheckWinner(board):
        break
