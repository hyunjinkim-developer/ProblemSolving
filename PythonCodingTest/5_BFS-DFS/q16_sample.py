"""
* Problem: BaekJoon 14502 https://www.acmicpc.net/problem/14502
 - 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
 - 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
 - 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
 - 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성

 * Solution:
 전체 맵의 크기가 8 × 8이므로,
 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존재 하지 않는 경우)
 64C3이 될 것이다.
 이는 100,000보다도 작은 수이므로,
 모든 경우의 수를 고려해도 제한시간 안에 문제를 해결 할 수 있다
 1. 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에
 2. 그러한 조합에 대해서 안 전 영역의 크기를 계산하면 된다.
    안전 영역의 크기를 구하는 것 또한 DFS나 BFS를 이용하여 계산

* PyPy3 is faster than Python3
Python3 :
- GIL(global interpreter lock)을 사용 -> 느림
    - bytecode를 실행할 때에 여러 thread를 사용할 경우, 전체에 lock을 걸어서 한번에 하나의 thread만이 python객체에 접근하도록 제한
    - 하지만 single thread일 떄는 문제가 없고, GIL단점을 보안하기 위한 방법들이 존재하고 있어 GIL로 인한 불편함을 느낄 가능성은 거의 없다

PyPy3 :
CPython : 컴파일 하여 bytecode로 -> 인터프리터(가장 머신) 실행
- JIT(just in time) 컴파일 방식 사용
    - 프로그램을 실행하기 전에 컴파일 하는 대신, 프로그램을 실행하는 시점에서 필요한 부분들을 즉석으로 컴파일 하는 방식
- 인터프리트 하면서 자주 쓰이는 코드를 캐싱, 느린 실행속도를 개선 가능 (메모리를 조금 더 사용)

-> Conclusion:
- 간단한 코드상에서는 Python3가 메모리, 속도 측에서 우세
- 복잡한 코드(반복)을 사용하는 경우에서는 PyPy3가 우세
"""

from copy import deepcopy

def main():
    answer = 0

    # Get input
    N, M = map(int, input().split())
    init_map = []
    for _ in range(N):
        init_map.append(list(map(int, input().split())))
    # Initialization
    map_with_wall = [[0] * M for _ in range(N)]

    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M

    def spread_virus(r, c):
        nonlocal map_with_wall

        # From up in clockwise
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not in_range(nr, nc): continue

            # Spread virus in safe area
            if map_with_wall[nr][nc] == 0:
                map_with_wall[nr][nc] = 2
                spread_virus(nr, nc)


    def count_safe_area():
        nonlocal map_with_wall

        count = 0
        for r in range(N):
            for c in range(M):
                if map_with_wall[r][c] == 0:
                    count += 1
        return count


    def DFS(walls_count):
        nonlocal map_with_wall, answer

        # if all walls(3) are built
        if walls_count == 3:
            """
            Copy by assigning with iteration
                time complexity O(n)
                space complexity O(1) (initial 2-dim array of map_with_wall)
            """
            for r in range(N):
                for c in range(M):
                    map_with_wall[r][c] = init_map[r][c]
            """
            copy.deepcopy() :
                time complexity O(n)
                space complexity O(function running times)
            In this case, assigning with iteration is better 
                in the manner of space complexity
            """
            # map_with_wall = deepcopy(init_map)

            # Spread virus
            for r in range(N):
                for c in range(M):
                    if map_with_wall[r][c] == 2:
                        spread_virus(r, c)

            # Count safe area
            answer = max(answer, count_safe_area())
            # print("!")
            return


        # Built walls in remained areas
        # 가능한 모든 경우의 수 -> DFS일 때 자주 쓰이는 pattern
        for r in range(N):
            for c in range(M):
                if init_map[r][c] == 0:
                    # Built a wall
                    init_map[r][c] = 1
                    walls_count += 1
                    DFS(walls_count)

                    # Remove a wall
                    init_map[r][c] = 0
                    walls_count -= 1

    # main()
    DFS(0)
    print(answer)


if __name__ == "__main__":
    main()