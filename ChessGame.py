import chess.svg


# If this library isn't installed run 'pip install chess'

# Uncomment these if you want to save gifs of the games
# from cairosvg import svg2png
# import imageio
# import os
# import glob

def gameToState(ascii_state):
    state = [[]]
    for pos in list(str(ascii_state)):
        if pos == '\n':
            state.append([])
        elif pos != ' ':
            state[-1].append(pos)
    return state


class ChessGame:

    def __init__(self, max_depth):  # , evaluation):
        """
        The constructor which sets up all the basic aspects that will be used in the class
        :param max_depth: the max depth that the alpha beta algorithm will go
        """
        self._board = chess.Board()
        self._state = gameToState(str(self._board))
        self._max_depth = max_depth
        # self._eval = evaluation
        self._game = []
        self._game.append(str(chess.svg.board(self._board)))
        self._move_number = 0

    def is_cutOff(self, depth):
        """
        The is_cutOff method checks if the game can continue
        :param depth: the current depth of the alpha beta algorithm
        :return: the game should continue
        """
        game = self._board
        game_state = game.is_checkmate() or game.is_stalemate() or game.is_insufficient_material()
        return game_state or depth >= self._max_depth

    def is_checkmate(self):
        """
        The is_checkmate method returns if a player has checkmated another
        :return: a player checkmated another player
        """
        return self._board.is_checkmate()

    # def eval(self, state, current_player):
    #     """
    #     The eval method will run the given eval function using the given state and player
    #     :param state: a 2d string array of the board
    #     :param current_player: either white or black aka 'W' or 'b'
    #     :return: the value of the current board according to the eval function
    #     """
    #     return self._eval(state, current_player)

    def getMoves(self):
        """
        The getMoves method returns a list of possible moves to put into the move method
        :return: a list of chess.Move objects that are valid
        """
        return list(self._board.legal_moves)

    def move(self, move):
        """
        The move method will take in a chess.Move object and apply it to the board
        :param move: a chess.Move object that's legal in the games current state
        """
        self._board.push(move)
        self._game.append(str(chess.svg.board(self._board, arrows=[(move.from_square, move.to_square)])))
        self._move_number += 1

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
