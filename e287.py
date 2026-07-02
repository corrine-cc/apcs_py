n, m = map(int,input().split())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)

min_ = 1000000000
start_r = 0
start_c = 0
for r in range(n):
    for c in range(m):
        if a[r][c] < min_:
            min_ = a[r][c]
            start_r = r
            start_c = c
now_r = start_r
now_c = start_c
s = a[now_r][now_c]
a[now_r][now_c] = -1

rc = [(0, -1), (-1, 0), (0, 1), (1, 0)] #左上右下

while True:
    next_r = -1
    next_c = -1
    next_min = 10000000000 #用來紀錄四周格子min值
    #檢查四個方向的坐標
    for dr, dc in rc:
        nr = now_r + dr
        nc = now_c + dc
        
        #有沒有超出範圍
        if 0 <= nr < n and 0 <= nc < m:
            #檢查是不是走過
            if a[nr][nc] !=-1:
                #找四周最小值
                if a[nr][nc] < next_min:
                    next_min = a[nr][nc]
                    next_r = nr
                    next_c = nc
    #判斷能不能走
    if next_r == -1 and next_c == -1:
        break
    else:
        now_r = next_r
        now_c = next_c
        s += a[now_r][now_c]
        a[now_r][now_c] = -1
print(s)
