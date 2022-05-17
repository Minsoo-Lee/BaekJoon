N = int(input())
price = list(map(int, input().split()))
if len(price) > 1:
    price.remove(max(price))
print(sum(price))