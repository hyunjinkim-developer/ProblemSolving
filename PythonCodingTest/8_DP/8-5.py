x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    # Current number - 1
    d[i] = d[i - 1] + 1
    # Current number is divided by 2
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # Current number is divided by 3_Greedy
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # Current number is divided by 5_BFS-DFS
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
