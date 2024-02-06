# Show called function in the recursive manner

d = [0] * 100

def fibo(x):
    print("Start f({})".format(str(x)))

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        print("f({}):{}".format(x, d[x]), end=" ")
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)