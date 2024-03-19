"""
X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면,
- 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
- 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요
- 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
    (1 ≤ N ≤ 30,000, 1 ≤ M ≤ 200,000, 1 ≤ C ≤ N)

C라는 도시에서 위급 상황이 발생했다. 최대한 많은 도시로 메시지를 보내고자 한다.
- 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며
- 도시들이 모두 메시지를 받는 데까지 걸리는 시간
    (도달할 수 있는 노드 중에서, 가장 멀리있는 노드의 최단 거리)
은 얼마인지 계산하는 프로그램을 작성

Solution:
- 한 도시에서 다른 도시까지의 최단 거리 문제
- N, M의 범위가 충분히 크기 때문에
    - Dijkstra simple implementation: O(V**2) ~ O(9 * 10^8)
    - (recommended) Dijkstra Faster implementation:
        O(ElogV) ~ O((2 * 10^5) * (10^2 * log3)) ~ O(2log3 * 10^7)

"""

"""
# Solution 1:
import heapq

N, C = 0, 0
INF = int(1e9)

#debug
def print_min_heap(queue):
    print(heapq.nsmallest(len(queue), queue))

def get_input():
    global N, C

    N, M, C = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        # From X to Y with weight of Z
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))
    return graph, C

def dijkstra(graph, start_node):
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

        for adjacent_node, weight_to_adjacent_node in graph[node_with_shortest_path]:
            weight_of_adjacent_node = distance[adjacent_node]
            new_weight = saved_weight + weight_to_adjacent_node
            if new_weight < weight_of_adjacent_node:
                distance[adjacent_node] = new_weight
                heapq.heappush(queue, (new_weight, adjacent_node))

        print_min_heap(queue)
    print(distance)
    return distance
    
def main():
    graph, C = get_input()
    distance = dijkstra(graph, C)

    reachable_city = 0
    max_arriving_time = 0
    for city_idx, time in enumerate(distance):
        if time == INF: continue
        if city_idx == C: continue # starting city
        reachable_city += 1
        max_arriving_time = max(max_arriving_time, time)
    print(reachable_city, max_arriving_time)
"""

# Solution 2: Sample Solution
import heapq
import sys
N = 0
INF = int(1e9)

def get_input():
    global N
    N, M, C = map(int, input().split())
    start_node = C

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        # From X to Y in weight of Z
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))
    return graph, start_node

def dijkstra(graph, start_node):
    global N

    distance = [INF] * (N + 1)
    distance[start_node] = 0

    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        # Extracted (shortest distance, node) pair from the priority queue
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] < current_distance: continue

        for adjacent_node, weight in graph[current_node]:
            new_weight = current_distance + weight
            if new_weight < distance[adjacent_node]:
                distance[adjacent_node] = new_weight
                heapq.heappush(q, (new_weight, adjacent_node))
    return distance

def main():
    graph, start_node = get_input()
    distance = dijkstra(graph, start_node)

    # 도달할 수 있는 노드의 개수
    reachable_city = 0
    max_arriving_time = 0
    for city_idx, time in enumerate(distance):
        if city_idx == start_node: continue
        if time == INF: continue
        reachable_city += 1
        max_arriving_time = max(max_arriving_time, time)
    print(reachable_city, max_arriving_time)


if __name__ == "__main__":
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        print(f"test case: {test_case}", "-"*30)
        main()