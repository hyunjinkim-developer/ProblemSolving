"""
Problem:
첫째 줄에 N(1 ≤ N ≤ 100,000)과 K(1 ≤ K ≤ 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
이때 입력으로 주어지는 N이 K보다 작을 수도 있다.
"""

N, K = 0, 0
count = 0

def get_input():
    global N, K, count

    # Initialization
    N, K, count = 0, 0, 0

    N, K = map(int, input().split())
    print(f"input N, K: {N, K}")

def process():
    global N, K, count

    if N < K or K == 1:
        while N != 1:
            N -= 1
            count += 1
    else:
        while N != 1:
            print(N)
            if N % K == 0:
                N /= K
            else:
                N -= 1
            count += 1
    return count

def main():
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        print(f"test case: {test_case}", "="*30)

        get_input()
        print(process())

if __name__ == "__main__":
    main()