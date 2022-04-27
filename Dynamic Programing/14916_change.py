n = int(input())
five_bucks = 0
result = [-1]

while five_bucks * 5 <= n:
    if (n - five_bucks * 5) % 2 == 0:
        result.append(five_bucks + (n - five_bucks * 5) // 2)
    five_bucks += 1

if len(result) == 1:
    print(result[0])
else:
    result.remove(-1)
    print(min(result))