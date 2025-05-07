#!/usr/bin/python3
"""
Simple command‑line Tic‑Tac‑Toe.
"""

def print_board(board):
    """Display the 3 × 3 board nicely."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i != 2:
            print("-" * 9)


def check_winner(board):
    """
    Return "X" or "O" if that player has three in a row,
    or None otherwise.
    """
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def board_full(board):
    """True if there are no empty spaces left."""
    return all(cell != " " for row in board for cell in row)


def get_coord(prompt):
    """Prompt until the user enters 0, 1, or 2."""
    while True:
        try:
            val = int(input(prompt))
            if val in (0, 1, 2):
                return val
            print("Please enter 0, 1 or 2.")
        except ValueError:
            print("Not a number. Try again.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current = "X"

    while True:
        print_board(board)
        print(f"Player {current}'s turn.")
        row = get_coord("  Row (0, 1, 2): ")
        col = get_coord("  Col (0, 1, 2): ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        board[row][col] = current

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # switch player
        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
