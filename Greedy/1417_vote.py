N = int(input())
celeb = []
for _ in range(N):
    celeb.append(int(input()))

if len(celeb) == 1:
    print(0)
else:
    count = 0
    while True:
        if celeb[0] <= max(celeb[1:]):
            index = celeb[1:].index(max(celeb[1:]))
            celeb[index + 1] -= 1
            celeb[0] += 1
            count += 1
        else:
            break
    print(count)