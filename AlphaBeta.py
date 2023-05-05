from typing import Tuple, Any, List

import chess

DEPTH_LIMIT = 5

def minimax_search(game: chess.Board, current_player: int, eval) -> list[Any]:
    """
    Start of the minimax algorithm
    :param game: Instance of a game
    :param board: List of 0s, 1s, and 2s that represents the state of the board.
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    value, move = max_value(game, str(game), 0, current_player, eval)
    return [value, move]


def max_value(game, state, d, current_player, eval) -> list[Any]:
    """
    Recursive function to find the max of possible successors
    to the game board.
    :param game: Instance of a game
    :param board: List of 0s, 1s, and 2s that represents the state of the board.
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_checkmate() or game.is_stalemate() or game.is_insufficient_material() or d >= DEPTH_LIMIT:
        return [eval(state, current_player), None]
    v = -2147483648
    move = None
    for a in game.legal_moves:
        v2, a2 = min_value(game, game.result(state, a), d + 1, current_player)
        if v2 > v:
            v, move = v2, a
    return [v, move]


def min_value(game, state, d, current_player):
    """
    Recursive function to find the min of possible successors
    to the game board.
    :param game: Instance of a game
        :param board: List of 0s, 1s, and 2s that represents the state of the board.
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_cutoff(state, d):
        return [game.eval(state, current_player), None]
    v = 2147483648
    move = None
    for a in game.actions(state):
        v2, a2 = max_value(game, game.result(state, a), d + 1, current_player)
        if v2 < v:
            v, move = v2, a
    return [v, move]
