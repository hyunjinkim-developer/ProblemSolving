commands = list(input())

y, x = 0, 0
d = 0
dy, dx = 1, 0
# from up in clockwise
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for command in commands:
    if command == "L":
        d = (d - 1) % 4
        dy, dx = dirs[d]
    if command == "R":
        d = (d + 1) % 4
        dy, dx = dirs[d]
    if command == "F":
        y, x = y + dy, x + dx
print(x, y)