from random import randint
from random import uniform
import operator

def create_chromosome(c_len):
    c = ""
    for i in range(c_len):
        if randint(0, 1) == 1:
            c += "1"
        else:
            c += "0"
    return c

def mutate_chromosome(chromo, c_len):
    i = randint(0, c_len - 1)
    chromo = list(chromo)
    chromo[i] = "0" if chromo[i] == "1" else "1"
    return "".join(chromo)

def crossover(chromo1, chromo2, c_len):
    i = randint(1, c_len - 1)
    chromo1 = list(chromo1); chromo2 = list(chromo2)
    return "".join(chromo1[0:i] + chromo2[i:])

def generate_random_population(n, c_len):
    lst = []
    for i in range(n):
        lst.append(create_chromosome(c_len))
    return lst

# Decoding functions
def get_totalx(chromo, denos):
    incre = c_len // len(denos)
    div = incre
    start = 0
    tx = 0
    for d in denos:
        tx += d * int(chromo[start:div], base=2)
        start += incre
        div += incre
    return tx

def get_n_items(chromo, d_len):
    incre = c_len // len(denos)
    div = incre
    start = 0
    n_items = 0
    for i in range(d_len):
        n_items += int(chromo[start:div], base=2)
        start += incre
        div += incre
    return n_items

def fitness_function(chromo, denos, total, c_len):
    totalx = get_totalx(chromo, denos)
    n_sum = get_n_items(chromo, len(denos))
    alpha = 1; betha = 1
    return alpha * abs(total - totalx) + betha * n_sum
    

def evaluate_population(chromosomes, denos, total, c_len):
    fitness_values = []
    for c in chromosomes:
        fitness_values.append(fitness_function(c, denos, total, c_len))
    return fitness_values

def generate_wheel_values(fitness_values):
    # Normalize fitness values
    sum_fit = max(fitness_values)
    w_values = [((sum_fit + 0.10 * sum_fit)-fv) for fv in fitness_values]
    w_values = [x/sum(w_values) for x in w_values]
    return w_values

def choose_random_from_wheel(fitness_values):
    maxfv = sum(fitness_values)
    spin = uniform(0, maxfv)
    current = 0
    for i in range(len(fitness_values)):
        current += fitness_values[i]
        if current > spin:
            return i

# Inputs
total = int(input())
denos = [int(x) for x in input().split()]

# Hyperparameters
deno_chrono_len = 3
c_len = deno_chrono_len * len(denos)
n_chromosomes = 10
prob_mutation = 0.50
n_generations = 10

# Utility
# Makes sorting a little faste
ig = operator.itemgetter(1)

first_gen = generate_random_population(n_chromosomes, c_len)
for g in range(n_generations):
    new_gen = []
    fitness_values = evaluate_population(first_gen, denos, total, c_len)
    # Sorting the chromosomes by their fitness value
    zipped = zip(first_gen, fitness_values)
    zipped = sorted(zipped, key=ig, reverse=True)
    first_gen, fitness_values = zip(*zipped)
    best_total = get_totalx(first_gen[-1], denos)
    best_items = get_n_items(first_gen[-1], len(denos))
    print("Generation {} -> Best result so far: {}, with the chromosome: {}, totalx and nitems ({}, {})".format(g + 1, fitness_values[-1], first_gen[-1], best_total, best_items))
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