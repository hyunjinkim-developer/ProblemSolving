# Solution 1:
import heapq

N, M, C = 0, 0, 0
INF = int(1e9)

def get_input():
    global N, M, C

    N, M, C = map(int, input().split())

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        # From X to Y with weight pf Z
        X, Y, Z = map(int, input().split())
        graph[X][Y] = Z
    return graph, C

def dijkstra(graph, start_node):
    distance = [INF] * (N + 1)
    distance[start_node]

    queue = []
    heapq.heappush(queue, (0, start_node))
    while queue:
        saved_weight, node_with_shortest_path = heapq.heappop(queue)
        # Node already handled (with the shortest path)
        # On progress



def main():
    graph = get_input()
    dijkstra(graph, C)


if __name__ == "__main__":
    main()