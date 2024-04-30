# Problem : https://www.acmicpc.net/problem/5532
# 방학은 총 L일이다.
# 수학은 총 B페이지, 국어는 총 A페이지를 풀어야 한다.
# 상근이는 하루에 국어를 최대 C페이지, 수학을 최대 D페이지 풀 수 있다.
# 상근이가 겨울 방학동안 숙제를 하지 않고 놀 수 있는 최대 날의 수를 구하는 프로그램을 작성하시오.

L, A, B, C, D = 0, 0, 0, 0, 0

def get_input():
    global L, A, B, C, D

    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

def count_days_left():
    global L, A, B, C, D

    while True:
        if A <= 0 and B <= 0: break

        A -= C
        B -= D
        L -= 1
    return L


def main():
    get_input()
    print(count_days_left())


# # Comment below before submission
# import sys
# sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    main()

    # T = int(input())
    # for test_case in range(1, T + 1):
    #     main()

