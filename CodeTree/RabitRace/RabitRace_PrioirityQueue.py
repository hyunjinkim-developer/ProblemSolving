import heapq

MAX_P = 2000

# 변수 선언 및 입력
N, M, P = 0, 0, 0

# 각 토끼의 id를 기록
pid = [0] * (MAX_P + 1)

# 각 토끼의 이동거리를 기록
pw = [0] * (MAX_P + 1)

# 각 토끼의 점프 횟수 기록
jump_cnt = [0] * (MAX_P + 1)

# 각 토끼의 점수 기록
result = [0] * (MAX_P + 1)

# 각 토끼의 현재 위치(좌표) 기록
point = [(0, 0)] * (MAX_P + 1)

# 각 토끼의 id를 인덱스로 변환
id_to_idx = {}

# 각각의 경주에서 토끼가 달렸는지 기록
is_runned = [0] * (MAX_P + 1)

# 하나를 제외한 모든 토끼들의 점수를 더할 때 편리하게 하기 위해
total_sum = 0

# 구조체 rabbit
class Rabbit:
    def __init__(self, x, y, j, pid):
        self.x = x
        self.y = y
        self.j = j
        self.pid = pid

    # 이동할 토끼를 결정하기 위한 정렬함수
    def __lt__(self, other):
        if self.j != other.j:
            return self.j < other.j
        if self.x + self.y != other.x + other.y:
            return self.x + self.y < other.x + other.y
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid

# 위치에 관한 우선순위 판단하기 위한 정렬함수
def compare(a, b):
    if a.x + a.y != b.x + b.y:
        return a.x + a.y < b.x + b.y
    if a.x != b.x:
        return a.x < b.x
    if a.y != b.y:
        return a.y < b.y
    return a.pid < b.pid

# 경주 준비
def init(inp):
    global N, M, P

    N, M, P, *rabbits = inp
    for i in range(1, P + 1):
        pid[i] = rabbits[i * 2 - 2]
        pw[i] = rabbits[i * 2 - 1]

        id_to_idx[pid[i]] = i
        point[i] = (1, 1)

def copy_rabbit(rabbit):
    return Rabbit(rabbit.x, rabbit.y, rabbit.j, rabbit.pid)

def get_up_rabbit(cur_rabbit, distance):
    up_rabbit = cur_rabbit
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((N - 1) * 2)

    # move up: All the way up to top
    if new_distance >= up_rabbit.x - 1:
        new_distance -= (up_rabbit.x - 1)
        up_rabbit.x = 1
    else:  # move up
        up_rabbit.x -= new_distance
        new_distance = 0

    # move up -> down
    if new_distance <= (N - 1):
        up_rabbit.x += new_distance
    # move up -> down -> up
    else:
        new_distance -= (N - 1)
        up_rabbit.x = N - new_distance

    return up_rabbit

def get_down_rabbit(cur_rabbit, distance):
    down_rabbit = cur_rabbit
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((N - 1) * 2)

    # move down: All the way up to bottom
    if new_distance >= N - down_rabbit.x:
        new_distance -= N - down_rabbit.x
        down_rabbit.x = N
    else:  # move down
        down_rabbit.x += new_distance
        new_distance = 0

    # move down -> up
    if new_distance <= (N - 1):
        down_rabbit.x -= new_distance
    # move down -> up -> down
    else:
        new_distance -= (N - 1)
        down_rabbit.x = 1 + new_distance

    return down_rabbit

def get_left_rabbit(cur_rabbit, distance):
    left_rabbit = cur_rabbit
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((M - 1) * 2)

    # move left: All the way up to left
    if new_distance >= (left_rabbit.y - 1):
        new_distance -= (left_rabbit.y - 1)
        left_rabbit.y = 1
    else:  # move left
        left_rabbit.y -= new_distance
        new_distance = 0

    # move left -> right
    if new_distance <= (M - 1):
        left_rabbit.y += new_distance
    # move left -> right -> left
    else:
        new_distance -= (M - 1)
        left_rabbit.y = M - new_distance

    return left_rabbit

def get_right_rabbit(cur_rabbit, distance):
    right_rabbit = cur_rabbit
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((M - 1) * 2)

    # move right: All the way up to right
    if new_distance >= M - right_rabbit.y:
        new_distance -= M - right_rabbit.y
        right_rabbit.y = M
    else:  # move right
        right_rabbit.y += new_distance
        new_distance = 0

    # move right -> left
    if new_distance <= (M - 1):
        right_rabbit.y -= new_distance
    # move right -> left -> right
    else:
        new_distance -= (M - 1)
        right_rabbit.y = 1 + new_distance

    return right_rabbit

