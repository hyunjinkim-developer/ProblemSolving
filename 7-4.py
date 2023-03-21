# Get a lot of input data: use sys library
import sys

# Get input in strings
# sys.stdin.readline() is different from the input() method as it also reads the escape character entered by the user
# rstrip() removes any trailing characters (characters at the end a string)
input_data = sys.stdin.readline().rstrip()

print(input_data)