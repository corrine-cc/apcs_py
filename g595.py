n = int(input())
a = list(map(int, input().split()))

cost = 0

for i in range(n):
    if a[i] == 0:
        if i == 0:
            cost += a[1]
        elif i == n-1:
            cost += a[n-2]
        else:
            cost += min(a[i-1], a[i+1])

print(cost)
