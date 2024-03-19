# Solution 1:
def get_input():
    N = input()
    return N

def find_luckystraight(string):
    string_mid_idx = int(len(string) / 2)
    front, rear = string[: string_mid_idx], string[string_mid_idx: len(string)]

    front_sum = 0
    for number in front:
        front_sum += int(number)

    rear_sum = 0
    for number in rear:
        rear_sum += int(number)

    if front_sum == rear_sum:
        print("LUCKY")
    else:
        print("READY")

def main():
    N = get_input()
    find_luckystraight(N)

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"test case: {test_case}", '-'*30)
        main()