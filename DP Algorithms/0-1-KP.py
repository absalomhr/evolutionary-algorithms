import numpy as np

# Capacity
c = int(input())
# Number of objects
n = int(input())
# Array of weights
w = [int(x) for x in input().split()]
# Array of values
v = [int(x) for x in input().split()]
# Matrix
m = np.zeros ((n + 1, c + 1), np.int8)

print(m, "\n")

for i in range(1, n + 1):
    for j in range(c + 1):
        index = i - 1
        if w[index] > j:
            m[i, j] = m[i-1, j]
        else:
            m[i, j] = max(m[i-1, j], m[i - 1, j - w[index]] + v[index])
    print(m, "\n")

i = n; j = c; res = []
while True:
    if m[i, j] == 0:
        break
    if m[i, j] == m[i - 1, j]:
        i -= 1
    else:
        res.append((w[i - 1], v[i - 1]))
        i -= 1; j -= w[i]
print("Items selected: ", len(res), res)
print("Total weight: ", sum([t[0] for t in res]))
print("Total value: ", sum([t[1] for t in res]))