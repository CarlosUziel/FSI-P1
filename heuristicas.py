from random import randint
from utils import *


def aleatoria(state):
    return randint(-100, 100)


def main_heuristics(state, h=7, v=6):
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
    heuristic_0 = 0
    pos = [1, 1]

    heuristic_0 += process_straight(h, board, pos, 0, 1)
    heuristic_0 += process_straight(v, board, pos, 1, 0)

    heuristic_0 += process_oblique(h, h, v, board, pos, -1, 1)
    heuristic_0 += process_oblique(1, h, v, board, pos, 1, 1)

    return heuristic_0


def process_straight(size, board, pos, delta_x, delta_y):
    heuristic_0 = 0
    for i in range(size):
        pos[0] += delta_y
        pos[1] = 1
        while pos in board:
            pos, heuristic_1 = k_in_row(board, pos, board.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos[0] += delta_x
            pos[1] += delta_y

    return heuristic_0


def process_oblique(origin, h, v, board, pos, delta_x, delta_y):
    heuristic_0 = 0
    for i in range(h-1):
        pos[0] += delta_y
        pos[1] = 1
        while pos in board:
            pos, heuristic_1 = k_in_row(board, pos, board.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos[0] += delta_x
            pos[1] += delta_y

    pos = [origin, 1]
    for i in range(v-1):
        pos[0] = h
        pos[1] += delta_y
        while pos in board:
            pos, heuristic_1 = k_in_row(board, pos, board.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos[0] += delta_x
            pos[1] += delta_y


def k_in_row(board, pos, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = pos
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    return [x, y], row_value(n)


def row_value(row):
    if row == 4:
        return 50
    elif row == 3:
        return 10
    elif row == 2:
        return 2
    else:
        return 0
