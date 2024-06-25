import random
import math
import matplotlib.pyplot as plt

def getCity(problem_file):
    cities = []
    start_reading = False
    with open(problem_file, 'r') as f:
        for line in f:
            if line.strip() == "NODE_COORD_SECTION":
                start_reading = True
                continue
            if line.strip() == "EOF":
                break
            if start_reading:
                parts = line.strip().split()
                cities.append([parts[0], float(parts[1]), float(parts[2])])
    return cities

def get_user_input():
    POPULATION_SIZE = int(input("Enter POPULATION_SIZE: "))
    TOURNAMENT_SELECTION_SIZE = int(input("Enter TOURNAMENT_SELECTION_SIZE: "))
    MUTATION_RATE = float(input("Enter MUTATION_RATE: "))
    CROSSOVER_RATE = float(input("Enter CROSSOVER_RATE: "))
    TARGET = float(input("Enter TARGET: "))
    MAX_GENERATIONS = int(input("Enter MAX_GENERATIONS: "))
    return POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS

def select_tsp_file():
    while True:
        print("Select a TSP file:")
        print("1. it9.tsp")
        print("2. Qatar194.tsp")
        print("3. WesternSahara29.tsp")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            return "it9.tsp"
        elif choice == 2:
            return "Qatar194.tsp"
        elif choice == 3:
            return "WesternSahara29.tsp"
        else:
            print("Invalid choice. Please try again.")

def calcDistance(cities):
    total_sum = 0
    for i in range(len(cities) - 1):
        d = math.hypot(cities[i + 1][1] - cities[i][1], cities[i + 1][2] - cities[i][2])
        total_sum += d
    total_sum += math.hypot(cities[0][1] - cities[-1][1], cities[0][2] - cities[-1][2])
    return total_sum

def tournamentSelection(population, k):
    best = random.choice(population)
    for _ in range(k - 1):
        ind = random.choice(population)
        if ind[0] < best[0]:
            best = ind
    return best

def rouletteWheelSelection(population):
    max_fitness = sum(1.0 / individual[0] for individual in population)
    pick = random.uniform(0, max_fitness)
    current = 0
    for individual in population:
        current += 1.0 / individual[0]
        if current > pick:
            return individual

def pmxCrossover(parent1, parent2, CROSSOVER_RATE):
    if random.random() < CROSSOVER_RATE:
        size = len(parent1)
        child = [[-1, -1, -1] for _ in range(size)]
        cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))

        # Copy segment from parent1 to child
        for i in range(cxpoint1, cxpoint2):
            child[i] = parent1[i]

        # Mapping of the copied segment
        mapping = {}
        for i in range(cxpoint1, cxpoint2):
            mapping[tuple(parent1[i])] = tuple(parent2[i])

        # Fill the rest with parent2 respecting the mapping
        for i in range(size):
            if not (cxpoint1 <= i < cxpoint2):
                current = tuple(parent2[i])
                while current in mapping:
                    current = mapping[current]
                child[i] = list(current)
        return child
    return parent1

def oxCrossover(parent1, parent2, CROSSOVER_RATE):
    if random.random() < CROSSOVER_RATE:
        size = len(parent1)
        child = [[-1, -1, -1] for _ in range(size)]
        cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
        
        # Copy segment from parent1 to child
        child[cxpoint1:cxpoint2] = parent1[cxpoint1:cxpoint2]
        
        # Fill the rest with parent2
        fill_pos = cxpoint2 % size
        parent2_pos = cxpoint2 % size
        while child.count([-1, -1, -1]) > 0:
            if parent2[parent2_pos] not in child:
                child[fill_pos] = parent2[parent2_pos]
                fill_pos = (fill_pos + 1) % size
            parent2_pos = (parent2_pos + 1) % size
        return child
    return parent1

