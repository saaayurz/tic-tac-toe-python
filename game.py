# Create empty board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Display the board
print("Tic Tac Toe Board:")
print(board[0] + " | " + board[1] + " | " + board[2])
print("--+---+--")
print(board[3] + " | " + board[4] + " | " + board[5])
print("--+---+--")
print(board[6] + " | " + board[7] + " | " + board[8])

# Ask player for a move
position = input("Enter a position (1-9): ")

# Convert input to number and adjust index
index = int(position) - 1

# Place X on the board
board[index] = "X"

# Show updated board
print("\nUpdated Board:")
print(board[0] + " | " + board[1] + " | " + board[2])
print("--+---+--")
print(board[3] + " | " + board[4] + " | " + board[5])
print("--+---+--")
print(board[6] + " | " + board[7] + " | " + board[8])
