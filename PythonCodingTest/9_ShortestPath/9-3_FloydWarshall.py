INF = int(1e9)
N = 0

def get_input():
    global N
    N = int(input())
    M = int(input())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # Initialization
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if row == col:
                graph[row][col] = 0

    for _ in range(M):
        start, destination, weight = map(int, input().split())
        graph[start][destination] = weight
    return graph

# Dab = min(Dab , Dak + Dkb)
def run_floyd_warshall(graph):
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][b] == INF:
                print("INFINITY", end='\t')
            else:
                print(graph[a][b], end='\t')
        print()
    return graph

def main():
    graph = get_input()
    graph = run_floyd_warshall(graph)

if __name__ == "__main__":
    main()