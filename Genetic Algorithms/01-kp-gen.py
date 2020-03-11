from random import randint
from random import uniform
import operator

# Genetic Algorithm Setup and functions
# Chromosome functions
def create_chromosome(c_len):
    return [randint(0,1) for i in range(c_len)]

def mutate_chromosome(chromo, c_len):
    i = randint(0, c_len - 1)
    chromo[i] = 0 if chromo[i] == 1 else 1
    return chromo

def crossover(chromo1, chromo2, c_len):
    i = randint(1, c_len - 1)
    return chromo1[0:i] + chromo2[i:]

def generate_random_population(n, c_len):
    lst = []
    for i in range(n):
        lst.append(create_chromosome(c_len))
    return lst

# Decoding functions
def get_value(chromo, vals):
    return sum([v for i,v in enumerate(vals) if chromo[i] != 0])

def get_weight(chromo, weis):
    return sum([w for i,w in enumerate(weis) if chromo[i] != 0])

def fitness_function(chromo, vals, weis, cap):
    return get_value(chromo, vals) - (get_weight(chromo, weis)) if get_weight(chromo, weis) > cap else get_value(chromo, vals)

def evaluate_population(chromosomes, vals, weis, cap):
    fitness_values = []
    for c in chromosomes:
        fitness_values.append(fitness_function(c, vals, weis, cap))
    return fitness_values

def generate_wheel_values(fitness_values):
    # Normalize fitness values
    sum_fit = sum(fitness_values)
    w_values = [fv/sum_fit for fv in fitness_values]
    return w_values

def choose_random_from_wheel(fitness_values):
    maxfv = 1.0
    spin = uniform(0, maxfv)
    current = 0
    for i in range(len(fitness_values)):
        current += fitness_values[i]
        if current > spin:
            return i

# Inputs and setup
# Capacity, values, weights and number of objects
cap = int(input())
weis = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]

c_len = len(vals)

# Hyperparameters
n_chromosomes = 100
prob_mutation = 0.50
n_generations = 500
# Utility
# Makes sorting a little faste
ig = operator.itemgetter(1)

# Main program
first_gen = generate_random_population(n_chromosomes, c_len)
for g in range(n_generations):
    new_gen = []
    fitness_values = evaluate_population(first_gen, vals, weis, cap)
    # Sorting the chromosomes by their fitness value
    zipped = zip(first_gen, fitness_values)
    zipped = sorted(zipped, key=ig)
    first_gen, fitness_values = zip(*zipped)
    best_value = get_value(first_gen[-1], vals)
    best_weight = get_weight(first_gen[-1], weis)
    print("Generation {} -> Best result so far: {}, with the chromosome: {}, value and weight ({}, {})".format(g + 1, fitness_values[-1], first_gen[-1], best_value, best_weight))
    # Normalizing the fitness values from 0 to 1
    wheel_values = generate_wheel_values(fitness_values)
    # Elitism, best 2 chromosomes go directly to the next generation
    new_gen.append(first_gen[-1]); new_gen.append(first_gen[-2])
    for i in range(n_chromosomes - 2):
        p1 = first_gen[choose_random_from_wheel(wheel_values)]
        p2 = first_gen[choose_random_from_wheel(wheel_values)]
        child = crossover(p1, p2, c_len)
        if uniform(0, 1) <= prob_mutation:
           child = mutate_chromosome(child, c_len)
        new_gen.append(child)
    if g != n_generations - 1:
        first_gen = new_gen.copy()

for i in range(n_chromosomes - 1, 0, -1):
    best_value = get_value(first_gen[i], vals)
    best_weight = get_weight(first_gen[i], weis)
    if best_weight <= cap:
        print("Best compatible chromosome: {}, value: {}, weight: {}".format(first_gen[i], best_value, best_weight))
        nitems = first_gen[i].count(1)
        print("Items selected: ", nitems)
        for j,i in enumerate(first_gen[i]):
            if i != 0:
                print("({}, {})".format(weis[j], vals[j]), end=" ")
        break