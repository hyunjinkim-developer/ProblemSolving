# Get input
n, m = map(int, input().split())
R, C = n, m

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

square = [[0 for _ in range(m)] for _ in range(n)]
r, c = 0, 0
d = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1 ,0)]

# Starting point
square[0][0] = 1
for num in range(2, n * m + 1):
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc
    if not in_range(nr, nc) or square[nr][nc] != 0:
        d = (d + 1) % 4

    dr, dc = dirs[d]
    r, c = r + dr, c + dc
    square[r][c] = num

# print square
for r in range(n):
    for c in range(m):
        print(square[r][c], end=' ')
    print()