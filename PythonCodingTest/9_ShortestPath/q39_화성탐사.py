"""
# Solution 1:
import heapq

N = 0

#debug
def print_matrix(matrix):
    global N
    for row in range(N):
        for col in range(N):
            print(matrix[row][col], end='\t')
        print()
    print('-'*10)

def get_input():
    global N

    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    return graph

def find_shortest_path(graph):
    global N
    count = 0#d

    INF = int(1e9)
    distance = [[INF] * (N) for _ in range(N)]
    distance[0][0] = graph[0][0]

    def in_range(row, col):
        return 0 <= row < N and 0 <= col < N
    # from up in clock-wise
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    while q:
        cur_distance, row, col = heapq.heappop(q)

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if not in_range(nr, nc): continue
            new_distance = min(distance[nr][nc], cur_distance + graph[nr][nc])
            if new_distance < distance[nr][nc]:
                distance[nr][nc] = new_distance
                heapq.heappush(q, (distance[nr][nc], nr, nc))
    return distance[N - 1][N - 1]

def main():
    graph = get_input()
    return find_shortest_path(graph)
"""


#Solution 2:
import heapq
import sys

N = 0

#debug
def print_matrix(matrix):
    global N
    for row in range(N):
        for col in range(N):
            print(matrix[row][col], end='\t')
        print()
    print('-'*10)

def get_input():
    global N
    input = sys.stdin.readline

    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    return graph

def find_shortest_path(graph):
    global N

    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    row, col = 0, 0 # Start location
    distance[row][col] = graph[row][col]
    q = [(graph[row][col], row, col)]

    def in_range(row, col):
        return 0 <= row < N and 0 <= col < N
    # from up in clock-wise
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        dist, row, col = heapq.heappop(q)
        # (0, 0)에서 (N - 1, N - 1)방향으로 최단거리를 찾으면서 piority queue에 push를 하기 때문에
        # 이미 찾아진 shortest path에 새로운 위치((nr, nc))의 weight을 더하면
        # 기존 경로에서의 최단거리보다 커질 수 밖에 없음
        # if distance[row][col] < dist: continue # 실질적으로 이 코드는 동작 하지 않음

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if not in_range(nr, nc): continue
            new_weight = dist + graph[nr][nc]
            if new_weight < distance[nr][nc]:
                distance[nr][nc] = new_weight
                heapq.heappush(q, (new_weight, nr, nc))
        #debug
        # print(heapq.nsmallest(len(q), q))
        # print_matrix(distance)
    return distance[N - 1][N - 1]

def main():
    graph = get_input()
    return find_shortest_path(graph)

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"test case: {test_case}", "-"*30)
        print(main())