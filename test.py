from heuristicas import *

board = {(3, 1): 'X', (4, 2): 'X', (5, 3): 'X', (6, 4): 'X'}
#board = {(1, 2): 'X', (2, 3): 'X', (3, 4): 'X', (4, 5): 'X'}
#board = {(7, 2): 'O', (6, 3): 'O', (5, 4): 'O', (4, 5): 'O'}
h = 7
v = 6
pos = [1, 1]
player = 'X'
display(board, v, h)
print '\n'
print process_oblique(h, h, v, board, pos, player, -1, 1)
print process_oblique(1, h, v, board, pos, player, 1, 1)
