n, k = map(int, input().split())

count = 0
total = 0

for i in range(n):
    a, b, c = map(int, input().split())
    
    mx = max(a, b, c)
    mn = min(a, b, c)
    
    if mx - mn >= k:
        count += 1
        total += (a + b + c) // 3

print(count, total)
