import random

POPULATION_SIZE = 100
GENOME_LENGTH = 30
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.6
GENERATIONS = 2000

# initialize genome
def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]

# initialize population
def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]

# fitness function
def fitness(genome):
    return sum(genome)

# select parent
def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness_values in zip(population, fitness_values):
        current += fitness_values
        if current > pick:
            return individual

# crossver
def crossver(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossver_point = random.randint(1, len(parent1) - 1)
        return parent1[:crossver_point] + parent2[crossver_point:], parent2[:crossver_point] + parent1[crossver_point:]
    else:
        return parent1, parent2

# mutation
def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = abs(genome[i] - 1)
    return genome
    
# main function
def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGTH)
    for generation in range(GENERATIONS):
        fitness_values = [fitness(genome) for genome in population]  # calculate fitness of population

        new_polulation = []                     # population of next generation
        for _ in range(POPULATION_SIZE //2):    # cause always take 2 parents
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            offspring1, offspring2 = crossver(parent1, parent2)
            new_polulation.extend([mutate(offspring1), mutate(offspring2)])

        population = new_polulation

        fitness_values = [fitness(genome) for genome in population]

        best_fitness = max(fitness_values)
        print(f"Generation {generation}: Best Fitness = {best_fitness}")

    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f'Best Index: {best_index}')
    print(f'Best Solution: {best_solution}')
    print(f'Best Fitness: {fitness(best_solution)}')

genetic_algorithm()