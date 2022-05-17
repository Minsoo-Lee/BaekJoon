while True:
    try :
        position = list(map(int, input().split()))
        position.sort()
        max_value = max(position[1]-position[0], position[2]-position[1])
        print(max_value - 1)
    except:
        exit()