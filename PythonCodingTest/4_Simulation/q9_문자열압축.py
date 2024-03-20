"""
Problem: https://programmers.co.kr/learn/courses/30/lessons/60057
"""

"""
# Solution 1:
def solution(s):
    answer = len(s)

    for length in range(1, len(s)):
        compressed_result = ""
        prev_chunk = s[:length]
        repeat = 1
        for i in range(length, len(s), length):
            if prev_chunk == s[i: i + length]:
                repeat += 1
            else:
                if 1 < repeat:
                    compressed_result += str(repeat)
                compressed_result += prev_chunk

                repeat = 1
                prev_chunk = s[i: i + length]
        # Add last chunk
        if 1 < repeat:
            compressed_result += str(repeat)
        compressed_result += prev_chunk

        answer = min(answer, len(compressed_result))
    return answer
"""

# Solution 2:
# 주어지는 문자열의 길이가 1000이하이므로
# 1 ~ N/2 길이까지 문자열을 압축하는 방법을 확인
# Brute Force Search 가능: O(N * N/2) ~ O(10^6)
def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed_result = ""
        prev_chunk = s[: step]
        repeat = 1
        for i in range(step, len(s), step):
            if prev_chunk == s[i: i + step]:
                repeat += 1
            else:
                compressed_result += (str(repeat) + prev_chunk) if 2 <= repeat else prev_chunk
                prev_chunk = s[i: i + step]
                repeat = 1
        compressed_result += (str(repeat) + prev_chunk) if 2 <= repeat else prev_chunk
        answer = min(answer, len(compressed_result))
    return answer