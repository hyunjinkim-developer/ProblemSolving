"""
# Solution 1:
def get_input():
    N = int(input())
    food_storage = list(map(int, input().split()))
    return N, food_storage

def rob_food(N, food_storage):
    max_robbed_food = 0
    dp_table = [0] * N
    for i in range(N):
        dp_table[i] = food_storage[i]

    for i in range(2, N):
        dp_table[i] += food_storage[i - 2]
        max_robbed_food = max(max_robbed_food, dp_table[i])

    return max_robbed_food

def main():
    N, food_storage = get_input()

    max_robbed_food = rob_food(N, food_storage)
    return max_robbed_food
"""


# Solution 2: Sample solution
def main():
    N = int(input())
    food_storage = list(map(int, input().split()))

    dp_table = [0] * N

    # Bottom up dynamic Programming
    # foods that saved in the last index is the maximum foods that can be robbed
    dp_table[0] = food_storage[0]
    dp_table[1] = max(dp_table[0], dp_table[1])
    for i in range(2, N):
        dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + food_storage[i])

    return dp_table[N - 1]



if __name__ == "__main__":
    print(main())