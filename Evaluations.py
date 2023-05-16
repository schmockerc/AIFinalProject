from typing import List
import numpy as np


MAX_SCORE = 2147483647
MIN_SCORE = -2147483647


class EvaluationFunction:

    def __init__(self, eval_type="Basic", genetic_eval=None):
        if genetic_eval is None:
            genetic_eval = [[0]]
        self._eval_type = eval_type
        self._genetic_eval = np.array(genetic_eval, dtype=np.int32)
        self._piece_scores = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}
        self._position_scores = {'P': ((0, 4), (7, 7)), 'N': ((2, 2), (5, 5)), 'B': ((0, 0), (7, 4)),
                                 'R': ((0, 0), (7, 7)), 'Q': ((0, 0), (7, 7)), 'p': ((0, 0), (7, 4)),
                                 'n': ((2, 2), (5, 5)), 'b': ((0, 4), (7, 7)), 'r': ((0, 0), (7, 7)),
                                 'q': ((0, 0), (7, 7))}

    def evalState(self, state: List[List[chr]], current_player: chr, turn: int, check_mate: bool, cutoff: bool) -> int:
        if self._eval_type == "Basic":
            return self.basicEval(state, current_player, turn, check_mate, cutoff)
        elif self._eval_type == "Better":
            return self.betterEval(state, current_player, turn, check_mate, cutoff)
        elif self._eval_type == "Genetic":
            return self.geneticEval(state, current_player, turn, check_mate, cutoff)
        return 0

    def basicEval(self, state: List[List[chr]], current_player: chr, turn: int, check_mate: bool, cutoff: bool) -> int:
        score = (MAX_SCORE if ('W' if (turn - 1) % 2 == 0 else 'b') == current_player else MIN_SCORE) \
            if check_mate else 0
        score += MIN_SCORE * 0.75 if not check_mate and cutoff else 0
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
                if pos in self._piece_scores:
                    score += self._piece_scores[pos] * first_modifier if pos.isupper() else self._piece_scores[pos] * second_modifier
        return score

    def betterEval(self, state: List[List[chr]], current_player: chr, turn: int, check_mate: bool, cutoff: bool) -> int:
        score = (MAX_SCORE if ('W' if (turn - 1) % 2 == 0 else 'b') == current_player else MIN_SCORE) \
            if check_mate else 0
        score += MIN_SCORE * 0.75 if not check_mate and cutoff else 0
        for row in range(0, len(state)):
            for col in range(0, len(state[row])):
                if state[row][col] in self._piece_scores:
                    (x_one, y_one), (x_two, y_two) = self._position_scores[state[row][col]]
                    if x_one <= col <= x_two and y_one <= row <= y_two:
                        score += self._piece_scores[state[row][col]]
                    else:
                        score -= self._piece_scores[state[row][col]]
        return score

    def geneticEval(self, state: List[List[chr]], current_player: chr, turn: int, check_mate: bool, cutoff: bool) -> int:
        score = (MAX_SCORE if ('W' if (turn - 1) % 2 == 0 else 'b') == current_player else MIN_SCORE) \
            if check_mate else 0
        score += MIN_SCORE * 0.75 if not check_mate and cutoff else 0
        np_state = np.array(list(map(lambda lst: (list(map(lambda char: (ord(char) - 46), lst))), state)), dtype=np.int64)
        score += np.sum(self._genetic_eval * np_state)
        return score
