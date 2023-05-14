from Problem import ChessGameProblem
from typing import List


def Genetic_Algorithm(problem: ChessGameProblem, initial: List[List[List[int]]], num_epochs: int = 10, ):
    """
    Genetic Algorithm implementation
    :param problem: Class the posses attributes for the initial population and methods for GA operator
    :param initial: Initial population
    :param num_epochs: How many iterations
    :return: Individual with the best fitness found after num_epochs or until a solution is found
    """
    population = initial
    for epoch in range(0, num_epochs):
        weights = []
        for individual in population:
            weights.append(problem.evaluation(individual))
            if weights[len(weights) - 1] == 1.0:
                return individual
        population2 = []
        for i in range(0, len(population)):
            parent1 = population[problem.fitness_proportionate_selection(population, weights)]
            parent2 = population[problem.fitness_proportionate_selection(population, weights)]
            child = problem.crossover(parent1, parent2)
            child = problem.mutate(child)
            population2.append(child)
        population = population2
    best_individual = population[0]
    for individual in population:
        if problem.evaluation(individual) > problem.evaluation(best_individual):
            best_individual = individual
    return best_individual


if __name__ == '__main__':
    pop_size = 20
    # Setup a simulation with a set population size
    chess_game_problem = ChessGameProblem(pop_size)
    # Runs the genetic algorithm and prints out the found solution to then be put into main.py
    print(Genetic_Algorithm(chess_game_problem, [chess_game_problem.random_state() for _ in range(pop_size)]))
