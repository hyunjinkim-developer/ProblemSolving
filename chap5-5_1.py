"""
Factorial
"""

# Method 1] iteratively
def factorial_iterative(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

# Method 2] recursively
def factorial_recursive(n):
	if n <= 1:
		return 1
	return n * factorial_recursive(n - 1)

print("Iterative: ", factorial_iterative(5)) 
print("Recursive: ", factorial_recursive(5))

