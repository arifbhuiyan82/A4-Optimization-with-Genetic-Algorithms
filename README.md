# Optimization with Genetic Algorithms

Students:MD ARIF ULLAH BHUIYAN & JULIO CÉSAR SIGUEÑAS PACHECO

Objective:
The aim of this assignment is to implement a genetic algorithm (GA) to find an optimal solution for the Traveling Salesman Problem (TSP). TSP involves determining the shortest possible route that visits each city exactly once and returns to the origin city.

TSP Problem:
The TSP revolves around a collection of cities interconnected by respective distances, creating a comprehensive graph. The primary objective is to strategically order the cities to minimize the overall traveling time. The challenge lies in identifying an optimal route that visits each city precisely once and culminates at the starting point. This problem finds applications in real-world scenarios such as logistics, transportation planning, circuit design, and manufacturing processes.

Genetic Algorithm:
Genetic algorithms are a subset of evolutionary computing, inspired by Darwin's evolutionary theory. The algorithm starts with a set of solutions (chromosomes) forming a population. Solutions from this population are utilized to create a new generation, aiming for an improved outcome. Selection of solutions for new offspring is based on their fitness.

Two fundamental parameters in genetic algorithms are crossover probability and mutation probability. Crossover probability determines how frequently crossover is executed, while mutation probability dictates the likelihood of parts of a chromosome being mutated.

Datasets:
1. TSP5cities: [Dataset Link](https://www.researchgate.net/figure/Coordinates-of-five-cities-on-A280tsp-dataset-TSPLIB_tbl1_327226141) - Represents the coordinates of five cities.
2. WesternSahara29: [Dataset Link](https://www.math.uwaterloo.ca/tsp/world/countries.html) - 29 Cities in Western Sahara, edge weight type specified as Euclidean distance in 2D space (EUC_2D).
3. Qatar194: [Dataset Link](https://www.math.uwaterloo.ca/tsp/world/countries.html) - 194 Cities in Qatar, edge weight type specified as Euclidean distance in 2D space (EUC_2D).

Parameter Combinations:
We explore six distinct sets of Genetic Algorithm parameters (Parameters1 to Parameters6) with variations in population size, tournament selection size, mutation rate, crossover rate, and target fitness.

Chromosome Representation:
The chromosome represents a possible route for the salesman to visit each city exactly once and return to the starting city. Each gene in the chromosome corresponds to a city, and the order of genes represents the sequence in which the cities are visited.
Selection Techniques:
- Tournament Selection: Randomly selects a specified number of individuals from the population and chooses the fittest one among them.
- Elitism: The two fittest individuals from the previous generation are automatically included in the next generation without undergoing crossover or mutation.

Crossover Techniques:
- Partially Mapped Crossover (PMX): Randomly selects a segment from one parent and maps it to the corresponding segment in the other parent. The remaining genes are then filled based on the mapping.
- Order Crossover (OX): Randomly selects a segment from one parent and copies it to the child. The remaining genes are filled in the order they appear in the other parent, excluding duplicates.

Mutation Techniques:
- Swap Mutation: Randomly selects two positions in the chromosome and swaps the cities at those positions.
- Inversion Mutation: Randomly selects a segment of the chromosome and reverses the order of cities in that segment.

Population Size:
We explore six different population sizes - 150, 250, 180, 200, 420, and 500. The choice of population size aims to strike a balance between exploration and exploitation.

Identifying Stationary State:
The stationary state is identified by monitoring the fittest individual's distance over generations. If the distance does not significantly improve over several generations, the system can be considered in a stationary state.

Results:
TSP5cities:
| Dataset       | Parameters  | Minimum Travel Distance |
|---------------|-------------|--------------------------|
| TSP5cities    | Parameters1 | 103.54                   |
| TSP5cities    | Parameters2 | 103.54                   |
| TSP5cities    | Parameters3 | 103.54                   |
| TSP5cities    | Parameters4 | 103.54                   |
| TSP5cities    | Parameters5 | 103.54                   |
| TSP5cities    | Parameters6 | 103.54                   |

WesternSahara29:
| Dataset          | Parameters  | Minimum Travel Distance |
|------------------|-------------|--------------------------|
| WesternSahara29  | Parameters1 | 37890.48                 |
| WesternSahara29  | Parameters2 | 29224.99                 |
| WesternSahara29  | Parameters3 | 32429.41                 |
| WesternSahara29  | Parameters4 | 29017.19                 |
| WesternSahara29  | Parameters5 | 29181.40                 |
| WesternSahara29  | Parameters6 | 37590.99                 |
Qatar194:
| Dataset       | Parameters  | Minimum Travel Distance |
|---------------|-------------|--------------------------|
| Qatar194      | Parameters1 | 42346.32                 |
| Qatar194      | Parameters2 | 42219.70                 |
| Qatar194      | Parameters3 | 40154.46                 |
| Qatar194      | Parameters4 | 38543.92                 |
| Qatar194      | Parameters5 | 36974.85                 |
| Qatar194      | Parameters6 | 38876.12                 |

### How to Use:
1. Clone the repository.
2. Run the genetic algorithm implementation with the desired parameters.
3. Analyze the results for minimum travel distance and explore the impact of different parameter combinations.

Feel free to explore the code and datasets to gain insights into solving the Traveling Salesman Problem using Genetic Algorithms!