"""
# Soltion 1:

N = 0
X, K = 0, 0
INF = int(1e9)

def print_matrix(matrix):
    global N
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            value = matrix[row][col]
            if value == INF:
                value = "INF"
            print(value, end='\t')
        print()
    print('-'*10)

def get_input():
    global N, X, K

    N, M = map(int, input().split())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0

    for _ in range(M):
        start, destination = map(int, input().split())
        print(start, destination)
        # 연결된 2개의 회사는 양방향으로 이동 가능
        graph[start][destination] = 1
        graph[destination][start] = 1

    X, K = map(int, input().split())
    print_matrix(graph)
    return graph

def floyd_warshall(graph):
    global N, X, K

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    print_matrix(graph)
    distance = graph[1][K] + graph[K][X]
    # Can't reach company X
    if 2 * INF <= distance:
        distance = -1
    return distance

def main():
    graph = get_input()

    answer = floyd_warshall(graph)
    return answer
"""


# Solution 2: Sample Solution
N = 0
X, K = 0, 0
INF = int(1e9)

def get_input():
    global N, X, K

    N, M = map(int,input().split())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0

    for _ in range(M):
        start, destination = map(int, input().split())
        # 연결된 2개의 회사는 양방향으로 이동 가능
        graph[start][destination] = 1
        graph[destination][start] = 1

    X, K = map(int, input().split())

    return graph

def floyd_warshall(graph):
    global N, X, K

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][K] + graph[K][X]
    # Max distance could be
    # Traverse every node with weight of 1 on every edge
    # Traverse node 1 -> K -> X
    # ((100 * 99 / 2) * 1) * 2 ~ 10 ** 4
    if INF <= distance:
        distance = -1
    return distance

def main():
    graph = get_input()

    answer = floyd_warshall(graph)
    return answer



if __name__ == "__main__":
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        print(f"test case: {test_case}", "-"*30)
        print(main())