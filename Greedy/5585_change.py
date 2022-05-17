product_price = int(input())
change = 1000 - product_price
coins = [500, 100, 50, 10, 5, 1]
count = 0

for index in range(len(coins)):
    count += change // coins[index]
    change %= coins[index]

print(count)