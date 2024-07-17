# 구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀
# 향을 바꾸는 데에는 1만큼의 시간이 소요

# Get input
n, t = map(int, input().split())
r, c, d = input().split()
r, c = map(int, [r, c])
r, c = r - 1, c - 1
direction = {"U": (-1, 0),
                "D": (1, 0),
                "R": (0, 1),
                "L": (0, -1)}
dr, dc = direction[d]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

for time in range(1, t + 1):
    nr, nc = r + dr, c + dc
    if not in_range(nr, nc):
        dr, dc = dr * -1, dc * -1
        continue
    r, c = nr, nc
print(r + 1, c + 1)