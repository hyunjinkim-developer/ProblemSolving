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

if __name__ == "__main__":
    print(main())