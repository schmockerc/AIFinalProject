from ChessGame import ChessGame
from AlphaBeta import minimax_search
from typing import List
import random
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
    game = ChessGame(clone=True)
    # game.print()
    # print()
    while not game.is_cutoff() or game.getTurn() <= 100:
        currentPlayer = 'W' if game.getTurn() % 2 == 0 else 'b'
        if currentPlayer == 'W':
            game.move(minimax_search(game, currentPlayer, basicEval)[1])
        else:
            game.move(minimax_search(game, currentPlayer, basicEval)[1])
        print(game.getTurn())
        # print(currentPlayer + " - " + str(basicEval(game.getState(), currentPlayer, game.getTurn(), game.is_checkmate())))
        # game.print()
    game.print()
    # game.downloadGame("game")
