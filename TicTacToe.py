def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, choose your move (row and column 0-2):")
        try:
            row = int(input("Row: "))
            col = int(input("Col: "))
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers from 0 to 2.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
print("1  |  2   |  3")
print("-----------")
print("4  |  5   |  6")
print("-----------")
print("7  |  8   |  9")
print("Welcome to Tic Tac Toe!")
print("Player 1 is 'X' and Player 2 is 'O'.")
tic_tac_toe()
