import sys

# --- Game Board Dimensions --- #
ROWS = 6
COLUMNS = 7

# --- Board Initialization --- #
def create_board():
    """
    Initializes an empty Connect Four board.
    ' ' represents an empty slot.
    """
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    return board

# --- Displaying the Board --- #
def print_board(board):
    """
    Prints the current state of the game board to the console.
    Displays column numbers 1-7 at the bottom.
    """
    # Print from top row down (ROW-1 to 0) to visualize correctly
    for r in range(ROWS - 1, -1, -1):
        for c in range(COLUMNS):
            print(f'| {board[r][c]} ', end='')
        print('|')
    print('-----------------------------') # Separator line
    print('  1   2   3   4   5   6   7  ') # Column numbers for player input

# --- Dropping a Piece --- #
def 