def swapMutation(chromosome, MUTATION_RATE):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def inversionMutation(chromosome, MUTATION_RATE):
    if random.random() < MUTATION_RATE:
        i, j = sorted(random.sample(range(len(chromosome)), 2))
        chromosome[i:j] = reversed(chromosome[i:j])

def applyMutations(chromosome, MUTATION_RATE):
    if random.random() < 0.5:
        swapMutation(chromosome, MUTATION_RATE)
    else:
        inversionMutation(chromosome, MUTATION_RATE)

def selectParent(population, SELECTION_METHOD_PROBABILITY, TOURNAMENT_SELECTION_SIZE):
    if random.random() < SELECTION_METHOD_PROBABILITY:
        return rouletteWheelSelection(population)[1]
    else:
        return tournamentSelection(population, TOURNAMENT_SELECTION_SIZE)[1]

def selectCrossover(parent1, parent2, CROSSOVER_RATE):
    CROSSOVER_METHOD_PROBABILITY = 0.5  # Fixed probability for choosing between PMX and OX
    if random.random() < CROSSOVER_METHOD_PROBABILITY:
        return pmxCrossover(parent1, parent2, CROSSOVER_RATE)
    else:
        return oxCrossover(parent1, parent2, CROSSOVER_RATE)

def geneticAlgorithm(cities, POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS):
    SELECTION_METHOD_PROBABILITY = 0.5  # Fixed probability for using Roulette Wheel Selection
    population = [[calcDistance(random.sample(cities, len(cities))), cities.copy()] for _ in range(POPULATION_SIZE)]
    best_distance = float('inf')
    best_route = None

    for generation in range(MAX_GENERATIONS):
        new_population = []
        population.sort(key=lambda x: x[0])
        if population[0][0] < best_distance:
            best_distance = population[0][0]
            best_route = population[0][1].copy()

        new_population.extend(population[:2])

        while len(new_population) < POPULATION_SIZE:
            parent1 = selectParent(population, SELECTION_METHOD_PROBABILITY, TOURNAMENT_SELECTION_SIZE)
            parent2 = selectParent(population, SELECTION_METHOD_PROBABILITY, TOURNAMENT_SELECTION_SIZE)
            child1 = selectCrossover(parent1, parent2, CROSSOVER_RATE)
            child2 = selectCrossover(parent2, parent1, CROSSOVER_RATE)
            applyMutations(child1, MUTATION_RATE)
            applyMutations(child2, MUTATION_RATE)
            new_population.append([calcDistance(child1), child1])
            new_population.append([calcDistance(child2), child2])

        population = new_population[:POPULATION_SIZE]

        if generation % 10 == 0 or population[0][0] < TARGET:
            print(f"Generation {generation}: Distance = {population[0][0]}")
            if population[0][0] < TARGET:
                break

    print(f"Optimal route distance: {best_distance}")
    print("Optimal route:", ' -> '.join([city[0] for city in best_route]))
    return best_distance, best_route

def drawMap(cities, solution):
    plt.figure(figsize=(10, 6))
    x, y = zip(*[(city[1], city[2]) for city in cities])
    plt.plot(x, y, 'ro')

    for i, city in enumerate(cities):
        plt.annotate(city[0], (city[1], city[2]))

    solution_cities = solution[1]
    for i in range(len(solution_cities) - 1):
        plt.plot([solution_cities[i][1], solution_cities[i + 1][1]], [solution_cities[i][2], solution_cities[i + 1][2]], 'k-')
    plt.plot([solution_cities[0][1], solution_cities[-1][1]], [solution_cities[0][2], solution_cities[-1][2]], 'k-')

    plt.title("TSP Solution")
    plt.show()

if __name__ == "__main__":
    tsp_file = select_tsp_file()
    POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS = get_user_input()
    cities = getCity(tsp_file)  # Use the selected TSP file
    best_distance, best_route = geneticAlgorithm(cities, POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS)
    drawMap(cities, [best_distance, best_route])
