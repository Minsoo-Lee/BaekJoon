N = int(input())
coins = [25, 10, 5, 1]

for _ in range(N):
    change = int(input())
    coins_count = [0, 0, 0, 0]
    for index in range(4):
        coins_count[index] += change // coins[index]
        change %= coins[index]

print(coins_count[0], coins_count[1], coins_count[2], coins_count[3])
