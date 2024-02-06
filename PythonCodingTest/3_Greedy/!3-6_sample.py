"""
Problem:
첫째 줄에 N(2 ≤ N ≤ 100,000)과 K(2 ≤ K ≤ 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

N이 K로 나누어 떨어지기 위해서 몇 번 1씩 빼야하는지 미리 계산하면, 일일이 1씩 빼는 것보다 효율적
-> N이 아주 큰 수일 때 더 효율적으로 동작 가능
"""

test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    print(f"test case: {test_case}")

    # Get input
    n, K = map(int, input().split())
    count = 0

    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
        quotient = n // K
        target = quotient * K
        count += (n - target) # 나누어 떨어지도록 1씩 뺀 횟수

        # 더 이상 나눌 수 없을 때
        n = target
        if n < K:
            break

        # K로 나누기
        n //= K
        count += 1

    # 더 이상 나눌 수 없을 때
    count += (n - 1) # 1씩 빼서 1이 될 때까지
    print(count)