import math

seed, total_year = map(int, input().split())

interest = [1.35, 1.2, 1.05]
year = [5, 3, 1]

arr = [0 for _ in range(0, total_year + 1)]
arr[0] = seed

for i in range(1, total_year + 1):
    if i >= 5:
        arr[i] = math.floor(max(arr[i - 5] * 1.35, arr[i - 3] * 1.2, arr[i - 1] * 1.05))
    elif i >= 3:
        arr[i] = math.floor(max(arr[i - 3] * 1.2, arr[i - 1] * 1.05))
    else:
        arr[i] = math.floor(arr[i - 1] * 1.05)
print(arr)
print(arr[total_year])
    