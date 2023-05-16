from ChessGame import ChessGame
from Evaluations import EvaluationFunction
from typing import List, Any

DEPTH_LIMIT = 3


def alpha_beta_search(game: ChessGame, current_player: chr, evaluation_function: EvaluationFunction) -> List[Any]:
    """
    Start of the minimax algorithm
    :param evaluation_function: the evaluation function that returns an int based on the given state
    :param game: Instance of a game
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    value, move = max_value(game.copyGame(), 0, current_player, -9999, 9999, evaluation_function)
    if move is None:
        move = game.getMoves()[0]
    return [value, move]


def max_value(game: ChessGame, d: int, current_player: chr, alpha: int, beta: int,
              evaluation_function: EvaluationFunction) -> List[Any]:
    """
    Recursive function to find the max of possible successors
    to the game board.
    :param alpha: the value of the best alternative for max along the path to the root
    :param beta: the value of the best alternative for min along the path to the root
    :param evaluation_function: the evaluation function that returns an int based on the given state
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_cutoff() or d >= DEPTH_LIMIT:
        return [evaluation_function.evalState(game.getState(), current_player,
                                              game.getTurn(), game.is_checkmate(), game.is_cutoff()), None]
    v = -2147483648
    move = None
    for a in game.getMoves():
        v2, a2 = min_value(game.copyGame().move(a), d + 1, current_player, alpha, beta, evaluation_function)
        if v2 > v:
            v, move = v2, a
        alpha = max(alpha, v)
        if v >= beta:
            return [v, move]
    return [v, move]


def min_value(game: ChessGame, d: int, current_player: chr, alpha: int, beta: int,
              evaluation_function: EvaluationFunction) -> List[Any]:
    """
    Recursive function to find the min of possible successors
    to the game board.
    :param alpha: the value of the best alternative for max along the path to the root
    :param beta: the value of the best alternative for min along the path to the root
    :param evaluation_function: the evaluation function that returns an int based on the given state
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param current_player: ID of the max player and player for which utility
    scores are calculated. This can either be 0 or 1.
    :return: value and action that corresponds to the optimal move
    """
    if game.is_cutoff() or d >= DEPTH_LIMIT:
        return [evaluation_function.evalState(game.getState(), current_player,
                                              game.getTurn(), game.is_checkmate(), game.is_cutoff()), None]
    v = 2147483648
    move = None
    for a in game.getMoves():
        v2, a2 = max_value(game.copyGame().move(a), d + 1, current_player, alpha, beta, evaluation_function)
        if v2 < v:
            v, move = v2, a
        beta = min(beta, v)
        if beta <= alpha:
            break
    return [v, move]
