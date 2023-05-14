from ChessGame import ChessGame
from AlphaBeta import alpha_beta_search
from Evaluations import EvaluationFunction
import random
import matplotlib
matplotlib.use('TkAgg')  # Note making the Pie chart doesn't work without this line of code
import matplotlib.pyplot as plt
import numpy as np
import time
import chess


if __name__ == '__main__':
    game = None
    win_rate = {'W': 0, 'b': 0, 'D': 0}
    state_eval = []
    time_taken = []
    moves_available = []
    win_index = 0

    # Change these values to change what the data files are saved as and what evaluation function alpha beta uses
    player1 = "BasicEval"
    player2 = "Random"
    evaluation_function = EvaluationFunction("Basic")

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
                move = game.move(alpha_beta_search(game, currentPlayer, evaluation_function)[1])

                time_taken[-1].append(time.process_time() - start)
                state_eval[-1].append(evaluation_function.evalState(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate(), game.is_cutoff()))

            else:

                game.move(random.choice(game.getMoves()))

            print(game.getTurn())
            # print(currentPlayer + " - " + str(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate(), game.is_cutoff())))
            # game.print()
        # print(game.getTurn())

        if game.is_checkmate():
            win_index = i
            currentPlayer = 'W' if (game.getTurn() - 1) % 2 == 0 else 'b'
            win_rate[currentPlayer] = win_rate[currentPlayer] + 1
        else:
            win_rate['D'] = win_rate['D'] + 1

    labels = ["White", "Black", "Tie"]
    sizes = [win_rate['W'], win_rate['b'], win_rate['D']]

    # Makes a pie chart of the win rate of 100 games
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Outcome of 100 Games')
    plt.savefig(player1 + 'V' + player2 + '.png')
    plt.clf()

    # Makes a plot of the score per move in the first game that player one won
    plt.plot(np.arange(0, len(state_eval[win_index])-1), np.array(state_eval[win_index][:-1]))
    plt.title('Score per Move')
    plt.ylabel('Score')
    plt.xlabel('Move Number')
    plt.savefig(player1 + 'V' + player2 + 'BasicEval.png')
    plt.clf()

    # Makes a plot of the time taken per move in the first game that player one won
    plt.plot(np.arange(0, len(time_taken[win_index])), np.array(time_taken[win_index]))
    plt.title('Time per Move')
    plt.ylabel('Time Taken (s)')
    plt.xlabel('Move Number')
    plt.savefig(player1 + 'V' + player2 + 'TimeTake.png')
    plt.clf()

    # Makes a plot of the amount of possible moves per move in the first game that player one won
    plt.plot(np.arange(0, len(moves_available[win_index])), np.array(moves_available[win_index]))
    plt.title('Possible Moves per Move')
    plt.ylabel('Amount of Possible Moves')
    plt.xlabel('Move Number')
    plt.savefig(player1 + 'V' + player2 + 'MoveAmounts.png')

    # Saves the last game played as a gif
    # game.downloadGame("gamePossible7")
