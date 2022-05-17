micro_time = [300, 60, 10]
cook_time = int(input())

def cook_func(micro_time, cook_time):    
    if cook_time % 10 != 0:
        print(-1)
    else:
        micro_count = [0, 0, 0]
        for index in range(0, 3):
            micro_count[index] += cook_time // micro_time[index]
            cook_time %= micro_time[index]
        print(micro_count[0], micro_count[1], micro_count[2])

cook_func(micro_time, cook_time)