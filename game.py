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
            print("❌ Enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("❌ Choose between 1 and 9.")
            continue

        index = move - 1

        if board[index] != " ":
            print("❌ Position already taken.")
            continue

        return index

def check_winner(player):
    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True

    return False

def check_draw():
    return " " not in board

current_player = "X"

while True:
    show_board()
    index = get_valid_move(current_player)
    board[index] = current_player

    if check_winner(current_player):
        show_board()
        print(f"🎉 Player {current_player} wins!")
        break

    if check_draw():
        show_board()
        print("🤝 It's a draw!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
