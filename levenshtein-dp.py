import numpy as np

str1 = input()
str2 = input()
n1 = len(str1)
n2 = len(str2)
# Matrix
m = np.zeros ((n1 + 1, n2 + 1), np.int8)

# filling first row
for i in range(n2 + 1):
    m[0, i] = i
# filling firts column
for i in range(n1 + 1):
    m[i, 0] = i

print(str1 + "/" + str2)
print(m)
print()

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if str1[i - 1] == str2[j - 1]:
            m[i, j] = m[i - 1, j - 1]
        else:
            m[i, j] = min(m[i - 1, j], m[i - 1, j - 1], m[i, j - 1]) + 1
    print(str1 + "/" + str2)
    print(m)
    print()

operations = []
i = n1; j = n2
while i != 0 or j != 0:
    if str1[i - 1] == str2[j - 1]:
        operations.append("Nothing on: " + str2[j - 1])
        i -= 1; j -= 1
    else:
        aux = [m[i - 1, j], m[i - 1, j - 1], m[i, j - 1]]
        opt = aux.index(min(aux))
        if opt == 0:
            operations.append("Insert: " + str1[i - 1])
            i -= 1
        elif opt == 1:
            operations.append("Replace: " + str2[j - 1] + " -> " + str1[i - 1])
            i -= 1; j -= 1
        elif opt == 2:
            operations.append("Remove: " + str2[j - 1])
            j -= 1

print("Converting " + str2 + " into " + str1 + " takes this operations: ")
for op in operations:
    print(op)