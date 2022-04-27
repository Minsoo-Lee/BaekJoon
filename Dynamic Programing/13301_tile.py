N = int(input())
a = 4
b = 6

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    for _ in range(3, N + 1):
        result = a + b
        a = b
        b = result
    print(result)