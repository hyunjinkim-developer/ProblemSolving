from collections import deque
from math import floor

# Input
N, L, R = map(int, input().split())
map_matrix = list()
for _ in range(N):
    map_matrix.append(list(map(int, input().split())))
ROW, COL = len(map_matrix), len(map_matrix[0])

# Output
days_borders_opened = 0

def move_population(start_r, start_c, idx):
    # from up in clockwise
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def in_range(r, c):
        return 0 <= r < ROW and 0 <= c <COL

    united = list()
    united.append((start_r, start_c))

    queue = deque([(start_r, start_c)])
    union[start_r][start_c] = idx
    union_population = map_matrix[start_r][start_c]
    union_count = 1

    while queue:
        r, c = queue.popleft()
        current_population = map_matrix[r][c]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if union[nr][nc] != -1: continue # Union already assigned

            new_population = map_matrix[nr][nc]
            if L <= abs(new_population - current_population) <= R:
                queue.append((nr, nc))

                # Assign union
                union[nr][nc] = idx
                united.append((nr, nc))
                union_count += 1
                union_population += map_matrix[nr][nc]

    # Assign population
    union_avg_population = floor(union_population / union_count)
    for r, c in united:
        map_matrix[r][c] = union_avg_population


while True:
    # Initiate union index as -1
    union = [[-1] * COL for _ in range(ROW)]
    idx = 0
    for r in range(ROW):
        for c in range(COL):
            if union[r][c] == -1:
                move_population(r, c, idx)
                idx += 1
    # No union has organized
    if idx == ROW * COL:
        break
    days_borders_opened += 1

# main()
print(days_borders_opened)