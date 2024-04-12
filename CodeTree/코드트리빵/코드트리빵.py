"""
# Solution 1:

from collections import defaultdict, deque

N, M = 0, 0

basecamp_loc = []
store_loc = dict()

current_location = dict()
arrived = 0
occupied = []
movable = []

def get_input():
    global N, M, basecamp_loc, store_loc, current_location, arrived, occupied, movable

    # Initialization
    N, M = 0, 0
    basecamp_loc = []
    store_loc = dict()

    current_location = dict()
    arrived = 0
    movable = []

    N, M = map(int, input().split())
    # 0의 경우에는 빈 공간, 1의 경우에는 베이스캠프
    for r in range(N):
        data = list(map(int, input().split()))
        for c in range(N):
            if data[c] == 1:
                basecamp_loc.append((r + 1, c + 1)) # Index starts from 1
    # Store location
    for idx in range(1, M + 1):
        r, c = map(int, input().split())
        store_loc[idx] = (r, c)

    movable = [[True] * (N + 1) for _ in range(N + 1)]


def in_range(r, c):
    global N
    return 1 <= r <= N and 1 <= c <= N

def find_shortest_distance(start, target):
    global N, movable
    distance = int(1e9)

    # The person arrived at the store
    if start == target:
        return 0

    start_r, start_c = start
    q = deque([(start, 0)])
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    visited[start_r][start_c] = True

    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while q:
        (r, c), dist = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if not movable[nr][nc]: continue
            if visited[nr][nc]: continue

            visited[nr][nc] = True
            new_distance = dist + 1
            q.append(((nr, nc), new_distance))
            if (nr, nc) == target:
                distance = min(distance, new_distance)
    return distance

def find_nearest_basecamp(person_idx):
    global basecamp_loc, store_loc, current_location, movable

    # 현재 시간이 t분이고 t ≤ m를 만족한다면,
    # t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
    # 여기서 가장 가까이에 있다는 뜻 역시 1에서와 같이 최단거리에 해당하는 곳을 의미합니다.
    store_r, store_c = store_loc[person_idx]
    min_distance = int(1e9)
    distance_to_basecamp = defaultdict(list)
    for r, c in basecamp_loc:
        if not movable[r][c]: continue
        distance = find_shortest_distance((r, c), (store_r, store_c))
        if distance <= min_distance:
            min_distance = distance
            distance_to_basecamp[min_distance].append((r, c))
    shortest_distance = min(distance_to_basecamp.keys())
    available_basecamp = distance_to_basecamp[shortest_distance]

    # 가장 가까운 베이스캠프가 여러 가지인 경우에는
    # 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 들어갑니다.
    # t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.
    def custom_sort(item):
        r, c = item
        return r, c
    available_basecamp = sorted(available_basecamp, key=custom_sort)

    # Save the person's location
    current_location[person_idx] = available_basecamp[0]
    return available_basecamp[0]

def move_person(person_idx):
    # 여기서 최단거리라 함은 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리를 뜻합니다.
    # 이동하는 도중 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우 역시 가능
    global current_location, movable

    r, c = current_location[person_idx]
    store_r, store_c = store_loc[person_idx]

    # 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
    # 최단거리로 움직이며 최단 거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다.
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    min_distance = int(1e9)
    next_move = (-1, -1)
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        if not movable[nr][nc]: continue

        distance = find_shortest_distance((nr, nc), (store_r, store_c)) #t
        if distance < min_distance:
            min_distance = distance
            next_move = (nr, nc)
    current_location[person_idx] = next_move

def find_person_arrived():
    # 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고,
    # 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
    # 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
    global current_location, store_loc, arrived

    arrived_person = []
    arrived_location = []
    for person_idx, (r, c) in current_location.items():
        if store_loc[person_idx] == (r, c):
            arrived_person.append(person_idx)
            arrived_location.append((r, c))

    for person_idx in arrived_person:
        arrived += 1
        current_location.pop(person_idx)
    return arrived_location

def main():
    time = 0
    global M, current_location, arrived, occupied, movable

    get_input()

    while True:
        time += 1

        # 1
        for person_idx in range(M + 1):
            if person_idx not in current_location.keys(): continue
            move_person(person_idx)

        # 2
        occupied = []
        arrived_location = find_person_arrived()
        occupied.extend(arrived_location)
        # Mark not movable locations
        for r, c in occupied:
            movable[r][c] = False

        # 3
        # print(3, '=' * 10)  # d
        # 현재 시간이 t분이고 t ≤ m를 만족한다면,
        # t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
        if time <= M:
            r, c = find_nearest_basecamp(time)
            movable[r][c] = False

        if arrived == M:
            print(time)
            return


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()
    # ///////////////////////////////////////////////////////////////////////////////////
"""


# Solution 2: Sample Solution
# #1 격자에 있는 사람들에 한하여 다음 움직일 위치
#     사람 위치를 기준으로 편의점 위치까지 상좌우하 우선순위대로 최단 거리 구하기
# #3 편의점으로부터 가장 가까운 베이스 캠프 고르기
#     편의점 위치를 시작으로 최단 거리 구하기

from collections import deque

cur_time = 0

N, M = 0, 0
grid = []
cvs_list = []

DEFAULT = (-1, -1)
people_loc = []

drs = [-1, 0, 0, 1]
dcs = [0, -1, 1, 0]
INT_MAX = int(1e9)

