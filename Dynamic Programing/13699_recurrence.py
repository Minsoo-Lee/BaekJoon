N = int(input())
arr = [0 for _ in range(N + 1)]
arr[0] = 1

for i in range(1, N + 1):
    for j in range(0, i):
        arr[i] += arr[j] * arr[i - j - 1]

print(arr[N])
