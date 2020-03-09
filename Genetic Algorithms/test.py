index = [int(x) for x in input().split(", ")]
w = [int(c) for c in input().split()]
v = [int(c) for c in input().split()]

vt = 0
wt = 0
print(w)
print(v)
for j,i in enumerate(index):
    if i != 0:
        vt += v[j]
        wt += w[j]
print(vt, wt)
print(sum(w), sum(v))