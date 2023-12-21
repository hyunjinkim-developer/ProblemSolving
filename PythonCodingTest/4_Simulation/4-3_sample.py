def main():
    input_data = input()
    row = int(input_data[1])
    # convert column name from alphabet to number using ord()
    # ord() function returns the number representing the unicode code of a specified character
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if 1 <= next_row and next_row <= 8 and 1 <= next_column and next_column <= 8:
            result += 1

    print(result)

if __name__ == "__main__":
    main()