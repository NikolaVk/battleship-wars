import random
import sys
import msvcrt

cellState_unknown = 0
cellState_boat = 1
cellState_missed = 2
cellState_hit = 3

gridstatus_boats_left = 0
gridstatus_noboats_left = 1

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


def check_grid_status(grid):
    """
    This status checking function
    checks if the player once fired
    if he/she has hit or missed the
    opponents boats
    """
    num_boats = 0
    num_hits = 0
    num_missings = 0

    for col_index in range(8):
        for row_index in range(8):
            if grid[row_index][col_index] == cellState_boat:
                num_boats = num_boats + 1
            elif grid[row_index][col_index] == cellState_hit:
                num_hits = num_hits + 1
            elif grid[row_index][col_index] == cellState_missed:
                num_missings = num_missings + 1

    if num_boats == 0:
        # all boatspositions are gone
        return gridstatus_boats_left
    return gridstatus_boats_left


def get_player_posinput(grid):
    """
    The player is able to type out
    the position he/she wishes to
    fire at the oponents boats.
    If the input is invalid the player
    must try again
    """
    while True:
        pos_as_tring = input("Provide the position you want to try (A-H/1-8): ")
        if (pos_as_tring):
            if (len(pos_as_tring) == 2) and (pos_as_tring[0] >= 'A') and (pos_as_tring[0] <= 'H') and (pos_as_tring[1] >= '1') and (pos_as_tring[1] <= '8'):
                # decode the position
                col_index = ord(pos_as_tring[0]) - ord('A')
                row_index = ord(pos_as_tring[1]) - ord('1')
                return (col_index, row_index)
            else:
                print("Invalid input. Type the columncharacter and the rownumber. (example A6 or F3)")
        else:
            if(msvcrt.getch() == chr(27).encode()):
                sys.exit()
