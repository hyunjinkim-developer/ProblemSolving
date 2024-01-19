"""
    Timeout
"""

"""
Problem: https://www.acmicpc.net/problem/18405
    N개의 줄에 걸쳐서 시험관의 정보, 1 ≤ N ≤ 200
    바이러스의 번호는 K 이하의 자연수, 1 ≤ K ≤ 1,000
    S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력합니다.
    0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N
    만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력
"""
N, K = 0, 0
map_ = list()
S, X, Y = -1, -1, -1

# For debugging
def print_matrix(matrix):
    global N
    for r in range(N):
        for c in range(N):
            print(matrix[r][c], end="\t")
        print("\n")

def get_input():
    global N, K, S, X, Y, map_

    # Initialize
    N, K = 0, 0
    map_ = list()
    S, X, Y = -1, -1, -1

    # Get input
    N, K = map(int, input().split())
    for _ in range(N):
        map_.append(list(map(int, input().split())))
    S, X, Y = map(int, input().split())

def spread(virus_no, visited):
    global N, K, map_

    def in_range(r, c):
        return 0 <= r < N and 0 <= c < N

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = list()
    for r in range(N):
        for c in range(N):
            if visited[r][c] == True: continue
            if map_[r][c] == virus_no:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not in_range(nr, nc): continue
                    if map_[nr][nc] == 0:
                        queue.append((nr, nc))
                visited[r][c] = True
    #d
    # print(f"virus: {virus_no}, visited:")
    # print_matrix(visited)

    for nr, nc in queue:
        map_[nr][nc] = virus_no
    return visited

def find_answer(map_):
    global X, Y

    # #d
    # print(f"map_:")
    # print_matrix(map_)
    #
    return map_[X - 1][Y - 1]

def main():
    global N, K, S, map_

    get_input()

    visited = [[False] * N for _ in range(N)]
    for s in range(1, S + 1):
        for virus_no in range(1, K + 1):
            visited = spread(virus_no, visited)

    return find_answer(map_)

# For debugging
if __name__ == "__main__":
    sample_number = int(input())
    for sample in range(1, sample_number + 1):
        print(f"Sample: {sample}", "=" * 30)
        print(main())

# # Submission
# if __name__ == "__main__":
#     print(main())
