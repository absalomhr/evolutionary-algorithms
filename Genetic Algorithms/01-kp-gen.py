from random import randint

# Inputs
# Capacity, values, weights and number of objects
cap = int(input())
vals = [int(x) for x in input().split()]
weis = [int(x) for x in input().split()]
n = len(vals)

# Genetic Algorithm Setup and functions
# Chromosome functions
def create_chromosome(c_len):
    return [randint(0,1) for i in range(c_len)]

def mutate_chromosome(chromo, n):
    i = randint(0, n - 1)
    chromo[i] = 0 if chromo[i] == 1 else 1

def crossover(chromo1, chromo2):
    i = randint(1, n - 1)
    return chromo1[0:i] + chromo2[i:]

# Decoding functions
def get_value(chromo, vals):
    return sum([v for i,v in enumerate(vals) if chromo[i] != 0])

def get_weight(chromo, weis):
    return sum([w for i,w in enumerate(weis) if chromo[i] != 0])

def fitness_function(chromo, vals, weis, cap):
    return get_value(chromo, vals) - cap if get_weight(chromo, weis) > cap else get_value(chromo, vals)