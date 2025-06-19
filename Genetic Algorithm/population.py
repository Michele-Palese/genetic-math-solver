from individual import Individual, INDIVIDUAL_SIZES
from configuration import MIN_SIZE, MAX_SIZE
import random


class Population:
    def __init__(self, size):
        self.individuals = [Individual(size=s) for s in INDIVIDUAL_SIZES]

    def sort(self):
        self.individuals.sort(key=lambda ind: ind.fitness())

    def best(self):
        return self.individuals[0]

    def evolve(self):
        self.sort()
        survivors = self.individuals[:len(self.individuals)//2]
        next_gen = survivors.copy()

        while len(next_gen) < len(self.individuals):
            parent1, parent2 = random.choices(survivors, k=2)
            child1, child2 = parent1.crossover(parent2)
            child1.mutate()
            child2.mutate()
            next_gen.extend([child1, child2])

        self.individuals = next_gen[:len(self.individuals)]
