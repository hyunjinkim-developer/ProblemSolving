import heapq
import sys

INF = int(1e9)
N = 0

def print_list(list_):
    print(["INF" if element == INF else element for element in list_])

# Print min heap implemented as heapq
def print_min_heap(queue):
    print(heapq.nsmallest(len(queue), queue))

def get_input():
    global N

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
    return start_node, graph

def dijkstra(start_node,graph):
    global N, INF

    # N + 1: for convenient access with node number
    distance = [INF] * (N + 1)
    distance[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))
    while queue:
        saved_weight, node_with_shortest_path = heapq.heappop(queue)
        # Node already handled (with the shortest path)
        if distance[node_with_shortest_path] < saved_weight: continue

        for adj_node, weight_to_adj_node in graph[node_with_shortest_path]:
            weight_of_adj_node = distance[adj_node]
            new_weight = saved_weight + weight_to_adj_node
            if new_weight < weight_of_adj_node:
                distance[adj_node] = new_weight
                heapq.heappush(queue, (new_weight, adj_node))

        # #debug
        # print_list(distance)
        # print_min_heap(queue)
    return distance

def main():
    global N

    start_node, graph = get_input()
    distance = dijkstra(start_node, graph)
    for i in range(1, N + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])

if __name__ == "__main__":
    main()