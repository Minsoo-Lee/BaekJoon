N = int(input())
five_bucks = 0
result = [-1]

while five_bucks * 5 <= N:
    temp = (N - five_bucks * 5) % 3
    if (N - five_bucks * 5) % 3 == 0:
        result.append(five_bucks + (N - five_bucks * 5) // 3)
    five_bucks += 1
    
if len(result) == 1:
    print(result[0])
else:
    result.remove(-1)
    print(min(result))