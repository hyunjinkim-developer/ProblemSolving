"""
# Solution 1:
from collections import defaultdict
import heapq

N = 0

def get_input():
    global N

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        # 양방향 통로
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    return graph

def dijkstra(graph):
    global N
    start_node = 1

    INF = int(1e9)
    distance = [INF] * (N + 1)
    distance[start_node] = 0

    q = []
    heapq.heappush(q, (0, 1))
    while q:
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] < current_distance: continue

        for adj_node in graph[current_node]:
            new_weight = current_distance + 1
            if new_weight < distance[adj_node]:
                distance[adj_node] = new_weight
                heapq.heappush(q, (new_weight, adj_node))

    # 첫 번째는 숨어야 하는 헛간 번호(1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단)를
    #   (만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력합니다)
    # 두 번째는 그 헛간까지의 거리를,
    # 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
    # Solution 1: O(3 * NlogN) ~ O(NlogN)
    #   Time complexity of sort() and sorted() is O(n log n) b/c they use Timsort
    counter = defaultdict(list)
    for i, shortest_distance in enumerate(distance): # O(NlogN)
        if shortest_distance == INF: continue
        counter[shortest_distance].append(i)
    def custom_sort(element): # O(NlogN)
        shortest_distance, list_ = element
        list_.sort() # O(NlogN)
        return shortest_distance * -1, list_
    counter = sorted(counter.items(), key=custom_sort)
    max_distance, huts = counter[0]
    hut_idx = huts[0]
    hut_count = len(huts)
    return print(hut_idx, max_distance, hut_count)

def main():
    graph = get_input()
    dijkstra(graph)
"""


# Solution 2:
import heapq
import sys

global N

def get_input():
    global N

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        # two-way
        graph[A].append((B, 1)) # From A to B in weight of 1
        graph[B].append((A, 1)) # From B to A in weight of 1
    return graph

def dijkstra(graph):
    global N
    start_node = 1

    INF = int(1e9)
    distance = [INF] * (N + 1)
    distance[start_node] = 0

    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        cur_distance, cur_node = heapq.heappop(q)
        if distance[cur_node] < cur_distance: continue

        for adj_node, weight in graph[cur_node]:
            new_weight = cur_distance + weight
            if new_weight < distance[adj_node]:
                distance[adj_node] = new_weight
                heapq.heappush(q, (new_weight, adj_node))
    
    # 첫 번째는 숨어야 하는 헛간 번호(1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단)를
    #   (만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력합니다)
    # 두 번째는 그 헛간까지의 거리를,
    # 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
    # Solution 2: O(N) (recommended)
    max_distance = 0
    target_hut_idx = 0
    huts_with_max_distance = []
    for i in range(1, N + 1):
        if max_distance < distance[i]:
            max_distance = distance[i]
            target_hut_idx = i # b/c iterate index number in ASC order
            huts_with_max_distance = [target_hut_idx]
        elif distance[i] == max_distance:
            huts_with_max_distance.append(i)
    return print(target_hut_idx, max_distance, len(huts_with_max_distance))

def main():
    graph = get_input()
    dijkstra(graph)


if __name__ == "__main__":
    main()