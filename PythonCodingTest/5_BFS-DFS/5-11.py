from collections import deque

N, M = 0, 0

def print_matrix(matrix):
    global N
    for r in range(N):
        print(matrix[r])

def in_range(r, c):
    global N, M
    return 0 <= r < N and 0 <= c < M

def dfs(graph):
    global N, M
    count = 1

    q = deque()
    q.append((count, (0, 0)))
    visited = [[False] * M for _ in range(M)]
    while q:
        count, (r, c) = q.popleft()
        # r, c = v
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue

            if nr == N - 1 and nc == M - 1:
                return count + 1
            q.append((count + 1, (nr, nc)))

def main():
    global N, M

    N, M = map(int, input().split())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, input())))

    print(dfs(graph))

if __name__ == "__main__":
    main()