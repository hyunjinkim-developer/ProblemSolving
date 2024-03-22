"""
Problem: https://www.acmicpc.net/problem/15686
    # N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
    # 집의 개수는 2N개를 넘지 않으며
    # 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
"""

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

    store_groups = list(combinations(stores, M))
    for group in store_groups:
        min_city_chicken_distance = min(min_city_chicken_distance, calculate_chicken_distance(group))
    return min_city_chicken_distance

def main():
    get_input()
    print(select_store())
"""

# Solution 2: Sample Solution
from itertools import combinations

N, M = 0, 0
houses, stores = [], []

def get_input():
    global N, M, houses, stores

    # Initialization
    N, M = 0, 0
    houses, stores = [], []

    N, M = map(int, input().split())
    for row in range(N):
        data = list(map(int, input().split()))
        for col in range(N):
            if data[col] == 1:
                houses.append((row, col))
            elif data[col] == 2:
                stores.append((row, col))

def select_store():
    global N, M, houses, stcores
    answer = int(1e9)

    def calculate_city_chicken_distance(group):
        city_chicken_distance = 0

        for h_r, h_c in houses:
            chicken_distance = int(1e9)
            for s_r, s_c in group:
                chicken_distance = min(chicken_distance, abs(h_r - s_r) + abs(h_c - s_c))
            city_chicken_distance += chicken_distance
        return city_chicken_distance

    store_groups = list(combinations(stores, M))
    for group in store_groups:
        # print(group)
        answer = min(answer, calculate_city_chicken_distance(group))
    return answer

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