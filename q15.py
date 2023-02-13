# BFS: same cost in every edge

from collections import deque

# Input
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

# Distance
distance = [-1] * (N + 1)
distance[X] = 1 # Assume distance from starting city to staring city 0

# BFS
q = deque([X])
while q:
    cur = q.popleft()
    # Check every city from current city
    for next_node in graph[cur]:
        # If not visited
        if distance[next_node] == -1:
            distance[next_node] = distance[cur] + 1
            q.append(next_node)

flag = False
for i in range(N + 1):
    if distance[i] == K:
        print(i)
        flag = True
# If none of cities meet requirements
if flag == False:
    print(-1)