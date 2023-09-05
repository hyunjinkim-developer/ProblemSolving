import sys

input = sys.std.readline # For faster input
INF = int(1e9) # Set infinite as 10^9:

# Get the number of nodes and edges
n, m = map(int, input().split()) # n: the number of nodes, m: the number of edges
# Get start node
start = int(input())

# list for adjcent nodes
graph = [[] for i in range(n + 1)]
# list for visited nodes
visited = [False] * (n + 1) # n + 1: for convenient acess with node number
# Initialize shortest path table
distance = [INF] * (n + 1)

# Get every nodes
for _ in range(m):
    # From a to b costs c
    a, b, c = map(int, input(), input().split())
    graph[a].append((b, c))


# Get the node index with shortest path among not visited nodes
def get_smallest_node():
    min_value = INF
    index = 0 # Index of the shortest path
    for i in range(n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # Initialize starting node
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[i]

    # Iterate over all nodes except starting node
    for i in range(n - 1):
        # Set the node with shortest path as visited
        now = get_smallest_node()
        visited[now] = True
        # Check other adjacent nodes
        cost = distance[now] + j[1]
        # Passing current nodes is more shorter 
        if cost < distance[j[0]]:
            distance[j[0]] = cost

# Run dijkstra
dijkstra(start)

# Print shortest path to every node
for i in range(1, n + 1):
    # Print INFINITY if the node is not reachable
    if distance[i] == INF:
        print("INFINTY")
    else:
        print(distance[i])
