# 시간초과 떠서 질문 올림

strokes = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
boy = input()
girl = input()
res = []
for x in range(0, len(boy)):
    res.append(strokes[ord(boy[x]) - 65])
    res.append(strokes[ord(girl[x]) - 65])

def get_name(lst):
    temp = [lst[index] for index in range(0, len(lst))]
    for x in range (0, len(lst) - 2):
        print(0)
        temp = [((temp[index] + temp[index + 1]) % 10) for index in range(0, len(temp) - 1)]
        print(temp)
    return temp[0] * 10 + temp[1]

print(get_name(res))