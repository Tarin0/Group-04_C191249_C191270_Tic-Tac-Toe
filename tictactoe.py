import math
import copy

#Me:
rows, cols = (3, 3)
board = [[0]*cols]*rows
#-----------------------------------


#______________________________________________________________________________________________________________________________________#


# 1. Initial State: 
# Every tic-tac-toe game starts with an empty 3x3 matrix.

X = "X"
O = "O"
EMPTY = None
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


#______________________________________________________________________________________________________________________________________#

# 2. Count:
# This will help to keep track of which player to move next. Returns the number of X and O on the board.

def count(board):
    count_x, count_o = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    return count_x, count_o
    