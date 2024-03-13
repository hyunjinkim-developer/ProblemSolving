import sys

# Set maximum value for initialization
# infinite as 10^9 to find ShortestPath
INF = int(1e9)
N = 0

def print_list(list_):
    row = ["INF" if element == 1000000000 else element for element in list_]
    print(row)
    print("-"*10)

def get_inut():
    global N

    # For faster input
    input = sys.stdin.readline
    N, M = map(int, input().split())
    start_node = int(input())

    # N + 1: for convenient access with node number
    # 모든 리스트는 (노드의 개수 + 1)로 할당
    # (노드의 번호를 인덱스로 써서 바로 리스트에 접근 가능)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, destination, weight = map(int, input().split())
        graph[start].append((destination, weight))
    print(graph)
    return start_node, graph

def dijkstra(start_node, graph):
    global N

    # 모든 리스트는 (노드의 개수 + 1)로 할당
    # (노드의 번호를 인덱스로 써서 바로 리스트에 접근 가능)
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1) # Initialize as Infinite

    # Initialization
    visited[start_node] = True
    distance[start_node] = 0
    for dst, weight in graph[start_node]:
        distance[dst] = weight

    # Find node with the shortest path
    def get_node_shortest_path():
        min_value = INF
        node_idx = -1
        for i in range(1, N + 1): # 모든 리스트는 (노드의 개수 + 1)로 할당했으므로
            if not visited[i] and distance[i] < min_value:
                min_value = distance[i]
                node_idx = i
        return node_idx

    # Iterate N - 1 times (all nodes except start node)
    for _ in range(N - 1):
        # Find node with the shortest path
        current_node = get_node_shortest_path()
        current_weight = distance[current_node]
        visited[current_node] = True

        # Browse other adjacent nodes
        for adj_node, weight_to_adjacent_node in graph[current_node]:
            weight_of_adjcent_node = distance[adj_node]
            new_weight = current_weight + weight_to_adjacent_node
            if new_weight < weight_of_adjcent_node:
                distance[adj_node] = new_weight

    return distance

def main():
    global N

    start_node, graph = get_inut()
    distance = dijkstra(start_node, graph)

    for i in range(1, N + 1): # 모든 리스트는 (노드의 개수 + 1)로 할당했으므로
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


if __name__ == "__main__":
    main()
