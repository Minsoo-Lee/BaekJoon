N = int(input())
arr = list(map(int, input().split()))

increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for index in range(1, N):
    if arr[index - 1] <= arr[index]:
        increase[index] = increase[index - 1] + 1
    if arr[index - 1] >= arr[index]:
        decrease[index] = decrease[index - 1] + 1

print(max(max(decrease), max(increase)))