"""
# Solution 1:
def get_input():
    string = input()
    return string

def parsing(string):
    answer = ""

    sum = 0
    letters = []
    for s in string:
        if s.isalpha():
            letters.append(s)
        elif s.isnumeric():
            number = ord(s) - ord("0")
            sum += number
    letters.sort()
    answer = answer.join(letters)
    answer += str(sum)
    return answer

def main():
    string = get_input()
    print(parsing(string))
"""

# Solution 2:
def get_input():
    input_string = input()
    return input_string

def parsing(input_string):
    result = []
    sum = 0
    for s in input_string:
        if s.isalpha():
            result.append(s)
        else:
            sum += int(s)
    result.sort()

    if sum != 0:
        result.append(str(sum))
    return "".join(result)

def main():
    input_string = get_input()
    print(parsing(input_string))


if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"test case: {test_case}", "-"*30)
        main()