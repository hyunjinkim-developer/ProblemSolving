"""
Problem:
N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수

화폐의 단위에서 큰 단위가 작은 단위의 배수가 아니기 때문에 -> (Greedy 방식을 사용할 수 없고) DP 방식을 사용해야함
적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾기
"""

N, M = 0, 0
coins = list()

def get_input():
    global N, M, coins

    # Initialization
    N, M = 0, 0
    coins = list()

    N, M = map(int, input().split())
    for _ in range(N):
        coins.append(int(input()))


def DP():
    global N, M, coins

    # Memoization
    # Initialize with number bigger than maximum of M  1 ≤ M ≤ 10,000
    dp_table = [10001 for _ in range(M + 1)]
    dp_table[0] = 0 # The price of 0 is available with 0 coins

    # Bottom-Up
    for coin in coins:
        for i in range(coin, M + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)
    return dp_table


def main():
    global M

    get_input()

    dp_table = DP()
    if dp_table[M] == 10001:
        return -1
    else:
        return dp_table[M]


if __name__ == "__main__":
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        # #debug
        # if test_case == 2:
        #     break

        print(f"test case: {test_case}", "="*10)
        print(main())