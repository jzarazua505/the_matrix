''' Plays text based connect four game '''
PLAYER_SYMBOLS = {1: "1", 2: "2"}
PLAYER_1_WINS = r"""
o--o  o      O  o   o o--o o--o        0       o       o o-O-o o   o  o-o  o
|   | |     / \  \ /  |    |   |      /|       |       |   |   |\  | |     |
O--o  |    o---o  O   O-o  O-Oo      o |       o   o   o   |   | \ |  o-o  o
|     |    |   |  |   |    |  \        |        \ / \ /    |   |  \|     |
o     O---oo   o  o   o--o o   o     o-o-o       o   o   o-O-o o   o o--o  O
"""
PLAYER_2_WINS = r"""
o--o  o      O  o   o o--o o--o       --      o       o o-O-o o   o  o-o  o 
|   | |     / \  \ /  |    |   |     o  o     |       |   |   |\  | |     | 
O--o  |    o---o  O   O-o  O-Oo        /      o   o   o   |   | \ |  o-o  o 
|     |    |   |  |   |    |  \       /        \ / \ /    |   |  \|     |   
o     O---oo   o  o   o--o o   o     o--o       o   o   o-O-o o   o o--o  O 
"""
NOBODY_WINS = r"""
o   o  o-o  o--o   o-o  o-o   o   o     o       o o-O-o o   o  o-o  o                /
|\  | o   o |   | o   o |  \   \ /      |       |   |   |\  | |     |         O     o
| \ | |   | O--o  |   | |   O   O       o   o   o   |   | \ |  o-o  o               |
|  \| o   o |   | o   o |  /    |        \ / \ /    |   |  \|     |           O     o
o   o  o-o  o--o   o-o  o-o     o         o   o   o-O-o o   o o--o  O                \
"""

# display board 6 x 7
# ask users where they want to place on the board
# verify if ther is a winnner and announce
# give response if spot is already taken
# 7 lists in 1 big list
# each column is a list

def print_title():
    print(r"""
                                          
  o-o  o-o  o   o o   o o--o   o-o o-O-o     o  o 
 /    o   o |\  | |\  | |     /      |       |  | 
O     |   | | \ | | \ | O-o  O       |       o--O 
 \    o   o |  \| |  \| |     \      |          | 
  o-o  o-o  o   o o   o o--o   o-o   o          o 
                                                  
""")

def create_board(columns, rows):
    ''' Creates a new connect four board with the given dimensions

    Args:
        columns: number of columns in the new board
        rows: number of rows in the new board
    
    Returns:
        The new board as a list of lists
    '''
    new_board = []
    for _ in range(columns):
        new_column = []
        for _ in range(rows):
            new_column.append("O")
        new_board.append(new_column)
    return new_board

def show_board(board):
    ''' prints the current state of the given board

    Args:
        board: the given 2D list to show
    '''
    for i in range(len(board)):
        print(i + 1, end=" ")
    print()
    for i in range(len(board)):
        print("_", end=" ")
    print()

    # outer loop controls the row, inner the column
    for i in range(len(board[0])):
        for col in board:
            print(col[i], end=" ")
        print()

def choose_valid_spot(board, current_player):
    ''' Prompts the user to chose a valid column and determines the board position of the next piece

    Args:
        board: the current board
        current_player: number id of current player

    Returns:
        A tuple containing the column and row numbers of the selected position
    '''
    def next_available(column):
        for i in range(len(column)):
            if column[i] != "O":
                return i - 1
        return i
        
    invalid_column = True
    while invalid_column:
        show_board(board)
        chosen_column = int(input(f"Where would you like to place your piece, Player {current_player}? (from 1 - 7) ")) - 1
        if chosen_column not in range(0, len(board)):
            print("That is not a valid column number! Choose a different one.")
            continue
        row = next_available(board[chosen_column])
        invalid_column = row == -1
        if invalid_column:
            print("There are no spots left in that column! Choose a different one.")
    return chosen_column, row

def check_for_win(board, start_position):
    ''' Determines if there is a winning combination of pieces branching from the given position

    Args:
        board: The current board
        start_position: The given position from which the search will start

    Returns:
        True if a winning combination is found, False if otherwise
    '''
    def check_direction(board, previous_position, direction, total):
        def get_symbol(board, position):
            if position[0] not in range(0, len(board)) or position[1] not in range(0, len(board[0])):
                return 0
            return board[position[0]][position[1]]

        current_position = (previous_position[0] + direction[0], previous_position[1] + direction[1])
        if get_symbol(board, current_position) == get_symbol(board, previous_position):
            return check_direction(board, current_position, direction, total + 1)
        return total

    # / piece orientation check
    if check_direction(board, start_position, (1, -1), 0) + check_direction(board, start_position, (-1, 1), 0) >= 3: return True
    # - piece orientation check
    if check_direction(board, start_position, (1, 0), 0) + check_direction(board, start_position, (-1, 0), 0) >= 3: return True
    # \ piece orientation check
    if check_direction(board, start_position, (1, 1), 0) + check_direction(board, start_position, (-1, -1), 0) >= 3: return True
    # | piece orientation check
    if check_direction(board, start_position, (0, 1), 0) >= 3: return True
    return False

def game_loop(columns, rows):
    print_title()
    board = create_board(7, 6)
    spots_filled = 0
    current_player = 1
    while True:
        chosen_column, chosen_row = choose_valid_spot(board, current_player)
        board[chosen_column][chosen_row] = PLAYER_SYMBOLS[current_player]
        if check_for_win(board, (chosen_column, chosen_row)):
            break
        spots_filled += 1
        if spots_filled >= len(board) * len(board[0]):
            break
        current_player = current_player % 2 + 1

    if spots_filled >= len(board) * len(board[0]):
        print(NOBODY_WINS)
    else:
        print(PLAYER_1_WINS if current_player == 1 else PLAYER_2_WINS)
    show_board(board)

if __name__ == "__main__":
    play_again = True
    while play_again:
        game_loop(7, 6)
        play_again = input("Would you like to play again? ") == "y"
