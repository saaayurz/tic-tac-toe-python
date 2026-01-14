board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def get_valid_move(player):
    while True:
        move = input(f"Player {player}, enter position (1-9): ")

        if not move.isdigit():
            print("❌ Please enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("❌ Number must be between 1 and 9.")
            continue

        index = move - 1

        if board[index] != " ":
            print("❌ That position is already taken.")
            continue

        return index

# Show empty board
show_board()

# Player X move
x_index = get_valid_move("X")
board[x_index] = "X"
show_board()

# Player O move
o_index = get_valid_move("O")
board[o_index] = "O"
show_board()
