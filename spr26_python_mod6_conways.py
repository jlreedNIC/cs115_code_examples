# conways game of life

import copy
import time

# --functions
def create_grid(rows, cols, dead_s):
    board = []
    # outer loop iterates over rows
    for y in range(0, rows):
        new_row = []
        # inner loop iterates over columns
        for x in range(0, cols):
            new_row.append(dead_s)
        board.append(new_row)
    
    return board

def print_board(board):
    # outer loop - rows
    for row in board:
        # inner loop - columns
        for cell in row:
            print(f'{cell}', end=' ')
        print()

def count_neighbors(board, cur_x, cur_y, alive_s):
    row_num = len(board)
    col_num = len(board[0])

    left = (cur_x - 1) % col_num
    right = (cur_x + 1) % col_num

    above = (cur_y - 1) % row_num
    below = (cur_y + 1) % row_num
    # holds alive neighbor count
    neighbor_count = 0

    neighbors = [
        board[above][left], board[above][cur_x], board[above][right],
        board[cur_y][left],                      board[cur_y][right],
        board[below][left], board[below][cur_x], board[below][right]
    ]

    for cell in neighbors:
        if cell == alive_s:
            neighbor_count += 1
    
    return neighbor_count

def update_cell(cell, num_neighbors, alive_s, dead_s):
    if cell == alive_s and (num_neighbors == 2 or num_neighbors == 3):
        return alive_s
    elif cell == dead_s and num_neighbors == 3:
        return alive_s
    else:
        return dead_s

def read_from_file(file_name):
    file = open(file_name, "r")

    board = []
    end_file = False
    while not end_file:
        # read a line
        row = file.readline()

        if row == "":
            end_file = True
        else:
            row = row.strip("\n")
            board.append(list(row))
    file.close()

    rows = len(board)
    cols = len(board[0])
    return board, rows, cols

# -- global variables
alive = "X"
dead = '.'

num_rows = 5
num_cols = 5

# -- main code -
# grid = create_grid(num_rows, num_cols, dead)
# grid[1][1] = grid[1][2] = grid[1][3] = alive

grid, num_rows, num_cols = read_from_file("sample_board.txt")

print_board(grid)

for generation in range(0, 5):
    # create a copy of the grid
    grid_copy = copy.deepcopy(grid)

    # outer loop - rows
    for y in range(num_rows):
        # inner loop - columns
        for x in range(num_cols):

            # count alive neighbors
            alive_neighbors = count_neighbors(grid_copy, x, y, alive)

            # update cell state
            grid[y][x] = update_cell(grid_copy[y][x], alive_neighbors, alive, dead)

    # print board
    print_board(grid)
    time.sleep(.5)