"""
Problem: https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""

import heapq

def solution(operations):
    answer = []

    q = []
    for operation in operations:
        if operation[0] == "I":
            op = operation.split()
            instruction, number = op[0], int(op[1])
            heapq.heappush(q, number)

        if operation == "D 1":
            if q != []:
                biggest_num = q[-1]
                q.remove(biggest_num)

        if operation == "D -1":
            if q != []:
                heapq.heappop(q)

        # debug
        # print(heapq.nsmallest(len(q), q))

    if q == []:
        answer = [0, 0]
    else:
        answer = [max(q), min(q)]

    return answer