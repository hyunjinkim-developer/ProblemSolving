"""
Problem: https://programmers.co.kr/learn/courses/30/lessons/60058
"""

"""
Solution 3: 
"""


def balanced_index(p):
    count = 0  # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우 True 반환


def solution(p):
    answer = ''

    if p == "":
        return answer

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
    # v는 빈 문자열이 될 수 있습니다.
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # 3. u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
    if check_proper(u):
        answer = u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1: -1])  # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer

# """
# Solution 1:
# """
# from collections import deque

# def correct_parentheses(p):
#     p = deque(p)
#     stack = deque()
#     while p:
#         c = p.popleft()
#         if c == "(":
#             stack.append(c)
#         elif c == ")":
#             if stack:
#                 popped = stack.pop()
#                 if popped == "(":
#                     continue
#                 else:
#                     return False
#             else:
#                 return False
#     return True


# def convert(p):
#     global answer

#     # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
#     if p == "":
#         return ""

#     # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
#     # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
#     # v는 빈 문자열이 될 수 있습니다.
#     # '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열
#     p = deque(p)
#     u, v = deque(), deque()
#     count = 0
#     while p:
#         c = p.popleft()
#         if c == "(":
#             count += 1
#             u.append(c)
#         elif c == ")":
#             count -= 1
#             u.append(c)

#         if count == 0:
#             v = p
#             break

#     u, v = "".join(u), "".join(v)
#     # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#     # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#     if correct_parentheses(u):
#         u += convert(v)
#         return u
#     # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#     else:
#         # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#         # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#         # 4-3. ')'를 다시 붙입니다.
#         # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#         # 4-5. 생성된 문자열을 반환합니다.
#         # "(" + convert(v)
#         str_ = "("
#         str_ += convert(v)
#         str_ += ")"

#         u_prime = ""
#         flip_d = {"(": ")", ")": "("}
#         for c in u[1:-1]:
#             u_prime += flip_d[c]
#         str_ += u_prime
#         return str_


# def solution(p):
#     answer = convert(p)
#     return answer


# """
# Solution 2:
# """
# # 올바른 괄호 문자열 :=
# # '(' 의 개수와 ')' 의 개수가 같고
# # '('와 ')'의 괄호의 짝도 모두 맞을 경우
# def is_correct_string(string):
#     count = 0
#     for s in string:
#         if s == '(':
#             count += 1
#         elif s == ')':
#             count -= 1

#         # When ")" comes before "("
#         if count < 0:
#             return False
#     return count == 0


# # 균형잡힌 괄호 문자열 :=
# # '(' 의 개수와 ')' 의 개수가 같은 경우
# def is_banlanced_string(string):
#     return string.count("(") == string.count(")")


# # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
# # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
# # v는 빈 문자열이 될 수 있습니다.
# def split_uv(string):
#     u, v = string, ""
#     # when the string is balanced, i.e. "()" "(())"
#     # the length of the string should be multiple of 2
#     for i in range(2, len(string), 2): # start from 2, step in 2
#         if is_banlanced_string(string[:i]):
#             u = string[:i]
#             v = string[i:]
#             break
#     return u, v


# # 문자열의 괄호 방향을 뒤집음
# def reverse_string(string):
#     # bracket_d = {"(": ")", ")": "("}
#     # for idx, s in enumerate(string):
#     #     string[idx] = bracket_d[s]
#     # print(string)
#     # return string
#     ans = ""
#     for s in string:
#         if s == "(":
#             ans += ")"
#         else:
#             ans += "("
#     return ans


# def process(string):
#     # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
#     if string == "":
#         return ""
#     # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
#     u, v = split_uv(string)
#     # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#     #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#     if is_correct_string(u):
#         u += process(v)
#         return u
#     # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#     else:
#         # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#         new_string = "("
#         # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#         new_string += process(v)
#         # 4-3. ')'를 다시 붙입니다.
#         new_string += ")"
#         # 4-4. u의 첫 번째와 마지막 문자를 제거하고,
#         # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#         new_string += reverse_string(u[1: -1])
#         return new_string


# def solution(p):
#     if is_correct_string(p):
#         return p
#     else:
#         return process(p)