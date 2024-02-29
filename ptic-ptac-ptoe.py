# import random number module
import random

# define the shape of the board
board_width = 3
board_height = 3

# create playing board with separators
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < board_height - 1: 
            print("-" * (board_width * 3 - 1))


def check_winner(board, player):
    # check for horizontal win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # check for vertical win
    for col in range(board_width):  
        if all(board[row][col] == player for row in range(board_height)): 
            return True

    # check for diagonal win
    if all(board[i][i] == player for i in range(board_height)) or all(
        board[i][board_width - 1 - i] == player for i in range(board_height)
    ):  
        return True

    # if none of those are true then return false for a winner
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_player_move(board):
    while True:
        try:
            player_input = int(input(
                "\nEnter your move (1-9): "))
            if player_input < 1 or player_input > board_width * board_height:
                print("Ope! That number doesn't work! Enter a number between 1 and", board_width * board_height)
                continue

            # Convert player input to row and column indices
            row = (player_input - 1) // board_width
            col = (player_input - 1) % board_width

            # if place on board is taken, send error message
            if board[row][col] != " ":
                print("Oops, that spot already has a mark in it.")
                continue

            return row, col
        except ValueError:
            print("Ope! That's not a valid number! Enter a number between 1 and", board_width * board_height)


def computer_move(board):
    empty_cells = [(i, j) for i in range(board_height) for j in range(board_width) if board[i][j] == " "]  
    return random.choice(empty_cells)


def play_again():
    while True:
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


def main():
    while True:
        # define what board looks like and what player symbols are
        board = [[" " for _ in range(board_width)] for _ in range(board_height)]  # Updated to use board_height and board_width variables
        player_symbol = "X"
        computer_symbol = "O"

        print("Welcome to Ptic-Ptac-Ptoe!\nYou're X. Good luck!\n")
        print_board(board)

        while True:
            player_row, player_col = get_player_move(board)
            board[player_row][player_col] = player_symbol
            print("\nYour move:")
            print_board(board)

            if check_winner(board, player_symbol):
                print("Hooray! You win!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

            row, col = computer_move(board)
            board[row][col] = computer_symbol
            print("\nComputer's move:")
            print_board(board)

            if check_winner(board, computer_symbol):
                print("The computer wins!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
