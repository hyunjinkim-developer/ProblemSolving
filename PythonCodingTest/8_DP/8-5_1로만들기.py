"""
# Solution 1:
def get_input():
    N = int(input())
    return N

def process(N):
    # Memoization
    dp_table = [0] * 30001 # 1 ≤ X ≤ 30,000

    for i in range(2, N + 1):
        dp_table[i] = dp_table[i - 1] + 1

        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)

        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)

        if i % 5 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)

    return dp_table[N]

def main():
    N = get_input()
    min_count = process(N)
    return min_count
"""

# Solution2: Sample solution
# Enter the number of food storage and food in each storage
def main():
    x = int(input())

    d = [0] * 30001

    for i in range(2, x + 1):
        # Current number - 1
        d[i] = d[i - 1] + 1
        # Current number is divided by 2
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        # Current number is divided by 3_Greedy
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        # Current number is divided by 5_BFS-DFS
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[x]


if __name__ == "__main__":
    print(main())