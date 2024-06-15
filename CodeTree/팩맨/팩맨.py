"""
# 이 문제의 핵심 포인트
* DFS로 이동 가능한 모든 경우의 수를 돌면서 죽인 몬스터의 개수를 바로 계산 가능
    최대로 많이 죽인 몬스터의 수와 그 때의 이동방향을 저장
* 같은 위치에 같은 방향을 가리키는 여러 몬스터를 이동할 때, monster_move()를 한 번만에 처리
    알에서 몬스터로 몬스터 복제가 일어나면서 같은 위치, 같은 방향을 가진 여러개의 몬스터가 grid에 존재
    각 grid[r][c]에 defaultdict(int)를 넣어서 key: d, value: r, c에 위치하고 d방향을 가진 몬스터의 개수로 처리해서 time complexity 줄이기
    - [[0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0]]의 자료구조로도 저장 가능
       (r, c)에 위치한 0 ~ 7의 방향을 가진 몬스터의 개수를 3-dimensional array의 각 원소로 표현 가능
* 죽은 몬스터들의 자료구조
    monster_move()를 실행할 때 움직이려고 하는 칸에 죽은 몬스터가 존재하면 이동이 불가함
    - 아래 코드에서는 defaultdict(list)형태로 표현됨
        key: (r, c) := 몬스터의 위치,
        value := [2, 1, ...] 해당 위치에 존재하는 죽은 몬스터의 timelimt (value 리스트의 길이 := (r, c)에 위치하는 죽은 몬스터의 개수)
        - 이런 자료구조를 취하게 되면, 죽은 몬스터들을 없앨 때(time_limt을 줄일 때) 죽은 몬스터의 개수 번의 연산 필요
    - [[[2, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]] 형태로도 표현 가능
        [2, 1, 0] := (0, 0)에 위치하는 죽은 몬스터의 time_limt을 0인 몬스터 2개/ 1인 몬스터 1개/ 2인 몬스터 0개 의미
        - 이런 자료구조를 취하게 되면, 죽은 몬스터들을 없앨 때 최대 4 * 4 * 3번의 연산 필요

# Debugging에 오랜 시간이 걸린 이유:
1) 문제 잘 읽기!
pacman이 상좌하우의 우선순위로 3번을 움직이는데 '지나갔던 자리를 다시 지날 수 있다!'는 조건을
지나간 자리를 다시 지날 수 없는 것으로 이해해서 더 복잡하고 어렵게 풀었음.
2) (자료구조, 알고리즘) 설계를 잘 하자!
더 효율적인 연산을 위해 자료구조를 변경함
기존에 동작하던 코드를 새로운 자료구조에 맞게 변형하는 버그가 발생
동작하던 테스트케이스까지도 다시 확인해야해서 더 많은 시간이 소요됨.
"""

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3_Greedy
c, d, e = 1.0, 2.5_BFS-DFS, 3_Greedy.4_Simulation
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

from collections import deque, defaultdict


answer = 0
t = -1, -1
pacman = (-1, -1)
grid = [] # 3-dimensional array contains monster's direction
eggs = defaultdict(int) # (r, c, d)
dead = defaultdict(list) # key: location of dead monsters, value: time limit

m_dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] # 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
p_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상-좌-하-우


def print_grid(grid):
    for r in range(4):
        for c in range(4):
            print(grid[r][c], end=' ')
        print()
    print('-'*10)


def print_dict(dictionary):
    for key in dictionary.keys():
        print(key, ":", dictionary[key])

def get_input():
    global answer, t, pacman, grid, eggs, dead

    # Initialization
    answer = 0
    m, t = -1, -1
    pacman = (-1, -1)
    eggs = defaultdict(int)  # key: (r, c, d), value: count
    # 3-dimensional array contains monster's direction
    # grid = []
    # for row in range(4):
    #     grid_row = []
    #     for col in range(4):
    #         grid_row.append([])
    #     grid.append(grid_row)
    grid = [[ defaultdict(int) for c in range(4)]for r in range(4)]
    dead = defaultdict(list)  # key: location of dead monsters, value: time limit

    m, t = map(int, input().split())
    # Pacman location
    r, c = map(int, input().split())
    pacman = (r - 1, c - 1)
    # Monster location
    # 몬스터의 초기 위치와 팩맨의 초기 위치는 같을 수도 있습니다.
    for _ in range(m):
        # 방향 d는 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
        r, c, d = map(int, input().split())
        grid[r - 1][c - 1][d - 1] += 1 # direction index starts from 0


def in_range(r, c):
    return 0 <= r < 4 and 0 <= c < 4

def create_egg():
# 몬스터 복제 시도
    # 현재의 위치에서 자신과 같은 방향을 가진 몬스터를 복제
    # 복제된 몬스터는 아직은 부화되지 않은 상태로 움직이지 못합니다.
    # 복제된 몬스터는 현재 시점을 기준으로 각 몬스터와 동일한 방향을 지니게 되며,
    # 이후 이 알이 부화할 시 해당 방향을 지닌 채로 깨어나게 됩니다.
    global grid, eggs

    for r in range(4):
        for c in range(4):
            if len(grid[r][c]) == 0: continue
            for d, count in grid[r][c].items():
                eggs[(r, c, d)] += count

    if DEBUG:
        print("create_egg:")
        print(eggs)


