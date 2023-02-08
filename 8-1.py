# Fibonacci in recursive function

# Time took for calculation: 2 ^ (2 ^ 99 similar to 6 * 10 ^ 29)
import time
start_time = time.time()

def fibo(x):
    if x == 1 or x == 2:
        print(time.time() - start_time)
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(99))