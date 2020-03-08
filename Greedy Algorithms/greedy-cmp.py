# total
T = int(input())
# denominations
d = [int(x) for x in input().split()]
d.sort(reverse=True)

total = T
choosen = [0 for i in range(len(d))]
i = 0
while total != 0:
    if d[i] <= total:
        total -= d[i]
        choosen[i] += 1
    else:
        i += 1
print("Total: ", T)
print("Currencies: ")
for i,c in enumerate(choosen):
    print(d[i], c)