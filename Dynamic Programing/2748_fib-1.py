n = int(input())

def fib(n):
    lst = [1 for x in range(0, n + 1)]
    for i in range(3, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    return lst[n]

print(fib(n))