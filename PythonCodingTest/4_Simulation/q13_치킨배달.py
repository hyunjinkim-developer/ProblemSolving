"""
Problem: https://www.acmicpc.net/problem/15686
"""

# Solution 1:
from itertools import combinations

N, M = 0, 0
houses, stores = [], []

def get_input():
    global N, M, houses, stores

    N, M = map(int, input().split())
    graph = []
    houses, stores = [], []
    for r in range(N):
        data = list(map(int, input().split()))
        graph.append(data)
        for c in range(N):
            if data[c] == 1:
                houses.append((r, c))
            elif data[c] == 2:
                stores.append((r, c))

def calculate_chicken_distance(group):
    global houses, stores
    city_chicken_distance = 0

    for house in houses:
        house_r, house_c = house
        chicken_distance = int(1e9)  # 2 <= N <= 50
        for store in group:
            store_r, store_c = store
            chicken_distance = min(chicken_distance, abs(house_r - store_r) + abs(house_c - store_c))
        city_chicken_distance += chicken_distance
    return city_chicken_distance

def select_store():
    global stores, M
    min_city_chicken_distance = int(1e9)
    # N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
    # 집의 개수는 2N개를 넘지 않으며
    # 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
    # chicken_distance 최대 2 * N 이라고 하면
    # 각 치킨집에서 집까지 chicken_distance의 합: (2 * N) * (2 * N) := 4 * N^2
    # M개의 치킨집을 선택하면 total_chicken_distance: M * (4 * N^2) ~ O(N^3)

    store_groups = list(combinations(stores, M))
    for group in store_groups:
        min_city_chicken_distance = min(min_city_chicken_distance, calculate_chicken_distance(group))
    return min_city_chicken_distance

def main():
    get_input()
    print(select_store())


import sys
sys.stdin = open("q13.txt", "r")

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"test case: {test_case}", "="*30)
        main()