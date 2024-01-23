"""
Problem: https://www.acmicpc.net/problem/14888
"""
N, A, add, sub, mul, div = 0, list(), 0, 0, 0, 0
answer_max, answer_min = -1e9, 1e9

def get_input():
    global N, A, add, sub, mul, div
    global answer_max, answer_min

    N = int(input())
    A = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    # 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고,
    # 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
    answer_max, answer_min = -1e9, 1e9

def DFS(i, current):
    global answer_max, answer_min, add, sub, mul, div

    if i == N:
        answer_max = max(answer_max, current)
        answer_min = min(answer_min, current)

    else:
        if add > 0:
            add -= 1
            DFS(i + 1, current + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            DFS(i + 1, current - A[i])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(i + 1, current * A[i])
            mul += 1
        if div > 0:
            div -= 1
            DFS(i + 1, int(current / A[i]))
            div += 1

# main()
test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    print(f"test case: {test_case}", "="*30)
    get_input()
    DFS(1, A[0])
    print(answer_max)
    print(answer_min)