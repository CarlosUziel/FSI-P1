from random import randint
from games import *
import pickle

def aleatoria(state):
    return randint(-100, 100)


def memoize(f):
    memo = {}

    def helper(x):
        key = frozenset(x.board.items())
        if key not in memo:
            memo[key] = f(x)
        return memo[key]

    return helper


"""
Returns the sum of the following:
    +1000 -> For each 4 or more in a row
    +10 -> For each 3 in a row
    +1  -> For each 2 in a row
    +-0 -> No consecutive pieces
    -1  -> For each 2 in a row (opponent)
    -10 -> For each 3 in a row (opponent)
    -1000 -> For each 4 or more in a row (opponent)
:param state:
:return:
"""
@memoize
def main_heuristics(state, h=7, v=6):

    pos = [1, 1]
    board = state.board.copy()
    player = state.to_move

    heuristic_0 = process_straight(h, v, board, pos, player, 0, 1) + \
                  process_straight(v, h, board, pos, player, 1, 0) + \
                  process_oblique(h, h, v, board, pos, player, -1, 1) + \
                  process_oblique(1, h, v, board, pos, player, 1, 1)

    return heuristic_0/len(board)


def process_straight(s0, s1, board, pos, player, delta_x, delta_y):
    heuristic_0 = 0
    for i in range(s0):
        while pos[delta_y] <= s1:
            pos, heuristic_1 = subprocess_general(board, pos, player, delta_x, delta_y)
            heuristic_0 += heuristic_1
            pos[delta_y] += 1

        pos[delta_x] += 1
        pos[delta_y] = 1

    return heuristic_0


# TO-DO: Double counting
def process_oblique(origin, h, v, board, pos, player, delta_x, delta_y):
    heuristic_0 = 0
    oblique_mode = 0
    for i in range(2):
        for j in range(2, 2 + h):
            while pos[delta_y] <= v:
                pos, heuristic_1 = subprocess_general(board, pos, player, delta_x, delta_y)
                heuristic_0 += heuristic_1
                pos[delta_x - 1] += delta_x
                pos[delta_y] += delta_y

            if oblique_mode:
                pos[delta_x - 1] = origin
                pos[delta_y] = j
            else:
                pos[delta_x - 1] = j
                pos[delta_y] = 1

        oblique_mode = not oblique_mode

    # Double counting temporary fix
    heuristic_0 = if_(heuristic_0 >= 1500, heuristic_0-1000, heuristic_0)
    heuristic_0 = if_(heuristic_0 <= -1500, heuristic_0+1000, heuristic_0)

    return heuristic_0


def subprocess_general(board, pos, player, delta_x, delta_y):
    heuristic_0 = 0
    while tuple(pos) in board:
        pos, heuristic_1 = k_in_row(board, pos, player, (delta_x, delta_y))
        heuristic_0 += heuristic_1
        pos, heuristic_1 = k_in_row(board, pos, if_(player == 'X', 'O', 'X'), (delta_x, delta_y))
        heuristic_0 += heuristic_1

    return pos, heuristic_0


def k_in_row(board, pos, player, (delta_x, delta_y)):
    x, y = pos
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    return [x, y], if_(player == 'X', +row_value(n), -row_value(n))


def row_value(row):
    if row >= 4:
        return 1000
    elif row == 3:
        return 10
    elif row == 2:
        return 1
    else:
        return 0
