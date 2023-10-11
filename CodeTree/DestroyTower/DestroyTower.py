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




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# 제출 전 주석
import sys
sys.stdin = open("input.txt", "r")

import collections


# User defined functions
# debugging purposes -----------------------------
def print_matrix(matrix, hightlight=[]):
    if hightlight == []:
        print("[", end="")
        for r in range(N):
            print("[", end="")
            for c in range(M):
                s = "%5s" % matrix[r][c]
                print(s, end=" ")
            print("]")
        print("]")

    # if highlight is set
    else:
        for r in range(N):
            for c in range(M):
                if [r, c] in hightlight:
                    s = "%3s" % f"-{matrix[r][c]}-"
                    print(s, end=" ")
                else:
                    s = "%5s" % matrix[r][c]
                    # print(matrix[r][c], end=" ")
                    print(s, end=" ")
            print()
# -----------------------------

def get_input():
    N, M, K = map(int, input().split())
    ground = list()

    for r in range(N):
        ground.append(list(map(int, input().split())))

    return N, M, K, ground

# Select Attacker ===========================
# Increase power
def select_attacker(ground, attack_sequence):
    # Find towers with the smallest power:
    attacker = [-1, -1]
    group_by_power = collections.defaultdict(list)
    for r in range(N):
        for c in range(M):
            # if the tower already destroyed
            if ground[r][c] == 0: continue

            current_power = ground[r][c]
            group_by_power[current_power].append([r, c])
    # 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    min_power = min(group_by_power)
    attacker_candidates = group_by_power[min_power]

    if len(attacker_candidates) == 1:
        attacker = attacker_candidates[0]
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑
    else:
        max_turn = -1 # 1 ≤ K ≤ 1,000
        for candidate in attacker_candidates:
            r, c = candidate[0], candidate[1]
            # 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑
            if max_turn < attack_sequence[r][c]:
                max_turn = attack_sequence[r][c]
                attacker[0], attacker[1] = r, c
            # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합(sum)이 가장 큰 포탑이 가장 약한 포탑
            elif max_turn == attack_sequence[r][c]:
                if attacker[0] + attacker[1] < r + c:
                    attacker[0], attacker[1] = r, c
                # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑
                elif attacker[0] + attacker[1] == r + c:
                    if attacker[0] < r:
                        attacker[0], attacker[1] = r, c

    # # Solution2: Timeout
    # # 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    # # 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑
    # # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합(sum)이 가장 큰 포탑이 가장 약한 포탑
    # # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑
    # # Find towers with the smallest power:
    # attacker = [-1, -1]
    # min_power = 6000  # 0 <= power <= 5000
    # for sum in range(N + M - 2, -1, -1): # (N - 1) + (M - 1) -> 0
    #     for c in range(M - 1, -1, -1): # 열 값이 가장 큰 포탑부터 순회
    #         r = sum - c
    #
    #         # [r, c] not in ground
    #         if not 0 <= r <= N - 1: continue
    #         # if the tower is already destroyed
    #         if ground[r][c] == 0: continue
    #
    #         # 공격력이 가장 낮은 포탑이 가장 약한 포탑
    #         if ground[r][c] < min_power:
    #             min_power = min(ground[r][c], min_power)
    #             attacker[0], attacker[1] = r, c
    #         # 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑
    #         elif ground[r][c] == min_power and attack_sequence[attacker[0]][attacker[1]] < attack_sequence[r][c]:
    #             attacker[0], attacker[1] = r, c

    # Increase power of selected attacker
    ground[attacker[0]][attacker[1]] += (N + M)

    return attacker, ground


