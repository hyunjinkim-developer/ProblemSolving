N, M = 0, 0
graph = list()

def print_matrix(matrix):
    global N
    for r in range(N):
        print(matrix[r])

def in_range(r, c):
    global N, M
    return 0 <= r < N and 0 <= c < M

def dfs(v):
    global graph

    r, c = v

    # if current position is out of the graph
    if not in_range(r, c):
        return False

    if graph[r][c] == 0: # if current position is hollow
        graph[r][c] = 1 # fill with water

        # check adjacent positions to fill water
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # from up in clockwise
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            dfs((nr, nc))
        return True # when filled with water
    # if current position was wall
    return False

def main():
    global N, M, graph

    N, M = map(int, input().split())
    graph = []

    for c in range(N):
        graph.append(list(map(int, input())))

    result = 0
    for r in range(N):
        for c in range(M):
            if dfs((r, c)) == True:
                result += 1
    print(result)


if __name__ == "__main__":
    main()