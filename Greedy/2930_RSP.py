round = int(input())
my = input()
friends_count = int(input())
friends = [input() for _ in range(friends_count)]
result1 = 0
result2 = 0

def round_result(my, fr):
    count = 0
    if (my == 'R' and fr == 'S') or (my == 'S' and fr == 'P') or (my == 'P' and fr == 'R'):
        count = 2
    elif (my == fr):
        count = 1
    return count

def set_winning_unit(data):
    if data == 'S':
        return 'R'
    elif data == 'R':
        return 'P'
    else:
        return 'S'

def winning_func(friends, data):
    arr = []
    RSP = []
    for index in range(round):
        RSP.append(set_winning_unit(friends[index]))
    #for index in range(1, friends_count):
        #if round_result(RSP[index], friends[index][data]):
            #return

winning = []
for _ in range(round):
    winning.append(winning_func(data))


for round_index in range(round):
    for friends_index in range(friends_count):
        result1 += round_result(my[round_index], friends[friends_index][round_index])
        result2 += round_result(winning[round_index], friends[friends_index][round_index])

print(winning)
print(result1)
print(result2)