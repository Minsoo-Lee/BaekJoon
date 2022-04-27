R, C, W = map(int, input().split())

pascal = [[0 for x in range(0, R + W + 1)] for x in range(0, R + W + 1)]
pascal[0] = [0]
pascal[1] = [1]
pascal[2] = [1, 1]

for i in range(3, R + W + 1):
    pascal[i][0] = 1
    for j in range(1, i - 1):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    pascal[i][i - 1] = 1

result = 0
for i in range(0, W):
    for j in range(0, i + 1):
        result += pascal[R + i][C + j - 1]

print(result)