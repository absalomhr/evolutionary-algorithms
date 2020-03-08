# Capacity
c = int(input())
# Number of objects
n = int(input())
# Array of weights
w = [int(x) for x in input().split()]
# Array of values
v = [int(x) for x in input().split()]

cap = c
ratios = [(v[i]/w[i], v[i], w[i]) for i in range(len(w))]
ratios.sort(reverse=True)
selected_items = []
for item in ratios:
    if item[2] <= cap:
        cap -= item[2]
        selected_items.append((item[1], item[2]))

total_v = sum([item[0] for item in selected_items])
total_w = sum([item[1] for item in selected_items])

print("Given capacity: ", c)
print("Items sorted by ratio v/w: ", ratios)
print("Selected items: ", selected_items)
print("Total value: ", total_v)
print("Total weight: ", total_w)