n, k = map(int, input().split())

pascal = [[0 for x in range(31)] for x in range(31)]
pascal[0] = [0]
pascal[1] = [1]
pascal[2] = [1, 1]

for i in range(3, n + 1):
    pascal[i][0] = 1
    for j in range(1, i - 1):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    pascal[i][i - 1] = 1

print(pascal[n][k - 1])