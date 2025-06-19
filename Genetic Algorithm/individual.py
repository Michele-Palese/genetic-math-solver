import random
import numpy as np
from configuration import OPERATION_SET, A, B, MUTATION_RATE, TARGET , MIN_SIZE, MAX_SIZE, POPULATION_SIZE
INDIVIDUAL_SIZES  = [random.randint( MIN_SIZE , MAX_SIZE ) for _ in range(POPULATION_SIZE)]

class Individual:
    def __init__(self, numbers=None, operators=None,  size = None):
        self.numbers = numbers or list(np.random.uniform(A, B, size=size))
        self.operators = operators or random.choices(OPERATION_SET, k=size - 1)

    def evaluate(self):
        expr = str(self.numbers[0])
        for i, op in enumerate(self.operators):
            expr += op + str(self.numbers[i + 1])
        try:
            return round(eval(expr), 2)
        except ZeroDivisionError:
            return float('inf')

    def fitness(self, target=TARGET):
        result = self.evaluate()
        return abs(result - target) + len(self.numbers)

    def mutate(self):
        n_idx = len(self.numbers) - 1
        op_idx = len(self.operators) - 1

        if random.random() < MUTATION_RATE:
            k_num = int(MUTATION_RATE * n_idx) + 1
            mutate_idx = random.choices(range(n_idx), k=k_num)
            for i in mutate_idx:
                self.numbers[i] = random.uniform(A, B)

        if random.random() < MUTATION_RATE:
            k_op = int(MUTATION_RATE * op_idx) + 1
            mutate_idx = random.choices(range(op_idx), k=k_op)
            for i in mutate_idx:
                self.operators[i] = random.choice(OPERATION_SET)

    def crossover(self, other):
        max_point = min(len(self.numbers), len(other.numbers)) - 1
        point = random.randint(1, max_point)

        child1 = Individual(
            numbers=self.numbers[:point] + other.numbers[point:],
            operators=self.operators[:point] + other.operators[point:]
        )
        child2 = Individual(
            numbers=other.numbers[:point] + self.numbers[point:],
            operators=other.operators[:point] + self.operators[point:]
        )
        return child1, child2
