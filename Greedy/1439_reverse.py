S = input()
check = [0, 0]
index = 0
length = len(S)

while index < length:
    if index < length and S[index] == '0':
        while index < length and S[index] == '0':
            index += 1
        check[0] += 1
    if index < length and S[index] == '1':
        while index < length and S[index] == '1':
            index += 1
        check[1] += 1
    
print(min(check))
