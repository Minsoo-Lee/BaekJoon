N = int(input())
road = list(map(int, input().split()))
start = 0
count = 1
front = 0

for index in range(1, len(road)):
    if road[start] != 0:
        start += 1
        front = start
    else:
        if road[front] == 1 or road[front] == 0:
            if road[index] == road[front] + 1:
                front = index
                count += 1
        else:
            if road[index] == 0:
                front = index
                count += 1

print(count)