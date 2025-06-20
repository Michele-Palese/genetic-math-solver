# Genetic Algorithm for Numerical Optimization
A simple Python-based evolutionary algorithm that evolves mathematical expressions to approximate a target value. This project demonstrates core concepts of genetic programming such as selection, crossover, and mutation using custom-defined expressions built from random numbers and operators.

## Featueres
- Initialization: a random population of individuals is generated. Each individual consists of a sequence of real numbers and operators forming a potentially valid mathematical expression.

- Fitness Evaluation: each individual's expression is evaluated numerically. The fitness is computed as the absolute distance between the evaluated result and the target value. Lower fitness means a better solution.

- Selection: the top 50% of the population with the best fitness (i.e., closest to the target) are selected to reproduce

- Crossover: Selected individuals are randomly combined to produce offspring, mixing their sequences of numbers and operations.

- Mutation: each offspring undergoes random mutations to introduce variability and avoid premature convergence.

 - Stopping Criteria: the algorithm runs for multiple generations. If the best fitness does not improve for a predefined number of consecutive generations, the algorithm terminates automatically.

## 📌 Configuration: 
All customizable parameters are defined in the configuration.py file, including:

- Range of numbers (A, B)

- Mutation rate (MUTATION_RATE)

- Population size (POPULATION_SIZE)

- Minimum and maximum individual expression sizes (MIN_SIZE, MAX_SIZE)

- Target value (TARGET)

- Allowed operators (OPERATION_SET)
