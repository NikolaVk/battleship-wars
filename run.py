cellState_unknown = 0
cellState_boat = 1


player_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
oponent_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


grid_chars = ["[ ]", " X ", " X ", " o "]


def draw_grid(player_states, oponent_states):
    """
    This draws the players and opponents 
    playfield grid. This will repeat after
    each turn with a new state.
    """
    print("              Player                                                  Oponent")
    print("   A   B   C   D   E   F   G   H                           A   B   C   D   E   F   G   H")
    for row_num in range(8):
        row_string = str(row_num + 1) + " "
        for col_index in range(8):
            row_string = row_string + grid_chars[player_states[row_num][col_index]] + " "
        row_string = row_string + "                      " + str(row_num + 1) + " "
        for col_index in range(8):
            if oponent_states[row_num][col_index] == cellState_boat:
                row_string = row_string + grid_chars[cellState_unknown] + ""
            else:
                row_string = row_string + grid_chars[oponent_states[row_num][col_index]] + " "
        print(row_string)


draw_grid(player_grid, oponent_grid)
