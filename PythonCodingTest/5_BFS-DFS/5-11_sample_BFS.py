from collections import deque

def main():
    N, M = map(int, input().split())
    graph = list()
    for i in range(N):
        graph.append(list(map(int, input())))

    # directions
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # if current position is out of graph
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                # if current position is a wall
                if graph[nx][ny] == 0: continue
                # if visit only for the first time, count for the shortest path
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        return graph[N - 1][M - 1]

    print(bfs(0, 0))

if __name__ == "__main__":
    main()