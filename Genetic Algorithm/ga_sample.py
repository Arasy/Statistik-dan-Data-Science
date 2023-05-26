import random

# Function to calculate fitness for a chromosome
def calculate_fitness(chromosome):
    # Your fitness function logic here
    # Return a fitness score for the chromosome
    x = int(chromosome,2)/10
    fit = -(1 + x*(-3 + x*(1 + x*(-5 + x*(2)))))
    precission = 4
    return round(fit,precission)

# Function to perform crossover between two parent chromosomes
def crossover(parent1, parent2):
    # Your crossover logic here
    # Return two new offspring chromosomes
    swapping_point = random.randint(1, len(parent1) - 1)  # Randomly select the swapping point
    child1 = parent1[:swapping_point] + parent2[swapping_point:]  # Create the first offspring
    child2 = parent2[:swapping_point] + parent1[swapping_point:]  # Create the second offspring
    return child1, child2

# Function to perform mutation on a chromosome
def mutate(chromosome):
    # Your mutation logic here
    # Return the mutated chromosome
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < mutation_factor:  # Mutation factor of 10%
            mutated_bit = '0' if bit == '1' else '1'  # Flip the bit
        else:
            mutated_bit = bit
        mutated_chromosome += mutated_bit
    return mutated_chromosome

# Initialize population
population_size = 5
chromosome_length = 5
population = []

for _ in range(population_size):
    chromosome = ''.join(random.choice('01') for _ in range(chromosome_length))
    population.append(chromosome)

# Main genetic algorithm loop
generations = 10
best_fitness = float('-inf')
number_of_parents = 3
mutation_factor = 0.1
successive_same_fitness = 0
termination_flag = False

for generation in range(generations):
    # Calculate fitness for each chromosome in the population
    fitness_scores = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome)
        fitness_scores.append((chromosome, fitness))
    
    # Sort chromosomes by fitness in descending order
    fitness_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Select the best chromosomes for reproduction
    selected_chromosomes = [chromosome for chromosome, _ in fitness_scores[:number_of_parents]]
    
    # Create new offspring through crossover and mutation
    offspring = []
    while len(offspring) < population_size - number_of_parents:
        parent1 = random.choice(selected_chromosomes)
        parent2 = random.choice(selected_chromosomes)
        child1, child2 = crossover(parent1, parent2)
        offspring.extend([child1, child2])
        
    mutated_chromosomes = []
    for c in selected_chromosomes:
        c = mutate(c) if random.random() < 0.1 else c
        
    # Update the population with the new offspring
    population = selected_chromosomes + offspring
    
    # Keep track of the best fitness in the current generation
    current_best_fitness = fitness_scores[0][1]
    
    # Check if the termination condition is met
    if current_best_fitness == best_fitness:
        successive_same_fitness += 1
        if successive_same_fitness >= 3:
            termination_flag = True
    else:
        successive_same_fitness = 0
    
    # Update the best fitness
    best_fitness = current_best_fitness
    
    # Print the best fitness in each generation
    print(f"\nGeneration {generation + 1}: Best Fitness = {best_fitness}")

    # Print all chromosome in the population
    for c in fitness_scores:
        print(c[0],", fitness =",c[1])

    if termination_flag:
        print("Termination condition met. Exiting the loop.")
        break
