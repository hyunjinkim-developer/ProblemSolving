# Soltuion 1:
N, M = 0, 0
start_row, start_col, start_direction = 0, 0, "d"
graph = []

def get_input():
    global N, M, start_row, start_col, start_direction, graph

    N, M = map(int, input().split())
    start_row, start_col, start_direction = map(int, input().split())

    # 0: 육지, 1: 바다
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

def simulate():
    global N, M, start_row, start_col, start_direction, graph
    answer = 1 # 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지

    dirs = {0: (-1, 0),  # north
            1: (0, 1),  # east
            2: (1, 0),  # south
            3: (0, -1)}  # west
    def find_next_direction(dir):
        new_dir = (dir - 1) % 4 # -1 % 4 := 3
        return dirs[new_dir], new_dir

    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M

    r, c, d = start_row, start_col, start_direction
    dr, dc = dirs[d]
    turn_count = 0
    while True:
        # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우
        if turn_count == 4:
            # 바라보는 방향을 유지한 채로 한 칸 뒤로 가고
            dr, dc = dr * -1, dc * -1
            nr, nc = r + dr, c + dc
            # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
            if graph[nr][nc] == 1:
                return answer
            # 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
            else:
                r, c = nr, nc
                answer += 1
                turn_count = 0

        # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다
        (dr, dc), new_dir = find_next_direction(d)
        nr, nc = r + dr, c + dc
        # To handle exception: index out of range
        if not in_range(nr, nc):
            turn_count += 1
            continue

        if graph[nr][nc] == 0: # Land
            graph[r][c] = 1  # Check the location as visited
            r, c, d = nr, nc, new_dir
            answer += 1
            turn_count = 0
            continue
        else: # Sea
            turn_count += 1
            continue

def main():
    get_input()
    print(simulate())



"""
# Solution 2:
N, M = 0, 0

def in_range(r, c):
    global N, M
    return 0 <= r < N and 0 <= c < M

def main():
    answer = 1
    global N, M

    N, M = map(int, input().split())

    r, c, d = map(int, input().split())
    current_direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    d_r, d_c = current_direction[d]

    map_ = list()
    for _ in range(N):
        map_.append(list(map(int, input().split())))

    # Set visited as value of 2
    map_[r][c] = 2

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    count = 1
    while True:
        if count == 4:
            r, c = r + (nr * -1), c + (nc * -1)
            if map_[r][c] == 1:
                break
            answer += 1
            count = 0
            continue

        # Turn left
        for idx, dir in enumerate(dirs):
            dir_r, dir_c = dir
            if d_r == dir_r and d_c == dir_c:
                d_r, d_c = dirs[(idx + 1) % 4]
                break

        nr, nc = r + d_r, c + d_c
        if not in_range(nr, nc):
            count += 1
            continue

        if map_[nr][nc] == 0:
            r, c = nr, nc
            map_[nr][nc] = 2
            answer += 1
            count = 0
            continue
        if map_[nr][nc] == 2 or map_[nr][nc] == 1:
            count += 1
    print(answer)
"""

"""
# Solution 3: Sample Solution with handling index out of range exception
# nonlocal VS global:
# reference: https://stackoverflow.com/a/71878951
# nonlocal:
#     already bound in the enclosing namespace
#     (otherwise an syntaxError will be raised)
# global:
#     does not require the variable is pre-bound
#     (it will create a new binding in the global namespace if the variable is not pre-bound)

def main():
    N, M = map(int, input().split())
    answer = 1

    visited = [[0] * M for _ in range(N)]
    r, c, direction = map(int, input().split())
    # Current position is already visited
    visited[r][c] = 1

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    def turn_left():
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3
    def in_range(r, c):
        return 0 <= r < N and 0 <= c < N

    # Start simulation
    turn_count = 1
    while True:
        # Cannot move in all directions
        if turn_count == 4:
            nr, nc = r - dr[direction], c - dc[direction]
            # Can move back(b/c it's land) in current direction
            if graph[nr][nc] == 0:
                r, c = nr, nc
            # Cannot move back b/c it's water
            else:
                break
            turn_count = 0

        turn_left()
        nr, nc = r + dr[direction], c + dc[direction]
        if not in_range(nr, nc):
            turn_count += 1
            continue

        # Move when new location is not visited and is not water
        if visited[nr][nc] == 0 and graph[nr][nc] == 0:
            visited[nr][nc] = 1
            r, c = nr, nc
            answer += 1
            turn_count = 0
            continue
        else:
            turn_count += 1

    print(answer)
"""

"""
# Solution 4: Sample Solution
def main():
    N, M = map(int, input().split())
    answer = 1

    visited = [[0] * M for _ in range(N)]
    r, c, direction = map(int, input().split())
    # Current position is already visited
    visited[r][c] = 1

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    def turn_left():
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3

    # Start simulation
    turn_count = 1
    while True:
        turn_left()
        nr, nc = r + dr[direction], c + dc[direction]

        # Move when new location is not visited and is not water
        if visited[nr][nc] == 0 and graph[nr][nc] == 0:
            visited[nr][nc] = 1
            r, c = nr, nc
            answer += 1
            turn_count = 0
            continue
        else:
            turn_count += 1

        # Cannot move in all directions
        if turn_count == 4:
            nr, nc = r - dr[direction], c - dc[direction]
            # Can move back(b/c it's land) in current direction
            if graph[nr][nc] == 0:
                r, c = nr, nc
            # Cannot move back b/c it's water
            else:
                break
            turn_count = 0

    print(answer)
"""



if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"test case: {test_case}")
        main()