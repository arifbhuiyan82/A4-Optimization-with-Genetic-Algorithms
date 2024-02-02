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

def crossover(parent1, parent2, CROSSOVER_RATE):
    if random.random() < CROSSOVER_RATE:
        cut = random.randint(0, len(parent1))
        child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
        return child
    return parent1

def mutate(chromosome, MUTATION_RATE):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def geneticAlgorithm(cities, POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS):
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
            parent1 = tournamentSelection(population, TOURNAMENT_SELECTION_SIZE)[1]
            parent2 = tournamentSelection(population, TOURNAMENT_SELECTION_SIZE)[1]
            child1 = crossover(parent1, parent2, CROSSOVER_RATE)
            child2 = crossover(parent2, parent1, CROSSOVER_RATE)
            mutate(child1, MUTATION_RATE)
            mutate(child2, MUTATION_RATE)
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
    POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS = get_user_input()
    cities = getCity("Qatar194.tsp")  # Make sure the file name matches your TSP file's name
    best_distance, best_route = geneticAlgorithm(cities, POPULATION_SIZE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, CROSSOVER_RATE, TARGET, MAX_GENERATIONS)
    drawMap(cities, [best_distance, best_route])
