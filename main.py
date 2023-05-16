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
    player1 = "Genetic"
    player2 = "Random"
    genetic_eval = [[10, -3, 9, 10, -8, -3, 2, -7],
                    [-2, 0, 7, 1, -6, 0, -7, 10],
                    [4, -8, 9, 1, 5, 1, -1, -7],
                    [-2, -9, -3, 9, 10, 0, -4, -8],
                    [1, -7, -4, -10, -9, -6, 4, 8],
                    [3, -2, -8, -4, 0, 6, 6, -3],
                    [10, 8, -6, 7, 9, -2, -4, -10],
                    [2, -6, -3, 4, -6, 7, 0, 9]]
    evaluation_function = EvaluationFunction("Genetic", genetic_eval)
    game_amount = 25
    beginning = time.process_time()

    for i in range(game_amount):
        game = ChessGame(clone=True, board=chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))

        state_eval.append([])
        time_taken.append([])
        moves_available.append([])

        while not game.is_cutoff():
            currentPlayer = 'W' if game.getTurn() % 2 == 0 else 'b'
            if currentPlayer == 'W':

                moves_available[-1].append(len(game.getMoves()))
                start = time.process_time()
                # move = random.choice(game.getMoves())
                move = alpha_beta_search(game, currentPlayer, evaluation_function)[1]
                game.move(move)

                time_taken[-1].append(time.process_time() - start)
                state_eval[-1].append(evaluation_function.evalState(game.getState(), currentPlayer, game.getTurn(),
                                                                    game.is_checkmate(), game.is_cutoff()))

            else:
                # move = alpha_beta_search(game, currentPlayer, evaluation_function)[1]
                move = random.choice(game.getMoves())
                game.move(move)

            # print(game.getTurn())
            # print(currentPlayer + " - " + str(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate(), game.is_cutoff())))
            # game.print()
        seconds = int(time.process_time() - beginning)
        print(str(i) + " " + str(game.getTurn()) + " " + f"{seconds // 3600}:{(seconds % 3600) // 60}:{seconds % 60}")

        if game.is_checkmate():
            win_index = i
            currentPlayer = 'W' if (game.getTurn() - 1) % 2 == 0 else 'b'
            win_rate[currentPlayer] = win_rate[currentPlayer] + 1
        else:
            win_rate['D'] = win_rate['D'] + 1

    labels = ["White: " + player1, "Black: " + player2, "Tie"]
    sizes = [win_rate['W'], win_rate['b'], win_rate['D']]

    # Makes a pie chart of the win rate of 100 games
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Outcome of ' + str(game_amount) + ' Games')
    plt.savefig('data\\' + player1 + 'V' + player2 + '.png')
    plt.clf()

    # Makes a plot of the score per move in the first game that player one won
    plt.plot(np.arange(0, len(state_eval[win_index])-1), np.array(state_eval[win_index][:-1]))
    plt.title('Score per Move')
    plt.ylabel('Score')
    plt.xlabel('Move Number')
    plt.xlim(0, len(state_eval[win_index]) - 2)
    plt.savefig('data\\' + player1 + 'V' + player2 + 'BasicEvalPerMove.png')
    plt.clf()

    # Makes a scatter plot of the score for each game
    plt.scatter(np.array(list(map(lambda game_states: len(game_states)-1, state_eval))),
                np.array(list(map(lambda state_list: sum(state_list[:-1]), state_eval))))
    plt.title('Score per Game')
    plt.ylabel('Score')
    plt.xlabel('Move Amount per Game')
    plt.savefig('data\\' + player1 + 'V' + player2 + 'BasicEvalPerGame.png')
    plt.clf()

    # Makes a plot of the time taken per move in the first game that player one won
    plt.plot(np.arange(0, len(time_taken[win_index])), np.array(time_taken[win_index]))
    plt.title('Time per Move')
    plt.ylabel('Time Taken (s)')
    plt.xlabel('Move Number')
    plt.xlim(0, len(time_taken[win_index]) - 1)
    plt.ylim(0, max(time_taken[win_index]))
    plt.savefig('data\\' + player1 + 'V' + player2 + 'TimeTakePerMove.png')
    plt.clf()

    # Makes a scatter plot of the time taken for each game
    plt.scatter(np.array(list(map(lambda time_list: len(time_list)-1, time_taken))),
                np.array(list(map(lambda time_list: sum(time_list), time_taken))))
    plt.title('Time per Game')
    plt.ylabel('Time Taken (s)')
    plt.xlabel('Move Amount per Game')
    plt.savefig('data\\' + player1 + 'V' + player2 + 'TimeTakePerGame.png')
    plt.clf()

    # Makes a plot of the amount of possible moves per move in the first game that player one won
    plt.plot(np.arange(0, len(moves_available[win_index])), np.array(moves_available[win_index]))
    plt.title('Possible Moves per Move')
    plt.ylabel('Amount of Possible Moves')
    plt.xlabel('Move Number')
    plt.xlim(0, len(moves_available[win_index]) - 1)
    plt.ylim(0, max(moves_available[win_index]))
    plt.savefig('data\\' + player1 + 'V' + player2 + 'MoveAmounts.png')

    # Saves the last game played as a gif
    # game.downloadGame("gamePossible7")