# Attack ===================================================
def attack(attacker, ground, attack_sequence, attacked_loc):

    # Select Target ------------------------------
    def select_target(attacker, ground, attack_sequence):
        # Find towers with the biggest power:
        target = [N + 100, M + 100]

        # group_by_power = collections.defaultdict(list)
        # for r in range(N):
        #     for c in range(M):
        #         # 선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격합니다.
        #         if r == attacker[0] and c == attacker[1]: continue
        #         # if the tower already destroyed
        #         if ground[r][c] == 0: continue
        #
        #         current_power = ground[r][c]
        #         group_by_power[current_power].append([r, c])
        # # 공격력이 가장 높은 포탑이 가장 강한 포탑입니다.
        # max_power = max(group_by_power)
        # target_candidates = group_by_power[max_power]
        #
        # if len(target_candidates) == 1:
        #     target = target_candidates[0]
        # # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다.
        # else:
        #     min_turn = 2000  # 1 ≤ K ≤ 1,000
        #     for candidate in target_candidates:
        #         r, c = candidate[0], candidate[1]
        #         # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다.
        #         if attack_sequence[r][c] < min_turn:
        #             min_turn = attack_sequence[r][c]
        #             target[0], target[1] = r, c
        #         # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑입니다.
        #         elif min_turn == attack_sequence[r][c]:
        #             if r + c < target[0] + target[1]:
        #                 target[0], target[1] = r, c
        #             # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑입니다.
        #             elif r + c ==  target[0] + target[1]:
        #                 if r < target[0]:
        #                     target[0], target[1] = r, c


        # Solution2: Timeout
        # 공격력이 가장 높은 포탑이 가장 강한 포탑입니다.
        # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다.
        # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑입니다.
        # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑입니다.
        # Find towers with the biggest power:
        target = [-1, -1]
        max_power = -1000  # 0 <= power <= 5000
        for sum in range(0, N + M -1): # [0 -> (N - 1) + (M - 1)]
            for c in range(0, M): # 열 값이 가장 작은 포탑부터 순회
                r = sum - c

                # Check whether r in range of ground
                if not 0 <= r <= N - 1: continue
                # Check whether the tower has already destroyed
                if ground[r][c] == 0: continue
                # 선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격합니다.
                if r == attacker[0] and c == attacker[1]: continue

                # 공격력이 가장 높은 포탑이 가장 강한 포탑
                if max_power < ground[r][c]:
                    target[0], target[1] = r, c
                    max_power = ground[r][c]
                # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑
                elif ground[r][c] == max_power and attack_sequence[r][c] < attack_sequence[target[0]][target[1]]:
                    target[0], target[1] = r, c

        return target

    # Razor attack -----------------------------
    # return True if razor attack is available
    # otherwise, return False
    def razor_attackable(start, end, ground):
        path = list()
        attackable = False

        # 우 / 하 / 좌 / 상 우선순위대로 먼저 움직인 경로가 선택
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        visited = [[0] * M for _ in range(N)]
        backtrack_r = [[0] * M for _ in range(N)]
        backtrack_c = [[0] * M for _ in range(N)]

        q = collections.deque()
        q.append(start)
        visited[start[0]][start[1]] = 1

        while q:
            # BFS
            r, c = q.popleft()
            # if razor attack available
            if [r, c] == end:
                attackable = True
                break

            for i in range(4):
                # new location
                # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다.
                nr, nc = (r + dr[i]) % N, (c + dc[i]) % M

                # limitations
                # Visit only when the location are not visited
                if visited[nr][nc] != 0:
                    continue
                # 부서진 포탑이 있는 위치는 지날 수 없습니다.
                if ground[nr][nc] == 0:
                    continue

                # check visited
                visited[nr][nc] = visited[r][c] + 1
                # save current r, c for backtracking
                backtrack_r[nr][nc] = r
                backtrack_c[nr][nc] = c
                # add new location in queue
                q.append([nr, nc])

        return attackable, backtrack_r, backtrack_c

    # Reduce power
    # target: reduce the power of attacker
    # towers which are located in the shortest path to target: reduce (the power of attacker) // 2
    def razor_attack(attacker, target, ground, backtrack_r, backtrack_c, attacked_loc):
        target_attack_power = ground[attacker[0]][attacker[1]]

        # Attack towers which are located in the shortest path to target
        path_attack_power = target_attack_power // 2
        cur_r, cur_c = backtrack_r[target[0]][target[1]], backtrack_c[target[0]][target[1]]
        while not (cur_r == attacker[0] and cur_c == attacker[1]):
            ground[cur_r][cur_c] = max(ground[cur_r][cur_c] - path_attack_power, 0)
            attacked_loc[cur_r][cur_c] = True

            # find next path
            next_r = backtrack_r[cur_r][cur_c]
            next_c = backtrack_c[cur_r][cur_c]
            cur_r, cur_c = next_r, next_c

        # Attack target
        ground[target[0]][target[1]] = max(ground[target[0]][target[1]] - target_attack_power, 0)
        attacked_loc[target[0]][target[1]] = True

        return ground, attacked_loc

    # Run razor attack
    def run_razor_attack(attacker, target, ground, attacked_loc):
        # Check whether razor attack is available
        attackable, backtrack_r, backtrack_c = razor_attackable(attacker, target, ground)

        # Run razor attack
        if attackable:
            ground, attacked_loc = razor_attack(attacker, target, ground, backtrack_r, backtrack_c, attacked_loc)

        return attackable, ground, attacked_loc


    # Bomb attack -------------------------------
    def bomb(attacker, target, ground, attacked_loc):
        target_attack_power = ground[attacker[0]][attacker[1]]

        # Attack target
        ground[target[0]][target[1]] = max(ground[target[0]][target[1]] - target_attack_power, 0)
        attacked_loc[target[0]][target[1]] = True

        # Attack surrounding towers
        # Bomb attack directions
        # from Up to clockwise
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        surrounding_attack_power = target_attack_power // 2
        for i in range(8):
            nr, nc = (target[0] + dr[i]) % N, (target[1] + dc[i]) % M
            # 공격자는 해당 공격에 영향을 받지 않습니다.
            if attacker[0] == nr and attacker[1] == nc:
                continue
            # if the tower are not destroyed, run bomb attack
            if ground[nr][nc] != 0:
                ground[nr][nc] = max(ground[nr][nc] - surrounding_attack_power, 0)
                attacked_loc[nr][nc] = True

        return ground, attacked_loc


    # Outer function start -------------------------------
    # Find target
    target = select_target(attacker, ground, attack_sequence)

    # if razor attack is not available, go for bomb attack
    razor_attack_available, ground, attacked_loc = run_razor_attack(attacker, target, ground, attacked_loc)
    if not razor_attack_available:
        ground, attacked_loc = bomb(attacker, target, ground, attacked_loc)

    return ground, attacked_loc