def monster_move():
    # 몬스터 이동
    global grid

    def movable(nr, nc):
        # 격자를 벗어나는 방향일 경우
        if not in_range(nr, nc): return False
        # 움직이려는 칸에 몬스터 시체가 있거나
        if (nr, nc) in dead.keys(): return False
        # 팩맨이 있는 경우거나
        if (nr, nc) == pacman: return False
        return True

    def move(r, c, d):
        global m_dirs, dead, pacman

        # 현재 자신이 가진 방향대로 한 칸 이동
        cur_dr, cur_dc = m_dirs[d]
        r_cur_d, c_cur_d = r + cur_dr, c + cur_dc
        if movable(r_cur_d, c_cur_d):
            return r_cur_d, c_cur_d, d
        else:
        # 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단
            for i in range(1, 8):
                nd = (d + i) % 8
                dr, dc = m_dirs[nd]
                nr, nc = r + dr, c + dc
                if not movable(nr, nc): continue
                return nr, nc, nd
        # 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
        return r, c, d

    moved_grid = [[ defaultdict(int) for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if len(grid[r][c]) == 0: continue
            for d, count in grid[r][c].items():
                # 몬스터 이동
                nr, nc, nd = move(r, c, d)
                for _ in range(count):
                    moved_grid[nr][nc][nd] += 1

                if DEBUG:
                    print(f"count: {count}")
                    print(f"{r, c, d} -> {nr, nc, nd}")
    grid = moved_grid

    if DEBUG:
        print("monster move:", '*'*10)
        print("not allowed")
        print("pacman loc:", pacman)
        global dead
        print("dead:", dead)

        print_grid(grid)


"""
# 팩맨이 한 번 지나온 길을 다시 반복하지 않음
def pacman_move():
    # 팩맨 이동
    global pacman, p_dirs, grid, dead
    paths = defaultdict(list)  # key: dead, value: paths [(r1, c1), (r2, c2), (r3, c3)], ... ]
    r, c = pacman

    def count_monsters(r, c):
        total_count = 0
        for d, count in grid[r][c].items():
            total_count += count
        return total_count

    # 총 3칸을 이동, 각 이동마다 상하좌우의 선택지
    def bfs(dead_count, path, r, c):
        nonlocal paths

        if len(path) == 3:
            # if DEBUG:
            #     print(dead_count, path, r, c)

            # path is the same object, keep changing as recursively run bfs()
            paths[dead_count].append(path.copy())
            return

        for idx, (dr, dc) in enumerate(p_dirs): # 상-좌-하-우
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue

            visited[nr][nc] = True
            path.append(idx)
            dead_count += count_monsters(nr, nc)

            bfs(dead_count, path, nr, nc)

            visited[nr][nc] = False
            path.pop()
            dead_count -= count_monsters(nr, nc)

    visited = [[False] * 4 for _ in range(4)]
    # 팩맨은 알은 먹지 않으며,
    # 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
    visited[r][c] = True # pacman location
    for idx, (dr, dc) in enumerate(p_dirs): # 상-좌-하-우
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        if visited[nr][nc]: continue

        visited[nr][nc] = True
        dead_count, path = count_monsters(nr, nc), [idx]

        bfs(dead_count, path, nr, nc)

        visited[nr][nc] = False

    if DEBUG:
        print("pacman paths: ", "*"*10)
        print("prev pacman loc:", pacman)
        print_dict(paths)


    # 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게
    max_dead = max(paths.keys())
    # 상-좌-하-우의 우선순위를 가지며
        # 우선순위가 높은 순서대로 배열하면 "상상상 - 상상좌 - 상상하 - 상상우 - 상좌상 - 상좌좌 - 상좌하 - ..."
    max_dead_available_paths = paths[max_dead]
    def custom_sort(item):
        d1, d2, d3 = item
        return d1, d2, d3
    max_dead_paths = sorted(max_dead_available_paths, key=custom_sort)[0]
    if DEBUG:
        print("max dead paths:")
        # print(max_dead_available_paths)
        print(max_dead_paths)

    # 이동하는 칸(과정)에 있는 몬스터는 모두 먹어치운 뒤, 그 자리에 몬스터의 시체를 남깁니다.
    # 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
    new_r, new_c = r, c
    for d in max_dead_paths:
        dr, dc = p_dirs[d]
        new_r, new_c = new_r + dr, new_c + dc
        # 그 자리에 몬스터의 시체를 남깁니다.
        dead_count = len(grid[new_r][new_c])
        for _ in range(dead_count):
            # debris of dead monsters last to 2 turn, except this turn
            dead[(new_r, new_c)].append(3)
        # 이동하는 칸(과정)에 있는 몬스터는 모두 먹어치움
        grid[new_r][new_c] = defaultdict(int)
    # 팩맨의 위치 저장
    pacman = (new_r, new_c)

    if DEBUG:
        print("몬스터를 먹어 치움:")
        print_dict(dead)
        print_grid(grid)
        print(f"post pacman loc: {pacman}")
"""


def count_monsters(r, c):
    # Count monsters on (r, c)
    global grid

    total_count = 0
    for d, count in grid[r][c].items():
        total_count += count
    return total_count

def pacman_move():
    # 팩맨 이동
    global pacman, p_dirs, grid, dead
    pac_r, pac_c = pacman

    best_path = []
    max_dead = -1
    def dfs(r, c, path, dead_count):
        global p_dirs, grid
        nonlocal best_path, max_dead, pac_r, pac_c

        if len(path) == 3:
            if DEBUG:
                print("path:", path, "dead_count:", dead_count)

            if max_dead < dead_count:
                max_dead = dead_count
                best_path = path.copy()
            return

        # 상-좌-하-우의 우선순위를 가지며
        # 우선순위가 높은 순서대로 배열하면 "상상상 - 상상좌 - 상상하 - 상상우 - 상좌상 - 상좌좌 - 상좌하 - ..."
        for idx, (dr, dc) in enumerate(p_dirs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue

            dead_count_to_add = 0
            if (nr, nc) not in path:
                dead_count_to_add = count_monsters(nr, nc)
            path.append((nr, nc))
            dfs(nr, nc, path, dead_count + dead_count_to_add)
            path.pop()
    dfs(pac_r, pac_c, [], 0)
    if DEBUG:
        print(f"find pacman path: {best_path}", "*"*10)

    # 이동하는 칸(과정)에 있는 몬스터는 모두 먹어치운 뒤, 그 자리에 몬스터의 시체를 남깁니다.
    # 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
    for pac_r, pac_c in best_path:
        # pacman이 움직인 위치에 몬스터가 있으면
        if len(grid[pac_r][pac_c]) != 0:
            for _ in range(count_monsters(pac_r, pac_c)):
                # debris of dead monsters last to 2 turn, except this turn
                dead[(pac_r, pac_c)].append(3)
        grid[pac_r][pac_c] = defaultdict(int)
    # Update pacman position
    pacman = (pac_r, pac_c)

    if DEBUG:
        print("몬스터를 먹어 치움:")
        print_dict(dead)
        print_grid(grid)
        print(f"post pacman loc: {pacman}")


def destroy():
    # 몬스터 시체 소멸
    # 몬스터의 시체는 총 2턴동안만 유지
    global dead

    spots_to_clean = []
    for key in dead.keys():
        dead_monsters = dead[key] # before removing dead monsters
        dead_after_removed = [] # after removing dead monsters
        for prev_time_limit in dead_monsters:
            time_limit = prev_time_limit - 1
            # Current monster is completely destroyed
            if 0 < time_limit:
                dead_after_removed.append(time_limit) # pop with index
        # All monsters are completely destroyed
        if len(dead_after_removed) == 0:
            spots_to_clean.append(key)
        else:
            dead[key] = dead_after_removed
    # Clean spots where's no debris of dead monsters
    for r, c in spots_to_clean:
        dead.pop((r, c))

    if DEBUG:
        print("destroy dead monsters:", "*"*10)
        print_dict(dead)


def egg_to_monster():
    # 몬스터 복제 완성
    # 처음 복제가 된 몬스터의 방향을 지닌 채로 알 형태였던 몬스터가 부화
    global eggs, grid

    if DEBUG:
        print("egg to monster:", "*"*10)
        print("eggs:", eggs)

    r_c_d_pairs = deque(eggs.keys())
    while r_c_d_pairs:
        r, c, d = r_c_d_pairs.popleft()
        count = eggs[(r, c, d)]
        grid[r][c][d] += count
    # Empty eggs
    eggs = defaultdict(int)

    if DEBUG:
        print_grid(grid)


def count_survivors(answer):
    global grid

    for r in range(4):
        for c in range(4):
            answer += count_monsters(r, c)
    return answer


def solution():
    # t개의 턴이 지난 이후 격자에 살아남은 몬스터는 총 몇 마리인지 출력
    global t, answer

    for turn in range(1, t + 1):
        if DEBUG:
            # if 4 < turn:
            #     break
            print(f"turn: {turn}", "=" * 20)

        # 몬스터 복제 시도
        create_egg()

        # 몬스터 이동
        monster_move()

        # 팩맨 이동
        pacman_move()

        # 몬스터 시체 소멸
        destroy()

        # 몬스터 복제 완성
        egg_to_monster()

    # Count survived monsters
    answer = count_survivors(answer)
    print(answer)
    return
'''x
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.h
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")
# answer
# 5
# 9
# 36
# 10
# 6
# 8


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()
    DEBUG = False

    # if DEBUG:
    #     if test_case == 2:
    #         print(pacman)
    #         print_grid(grid)
    #         print(f"test case: {test_case}", "="*50)
    #         solution()

    solution()
    # ///////////////////////////////////////////////////////////////////////////////////
