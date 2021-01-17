''' Plays text based connect four game '''
PLAYER_SYMBOLS = {1: "1", 2: "2"}

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

def next_available(column):
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

# def fill_spot(board, column_num, player_sym):
#     chosen_column = board[column_num]
#     chosen_spot = last_zero(chosen_column)
#     if chosen_spot == -1:
#         return False
#     chosen_column[chosen_spot] = player_sym
#     return True

def get_symbol(board, position):
    if position[0] not in range(0, len(board)) or position[1] not in range(0, len(board[0])):
        return 0
    return board[position[0]][position[1]]

def check_direction(board, previous_position, direction, total):
    current_position = (previous_position[0] + direction[0], previous_position[1] + direction[1])
    if get_symbol(board, current_position) == get_symbol(board, previous_position):
        return check_direction(board, current_position, direction, total + 1)
    return total

def check_for_win(board, start_position):
    if check_direction(board, start_position, (1, -1), 0) + check_direction(board, start_position, (-1, 1), 0) >= 3: return True
    if check_direction(board, start_position, (1, 0), 0) + check_direction(board, start_position, (-1, 0), 0) >= 3: return True
    if check_direction(board, start_position, (1, 1), 0) + check_direction(board, start_position, (-1, -1), 0) >= 3: return True
    if check_direction(board, start_position, (0, 1), 0) >= 3: return True
    return False

if __name__ == "__main__":
    board = []
    for x in range(7):
        board.append(["O", "O", "O", "O", "O", "O"])

    spots_filled = 0
    current_player = 1
    while True:
        chosen_row = -1
        while chosen_row == -1:
            show_board(board)
            chosen_column = int(input(f"Where would you like to place your piece, Player {current_player}? (from 0 - 6) "))
            if chosen_column not in range(0, len(board)):
                print("That is not a valid column number! Choose a different one.")
                continue
            chosen_row = next_available(board[chosen_column])
            if chosen_row == -1:
                print("There are no spots left in that column! Choose a different one.")

        board[chosen_column][chosen_row] = PLAYER_SYMBOLS[current_player]
        if check_for_win(board, (chosen_column, chosen_row)):
            break

        spots_filled += 1
        if spots_filled >= len(board) * len(board[0]):
            break

        current_player = current_player % 2 + 1

    if spots_filled >= len(board) * len(board[0]): 
        print("Nobody wins! D:")
    else:
        print(f"Player {current_player} wins!")
    show_board(board)
