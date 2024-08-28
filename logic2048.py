import random

def start_game():
    """Function to initialize the 2048 game and board grid as a list of lists.
    
    Returns the initial game board with a 2 in a random cell.
    """

    # initialize the game board
    board = []

    for r in range(4):
        board.append([0] * 4)

    # print the controls for the user
    print("""\n   GAME CONTROLS:
        "W": Move Up
        "S": Move Down
        "A": Move Left
        "D": Move Right\n""")
    
    # call function to add the initial 2 in the grid
    add_new_2(board)

    # print the initial board
    for r in range(4):
        print(board[r])
    
    # return the game board grid
    return board

def add_new_2(board):
    """Function to add a new 2 in a random empty cell of the game board grid."""

    # choose a random grid cell
    r = random.randint(0,3)
    c = random.randint(0,3)

    # variable to track number of filled cells on board
    filled_cells = 0

    # if that cell is not empty, choose another until an empty cell is chosen
    while board[r][c] != 0: # check if board is full already, loop gets stuck otherwise
        filled_cells += 1
        if filled_cells == 16:
            return
        else:
            r = random.randint(0,3)
            c = random.randint(0,3)

    # place a 2 in that random empty cell
    board[r][c] = 2

def get_current_state(board):
    """Function to get the current state of the game.
    
    Returns str WIN, CONTINUE, or LOSS, depending on game state.
    """

    # check if any cell contains 2048 -- win condition
    for r in range(4):
        for c in range(4):
            if board[r][c] == 2048:
                return "WIN"
    
    # check if game board still contains empty cells -- game continues
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return "CONTINUE"
            
    # check if game board will contain empty cells after a move - game continues
    for r in range(3):
        for c in range(3):
            if board[r][c] == board[r+1][c] or board[r][c] == board[r][c+1]:
                return "CONTINUE"
            
    # else, user has lost the game
    return "LOSS"

def compress(board):

    # bool to track if a change occurred
    changed = False

    # new empty grid
    new_board = []
    for r in range(4):
        new_board.append([0] * 4)

    # shift each non-empty cell to the extreme left of the row
    for r in range(4):
        # variable to track leftmost empty cell in each row
        pos = 0

        for c in range(4):
            if board[r][c] != 0: # if cell is non-empty, shift its contents to the leftmost empty cell in that row
                new_board[r][pos] = board[r][c]

                if c != pos: # check if any cells actually moved, set flag and update leftmost empty cell
                    changed = True
                
                pos += 1

    # return new compressed game board and change flag
    return new_board, changed

def merge(board):
    """Function to merge two adjacent, non-empty cells in a row if they contain the same value.
    
    Only set up for left move. Combine merge() with reverse() and transpose() functions to make other moves possible.
    """
    changed = False
    for r in range(4):
        for c in range(3):
            # if current cell has same value as next cell in row
            # AND they are both not empty, cells will merge
            if board[r][c] == board[r][c+1] and board[r][c] != 0:
                board[r][c] *= 2
                board[r][c+1] = 0
                
                changed = True 

    return board, changed

def reverse(board):
    """Function to reverse the contents of each row.
    
    Use with merge() to perform a right move and with transpose() and merge() for a down move.
    """
    rev_board = []
    for r in range(4):
        rev_board.append([])
        for c in range(4):
            rev_board[r].append(board[r][3-c])
    return rev_board

def transpose(board):
    """Function to transpose the board (switch rows and columns).
    
    Use with merge() to perform an up move and with reverse() and merge() for a down move.
    """
    trans_board = []
    for r in range(4):
        trans_board.append([])
        for c in range(4):
            trans_board[r].append(board[c][r])
    return trans_board

def move_left(grid):
    """Function to update the game board if the user performs a left move."""
    # compress the grid
    new_grid, changed1 = compress(grid)    
    
    # merge the cells
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2

    # compress the grid again after merging
    new_grid, temp = compress(new_grid)

    return new_grid, changed

def move_right(grid):
    """Function to update the game board if the user performs a right move."""
    # to move right, first reverse the grid
    new_grid = reverse(grid)

    # then perform a left move on the reversed grid
    new_grid, changed = move_left(new_grid)

    # then reverse the grid again to show result
    new_grid = reverse(new_grid)

    return new_grid, changed

def move_up(grid):
    """Function to update the game board if the user performs an up move."""
    # to move up, first transpose the grid
    new_grid = transpose(grid)

    # then perform a left move on the transposed grid
    new_grid, changed = move_left(new_grid)

    # then transpose the grid again to show result
    new_grid = transpose(new_grid)

    return new_grid, changed

def move_down(grid):
    """Function to update the game board if the user performs a down move."""
    # to move down, first transpose the grid
    new_grid = transpose(grid)

    # then perform a right move on the transposed grid
    new_grid, changed = move_right(new_grid)

    # then transpose the grid again to show result
    new_grid = transpose(new_grid)

    return new_grid, changed