import numpy as np
# total
T = int(input())
# denominations
d = sorted([int(x) for x in input().split()])
# Matrix
m = np.zeros ((len(d), T + 1), np.int8)

for i in range(T + 1):
    m[0, i] = i
print(m, "\n")

for i in range(1, len(d)):
    for j in range(T + 1):
        if d[i] > j:
            m[i, j] = m[i-1, j]
        else:
            m[i, j] = min(m[i - 1 ,j], m[i, j - d[i]] + 1)
    print(m, "\n")
# Which coins were used
i = len(d) - 1; j = T; coins = [0 for i in range(len(d))]
while m[i, j] != 0:
    if m[i, j] < m[i - 1, j]:
        coins[i] += 1
        j -= d[i]
    else:
        i -= 1
print("Coins used: ")
for i,den in enumerate(d):
    print(den, coins[i])