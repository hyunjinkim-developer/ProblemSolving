# Bottom-Up
# Iteration with Memoization
# Memoization: save already calculated

d =[0] * 100

d[1] = 1
d[2] = 1
n = 99

# Bottom up Dynamic Programming Fibonacci in iteration
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])