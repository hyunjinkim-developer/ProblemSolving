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
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# ! Comment before submission
# import sys
# sys.stdin = open("5658_sample_input.txt", "r")


# User defined functions
def get_input():
    N, K = map(int, input().split())
    num_str = input()
    return N, K, num_str

# Split string in every N/4 characeters
def split_str(num_length, num_str, nums):
    new_num = ""
    for idx, char in enumerate(num_str):
        if idx != 0 and idx % num_length == 0:
            nums.add(new_num)
            new_num = ""
        new_num += char
        # Add last number
        if idx == len(num_str) - 1:
            nums.add(new_num)
    return nums


# Convert hex to decimal
def convert_to_decimal(target_number: str):
    decimal_num = 0
    hex_converstion = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15 }
    # target_number[::-1]: Convert left-right for easeier calculation
    for idx, char in enumerate(target_number[::-1]):
        if "0" <= char <= "9":
            decimal_num += int(char) * (16 ** idx)
        else:
            decimal_num += hex_converstion[char] * (16 ** idx)
    return decimal_num


# Solution
def solution(N, K, num_str):
    nums = set()  # available numbers
    num_length = N // 4

    # Rotate in max of (num_length - 1)
    for start_idx in range(num_length):
        rotated_str = num_str[start_idx:] + num_str[:start_idx]
        nums = split_str(num_length, rotated_str, nums)

    # Sort in DESC
    nums = sorted(nums, reverse=True)
    target_number = nums[K - 1]


    # Convert hex to decimal
    decimal_number = convert_to_decimal(target_number)

    return decimal_number


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # get input
    N, K, num_str = -1, -1, ""
    N, K, num_str = get_input()

    # solution
    answer = solution(N, K, num_str)

    print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////