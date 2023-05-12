import chess.svg
from typing import List


# If this library isn't installed run 'pip install chess'

# Uncomment these if you want to save gifs of the games
# from cairosvg import svg2png
# import imageio
# import os
# import glob


def gameToState(ascii_state) -> List[chr]:
    state = [[]]
    for pos in list(str(ascii_state)):
        if pos == '\n':
            state.append([])
        elif pos != ' ':
            state[-1].append(pos)
    return state


class ChessGame:

    def __init__(self, board=chess.Board(),
                 game=None, move_number=0, clone=False):
        """
        The constructor which sets up all the basic aspects that will be used in the class
        :param max_depth: the max depth that the alpha beta algorithm will go
        """
        if game is None:
            game = []
        self._board = board
        self._state = gameToState(str(board))
        self._game = game
        self._clone = clone
        if not clone:
            self._game.append(str(chess.svg.board(self._board)))
        self._move_number = move_number

    def is_cutoff(self) -> bool:
        """
        The is_cutOff method checks if the game can continue
        :param depth: the current depth of the alpha beta algorithm
        :return: the game should continue
        """
        game = self._board
        game_state = game.is_checkmate() or game.is_stalemate() or game.is_insufficient_material()
        game_repeat = game.can_claim_threefold_repetition() or game.can_claim_fifty_moves()
        return game_state or game_repeat# or self._move_number >= 100

    def is_checkmate(self) -> bool:
        """
        The is_checkmate method returns if a player has checkmated another
        :return: a player checkmated another player
        """
        return self._board.is_checkmate()

    def getMoves(self) -> List[chess.Move]:
        """
        The getMoves method returns a list of possible moves to put into the move method
        :return: a list of chess.Move objects that are valid
        """
        return list(self._board.legal_moves)

    def move(self, move: chess.Move):
        """
        The move method will take in a chess.Move object and apply it to the board
        :param move: a chess.Move object that's legal in the games current state
        :return: a copy of the self
        """
        self._board.push(move)
        if not self._clone:
            self._game.append(str(chess.svg.board(self._board, fill=dict.fromkeys(list(filter(lambda valid_move: not self._board.piece_at(valid_move) is None, map(lambda possible_move: possible_move.to_square, list(self._board.legal_moves)))), ("#cc0000cc" if self._move_number % 2 == 0 else "#4dff00")), arrows=[(move.from_square, move.to_square)])))
        self._move_number += 1
        return self

    def copyGame(self):
        return ChessGame(self._board.copy(), [], self._move_number, True)

    def getState(self) -> List[chr]:
        return self._state

    def print(self):
        print(self._board)

    def getTurn(self):
        return self._move_number

    def getGame(self):
        return self._board

    # def downloadGame(self, file_name):
    #     """
    #     The downloadGame method takes in a file name and will turn the current game so far into a gif
    #     :param file_name: the name of the gif file that will be made
    #     """
    #     if os.path.exists(file_name + ".gif"):
    #         os.remove(file_name + ".gif")
    #     file_names = []
    #     for move in range(self._move_number + 1):
    #         file_names.append("game/move" + str(move) + ".png")
    #         svg2png(bytestring=(self._game[move]), write_to=(file_names[-1]), scale=2.5)
    #     frames = []
    #     for filename in file_names:
    #         frames.append(imageio.v2.imread(filename))
    #     imageio.mimsave(file_name + ".gif", frames, 'GIF', duration=len(frames)/1000000)
    #
    #     files = glob.glob('game/*')
    #     for f in files:
    #         os.remove(f)
