import random

from ChessGame import ChessGame
from typing import List, Any

DEPTH_LIMIT = 3


def minimax_search(game: ChessGame, current_player: chr, evaluation) -> List[Any]:
    """
    Start of the minimax algorithm
    :param evaluation:
    :param game: Instance of a game
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    value, move = max_value(game.copyGame(), 0, current_player, evaluation)
    return [value, move]


def max_value(game: ChessGame, d: int, current_player: chr, evaluation) -> List[Any]:
    """
    Recursive function to find the max of possible successors
    to the game board.
    :param evaluation:
    :param game: Instance of a game
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_cutoff() or d >= DEPTH_LIMIT:
        return [evaluation(game.getState(), current_player, game.getTurn(), game.is_checkmate(), game.is_cutoff()), None]
    v = -2147483648
    move = None
    moveSet = []
    for a in game.getMoves():
        v2, a2 = min_value(game.copyGame().move(a), d + 1, current_player, evaluation)
        if v2 > v:
            v, move = v2, a
            moveSet = [[v, move]]
        elif v2 == v:
            moveSet.append([v2, a])
    return [v, move]


def min_value(game: ChessGame, d: int, current_player: chr, evaluation) -> List[Any]:
    """
    Recursive function to find the min of possible successors
    to the game board.
    :param evaluation:
    :param game: Instance of a game
    0s indicate where player 1 has moved, 1 indicates where player 2 has moved, and
    2s indicate an empty space
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_cutoff() or d >= DEPTH_LIMIT:
        return [evaluation(game.getState(), current_player, game.getTurn(), game.is_checkmate(), game.is_cutoff()), None]
    v = 2147483648
    move = None
    moveSet = []
    for a in game.getMoves():
        v2, a2 = max_value(game.copyGame().move(a), d + 1, current_player, evaluation)
        if v2 < v:
            v, move = v2, a
            moveSet = [[v, move]]
        elif v2 == v:
            moveSet.append([v2, a])
    return random.choice(moveSet)
