from random import randint
from games import *


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
    pos = [1, 1]

    heuristic_0 = process_straight(h, v, state, pos, 0, 1) + \
                  process_straight(v, h, state, pos, 1, 0) + \
                  process_oblique(h, h, v, state, pos, -1, 1) + \
                  process_oblique(1, h, v, state, pos, 1, 1)

    # if heuristic_0 > 500 or heuristic_0 < -500:
    #    print '\n'
    #    print heuristic_0
    #    print '\n'
    #    display(state, v, h)
    return heuristic_0


def process_straight(s0, s1, state, pos, delta_x, delta_y):
    board = state.board.copy()
    heuristic_0 = 0
    for i in range(s0):
        while pos[delta_y] <= s1:
            if tuple(pos) not in board:
                pos[delta_y] += 1
            pos, heuristic_1 = k_in_row(board, pos, state.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos, heuristic_1 = k_in_row(board, pos, if_(state.to_move == 'X', 'O', 'X'), (delta_x, delta_y))
            heuristic_0 += heuristic_1

        pos[delta_x] += 1
        pos[delta_y] = 1

    return heuristic_0


def process_oblique(origin, h, v, state, pos, delta_x, delta_y):
    board = state.board.copy()
    heuristic_0 = 0
    for i in range(h - 1):
        while tuple(pos) in board:
            pos, heuristic_1 = k_in_row(board, pos, state.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos, heuristic_1 = k_in_row(board, pos, if_(state.to_move == 'X', 'O', 'X'), (delta_x, delta_y))
            heuristic_0 += heuristic_1
        pos[0] += delta_y
        pos[1] = 1

    pos = [origin, 1]
    for i in range(v - 1):
        while tuple(pos) in board:
            pos, heuristic_1 = k_in_row(board, pos, state.to_move, (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos, heuristic_1 = k_in_row(board, pos, if_(state.to_move == 'X', 'O', 'X'), (delta_x, delta_y))
            heuristic_0 += heuristic_1
            pos[0] += delta_x
            pos[1] += delta_y
        pos[0] = h
        pos[1] += delta_y

    return heuristic_0


def k_in_row(board, pos, player, (delta_x, delta_y)):
    x, y = pos
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    return [x, y], if_(player == 'X', row_value(n), -row_value(n))


def row_value(row):
    if row >= 4:
        return 1000
    elif row == 3:
        return 10
    elif row == 2:
        return 1
    else:
        return 0


def display(state, v, h):
    board = state.board
    for y in range(v, 0, -1):
        for x in range(1, h + 1):
            print board.get((x, y), '.'),
        print
    print "-------------------"
    for n in range(1, h + 1):
        print n,