# Reconstruction ===================================================
# reconstruct towers that are not affected by the previous attack
def reconstruct(ground, attacked_loc):
    for r in range(N):
        for c in range(M):
            # if the tower not destroyed and not affected by previous attack
            if ground[r][c] != 0 and attacked_loc[r][c] == False:
                ground[r][c] += 1

    return ground

def count_not_destroyed(ground):
    count = 0
    for r in range(N):
        for c in range(M):
            if ground[r][c] != 0:
                count += 1

    return count

def find_max_power(ground):
    max_power = -1000  # 0 <= power <= 5000
    for r in range(N):
        for c in range(M):
            max_power = max(max_power, ground[r][c])
    return max_power

def solution(ground):
    # 모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.
    attack_sequence = [[0] * M for _ in range(N)]

    # For every second
    for sec in range(1, K + 1):

        # Initialize attacked location
        # Save attacked locations for reconstruction
        attacked_loc = [[False] * M for _ in range(N)]

        # Select Attacker
        attacker, ground = select_attacker(ground, attack_sequence)
        # Save attacker as relevant to attacked location
        attacked_loc[attacker[0]][attacker[1]] = True
        # Update attack sequence
        attack_sequence[attacker[0]][attacker[1]] = sec

        # Attack
        ground, attacked_loc = attack(attacker, ground, attack_sequence, attacked_loc)

        # Organize destroyed towers
        # attack_sequence = organize(attack_sequence, ground, attacked_loc)

        # Reconstruction
        ground = reconstruct(ground, attacked_loc)

        # 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지
        if count_not_destroyed(ground) == 1:
            break

    # Answer
    return find_max_power(ground)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # ///////////////////////////////////////////////////////////////////////////////////
    global N, M, K

    # Get input
    N, M, K, ground = get_input()

    # Solution
    print(solution(ground))
    # ///////////////////////////////////////////////////////////////////////////////////

