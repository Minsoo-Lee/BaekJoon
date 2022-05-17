N = int(input())
seats = str(input())

if len(seats) == 1:
    print(1)
else:
    seats = seats.replace('S', '*')
    seats = seats.replace('LL', '*')
    print(len(seats) + 1)