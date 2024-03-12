"""
Problem:
N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수

화폐의 단위에서 큰 단위가 작은 단위의 배수가 아니기 때문에 -> (Greedy 방식을 사용할 수 없고) DP 방식을 사용해야함
적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾기
"""

"""
# Solution 1
def get_input():
    N, M = map(int, input().split())

    COINS = list()
    for i in range(N):
        COINS.append(int(input()))

    return N, M, COINS

def find_min_counts(N, M, COINS):
    # Initialization
    # 화폐 가치는 10,000보다 작거나 같은 자연수
    dp_table = [10001] * (M + 1)
    dp_table[0] = 0 

    for coin in COINS:
        for i in range((M + 1) - coin):
            dp_table[i + coin] = min(dp_table[i + coin], dp_table[i] + 1)
    return dp_table[M]

def main():
    N, M, COINS = get_input()

    answer = find_min_counts(N, M, COINS)
    if answer == 10001:
        answer = -1
    return answer
"""


# Solution 2: Sample Solution
def get_input():
    N, M = map(int, input().split())
    COINS = list()
    for i in range(N):
        COINS.append(int(input()))
    return N, M, COINS

# Bottom-up dynamic programming
def find_min_counts(N, M, COINS):
    # Initialization
    dp_table = [10001] * (M + 1)
    dp_table[0] = 0

    for coin in COINS:
        for i in range(coin, M + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)
    return dp_table[M]
def main():
    N, M, COINS = get_input()

    answer = find_min_counts(N, M, COINS)
    if answer == 10001:
        return -1
    else:
        return answer


if __name__ == "__main__":
    test_case = int(input())
    for i in range(1, test_case + 1):
        print(f"test case {i}: {main()}")