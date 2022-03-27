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

