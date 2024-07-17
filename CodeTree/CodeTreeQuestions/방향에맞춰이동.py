# Get input
n = int(input())
commands = []
for _ in range(n):
    d, count = input().split()
    count = int(count)
    commands.append((d, count))

y, x = 0, 0
direction = {"N": (1, 0),
             "E": (0, 1),
             "S": (-1, 0),
             "W": (0, -1)}
for d, count in commands:
    dy, dx = direction[d]
    dy, dx = dy * count, dx * count
    y, x = y + dy, x + dx
print(x, y)