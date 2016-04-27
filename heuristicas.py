from random import randint
from utils import *

def aleatoria(state):
    return randint(-100, 100)


def heuristica(state,h=7,v=6):
    """
    Returns the sum of the following:
        +50 -> For each 4 in a row
        +10 -> For each 3 in a row
        +2  -> For each 2 in a row
        +-0 -> No consecutive pieces
        -2  -> For each 2 in a row (opponent)
        -10 -> For each 3 in a row (opponent)
        -50 -> For each 4 in a row (opponent)
    :param state:
    :return:
    """

    board = state.board.copy()
    heur=0

    for i in range(h):
        heur += k_in_row(board,(0,i),board.to_move, (0,1))



  """  n = k_in_row(board, move, player, (0, 1) +
        k_in_row(board, move, player, (1, 0) +
        k_in_row(board, move, player, (1, -1) +
        k_in_row(board, move, player, (1, 1)
"""

def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    return n


def rowValue(row):
    if row == 4:
        return 50
    elif row == 3:
        return 10
    elif row == 2:
        return 2
    else:
        return 0

