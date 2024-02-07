"""
Solution:
1. Save in queue, in the form of virus number, time, location r(X), c(Y)
    queue.append((virus_no, s + 1, nr, nc))
2. Sort to visit from the lower virus number
3_Greedy. Spread virus with BFS
"""
"""
Problem: https://www.acmicpc.net/problem/18405
    N개의 줄에 걸쳐서 시험관의 정보, 1 ≤ N ≤ 200
    바이러스의 번호는 K 이하의 자연수, 1 ≤ K ≤ 1,000
    S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력합니다.
    0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N
    만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력
"""

from collections import deque

# Initialization
N, K = map(int, input().split())
map_ = list()
virus_data = list()

# Get input
for r in range(N):
    map_.append(list(map(int, input().split())))
    for c in range(N):
        if map_[r][c] != 0:
            # virus number, time, location r(X), c(Y)
            virus_data.append((map_[r][c], 0, r, c))
# Sort in virus number
virus_data.sort()
q = deque(virus_data)

target_s, target_x, target_y = map(int, input().split())

# from up in  clockwise
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

# BFS
while q:
    virus_no, s, r, c = q.popleft()
    # Repeat until S seconds or queue is empty
    if s == target_s: break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not in_range(nr, nc): continue
        # if the location is not visited yet
        if map_[nr][nc] == 0:
            map_[nr][nc] = virus_no
            q.append((virus_no, s + 1, nr, nc))

print(map_[target_x - 1][target_y - 1])



