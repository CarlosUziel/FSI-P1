from heuristicas import *

def display(board, v, h):
    for y in range(v, 0, -1):
        for x in range(1, h + 1):
            print board.get((x, y), '.'),
        print
    print "-------------------"
    for n in range(1, h + 1):
        print n,

board = {(4, 1): 'X', (3, 2): 'X', (2, 3): 'X', (1, 4): 'X'}
#board = {(1, 2): 'X', (2, 3): 'X', (3, 4): 'X', (4, 5): 'X'}
#board = {(7, 2): 'O', (6, 3): 'O', (5, 4): 'O', (4, 5): 'O'}
h = 7
v = 6
display(board, v, h)
pos = [1, 1]
player = 'X'
print '\n'
print process_oblique(h, h, v, board, pos, player, -1, 1)
print process_oblique(1, h, v, board, pos, player, 1, 1)


