# Get input()
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

location_count = 0
# from up in clockwise
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for r in range(n):
    for c in range(n):
        count = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if graph[nr][nc] == 1:
                count += 1

        if 3 <= count:
            location_count += 1
print(location_count)