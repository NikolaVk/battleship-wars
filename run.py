import random
import sys

cell_state_unknown = 0
cell_state_boat = 1
cell_state_missed = 2
cell_state_hit = 3

gridstatus_boats_left = 0
gridstatus_noboats_left = 1

player_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
oponent_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
player_boats = []
oponent_boats = []
boat_sizes = [5, 4, 3, 2]

last_hit_col_pos = -1
last_hit_row_pos = -1

grid_chars = ["[ ]", " * ", " o ", " X "]


def draw_grid(player_states, oponent_states):
    """
    This draws the players and oponents
    playfield grid. This will repeat after
    each turn with a new state.
    """
    global cell_state_unknown
    global cell_state_boat
    global cell_state_missed
    global cell_state_hit

    print("              Player                     ",
          "                           Oponent")
    print("   A   B   C   D   E   F   G   H         ",
          "                 A   B   C   D   E   F   G   H")
    for row_num in range(8):
        row_string = str(row_num + 1) + " "
        for col_index in range(8):
            row_string = row_string + \
                 grid_chars[player_states[row_num][col_index]] + " "
        row_string = row_string + \
            "                      " + str(row_num + 1) + " "
        for col_index in range(8):
            if oponent_states[row_num][col_index] == cell_state_boat:
                row_string = row_string + grid_chars[cell_state_unknown] + " "
            else:
                row_string = row_string + \
                     grid_chars[oponent_states[row_num][col_index]] + " "
        print(row_string)


def init_grid(grid):
    """
    Randomly generates ships for player
    and oponent and makes sure its inside
    the grid and that the boats do not overlap
    """
    global cell_state_unknown
    global cell_state_boat
    global cell_state_missed
    global cell_state_hit

    for col_index in range(8):
        for row_index in range(8):
            grid[row_index][col_index] = cell_state_unknown

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
                    if grid[row_index][colcelloffset + col_index] \
                         != cell_state_unknown:
                        # spot already occupied
                        hits = True
                if hits is False:
                    for colcelloffset in range(0, boat_sizes[boat_index]):
                        grid[row_index][colcelloffset + col_index] = \
                             cell_state_boat
                    break
            else:
                # vertical
                row_index = random.randint(0, 7 - boat_sizes[boat_index])
                col_index = random.randint(0, 7)
                hits = False
                for rowcelloffset in range(0, boat_sizes[boat_index]):
                    if grid[row_index + rowcelloffset][col_index] != \
                         cell_state_unknown:
                        # spot already occupied
                        hits = True
                if hits is False:
                    for rowcelloffset in range(0, boat_sizes[boat_index]):
                        grid[row_index + rowcelloffset][col_index] = \
                             cell_state_boat
                    break


def check_grid_status(grid):
    """
    This status checking function
    checks if the player once fired
    if he/she has hit or missed the
    oponents boats
    """
    num_boats = 0
    num_hits = 0
    num_missings = 0
    global cell_state_unknown
    global cell_state_boat
    global cell_state_missed
    global cell_state_hit

    for col_index in range(8):
        for row_index in range(8):
            if grid[row_index][col_index] is cell_state_boat:
                num_boats = num_boats + 1
            elif grid[row_index][col_index] is cell_state_hit:
                num_hits = num_hits + 1
            elif grid[row_index][col_index] is cell_state_missed:
                num_missings = num_missings + 1

    if num_boats == 0:
        # all boatspositions are gone
        return gridstatus_noboats_left
    return gridstatus_boats_left


def get_player_posinput(grid):
    """
    The player is able to type out
    the position he/she wishes to
    fire at the oponents boats.
    If the input is invalid the player
    must try again
    """
    global cell_state_unknown
    global cell_state_boat
    global cell_state_missed
    global cell_state_hit
    while True:
        pos_as_string = \
            input("Provide the position you want to try (A-H/1-8):\n").upper()
        if (len(pos_as_string) == 2) and \
                (pos_as_string[0] >= 'A') and(pos_as_string[0] <= 'H') and \
                (pos_as_string[1] >= '1') and (pos_as_string[1] <= '8'):
                # decode the position
            col_index = ord(pos_as_string[0]) - ord('A')
            row_index = ord(pos_as_string[1]) - ord('1')
            return (col_index, row_index)
        elif pos_as_string == 'Q':
            sys.exit()
        else:
            print("Invalid input. Type the columncharacter "
                  "and the rownumber. (example A6 or F3)")


