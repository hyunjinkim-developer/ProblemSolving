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
temp = list()
temp_total = list()
temp_total_set = set()
temp_count = 0

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

    # Initialization
    N = 0
    graph, teachers = list(), list()
    answer = False

    N = int(input())
    for r in range(N):
        graph.append(list(input().split()))
        for c in range(N):
            if graph[r][c] == "T":
                teachers.append((r, c))

def set_barrier(count):
    global N, graph, answer
    global temp, temp_count, temp_total, temp_total_set

    # if answer == True:
    #     return

    if count == 3:
        answer = avoid_teachers()
        temp_count += 1 #d
        # if answer == True:
        #     print_matrix(graph) #d
        temp_total.append(temp) #d
        temp_total_set.add(tuple(temp)) #d
        return

    for r in range(N):
        for c in range(N):
            if graph[r][c] == "X":
                # Set barrier
                graph[r][c] = "B"
                temp.append((r, c)) #d
                print(temp)
                count += 1
                set_barrier(count)
                # Remove barrier
                graph[r][c] = "X"
                count -= 1
                temp.pop(-1) #d

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

    print(temp_count)
    print(len(temp_total))
    print(len(temp_total_set))
    # print(temp_total_set)

    if answer == True:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        print(f"test case: {test_case}", "="*30)
        print(main())

        #d
        if test_case == 1:
            break

# # For submission
# if __name__ == "__main__":
#     print(main())