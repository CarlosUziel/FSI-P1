import games
import heuristicas

player, dif = '', 0

while player not in ['X', 'O']:
    player = raw_input("Who moves first? (X,O): ")

difficulty = {"Easy": 2, "Normal": 3, "Hard": 5}
while dif not in difficulty:
    dif = raw_input("Choose difficulty (Easy, Normal, Hard): ")

# game = games.TicTacToe(h=3, v=3, k=3)
game = games.ConnectFour(player=player)
state = game.initial

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        # move = games.minimax_decision(state, game)
        # move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, d=difficulty[dif], eval_fn=heuristicas.main_heuristics)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
