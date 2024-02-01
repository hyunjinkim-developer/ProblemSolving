"""
Problem: https://www.acmicpc.net/problem/18428
- 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력
- input:
    - 각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다.
    - 해당 위치에 학생이 있다면 S
    - 선생님이 있다면 T
    - 아무것도 존재하지 않는다면 X
"""

N = 0
graph = list()
teachers = list()
answer = False
border_set, total_border_set = list(), set()

#debug
def print_matrix(matrix):
    global N
    for r in range(N):
        for c in range(N):
            print(matrix[r][c], end="\t")
        print()
    print("-"*10)

def get_input():
    global N, graph, teachers, answer
    global border_set, total_border_set

    # Initialization
    N = 0
    graph, teachers = list(), list()
    answer = False
    border_set, total_border_set = list(), set()

    N = int(input())
    for r in range(N):
        graph.append(list(input().split()))
        for c in range(N):
            if graph[r][c] == "T":
                teachers.append((r, c))

def set_barrier(count):
    global N, graph, answer
    global border_set, total_border_set

    # If already found a way to avoid teachers
    if answer == True:
        return

    if count == 3:
        new_border_set = tuple(sorted(border_set))
        if new_border_set not in total_border_set:
            answer = avoid_teachers()
            total_border_set.add(new_border_set)
        return

    for r in range(N):
        for c in range(N):
            if graph[r][c] == "X":
                # Set barrier
                graph[r][c] = "B"
                count += 1
                border_set.append((r,c))
                set_barrier(count)
                # Remove barrier
                graph[r][c] = "X"
                count -= 1
                border_set.pop(-1)

def avoid_teachers():
    global N, graph, teachers

    for teacher_location in teachers:
        r, c = teacher_location
        # Row-wise
        for c_left in range(c - 1, -1, -1):
            if graph[r][c_left] == "B":
                break
            if graph[r][c_left] == "S":
                return False
        for c_right in range(c + 1, N):
            if graph[r][c_right] == "B":
                break
            if graph[r][c_right] == "S":
                return False
        # Column-wise
        for r_left in range(r - 1, -1, -1):
            if graph[r_left][c] == "B":
                break
            if graph[r_left][c] == "S":
                return False
        for r_right in range(r + 1, N):
            if graph[r_right][c] == "B":
                break
            if graph[r_right][c] == "S":
                return False
    return True

def main():
    global answer

    get_input()
    set_barrier(0)

    if answer == True:
        return "YES"
    else:
        return "NO"

# if __name__ == "__main__":
#     test_case_count = int(input())
#     for test_case in range(1, test_case_count + 1):
#         print(f"test case: {test_case}", "="*30)
#         print(main())
#
#         #debug
#         if test_case == 1:
#             break

# For submission
if __name__ == "__main__":
    print(main())