from individual import Individual
from population import Population
from configuration import POPULATION_SIZE, N_ITERATIONS , TARGET, PATIENCE

def run():
    population = Population(size=POPULATION_SIZE)
    patience_counter = 0
    best_fit = float('inf')

    for generation in range(N_ITERATIONS):
        population.evolve()
        population.sort()
        current_fit = population.best().fitness()

        # for ind in population.individuals:
        #     print(f'individual\'s lenght : {len(ind.numbers)}, eval {ind.evaluate()}')

        print(f"Generation {generation}, best eval: {population.best().numbers},  eval: {population.best().evaluate()}")

        if population.best().evaluate() == TARGET:
            print("EUREKA!")
            break

        if current_fit < best_fit:
            best_fit = current_fit
            patience_counter = 0
        else:
            patience_counter += 1

        if patience_counter >= PATIENCE:
            print(f"Early stopping at generation {generation}")
            break

    best = population.best()
    print(f"Best individual: {best.numbers} {best.operators}, value: {best.evaluate()}")
