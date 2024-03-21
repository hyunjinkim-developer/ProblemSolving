"""
Problem: BaekJoon 14502 https://www.acmicpc.net/problem/14502
 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3_Greedy ≤ N, M ≤ 8_DynamicProgramming)
 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성
"""

from itertools import combinations
from copy import deepcopy

N, M = 0, 0
_map = list()
answer = 0

# For debugging
debug = False
def print_matrix(matrix):
    global N, M
    for r in range(N):
        for c in range(M):
            print(matrix[r][c], end='\t')
        print(end="\n")

def get_input():
    global N, M, _map, answer

    # Initialize global variables
    N, M = 0, 0
    _map = list()
    answer = 0

    N, M = map(int, input().split())

    for _ in range(N):
        _map.append(list(map(int, input().split())))


def find_wall_location():
    global N, M, _map

    total_available_spots = list()
    for r in range(N):
        for c in range(M):
            if _map[r][c] == 0:
                total_available_spots.append((r, c))

    # 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
    available_spots = list(combinations(total_available_spots, 3))
    return available_spots


def spread_virus(spots):
    global N, M, _map, answer
    remain_spots = -1000 # initializaion

    spreaded_map = list()
    spreaded_map = deepcopy(_map)
    # Build walls
    for spot in spots:
        r, c = spot
        spreaded_map[r][c] = 1

    # DFS
    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M

    def DFS(v):
        nonlocal spreaded_map
        r, c = v

        if spreaded_map[r][c] == 0:
            spreaded_map[r][c] = 2

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # from up in clockwise
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc): continue
            if not spreaded_map[nr][nc] == 0: continue

            DFS((nr, nc))

    def count_safe_area():
        global N, M
        nonlocal spreaded_map

        count = 0
        for r in range(N):
            for c in range(M):
                if spreaded_map[r][c] == 0:
                    count += 1
        return count

    # Spread virus
    for virus_r in range(N):
        for virus_c in range(M):
            if _map[virus_r][virus_c] == 2:
                # if there's no more space to spread virus
                if remain_spots == 0: continue

                DFS((virus_r, virus_c))

                # Count safe areas
                remain_safe_areas = count_safe_area() # remain_spots gets smaller

    return remain_safe_areas


def main():
    global N, M, _map, answer

    get_input()
    # d
    if debug:
        print_matrix(_map)

    available_spots = find_wall_location()
    for spots in available_spots:
        remain_safe_areas = spread_virus(spots)

        # 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성
        answer = max(answer, remain_safe_areas)
    return answer


if __name__ == "__main__":
    sample_number = int(input())

    for test_case in range(1, sample_number + 1):
        print(f"Test case: {test_case}")
        print(f"Answer: {main()}")
        print("="*30)

# # Submission
# if __name__ == "__main__":
#     print(main())