arr = str(input())
count = 1

for index in range(len(arr) - 1):
    if ord(arr[index]) >= ord(arr[index + 1]):
        count += 1

print(count)