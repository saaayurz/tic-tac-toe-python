# Create empty board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Function to display board
def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Show empty board
show_board()

# Player X move
x_pos = int(input("Player X, enter position (1-9): ")) - 1
board[x_pos] = "X"
show_board()

# Player O move
o_pos = int(input("Player O, enter position (1-9): ")) - 1
board[o_pos] = "O"
show_board()
