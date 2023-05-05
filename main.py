from ChessGame import ChessGame
from AlphaBeta import minimax_search
from typing import List
import random
import chess


def basicEval(state: List[List[chr]], current_player: chr, turn: int, check_mate: bool) -> int:
    score = (1000 if ('W' if (turn - 1) % 2 == 0 else 'b') == current_player else -1000) if check_mate else 0
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
            match pos:
                case 'P':
                    score += (1 * first_modifier)
                case 'N':
                    score += (3 * first_modifier)
                case 'B':
                    score += (3 * first_modifier)
                case 'R':
                    score += (5 * first_modifier)
                case 'Q':
                    score += (9 * first_modifier)
                case 'p':
                    score += (1 * second_modifier)
                case 'n':
                    score += (3 * second_modifier)
                case 'b':
                    score += (3 * second_modifier)
                case 'r':
                    score += (5 * second_modifier)
                case 'q':
                    score += (9 * second_modifier)
    # Uncomment code if your using python 3.9
    # for row in state:
    #     for pos in row:
    #         if pos == 'P':
    #             score += (1 * first_modifier)
    #         elif pos == 'N':
    #             score += (3 * first_modifier)
    #         elif pos == 'B':
    #             score += (3 * first_modifier)
    #         elif pos == 'R':
    #             score += (5 * first_modifier)
    #         elif pos == 'Q':
    #             score += (9 * first_modifier)
    #         if pos == 'p':
    #             score += (1 * second_modifier)
    #         elif pos == 'n':
    #             score += (3 * second_modifier)
    #         elif pos == 'b':
    #             score += (3 * second_modifier)
    #         elif pos == 'r':
    #             score += (5 * second_modifier)
    #         elif pos == 'q':
    #             score += (9 * second_modifier)
    return score


if __name__ == '__main__':
    game = ChessGame(3)
    # game.print()
    # print()
    while not game.is_cutoff():
        currentPlayer = 'W' if game.getTurn() % 2 == 0 else 'b'
        if currentPlayer == 'W':
            game.move(minimax_search(game, currentPlayer, basicEval)[1])
        else:
            game.move(random.choice(game.getMoves()))
        print(game.getTurn())
        # print(currentPlayer + " - " + str(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate())))
        # game.print()
    print(game.is_checkmate())
    game.print()
    # game.downloadGame("game")
