n, k = map(int, input().split())
prices = list(map(int, input().split()))

h = False
buy_price = 0
last = 0
profit = 0
first_buy = True 

for p in prices:
    if not h:
        if first_buy or p <= last - k:
            buy_price = p
            h = True
            first_buy = False
    else:
        if p >= buy_price + k:
            profit += (p - buy_price)
            last = p
            h = False

print(profit)
