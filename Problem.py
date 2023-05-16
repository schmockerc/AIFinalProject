from typing import List
from Evaluations import EvaluationFunction
from ChessGame import ChessGame
from AlphaBeta import alpha_beta_search
import chess
import random


class ChessGameProblem:

    """
    Class that represents a set of evaluation functions for analyzing a chess game.
    """

    def __init__(self, genome_size:int):
        """
        Initializes a BitString type search problem. The state objects are
        python lists of 1s or 0s
        :param genome_size: length of the state list
        """
        self._genome_size = genome_size

    def selection(self, current_population:List[List[List[int]]], weights:List[float],
                  num_parents:int) -> List[List[List[int]]]:
        """
        Performs selection on the passed in population.
        Makes use of the fitness_proportionate_selection method
        :param current_population: List of 8x8 matrices that work as evaluation functions
        :param weights: List of fitness values for each genome in current_population.
        Assumes bigger is better (maximization).
        :param num_parents: number of individuals to return from the selection
        :return:
        """
        ret = []
        for i in range(num_parents):
            index = self.fitness_proportionate_selection(current_population, weights)
            ret.append(current_population[index])
        return ret

    def fitness_proportionate_selection(self, current_population:List[List[List[int]]],
                                        weights:List[float]) -> int:
        """
        Performs fitness proportionate selection.
        :param current_population: List of 8x8 matrices that work as evaluation functions
        :param weights: List of fitness values for each genome in current_population.
        Assumes bigger is better (maximization).
        :return: index of individual to choose
        """
        weights_sum = sum(weights)
        adjusted_weights = [weights[0] / weights_sum]
        for i in range(1, len(weights)):
            adjusted_weights.append(adjusted_weights[i-1] + (weights[i] / weights_sum))
        chance = random.uniform(0, 1)
        index = 0
        while index < len(weights) and adjusted_weights[index] < chance:
            index += 1
        return index

    def crossover(self, parent1:List[List[int]], parent2:List[List[int]]) -> List[List[int]]:
        """
        Performs crossover on the two passed in parents.
        :param parent1: 8x8 matrices that work as an evaluation function
        :param parent2: 8x8 matrices that work as an evaluation function
        :return: child that is the combination of parent1 and parent2
        """
        return self.single_point_crossover(parent1, parent2, random.randint(0, 63))

    def single_point_crossover(self, parent1:List[List[int]], parent2:List[List[int]],
                               cross_point:int) -> List[List[int]]:
        """
        Performs single point crossover on the two passed in parents
        :param parent1: 8x8 matrices that work as an evaluation function
        :param parent2: 8x8 matrices that work as an evaluation function
        :param cross_point: Cross point.
        :return:child that is the combination of parent1 and parent2
        """
        child = [[random.randint(-10, 10) for _ in range(8)] for _ in range(8)]
        for i in range(0, 64):
            row = (i - (i % 8)) // (8 if (i - (i % 8)) >= 7 else 1)
            col = i % 8
            child[row][col] = parent1[row][col] if i < cross_point else parent2[row][col]
        return child

    def mutate(self, child:List[List[int]]) -> List[List[int]]:
        """
        Performs mutation of a genome
        :param child: 8x8 matrices that work as an evaluation function
        :return: Genome that has been mutated
        """
        # TODO: Implement a bit mutation where each bit has a 1/n chance of being mutated.
        #  To mutate a bit, call the mutate_bit method which is overridden in the child classes
        mutant = child.copy()
        for row in range(8):
            for col in range(8):
                if random.random() < 1 / 64:
                    mutant = self.mutate_bit(mutant, row, col)
        return mutant

    def evaluation(self, current: List[List[int]]) -> float:
        """
        Evaluates the current state and returns a score the represents
        the fitness of that state. Higher means better.
        :param current: 8x8 matrices that work as an evaluation function
        :return: Plays a game and returns value based on outcome
        """
        # TODO - copy your evaulation function from prior Lab here
        # TODO Implement a full playthorugh of a game that reutnr the output
        #  If win 1/# of turns
        #  If lose -1/# of turns
        #  If tie 0.0
        evaluation_function = EvaluationFunction("Genetic", current)
        game = ChessGame(clone=True, board=chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))
        currentPlayer = ''
        while not game.is_cutoff():
            currentPlayer = 'W' if game.getTurn() % 2 == 0 else 'b'
            if currentPlayer == 'W':
                game.move(alpha_beta_search(game, currentPlayer, evaluation_function)[1])
            else:
                game.move(random.choice(game.getMoves()))
        turn = game.getTurn()
        print(turn)
        return 0.0 if not game.is_checkmate() else (1.0/turn) if currentPlayer == 'W' else (-1.0/game.getTurn()())

    def successors(self, current: List[List[int]]) -> List[List[List[int]]]:
        """
        Creates a new list of states that are one step away from the current state
        :param current: 8x8 matrices that work as an evaluation function
        :return: List of neighboring states
        """
        successors = []
        n = self._genome_size
        for i in range (n):
            successor = current.copy()
            successor[random.randint(0, 7)][random.randint(0, 7)] = random.randint(-10, 10)
            successors.append(successor)
        return successors

    def random_state(self) -> List[List[int]]:
        """
        Generates a random state (i.e. genome) of the given size.
        :return: New random list of 8x8 matrices that work as an evaluation function of size self._genome_size
        """
        return [[random.randint(-10, 10) for _ in range(8)] for _ in range(8)]

    def mutate_bit(self, child: List[List[int]], bit_row: int, bit_col: int) -> List[List[int]]:
        """
        Performs a bit mutation on the passed in genome. Changes the
        bit at bit_index to one of the other moves in self._moves
        :param child: Genome which is a list of type T
        :param bit_index: Which bit to mutate
        :return: Genome that has been mutated
        """
        mutant = child.copy()
        mutant[bit_row][bit_col] = random.randint(-10, 10)
        return mutant
