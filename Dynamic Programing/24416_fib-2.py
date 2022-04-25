n = int(input())
count = 1

def fib(n):
    fib = [1 for x in range(0, n + 1)]
    for index in range(3, n + 1):
        fib[index] = fib[index - 1] + fib[index - 2]
    return fib[n]
print(fib(n))