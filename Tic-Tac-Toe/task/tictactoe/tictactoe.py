# write your code here
Blank = '_'
PlayerX = 'X'
PlayerO = 'O'

# all possible game states
S_continue = 'Game not finished'
S_draw = 'Draw'
S_x_win = 'X wins'
S_o_win = 'O wins'
S_impossible = 'Impossible'
WINNING_POSITIONS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

VALID_NUM = {1, 2, 3}
IDX_TO_COORD = {0:(1, 3), 1:(2, 3), 2:(3, 3), 3:(1, 2), 4:(2, 2), 5:(3, 2), 6:(1, 1), 7:(2, 1), 8:(3, 1)}
COORD_TO_IDX = {v:k for k, v in IDX_TO_COORD.items()}


def print_cells(cells):
    '''Print current game'''
    cells = cells.strip()
    print('-'*9)
    row1 = ['|'] + list(cells[:3]) + ['|']
    print(" ".join(row1))
    print()
    row2 = ['|'] + list(cells[3:6]) + ['|']
    print(" ".join(row2))
    print()
    row3 = ['|'] + list(cells[6:]) + ['|']
    print(" ".join(row3))
    print()
    print('-'*9)


def get_current_state(symbols):
    '''return current game's state'''
    diff_xo_count = abs(symbols.count(PlayerX) - symbols.count(PlayerO))
    has_blank = symbols.count(Blank) > 0
    is_player_x_wins = any([True for i, j, k in WINNING_POSITIONS
                            if symbols[i] == PlayerX and symbols[j] == PlayerX and symbols[k] == PlayerX])
    is_player_o_wins = any([True for i, j, k in WINNING_POSITIONS
                            if symbols[i] == PlayerO and symbols[j] == PlayerO and symbols[k] == PlayerO])

    if (diff_xo_count > 1) or (is_player_x_wins and is_player_o_wins):
        return S_impossible
    elif is_player_x_wins:
        return S_x_win
    elif is_player_o_wins:
        return S_o_win
    elif has_blank:
        return S_continue
    else:
        return S_draw


def get_user_coordinate(cells, turn=PlayerX):
    cells = list(cells)
    valid_coords = {IDX_TO_COORD[i] for i in range(len(cells)) if cells[i] == Blank}
    while True:
        try:
            i, j = map(int, input("Enter the coordinates: >").split())
            if (i not in VALID_NUM) or (j not in VALID_NUM):
                print("Coordinates should be from 1 to 3!")
            elif (i, j) not in valid_coords:
                print("This cell is occupied! Choose another one!")
            else:
                cells[COORD_TO_IDX[(i, j)]] = turn
                return ''.join(cells)
        except ValueError:
            print("You should enter numbers!")


# Play Game
current_cells = Blank * 9
current_state = S_continue
current_player = PlayerX

print_cells(current_cells)
while current_state == S_continue:
    current_cells = get_user_coordinate(current_cells, current_player)
    print_cells(current_cells)
    new_state = get_current_state(current_cells)

    if new_state in {S_draw, S_x_win, S_o_win}:
        print(new_state)
        break
    else:
        current_state = new_state
        current_player = PlayerX if current_player == PlayerO else PlayerO   # switch player
else:
    print(S_impossible