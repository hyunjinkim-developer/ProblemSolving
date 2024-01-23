"""
Problem: https://www.acmicpc.net/problem/14888
"""

from itertools import permutations

N = 0
A = list()
operator_count = list()
answer_max, answer_min = float("-inf"), float("inf")

def get_input():
    global N, A, operator_count, answer_max, answer_min

    N = int(input())
    A = list(map(int, input().split()))
    operator_count = list(map(int, input().split()))

    answer_max, answer_min = float("-inf"), float("inf")

def find_available_operators():
    global operator_count

    operator_dict = {0: "+", 1: "-", 2: "*", 3: "/"}
    available_operators = list()

    for i in range(4):
        counts = operator_count[i]
        for _ in range(counts):
            available_operators.append(operator_dict[i])
    return available_operators

def order_operators():
    available_operators = find_available_operators()

    ordered_operators = set(list(permutations(available_operators, len(available_operators))))
    return ordered_operators

def calcuate():
    global N, A
    global answer_max, answer_min

    operator_paris = order_operators()
    for operator_pair in operator_paris:
        answer = A[0]
        for idx, op in enumerate(list(operator_pair)):
            # Switch statement is not available in Python syntax
            if op == "+":
                answer += A[idx + 1]
            elif op == "-":
                answer -= A[idx + 1]
            elif op == "*":
                answer *= A[idx + 1]
            elif op == "/":
                answer = int(answer / A[idx + 1])
        answer_max = max(answer_max, answer)
        answer_min = min(answer_min, answer)

    return answer_max, answer_min

def main():
    get_input()
    calcuate()
    print(answer_max)
    print(answer_min)


# if __name__ == "__main__":
#     test_case_count = int(input())
#     for test_case in range(1, test_case_count + 1):
#         print(f"test case:", test_case, "=" * 30)
#         main()


# For submission
if __name__ == "__main__":
    main()