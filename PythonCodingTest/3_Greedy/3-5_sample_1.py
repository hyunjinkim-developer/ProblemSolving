"""
Problem:
첫째 줄에 N(2 ≤ N ≤ 100,000)과 K(2 ≤ K ≤ 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
"""

test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    print(f"test case: {test_case}")

    # Get input
    n, K = map(int, input().split())
    count = 0

    # N이 K 이상이라면 K로 계속 나누기
    while n >= K:
        # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        while n % K != 0:
            n -= 1
            count += 1
        # K로 나누기
        n //= K
        count += 1

    # 남은 수에 대하여 1씩 빼기
    while n > 1:
        n -= 1
        count += 1

    print(count)