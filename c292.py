x = int(input())
y = int(input()) #0代表左 、1代表上 、2代表右 、3代表下

n = []
for i in range(x):
        m = list(map(int,input().split()))
        n.append(m)

#初始位子
r = x//2
c = x//2

ans = str(n[r][c])

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

index_dir = y   #目前方向

step_size = 1
step_count = 0

while len(ans) < x * x:
    for i in range(step_size):
        if len(ans) == x * x:
            break
        
        r += dr[index_dir]
        c += dc[index_dir]
        
        ans += str(n[r][c])
    if len(ans) == x*x:
        break
    
    index_dir = (index_dir + 1) % 4
    
    #計算步長
    step_count += 1
    if step_count == 2:
        step_size += 1
        step_count = 0
print(ans)
        
        
