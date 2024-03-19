"""
* 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있습니다
모든 도시의 쌍(A, B )에 대해서 도시 A에서 B로 가는 데 필요한 비용의 최솟값을 구하는 프로그램을 작성
Solution:
- Floyd Warshall algorithm
"""

"""
# Solution 1:
N = 0
INF = int(1e9)

def print_matrix(matrix):
    global N
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if matrix[row][col] == INF:
                print("INF", end='\t')
            else:
                print(matrix[row][col], end='\t')
        print()

def get_input():
    global N, INF

    N = int(input())
    M = int(input())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0
    for _ in range(M):
        # from a to b in weight of c
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
    return graph

# Dab = min(Dab , Dak + Dkb)
def floyd_warshall(graph):
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

def main():
    global N

    graph = get_input()
    graph = floyd_warshall(graph)

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if graph[row][col] == INF:
                print(0, end=" ")
            else:
                print(graph[row][col], end=" ")
        print()
"""


# Solution 2: Sample Solution
N = 0
INF = int(1e9)
graph = []

def get_input():
    global N, INF, graph

    N = int(input())
    M = int(input())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        # Several edges provided
        # To get the shortest path,
        # the edge of the smallest weight should be selected
        graph[a][b] = min(graph[a][b], c)
    return graph

# Dab = min(Dab , Dak + Dkb)
def floyd_warshall(graph):
    global N

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

def main():
    global N, INF

    graph = get_input()
    graph = floyd_warshall(graph)
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if graph[row][col] == INF:
                print(0, end=' ')
            else:
                print(graph[row][col], end=' ')
        print()


if __name__ == "__main__":
    main()