# #debug
# def print_matrix(matrix):
#     global N
#     for r in range(N):
#         for c in range(N):
#             print(matrix[r][c], end="\t")
#         print()
#     print('-'*10)


def get_input():
    global N, M, grid, cvs_list, people_loc, cur_time, DEFAULT

    # Initialization
    gird = []
    cvs_list = []
    cur_time = 0

    N, M = map(int, input().split())
    # 0이면 빈 칸, 1이면 베이스 캠프, 2라면 아무도 갈 수 없는 곳
    grid = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    for _ in range(M):
        r, c = map(int, input().split())
        cvs_list.append((r - 1, c - 1))

    people_loc = [DEFAULT] * M


def in_range(r, c):
    global N
    return 0 <= r < N and 0 <= c < N


def bfs_from_person(person, store):
    global drs, dcs, grid, INT_MAX, DEFAULT
    min_distane = INT_MAX

    visited = [[False] * N for _ in range(N)]

    q = deque()
    pr, pc = person
    q.append(((pr, pc), 0))
    visited[pr][pc] = True
    while q:
        (r, c), dist = q.popleft()
        if (r, c) == store and dist < min_distane:
            min_distane = dist

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue
            if grid[nr][nc] == 2: continue # occupied

            visited[nr][nc] = True
            new_dist = dist + 1
            q.append(((nr, nc), new_dist))
    return min_distane

# start_pos를 시작으로 하는 BFS를 진행합니다.
# 시작점으로부터의 최단거리 결과는 distance배열에 기록됩니다.
def bfs_from_store(start_pos, visited, distance):
    global N, drs, dcs, grid

    q = deque()
    q.append(start_pos)
    sr, sc = start_pos
    visited[sr][sc] = True
    distance[sr][sc] = 0

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue
            if grid[r][c] == 2: continue # occupied

            visited[nr][nc] = True
            distance[nr][nc] = distance[r][c] + 1
            q.append((nr, nc))

def simulate():
    global M, people_loc, grid, DEFAULT, INT_MAX, drs, dcs

    # Step 1. 격자에 있는 사람들에 한하여 편의점 방향을 향해 1칸 움직입니다.
    for person_idx in range(M):
        if people_loc[person_idx] == DEFAULT: continue
        if people_loc[person_idx] == cvs_list[person_idx]: continue

        pr, pc = people_loc[person_idx]
        sr, sc = cvs_list[person_idx]
        # 현재 위치에서 상좌우하 중 최단거리 값이 가장 작은 곳을 고르면
        # 그 곳으로 이동하는 것이 최단거리 대로 이동하는 것이 됩니다.
        # 그러한 위치 중 상좌우하 우선순위대로 가장 적절한 곳을 골라줍니다.
        min_distance = INT_MAX
        min_r, min_c = DEFAULT
        for dr, dc in zip(drs, dcs):
            nr, nc = pr + dr, pc + dc
            if not in_range(nr, nc): continue
            if grid[nr][nc] == 2: continue # occupied

            dist = bfs_from_person((nr, nc), (sr, sc))
            if dist < min_distance:
                min_distance = dist
                min_r, min_c = nr, nc
        people_loc[person_idx] = (min_r, min_c)

    # Step 2. 편의점에 도착한 사람에 한하여
    #         앞으로 이동 불가능하다는 표시로
    #         grid값을 2로 바꿔줍니다.
    for person_idx in range(M):
        if people_loc[person_idx] == cvs_list[person_idx]:
            pr, pc = people_loc[person_idx]
            grid[pr][pc] = 2

    # Step 3. 현재 시간 curr_t에 대해 curr_t ≤ m를 만족한다면
    #         t번 사람이 베이스 캠프로 이동합니다.
    if cur_time > M:
        return
    # Step 3-1. 편의점으로부터 가장 가까운 베이스 캠프를 고르기 위해
    #           편의점을 시작으로 하는 BFS를 진행합니다.
    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    person_idx = cur_time - 1
    bfs_from_store(cvs_list[person_idx], visited, distance)
    # Step 3-2. 편의점에서 가장 가까운 베이스 캠프를 선택합니다.
    #           r, c가 증가하는 순으로 돌리기 때문에
    #           가장 가까운 베이스 캠프가 여러 가지여도
    #           알아서 (행, 열) 우선순위대로 골라집니다.
    min_distance = INT_MAX
    min_r, min_c = DEFAULT
    for r in range(N):
        for c in range(N):
            if not visited[r][c]: continue
            if grid[r][c] != 1: continue
            if distance[r][c] < min_distance:
                min_distance = distance[r][c]
                min_r, min_c = r, c
    # 우선순위가 가장 높은 베이스 캠프로 이동합니다.
    people_loc[person_idx] = (min_r, min_c)
    # 해당 베이스 캠프는 앞으로 이동이 불가능한 칸임을 표시합니다.
    grid[min_r][min_c] = 2

# 전부 편의점에 도착헀는지를 확인합니다.
def end():
    global people_loc

    # 단 한 사람이라도
    # 편의점에 도착하지 못했다면
    # 아직 끝나지 않은 것입니다.
    for i in range(M):
        if people_loc[i] != cvs_list[i]:
            return False
    # 전부 편의점에 도착했다면 끝입니다.
    return True


def main():
    global cur_time

    get_input()

    while True:
        cur_time += 1
        simulate()
        if end():
            break
    print(cur_time)


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")
# answer
# 7
# 7
# 5

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()
    # ///////////////////////////////////////////////////////////////////////////////////

