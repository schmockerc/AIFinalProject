from ChessGame import ChessGame
from AlphaBeta import minimax_search
from typing import List
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import chess


def basicEval(state: List[List[chr]], current_player: chr, turn: int, check_mate: bool, cutoff: bool) -> int:
    scores = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}
    score = (117 if ('W' if (turn - 1) % 2 == 0 else 'b') == current_player else -117) if check_mate else 0
    score += -78 if not check_mate and cutoff else 0
    first_modifier = 0
    second_modifier = 0
    if current_player == 'W':
        first_modifier = 1
        second_modifier = -1
    elif current_player == 'b':
        first_modifier = -1
        second_modifier = 1
    for row in state:
        for pos in row:
            if pos in scores:
                score += scores[pos] * first_modifier if pos.isupper() else scores[pos] * second_modifier
    return score


if __name__ == '__main__':
    game = None
    winrate = {'W': 0, 'b': 0, 'D': 0}
    state_eval = []
    time_taken = []
    moves_available = []
    win_index = 0
    for i in range(1):
        game = ChessGame(clone=True, board=chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))

        state_eval.append([])
        time_taken.append([])
        moves_available.append([])

        while not game.is_cutoff():
            currentPlayer = 'W' if game.getTurn() % 2 == 0 else 'b'
            if currentPlayer == 'W':

                moves_available[-1].append(len(game.getMoves()))
                start = time.process_time()

                # move = game.move(random.choice(game.getMoves()))
                move = game.move(minimax_search(game, currentPlayer, basicEval)[1])

                time_taken[-1].append(time.process_time() - start)
                state_eval[-1].append(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate(), game.is_cutoff()))

            else:

                game.move(random.choice(game.getMoves()))

            print(game.getTurn())
            # print(currentPlayer + " - " + str(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate(), game.is_cutoff())))
            # game.print()
        # print(game.getTurn())

        if game.is_checkmate():
            win_index = i
            currentPlayer = 'W' if (game.getTurn() - 1) % 2 == 0 else 'b'
            winrate[currentPlayer] = winrate[currentPlayer] + 1
        else:
            winrate['D'] = winrate['D'] + 1

    labels = ["White", "Black", "Tie"]
    sizes = [winrate['W'], winrate['b'], winrate['D']]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('randomVrandom.png')
    plt.clf()

    plt.plot(np.arange(0, len(state_eval[win_index])-1), np.array(state_eval[win_index][:-1]))
    plt.savefig('randomVrandomBasicEval.png')
    plt.clf()

    plt.plot(np.arange(0, len(time_taken[win_index])), np.array(time_taken[win_index]))
    plt.savefig('randomTimeTake.png')
    plt.clf()

    plt.plot(np.arange(0, len(moves_available[win_index])), np.array(moves_available[win_index]))
    plt.savefig('randomMoveAmounts.png')

    # game.downloadGame("gamePossible7")
