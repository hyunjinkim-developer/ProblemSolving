# Top-Down
# Fibonacci in recursive function using memoization (caching) method

# List for memoization
d = [0] * 100

# Top-down dynamic programming: Fibonacci in recursive function
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # Apply already calculated
    if d[x] != 0:
        return d[x]
    # if not calculated
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))