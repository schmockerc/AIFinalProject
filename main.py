import random

import chess

from ChessGame import ChessGame

if __name__ == '__main__':
    game = ChessGame(5)
    while not game.is_checkmate():
        game = ChessGame(5)
        while not game.is_cutOff(3):
            game.move(random.choice(game.getMoves()))
    # game.downloadGame("game")
