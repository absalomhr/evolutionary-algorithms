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
def get_totalx(chromo, denos, incre):
    div = incre
    start = 0
    tx = 0
    for d in denos:
        tx += d * int(chromo[start:div], base=2)
        start += incre
        div += incre
    return tx

def get_n_items(chromo, d_len, incre):
    div = incre
    start = 0
    n_items = 0
    for i in range(d_len):
        n_items += int(chromo[start:div], base=2)
        start += incre
        div += incre
    return n_items

def fitness_function(chromo, denos, total, c_len):
    incre = c_len // len(denos)
    totalx = get_totalx(chromo, denos, incre)
    n_sum = get_n_items(chromo, len(denos), incre)
    alpha = 1; betha = 1
    return alpha * abs(total - totalx) + betha * n_sum
    

def evaluate_population(chromosomes, demos, total, c_len):
    fitness_values = []
    for c in chromosomes:
        fitness_values.append(fitness_function(c, demos, total, c_len))
    return fitness_values

def generate_wheel_values(fitness_values):
    # Normalize fitness values
    sum_fit = sum(fitness_values)
    w_values = [1.0-(fv/sum_fit) for fv in fitness_values]
    return w_values

def choose_random_from_wheel(fitness_values):
    maxfv = 1.0
    spin = uniform(0, maxfv)
    current = 0
    for i in range(len(fitness_values)):
        current += fitness_values[i]
        if current > spin:
            return i

# print(create_chromosome(9))
# print(mutate_chromosome("000111", 6))
# print(crossover("000000", "111111", 6))
# print(fitness_function("010010010", [5,2,1], 9, 9))

# chromos = ["000111", "000001", "100000"]
# t = 10
# de = [5,2,1]
# c_len = 6

# fv = evaluate_population(chromos, de, t, c_len)
# print(fv)
# wv = generate_wheel_values(fv)
# print(wv)

# Inputs
total = int(input)
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

