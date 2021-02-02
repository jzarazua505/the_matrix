''' Plays text based connect four game '''
player_symbols = {1: "1", 2: "2"}
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
        if column[i] != "O":
            return i - 1
    return i 

def choose_spot(board, player_num):
    ''' prompts user for a spot to place their piece

    Args:
        board: the current board
        player_num: the current player number

    Returns:
        A tuple containing the chosen column and row
    '''
    valid_spot = False
    while not valid_spot:
        show_board(board)
        chosen_column = int(input(f"Where would you like to place your piece, player number {player_num}? (from 0 - 6) "))
    
        row = last_zero(board[chosen_column])
        valid_spot = row != -1
        if not valid_spot:
            print("That column is full. Pick another column.")
    return chosen_column, row 

def get_horizontal(board, row):
    horizontal = ""
    for column in board:
        horizontal += column[row]
    return horizontal

def get_up_diagonal(board, column, row):
    up_diagonal = ""
    for c in range(len(board)):
        for r in range(len(board[c])):
            if column + row == c + r:
                up_diagonal += board[c][r]
    return up_diagonal
    
def get_down_diagonal(board, columm, row):
    down_diagonal = ""
    for c in range(len(board)):
        for r in range(len(board[c])):
            if column - row == c - r:
                down_diagonal += board[c][r]
    return down_diagonal

def check_win(board, column, row):
    win_string = board[column][row]*4
    if win_string in "".join(board[column]):
        return True
    if win_string in get_horizontal(board, row):
        return True
    if win_string in get_up_diagonal(board, column, row):
        return True
    if win_string in get_down_diagonal(board, column, row):
        return True
    return False

if __name__ == "__main__":
    board = []
    for x in range(7):
        board.append(["O", "O", "O", "O", "O", "O"])

    player_num = 1
    turn = 0
    while True:
        column, row = choose_spot(board, player_num)
        board[column][row] = player_symbols[player_num]
        if check_win(board, column, row):
            break
        turn += 1
        if turn == 42:
            break
        if player_num == 1:
            player_num = 2
        else:
            player_num = 1
    if turn == 42:
        print("The game is a tie -_-")
    else:
        print(f"Player number {player_num} wins!")
    show_board(board)

    
        