# SWEA 모의 SW역량 테스트 baseline

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3_Greedy
c, d, e = 1.0, 2.5_BFS-DFS, 3_Greedy.4_Simulation
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

n = 0
dust = []

def get_input():
    global n, dust

    # Initialization
    n = 0
    dust = []

    n = int(input())

    for _ in range(n):
        dust.append(list(map(int, input().split())))

def next_move():
    global n
    moves = []

    dirs = []
    for step in range(n - 1):
        for

def solution():
    # 처음에 정가운데 격자에는 먼지가 존재하지 않습니다.
    # 왼쪽 - 아래쪽 - 오른쪽 - 위쪽 순서로 이동하며 청소
    #  n이 홀수이기 때문에 항상 왼쪽 위에서 끝나게
    # 이동한 먼지는 기존의 먼지 양에 더해지고, 빗자루가 이동한 위치(Curr)에 있는 먼지는 모두 없어지게
    #  a%에 해당하는 먼지 양은
    #   다른 격자에 이동한 먼지의 양을 모두 합한 것을
    #   이동한 위치에 있던 먼지의 양에서 빼고 남은 먼지에 해당합니다.
    #  비율을 곱해줄 때 소숫점 아래의 숫자는 버림
    next_move()

    # 격자 바깥으로 나간 먼지의 양을 출력하세요.
    return



'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

DEBUG = True
# DEBUG = False # For submission


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    if DEBUG:
        print(f"test case: {test_case}", "="*30)
        print(solution())
    # ///////////////////////////////////////////////////////////////////////////////////
    if not DEBUG:
        answer = solution()
        print("#%d:" % test_case, answer)