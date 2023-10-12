# SWEA 모의 SW역량 테스트 baseline

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

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
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

# User defined functions
# Debugging purposes
def print_matrix(matrix):
    width = 5
    for r in range(N):
        for c in range(N):
            # print("{0: <{width}}".format(str(matrix[r][c]), width=width), end=" ")
            print("{0: <{width}}".format(matrix[r][c], width=width), end=" ")
        print()

# Get input
def get_input():
    N, M, K = map(int, input().split())

    ground = list()
    for _ in range(N):
        ground.append(list(map(int, input().split())))

    return N, M, K, ground


def dfs(current_location, ground, head, visited):
    # Traverse ends when visit the start location !
    if current_location == [-1, -1]:
        return head, visited

    r, c = current_location[0], current_location[1]
    visited[r][c] = True
    # Find head
    if ground[r][c] < ground[head[0]][head[1]]:
        head = [r, c]

    next_location = next_move(current_location, ground, visited)
    head, visited = dfs(next_location, ground, head, visited)
    return head, visited

def next_move(start, ground, visited):
    # Move in up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr, nc = start[0] + dr[i], start[1] + dc[i]
        # Whether new location is within ground
        if not (0 <= nr <= (N - 1) and 0 <= nc <= (N - 1)): continue
        # If there is no path in new location
        if ground[nr][nc] == 0: continue
        # If already visited
        if visited[nr][nc] == True: continue

        else:
            return [nr, nc]

    return [-1, -1] # If there's no more location to visit


def find_path_and_head(start, ground, head):
    # Trace each teams path
    visited = [[False] * N for _ in range(N)]

    visited[start[0]][start[1]] = True

    nr, nc = next_move(start, ground, visited)
    head, visited = dfs([nr, nc], ground, head, visited)

    return head, visited

def find_next_player(start, path, ground, visited_find_next_player):
    # Move in up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr, nc = start[0] + dr[i], start[1] + dc[i]
        # Whether new location is within ground
        if not (0 <= nr <= (N - 1) and 0 <= nc <= (N - 1)): continue
        # Follow only path
        if path[nr][nc] == False: continue
        # If there is no player
        if ground[nr][nc] == 4: continue
        # If head and tail meet, traverse in head -> mid -> tail
        if ground[start[0]][start[1]] == 1 and ground[nr][nc] == 3: continue
        if ground[start[0]][start[1]] == 3 and ground[nr][nc] == 1: continue
        # If already visited
        if visited_find_next_player[nr][nc] == True: continue

        # Follow next sequence player
        else:
            return [nr, nc]

    return [-1, -1] # If there's no more location to visit

def find_players(head, path, ground):
    visited_find_next_player = [[False] * N for _ in range(N)]

    team = collections.defaultdict(list)
    player_location = head
    while player_location != [-1, -1]:
        # head of the current team
        r, c = player_location[0], player_location[1]
        team[ground[r][c]].append([r, c])
        visited_find_next_player[r][c] = True

        player_location = find_next_player(player_location, path, ground, visited_find_next_player)

    return team

def update_total_path(path, total_visited):
    # Update current team's path in total visited path
    for r in range(N):
        for c in range(N):
            if path[r][c] == True:
                total_visited[r][c] = True
    return total_visited


# Find players location for each team
def initialize(M, ground):
    teams = list()

    total_visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if ground[r][c] != 0 and total_visited[r][c] == False:
                # Find path and head player
                head = [r, c]
                head, path = find_path_and_head([r, c], ground, head)

                # Find players for each team
                team = find_players(head, path, ground)
                teams.append(team)

                # Update visited locations
                total_visited = update_total_path(path, total_visited)

    return teams

