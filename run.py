import random

cellState_unknown = 0
cellState_boat = 1

player_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
oponent_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
player_boats = []
oponent_boats = []
boat_sizes = [5, 4, 3, 2]


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



def init_grid(grid):
    """
    Randomly generates ships for player
    and opponent and makes sure its inside
    the grid and that the boats do not overlap
    """
    # position the boats
    for boat_index in range(4):
        # Place the boat
        orientation = random.randint(0, 1)

        while True:
            if orientation == 0:
                # horizontal
                row_index = random.randint(0, 7)
                col_index = random.randint(0, 7 - boat_sizes[boat_index])
                # check if we are not overriding existing boats
                hits = False
                for colcelloffset in range(0, boat_sizes[boat_index]):
                    if grid[row_index][colcelloffset + col_index] != cellState_unknown:
                        # spot already occupied
                        hits = True
                if hits is False:
                    for colcelloffset in range(0, boat_sizes[boat_index]):
                        grid[row_index][colcelloffset + col_index] = cellState_boat
                    break
            else:
                # vertical
                row_index = random.randint(0, 7 - boat_sizes[boat_index])
                col_index = random.randint(0, 7)
                hits = False
                for rowcelloffset in range(0, boat_sizes[boat_index]):
                    if grid[row_index + rowcelloffset][col_index] != cellState_unknown:
                        # spot already occupied
                        hits = True
                if hits is False:
                    for rowcelloffset in range(0, boat_sizes[boat_index]):
                        grid[row_index + rowcelloffset][col_index] = cellState_boat
                    break
