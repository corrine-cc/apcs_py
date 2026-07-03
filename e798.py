n = int(input())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)

cat = []
for r in range(0, n, 2):
    new_cat = []
    for c in range(0, n, 2):
        v1 = a[r][c]
        v2 = a[r][c + 1]
        v3 = a[r + 1][c]
        v4 = a[r + 1][c + 1]
        max_cattt = max(v1, v2, v3, v4)
        new_cat.append(max_cattt)
    cat.append(new_cat)
for i in cat:
    print(*i)