def opponent_turn(grid):
    """
    The oponent is able to fire at
    the player. This includes a little
    smarter oponent. The oponent will
    make sure that if he got a hit that
    he will try to find the entire boat
    """
    global last_hit_col_pos
    global last_hit_row_pos
    global cell_state_unknown
    global cell_state_boat
    global cell_state_missed
    global cell_state_hit

    # Be a little bit smarter then plain stupid
    col_index = 0
    row_index = 0
    if last_hit_col_pos >= 0 and last_hit_col_pos < 7 and \
            grid[last_hit_row_pos][last_hit_col_pos + 1] is not \
            cell_state_hit and\
            grid[last_hit_row_pos][last_hit_col_pos + 1]\
            is not cell_state_missed:
                col_index = last_hit_col_pos + 1
                row_index = last_hit_row_pos
    elif last_hit_col_pos >= 1 and last_hit_col_pos < 8 and \
            grid[last_hit_row_pos][last_hit_col_pos - 1] is not \
            cell_state_hit and\
            grid[last_hit_row_pos][last_hit_col_pos - 1]\
            is not cell_state_missed:
                col_index = last_hit_col_pos - 1
                row_index = last_hit_row_pos
    elif last_hit_row_pos >= 0 and last_hit_row_pos < 7 and \
            grid[last_hit_row_pos + 1][last_hit_col_pos] is not \
            cell_state_hit and\
            grid[last_hit_row_pos + 1][last_hit_col_pos]\
            is not cell_state_missed:
                col_index = last_hit_col_pos
                row_index = last_hit_row_pos + 1
    elif last_hit_row_pos >= 1 and last_hit_row_pos < 8 and \
            grid[last_hit_row_pos - 1][last_hit_col_pos] is not \
            cell_state_hit and\
            grid[last_hit_row_pos - 1][last_hit_col_pos] \
            is not cell_state_missed:
                col_index = last_hit_col_pos
                row_index = last_hit_row_pos - 1
    else:
        while True:
            col_index = random.randint(0, 7)
            row_index = random.randint(0, 7)

            # print("Test " + str(col_index) + "," + str(row_index))

            # check if we already tried this position
            if grid[row_index][col_index] is not cell_state_hit \
               and grid[row_index][col_index] is not cell_state_missed:
                break
    # update the status
    if grid[row_index][col_index] is cell_state_boat:
        # yes,  we hit something
        grid[row_index][col_index] = cell_state_hit
        print("Oponent played " + chr(col_index + ord('A')) +
              str(row_index + 1) + ' HIT')
        last_hit_col_pos = col_index
        last_hit_row_pos = row_index
    else:
        grid[row_index][col_index] = cell_state_missed
        print("Oponent played " + chr(col_index + ord('A')) +
              str(row_index + 1) + ' MISSED')
        last_hit_col_pos = -1
        last_hit_row_pos = -1


def start_game():
    """
    Gives option to start, restart the game
    and choose shooting position on oponent
    grid. It also starts the game after player
    has provided input
    """
    global gridstatus_noboats_left

    # generate random player positions in grid
    init_grid(player_grid)
    # generate random oponent positions in grid
    init_grid(oponent_grid)

    # inner game loop
    while True:
        # draw current state
        draw_grid(player_grid, oponent_grid)

        # ask player what he wants
        grid_pos_totry = get_player_posinput(oponent_grid)
        if (oponent_grid[grid_pos_totry[1]][grid_pos_totry[0]] ==
           cell_state_boat):
                oponent_grid[grid_pos_totry[1]][grid_pos_totry[0]] = \
                    cell_state_hit
                print("You played " + chr(grid_pos_totry[0] + ord('A')) +
                      str(grid_pos_totry[1] + 1) + ' HIT')
        elif (oponent_grid[grid_pos_totry[1]][grid_pos_totry[0]] ==
              cell_state_unknown):
            oponent_grid[grid_pos_totry[1]][grid_pos_totry[0]] = \
                cell_state_missed
            print("You played " + chr(grid_pos_totry[0] + ord('A')) +
                  str(grid_pos_totry[1] + 1) + ' MISSED')

        # perform the check
        if check_grid_status(oponent_grid) == gridstatus_noboats_left:
            # yeah, oponent loose
            draw_grid(player_grid, oponent_grid)
            print("You win")
            return

        opponent_turn(player_grid)

        # perform the check
        if check_grid_status(player_grid) is gridstatus_noboats_left:
            # oeps, you loose
            draw_grid(player_grid, oponent_grid)
            print("You lost")
            return


# Start game
print("Welcome to Battleship Wars!\n")
print("How it works?")
print("-----------------------------------------------------")
print("The ships will be randomly generated for both parties")
print("The first to sinks all ships wins the game")
print("Empty spot = []")
print("Player boats = *")
print("Hit = X")
print("Missed = o")
print("To quit enter q")
print("Enjoy!")
print("-----------------------------------------------------\n")


# start game loop
while True:
    answer = input("Enter any key to start:\n")
    start_game()

    while True:
        answer = input("Do you want to play again (y/n):\n")
        if answer == 'n' or answer == 'y':
            break
    if answer == 'n':
        break
print("Goodbye")
