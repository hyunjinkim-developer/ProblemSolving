from collections import defaultdict, deque

N, M, K, X = 0, 0, 0, 0
graph = defaultdict(list)

def get_input():
    global N, M, K, X, graph

    N, M, K, X = map(int, input().split())
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)

def main():
    global N, M, K, X, graph

    get_input()

    distance = [-1 for _ in range(N + 1)]
    distance[X] = 0

    q = deque([X])
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current_node] + 1
                q.append(next_node)

    # If there is a city with the shortest path of K
    check = False
    for i in range(1, N + 1):
        if distance[i] == K:
            print(i)
            check = True

    # if there's no available city
    if check == False:
        print(-1)

    print(f"shortest path: {distance}")










if __name__ == "__main__":
    main()