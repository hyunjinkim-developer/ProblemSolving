def get_input():
    N = int(input())
    return N

def cover_floor(N):
    dp_table = [0] * N

    dp_table[0] = 1
    dp_table[1] = 3
    # ai = ai-1 + ai-2 × 2
    for i in range(2, N):
        dp_table[i] = dp_table[i - 1] + (dp_table[i - 2] * 2)

    return dp_table[N - 1]

def main():
    N = get_input()

    answer = cover_floor(N)
    return answer % 796796

if __name__ == "__main__":
    print(main())