def start_round(inp):
    global total_sum

    k, bonus = inp
    rabbit_pq = []

    for i in range(1, P + 1):
        is_runned[i] = False

    # 우선 p마리의 토끼들을 전부 priority queue에 넣어줍니다.
    for i in range(1, P + 1):
        x, y = point[i]
        new_rabbit = Rabbit(x, y, jump_cnt[i], pid[i])
        heapq.heappush(rabbit_pq, new_rabbit)

    # 경주를 k회 진행
    for _ in range(k):
        # 우선순위가 가장 높은 토끼를 priority queue에서 뽑아옵니다.
        cur_rabbit = heapq.heappop(rabbit_pq)

        # 해당 토끼를 상, 하, 좌, 우 4개의 방향으로 이동시킵니다.
        # 각각의 방향으로 이동시킨 후 최종 위치를 구하고
        # 가장 시작점으로부터 멀리 있는 위치를 찾아줍니다.
        distance = pw[id_to_idx[cur_rabbit.pid]]
        nex_rabbit = copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0

        # 토끼를 위로 이동시킵니다.
        up_rabbit = get_up_rabbit(copy_rabbit(cur_rabbit), distance)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, up_rabbit):
            nex_rabbit = up_rabbit

        # 토끼를 아래로 이동시킵니다.
        down_rabbit = get_down_rabbit(copy_rabbit(cur_rabbit), distance)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, down_rabbit):
            nex_rabbit = down_rabbit

        # 토끼를 왼쪽으로 이동시킵니다.
        left_rabbit = get_left_rabbit(copy_rabbit(cur_rabbit), distance)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, left_rabbit):
            nex_rabbit = left_rabbit

        # 토끼를 오른쪽으로 이동시킵니다.
        right_rabbit = get_right_rabbit(copy_rabbit(cur_rabbit), distance)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, right_rabbit):
            nex_rabbit = right_rabbit

        # 토끼의 점프 횟수를 갱신해주고, priority queue에 다시 집어넣습니다.
        nex_rabbit.j += 1
        heapq.heappush(rabbit_pq, nex_rabbit)

        # 실제 point, jump_cnt 배열에도 값을 갱신해줍니다.
        nex_idx = id_to_idx[nex_rabbit.pid]
        point[nex_idx] = (nex_rabbit.x, nex_rabbit.y)
        jump_cnt[nex_idx] += 1

        # 토끼가 달렸는지 여부를 체크해줍니다.
        is_runned[nex_idx] = True

        # 토끼가 받는 점수는 (현재 뛴 토끼)만 (r + c)만큼 점수를 빼주고,
        # 모든 토끼(total_sum)에게 (r + c)만큼 점수를 더해줍니다.
        # 최종적으로 i번 토끼가 받는 점수는 result[i] + total_sum이 됩니다.
        # print_result()에서 total_sum을 고려해서 점수 계산
        result[nex_idx] -= (nex_rabbit.x + nex_rabbit.y)
        total_sum += (nex_rabbit.x + nex_rabbit.y)

    # 보너스 점수를 받을 토끼를 찾습니다.
    # 이번 경주때 달린 토끼 중 가장 멀리있는 토끼를 찾습니다.
    bonus_rabbit = Rabbit(0, 0, 0, 0)
    while rabbit_pq:
        cur_rabbit = heapq.heappop(rabbit_pq)

        # 달리지 않은 토끼는 스킵합니다.
        if not is_runned[id_to_idx[cur_rabbit.pid]]:
            continue

        if compare(bonus_rabbit, cur_rabbit):
            bonus_rabbit = cur_rabbit

    # 해당 토끼에게 bonus만큼 점수를 추가해줍니다.
    result[id_to_idx[bonus_rabbit.pid]] += bonus

def power_up(inp):
    pid, t = inp
    idx = id_to_idx[pid]

    pw[idx] *= t

def print_result():
    answer = 0
    for i in range(1, P + 1):
        answer = max(answer, result[i] + total_sum)

    print(answer)


# # Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    Q = int(input())
    for _ in range(Q):
        query, *inp = list(map(int, input().split()))

        # 경주 준비
        if query == 100:
            init(inp)
        # 경주
        if query == 200:
            start_round(inp)
        # 이동거리 변경
        if query == 300:
            power_up(inp)
        # 최고의 토끼 선정
        if query == 400:
            print_result()
    # ///////////////////////////////////////////////////////////////////////////////////
