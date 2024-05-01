"""
# Problem: https://www.acmicpc.net/problem/16199
어떤 사람의 생년월일과 기준 날짜가 주어졌을 때, 기준 날짜를 기준으로 그 사람의 만 나이, 세는 나이, 연 나이를 모두 구하는 프로그램을 작성하시오.
"""

birth_year, birth_month, birth_day = 0, 0, 0
current_year, current_month, current_day = 0, 0, 0

def get_input():
    global birth_year, birth_month, birth_day, current_year, current_month, current_day

    birth_year, birth_month, birth_day = map(int, input().split())
    current_year, current_month, current_day = map(int, input().split())

def calculate_gloabl_age():
    # 만 나이: 국제적인 표준 방법이다. 한국에서도 법에서는 만 나이만을 사용한다.
    # 만 나이는 생일을 기준으로 계산한다. 어떤 사람이 태어났을 때, 그 사람의 나이는 0세이고, 생일이 지날 때마다 1세가 증가한다.
    # 예를 들어, 생일이 2003년 3월 5일인 사람은 2004년 3월 4일까지 0세이고, 2004년 3월 5일부터 2005년 3월 4일까지 1세이다.
    global birth_year, birth_month, birth_day, current_year, current_month, current_day
    age = 0
    if birth_month < current_month:
        age += (current_year - birth_year)
    elif current_month == birth_month:
        if 0 <= (current_day - birth_day):
            age += (current_year - birth_year)
        else:
            age += (current_year - birth_year - 1)
    else:
        age += (current_year - birth_year - 1)
    return age

def calculate_korean_age():
    # 세는 나이: 한국에서 보통 나이를 물어보면 세는 나이를 의미한다.
    # 세는 나이는 생년을 기준으로 계산한다. 어떤 사람이 태어났을 때, 그 사람의 나이는 1세이고, 연도가 바뀔 때마다 1세가 증가한다.
    # 예를 들어, 생일이 2003년 3월 5일인 사람은 2003년 12월 31일까지 1세이고, 2004년 1월 1일부터 2004년 12월 31일까지 2세이다.
    global birth_year, birth_month, birth_day, current_year, current_month, current_day

    age = 1 + (current_year - birth_year)
    return age

def calculate_legal_age():
    # 연 나이: 법률에서 일괄적으로 사람을 구분하기 위해서 사용하는 나이이다.
    # 연 나이는 생년을 기준으로 계산하고, 현재 연도에서 생년을 뺀 값이다.
    # 예를 들어, 생일이 2003년 3월 5일인 사람은 2003년 12월 31일까지 0세이고, 2004년 1월 1일부터 2004년 12월 31일까지 1세이다.
    global birth_year, birth_month, birth_day, current_year, current_month, current_day

    age = 0 + (current_year - birth_year)
    return age

def main():
    get_input()

    print(calculate_gloabl_age())
    print(calculate_korean_age())
    print(calculate_legal_age())

# # Comment below before submission
# import sys
# sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    main()

    # #debug
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     main()
