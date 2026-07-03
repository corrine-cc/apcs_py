n, m = map(int, input().split())

a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

blank_line = input()

b = []
for i in range(n):
    y = list(map(int, input().split()))
    b.append(y)

# 計算轉換圖的列總和與行總和
row = []
for r in range(n):
    row.append(sum(b[r]))

col = []
for c in range(m):
    total = 0
    for r in range(n):
        total += b[r][c]
    col.append(total)

new = []
for r in range(n):
    new_r = []
    for c in range(m):
        tt = row[r] + col[c] - b[r][c]

        if tt % 2 != 0:

            new_r.append(1 - a[r][c])
        else:

            new_r.append(a[r][c])
    new.append(new_r)

for r in range(n):
    for c in range(m):
        print(new[r][c], end=" ")
    print()  
