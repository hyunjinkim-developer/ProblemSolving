def get_input():
    N, M, K = map(int, input().split())

    ground = list()
    for _ in range(N):
        ground.append(list(map(int, input().split())))

    return N, M, K, ground

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

# head[sr, sc]가 주어졌을 때 그 팀의 팀원들 찾기
def detect_line(sr, sc):
    teammates = [(sr, sc)]

    # 머리에서 시작해서 꼬리를 향해(Head, Mid) 한칸씩 이동
    r, c = sr, sc
    while ground[r][c] != 3:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # within ground range
            if not in_range(nr, nc): continue
            # 3(nr, nc), 2, 1 / teammates = [1, 2] 형태일 때 2가 다음 위치 탐색 중
            # 2 -> 1로 돌아가는 경우를 막기 위해
            if len(teammates) >= 2 and (nr, nc) == teammates[-2]: continue
            # When Head and Tail meet
            # Head -> Tail traverse (Not to traverse Tail -> Head)
            if ground[r][c] == 1 and ground[nr][nc] == 3: continue
            # There's no player in new location
            if ground[nr][nc] not in [2, 3]: continue
            r, c = nr, nc # new location toward Tail
            break
        teammates.append((r, c))
    return teammates

# 모든 팀의 좌표를 찾기
def detect_whole_teams():
    teams = []
    for r in range(N):
        for c in range(N):
            # 모든 팀의 head 찾기
            if ground[r][c] == 1:
                # 각 팀의 팀원 찾기
                teams.append(detect_line(r, c))
    return teams

# teammates: Head -> Tail 순서로 저장됨
def move_one_team(teammates):
    # Find new Head location for Head
    r, c = teammates[0]
    for dx, dy in dirs:
        nr, nc = r + dx, c + dy
        if not in_range(nr, nc): continue
        if ground[nr][nc] not in [3, 4]: continue
        break
    # Found new Head location(nr, nc): 3 or 4
    new_coordinates = [] # new locations for teammates
    for teammate in teammates:
        cur_r, cur_c = teammate  # current location
        new_coordinates.append((nr, nc))
        nr, nc = cur_r, cur_c
        # 팀원들이 있던 위치를 4로 초기화
        # (head, tail이 만나지 않는 경우 이존에 tail이 있던 위치는 4로 바뀌어야 함)
        ground[cur_r][cur_c] = 4

    # Update ground
    for idx, (r, c) in enumerate(new_coordinates):
        # new Head location
        if idx == 0:
            ground[r][c] = 1
        # New Tail location
        elif idx == len(new_coordinates) - 1:
            ground[r][c] = 3
        # New Mid location
        else:
            ground[r][c] = 2

def move_whole_teams():
    # 1. 모든 팀을 찾고
    teams = detect_whole_teams()

    # 2. 한 칸씩 이동
    for teammates in teams:
        move_one_team(teammates)

# *
# 이동하는 좌표의 범위를 지정하고
# dr, rc를 구해서 player가 위치한 좌표만 탐색하는데
# 시작 점에서 끝점까지 iterate 하면서 충돌한 player 찾음
def throw_ball(round):
    # 공을 조건에 맞게 던지고, 충돌하는 좌표를 돌려주기
    # (r1, c1)에서 시작, (r2, c2) 방향으로 공 던지기
    round = round % (N * 4)
    if round < N: # r: round, c: [0, N -1]
        r1, c1 = round, 0
        r2, c2 = round, N
    elif round < N * 2: # r: [N - 1, 0], c: round - N
        r1, c1 = N - 1, round - N
        r2, c2 = -1, round - N
    elif round < N * 3: # r: (3 * N - 1) - round, c: [N - 1, 0]
        r1, c1 = (3 * N - 1) - round, N - 1
        r2, c2 = (3 * N - 1) - round, -1
    else: # r: [0, N - 1] , c: (4 * N - 1) - round
        r1, c1 = 0, (4 * N - 1) - roundg
        r2, c2 = N, (4 * N - 1) - round

    # (r1, c1)에서 시작, (r2, c2) 방향으로 공 던지기
    dr, dc = (r2 - r1) // N, (c2 - c1) // N
    r, c = r1, c1
    while (r, c) != (r2, c2):
        if ground[r][c] not in [0, 4]:
            return (r, c)
        r, c = r + dr, c + dc
    # If no player get the ball
    return None

def calculate(player_coordinates):
    teams = detect_whole_teams()
    for teammates in teams:
        #  enumerate(iterable, start=0)
        # Start: the index value from which the counter is to be started, by default it is 0
        for idx, teammate in enumerate(teammates, 1):
            if teammate == player_coordinates:
                # Reverse order from Head to Tail
                r1, c1 = teammates[0]
                r2, c2 = teammates[-1]
                # Change Head and Tail
                ground[r1][c1], ground[r2][c2] = ground[r2][c2], ground[r1][c1]
                # The player who get the ball is in idx order
                return idx * idx

def solution(N, M, K, round):
    answer = 0
    for round in range(0, K):
        # 각 팀을 한 칸 이동시키기
        move_whole_teams()
        # Throw ball
        player = throw_ball(round)
        # If no player get the ball
        if player is None:
            continue
        answer += calculate(player)

    return answer




# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

import collections
global N, M, K
global ground, dirs
dirs = [[1, 0], [0, 1], [-1, 0], [0 ,-1]]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # Get input
    N, M, K, ground = get_input()

    # Solution
    print(solution(N, M, K, ground))
    # ///////////////////////////////////////////////////////////////////////////////////