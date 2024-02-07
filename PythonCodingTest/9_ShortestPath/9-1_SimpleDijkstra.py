import sys

input = sys.stdin.readline # For faster input
# Set maximum value for initialization
# infinite as 10^9 to find ShortestPath
INF = int(1e9)

# Get input
# Get the number of nodes and edges
N, M = map(int, input().split())
# Get start node
start = int(input())

# N + 1: for convenient access with node number
# list for adjacent nodes
graph = [[] for i in range(N + 1)]
# list for visited nodes
visited = [False] * (N + 1)
# Initialize the shortest path table as infinite
distance = [INF] * (N + 1)

# Get every node
for _ in range(M):
    # From start(s) to end(e) costs cost(c)
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

# Get the node index with the shortest path among not visited nodes
def get_smallest_node():
    # Initialization
    min_value = INF
    index = 0 # Index of the shortest path

    for i in range(N + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # Initialize starting node
    distance[start] = 0
    visited[start] = True
    for adjacent_node in graph[start]:
        end, cost = adjacent_node
        distance[end] = cost
    # Iterate over all nodes except starting node
    for i in range(N - 1):
        # Set the node with the shortest path as visited
        now = get_smallest_node()
        visited[now] = True
        # Check other adjacent nodes
        for adjacent_node in graph[now]:
            end, cost = adjacent_node
            now_cost = distance[now]
            new_cost = now_cost + cost
            if new_cost < distance[end]:
                distance[end] = new_cost


# main()
# Run dijkstra
dijkstra(start)

# Print shortest path to every node
for i in range(1, N + 1):
    # Print INFINITY if the node is not reachable
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])