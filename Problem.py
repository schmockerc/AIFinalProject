from typing import List
import random


class ChessGame:

    """
    Class the represents a BitSTring Problem that can be solved with a Local Search.
    Contains functions needed to manipulate a state (also called a genome) that is a python
    lists of 1s and 0s.
    """

    def __init__(self, genome_size:int):
        """
        Initializes a BitString type search problem. The state objects are
        python lists of 1s or 0s
        :param genome_size: lenght of the state list
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
        #TODO Check if this is correct
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
        # TODO: Implement fitness proportionate selection based on material from lecture
        # TODO Check if works
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
        #TODO Reimplement
        return parent1

    def single_point_crossover(self, parent1:List[List[int]], parent2:List[List[int]],
                               cross_point:int) -> List[List[int]]:
        """
        Performs single point crossover on the two passed in parents
        :param parent1: 8x8 matrices that work as an evaluation function
        :param parent2: 8x8 matrices that work as an evaluation function
        :param cross_point: Cross point.
        :return:child that is the combination of parent1 and parent2
        """
        #TODO Reimplement
        return parent1

    def mutate(self, child:List[List[int]]) -> List[List[int]]:
        """
        Performs mutation of a genome
        :param child: 8x8 matrices that work as an evaluation function
        :return: Genome that has been mutated
        """
        # TODO: Implement a bit mutation where each bit has a 1/n chance of being mutated.
        #  To mutate a bit, call the mutate_bit method which is overridden in the child classes
        # TODO Reimplement
        return child

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
        return 0.0

    def successors(self, current: List[List[int]]) -> List[List[List[int]]]:
        """
        Creates a new list of states that are one step away from the current state
        :param current: 8x8 matrices that work as an evaluation function
        :return: List of neighboring states
        """
        # TODO reimplement
        return [current]

    def random_state(self) -> List[List[int]]:
        """
        Generates a random state (i.e. genome) of the given size.
        :return: New random list of 8x8 matrices that work as an evaluation function of size self._genome_size
        """
        #TODO reimplement
        return [[0]]

    def mutate_bit(self, child: List[List[int]], bit_index: int) -> List[List[int]]:
        """
        Performs a bit mutation on the passed in genome. Changes the
        bit at bit_index to one of the other moves in self._moves
        :param child: Genome which is a list of type T
        :param bit_index: Which bit to mutate
        :return: Genome that has been mutated
        """
        # TODO - reimplement
        return child