A4: Optimization with Genetic Algorithms

Authors: MD ARIF ULLAH BHUIYAN & JULIO CÉSAR SIGUEÑAS PACHECO

Objective
The primary objective of this assignment is to implement a genetic algorithm (GA) to find an optimal solution for the Traveling Salesman Problem (TSP). The TSP aims to determine the shortest possible route that visits each city exactly once and returns to the origin city.

Traveling Salesman Problem (TSP)
The Traveling Salesman Problem (TSP) revolves around a collection of cities interconnected by respective distances, creating a comprehensive graph. The primary objective is to strategically order the cities to minimize the overall traveling time. The challenge lies in identifying an optimal route that visits each city precisely once and culminates at the starting point.

This problem encapsulates a fundamental question: "Given a network of cities and the distances between each pair, what is the most efficient route that ensures a visit to every city and returns to the origin?" The TSP's significance extends to its applicability in real-world scenarios, ranging from logistics and transportation planning to circuit design and manufacturing processes.

Genetic Algorithm
Genetic algorithms are a subset of evolutionary computing, an expanding field within artificial intelligence. Drawing inspiration from Darwin's evolutionary theory, genetic algorithms approach problem-solving as an evolutionary process.

The algorithm initiates with a set of solutions (represented as chromosomes) forming a population. Solutions from this population are utilized to create a new generation, aiming for an improved outcome. The selection of solutions to form new offspring is based on their fitness, favoring those better suited for reproduction.

Two fundamental parameters in genetic algorithms are crossover probability and mutation probability.

Crossover probability determines how frequently crossover is executed, where offspring can either be exact copies of parents or inherit parts of their chromosomes. A 100% crossover probability results in all offspring being generated through crossover, while 0% implies new generations are identical copies of the previous one.

Mutation probability dictates the likelihood of parts of a chromosome being mutated. A 100% mutation probability leads to an entire chromosome transformation, while 0% ensures no changes. Mutation serves to prevent the algorithm from getting stuck in local extremes but should not occur too frequently to avoid the algorithm devolving into random search.

Datasets
We will work with three distinct datasets for this assignment:

it9cities: Dataset available in a file named "it9.tsp". This dataset, renamed for easier identification and management as "it9," We have modified the dataset to calculate only 9 cities as far as our assignment instruction. This dataset can be accessed from this URL.

WI29 - Western Sahara: This dataset, renamed for easier identification and management as "WesternSahara29," can be accessed from this URL. It comprises 29 cities in Western Sahara, derived from data from the National Imagery and Mapping Agency database of geographic feature names. The dataset includes coordinates for each node in 2D space, with edge weight specified as Euclidean distance.

QA194 – Qatar: This dataset, also renamed for easier identification as "Qatar194," is available from this URL. It consists of 194 cities in Qatar, derived from data from the National Imagery and Mapping Agency database of geographic feature names. The dataset includes coordinates for each node in 2D space, with edge weight specified as Euclidean distance.

Parameter Combinations
We will explore six distinct sets of Genetic Algorithm parameters, denoted as Parameters1, Parameters2, and so forth. Each parameter set represents a different configuration of the genetic algorithm to optimize the TSP. Here are the parameter sets:

Parameters1:

POPULATION_SIZE: 150
TOURNAMENT_SELECTION_SIZE: 5
MUTATION_RATE: 0.05
CROSSOVER_RATE: 0.8
TARGET: 500.0
MAX_GENERATIONS: 1000
Parameters2:

POPULATION_SIZE: 250
TOURNAMENT_SELECTION_SIZE: 3
MUTATION_RATE: 0.2
CROSSOVER_RATE: 0.7
TARGET: 400.0
MAX_GENERATIONS: 800
Parameters3:

POPULATION_SIZE: 180
TOURNAMENT_SELECTION_SIZE: 4
MUTATION_RATE: 0.1
CROSSOVER_RATE: 0.9
TARGET: 480.0
MAX_GENERATIONS: 1200
Parameters4:

POPULATION_SIZE: 200
TOURNAMENT_SELECTION_SIZE: 6
MUTATION_RATE: 0.15
CROSSOVER_RATE: 0.85
TARGET: 420.0
MAX_GENERATIONS: 1000
Parameters5:

POPULATION_SIZE: 420
TOURNAMENT_SELECTION_SIZE: 5
MUTATION_RATE: 0.08
CROSSOVER_RATE: 0.75
TARGET: 460.0
MAX_GENERATIONS: 700
Parameters6:

POPULATION_SIZE: 500
TOURNAMENT_SELECTION_SIZE: 3
MUTATION_RATE: 0.12
CROSSOVER_RATE: 0.95
TARGET: 440.0
MAX_GENERATIONS: 600

Chromosome Representation: The chromosome represents a possible route for the salesman to visit each city exactly once and return to the starting city. Each gene in the chromosome corresponds to a city, and the order of genes represents the sequence in which the cities are visited.
Selection: Two selection techniques are implemented:

Tournament Selection: This method randomly selects a specified number of individuals (determined by TOURNAMENT_SELECTION_SIZE) from the population and chooses the fittest one among them.

Roulette Wheel Selection: This method selects individuals based on their fitness proportionate probability. Fitter individuals have a higher chance of being selected.
Elitism: The two fittest individuals from the previous generation are automatically included in the next generation without undergoing crossover or mutation.

Crossover: Two crossover techniques are implemented:

Partially Mapped Crossover (PMX): This method randomly selects a segment from one parent and maps it to the corresponding segment in the other parent. The remaining genes are then filled based on the mapping.

Order Crossover (OX): This technique randomly selects a segment from one parent and copies it to the child. The remaining genes are filled in the order they appear in the other parent, excluding duplicates.

Mutation: Two mutation techniques are implemented:

Swap Mutation: This method randomly selects two positions in the chromosome and swaps the cities at those positions.

Inversion Mutation: This technique randomly selects a segment of the chromosome and reverses the order of cities in that segment.

Population Size: The choice of population size is crucial as it affects the trade-off between exploration and convergence. Larger populations increase diversity and exploration, while smaller populations accelerate convergence. Adjustments in population sizes within the specified range allow for the exploration of different trade-offs between exploration and convergence speed.

Identifying Stationary State: The stationary state is identified by monitoring the distance of the fittest individual over generations. If the distance does not significantly improve over several generations, the system can be considered in a stationary state. The maximum number of generations allowed for each parameter set is indicated accordingly.

User Input for TSP File: The user is prompted to select one of the available TSP files (it9.tsp, Qatar194.tsp, or WesternSahara29.tsp). If an invalid choice is made, the user is asked to try again until a valid selection is made.
