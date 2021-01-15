''' Plays text based connect four game '''
play1_sym = "1"
play2_sym = "2"
# display board 6 x 7
# ask users where they want to place on the board
# verify if ther is a winnner and announce
# give response if spot is already taken
# 7 lists in 1 big list
# each column is a list

def show_board(board):
    ''' prints the current state of the given board

    Args:
        board: the given 2D list to show
    '''
    # outer loop controls the row, inner the column
    for i in range(len(board[0])):
        for col in board:
            print(col[i], end=" ")
        print()

def last_zero(column):
    ''' determines the next available spot in the given column
    
    Args:
        column: the given column being searched for zero
   
    Returns:
        The next available index in the given column.
        -1 if there are no available spots.
    '''
    for i in range(len(column)):
        if column[i] != 0:
            return i - 1
    return i 

def choose(board, column_num, player_sym):
    chosen_column = board[column_num]
    chosen_spot = last_zero(chosen_column)
    if chosen_spot == -1:
        return False
    chosen_column[chosen_spot] = player_sym
    return True


board = []
for x in range(7):
    board.append(["O", "O", "O", "O", "O", "O"])

while True:
    spot_chosen = False
    while not spot_chosen:
        show_board(board)
        chosen_column = int(input("Where would you like to place your piece? (from 0 - 6) "))
        spot_chosen = choose(board, chosen_column, play1_sym)