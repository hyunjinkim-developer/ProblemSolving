"""
성적을 비교한 결과가 M번 주어지고 이를 바탕으로
A번 학생의 성적이 B번 학생보다 낮다면 화살표가 A에서 B를 가리키도록 그래프를 그림.

학생들의 성적을 비교한 결과가 주어질 때,
성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성

Solution:
N <= 500이므로 O(V**3) = O(125 * 10^6) ~ O(10^8)
Floyd Warshall 사용 가능
"""

"""
# Solution 1:
N = 0
INF = int(1e9)

#debug
def print_matrix(matrix):
    global N, INF

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if matrix[row][col] == INF:
                print("INF", end='\t')
            else:
                print(matrix[row][col], end="\t")
        print()

def get_input():
    global N, INF
    N, M = map(int, input().split())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start][end] = 1
    return graph

def floyd_warshall(graph):
    global N, INF

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                if graph[a][k] == INF or graph[k][b] == INF: continue
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

def main():
    global N, INF

    graph = get_input()

    graph = floyd_warshall(graph)
    count_fixed_rank = 0
    for node in range(1, N + 1):
        from_node = 0
        for idx in range(1, N + 1):
            if graph[node][idx] == INF: continue
            if graph[node][idx] == 0: continue
            from_node += 1

        to_node = 0
        for idx in range(1, N + 1):
            if graph[idx][node] == INF: continue
            if graph[idx][node] == 0: continue
            to_node += 1

        if from_node + to_node == N - 1:
            count_fixed_rank += 1
    return count_fixed_rank
"""

# Solution 2: Sample Solution
# A에서 B로 도달 가능 || B가 A로 도달 가능 -> 성적 비교가 가능한 경우
# A에서 B로 도달 불가능 && B가 A로 도달 불가능 -> 성적 비교 결과를 알 수 없는 경우

N = 0
INF = int(1e9)

def get_input():
    global N

    N, M = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
    return graph

def floyd_warshall(graph):
    global N

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

def define_rank(graph):
    global N
    answer = 0

    for node in range(1, N + 1):
        count = 0
        # if the value is 0,
        # which means the node can reachable itself
        for idx in range(1, N + 1):
            if graph[node][idx] != INF or graph[idx][node] != INF:
                count +=1
        if count == N:
            answer += 1
    return answer

def main():
    graph = get_input()
    graph = floyd_warshall(graph)
    return define_rank(graph)


if __name__ == "__main__":
    print(main())