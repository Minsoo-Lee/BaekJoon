boy = input()
girl = input()
result = []
for index in range(0, len(boy)):
    result.append(ord(boy[index]) - 48)
    result.append(ord(girl[index]) - 48)

def phone_recursive(lst):
    if len(lst) == 2:
        return str(lst[0]) + str(lst[1])
    temp = [(lst[index] + lst[index + 1]) % 10 for index in range(0, len(lst) - 1)]
    return phone_recursive(temp)

print(phone_recursive(result))