def move(ground, teams):
    # For each team
    for team in teams:
        # Move toward head position for 1 step
        head = team[1][0] # team[1]: [[r, c]]
        # Find movable location
        next_head = [-1, -1]
        # Head Tail meet
        head_tail_meet = False
        # Move in up, right, down, left
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr, nc = head[0] + dr[i], head[1] + dc[i]
            # If new location is not within ground
            if not(0 <= nr <= N - 1 and 0 <= nc <= N - 1): continue

            if ground[nr][nc] == 4:
                next_head[0], next_head[1] = nr, nc
                break
            # Head and tail can meet: ground[nr][nc] == 3
            if ground[nr][nc] == 3:
                head_tail_meet = True
                next_head[0], next_head[1] = nr, nc
                break

        destinations = []
        destinations.append(next_head)
        # Save locations of previous head and mid
        for sequence in range(1, 3):
            for location in team[sequence]:
                destinations.append(location)
        prev_tail = team[3][0] # team[3]: [[r, c]]

        # Move
        # 3명 이상이 한 팀
        # 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지
        team[2] = []
        for idx, destination in enumerate(destinations):
            r, c = destination[0], destination[1]
            # Head
            if idx == 0:
                ground[r][c] = 1
                team[1] = [[r, c]]
            # Tail
            elif idx == len(destinations) - 1:
                ground[r][c] = 3
                team[3] = [[r, c]]
            # Mid
            else:
                ground[r][c] = 2
                team[2].append([r, c])

        if head_tail_meet == False:
            # Update previous tail location
            ground[prev_tail[0]][prev_tail[1]] = 4

    return ground, teams

# 공이 던져지는 경우에 해당 선에 사람이 있으면
# 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
def get(ground, round, teams):
    target = [-1, -1]
    score = 0

    quotient, remainder = divmod(round - 1, N)
    side = quotient % 4

    if side == 0:
        r = remainder
        for c in range(0, N):
            if ground[r][c] in [1, 2, 3]:
                target[0], target[1] = r, c
                break

    elif side == 1:
        c = remainder
        for r in range(N - 1, -1, -1):
            if ground[r][c] in [1, 2, 3]:
                target[0], target[1] = r, c
                break

    elif side == 2:
        r = (N - 1) - remainder
        for c in range(N - 1, -1, -1):
            if ground[r][c] in [1, 2, 3]:
                target[0], target[1] = r, c
                break

    elif side == 3:
        c = (N - 1) - remainder
        for r in range(0, N):
            if ground[r][c] in [1, 2, 3]:
                target[0], target[1] = r, c
                break

    # If player get the ball
    #  점수는 해당 사람이 머리사람을 시작으로
    #  팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻게 됩니다.
    if target != [-1, -1]:
        for team in teams:
            nth = 0
            for sequence in range(1, 4):
                players = team[sequence]
                for player in players:
                    nth += 1
                    if target == player:
                        score = nth ** 2
                        # 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
                        ground, team = reverse_direction(ground, team)
                        return score, ground, teams
    # If there's no player who get the ball
    else:
        return score, ground, teams

# 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
def reverse_direction(ground, team):
    destinations = []
    # Sort in reverse order
    for sequence in range(3, 0, -1): # 3 -> 1
        # to reverse Mid
        reverse = team[sequence][::-1]
        for location in reverse:
            destinations.append(location)

    # Save as reversed order
    team[2] = list()  # Initialize mid
    for idx, destination in enumerate(destinations):
        r, c = destination[0], destination[1]

        # Tail -> Head
        if idx == 0:
            team[1] = [[r, c]]
            ground[r][c] = 1
        # Head -> Tail
        elif idx == len(destinations) - 1:
            team[3] = [[r, c]]
            ground[r][c] = 3

        # Mid in reverse order
        else:
            team[2].append([r, c])
            ground[r][c] = 2

    return ground, team

def solution(N, M, K, ground):
    # Initialize
    # Save team data
    teams = initialize(M, ground)

    # Solution
    answer = 0
    # For every round
    for round in range(1, K + 1):

        # Move all team toward head position for 1 step
        ground, teams = move(ground, teams)

        # Get the ball
        # 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
        score, ground, teams = get(ground, round, teams)
        answer += score

    return answer






# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    global N, M, K

    # Get input
    N, M, K, ground = get_input()

    # Solution
    print(solution(N, M, K, ground))

    # ///////////////////////////////////////////////////////////////////////////////////