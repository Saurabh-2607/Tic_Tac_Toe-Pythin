board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    while True:
        try:
            choice = int(input("Enter your move(1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Please enter a number between 1 and 9.")
                continue
            if board[choice-1] == " ":
                board[choice-1] = icon
                break
            else:
                print("That space is taken!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def is_victory(icon):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == icon for i in condition):
            return True
    return False

def is_draw():
    return " " not in board

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
