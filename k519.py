#k519. P7.機票 (Ticket)
n = int(input())

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start, end = map(int, input().split())
start -= 1
end -= 1

# 設定距離
l = [999999999] * n  
v = [False] * n        # 紀錄有沒有走過

l[start] = 0

for i in range(n):
    # 找目前最小距離的點
    min_l = 999999999999
    min_index = -1
    
    for j in range(n):
        if not v[j] and l[j] < min_l:
            min_l = l[j]
            min_index = j
    
    if min_index == -1: break # 如果找不到路了就跳出
    v[min_index] = True
    

    for k in range(n):
        if graph[min_index][k] != -1 and not v[k]:
            cost = graph[min_index][k]
            if min_index != start:
                cost -= 50
            
            if l[min_index] + cost < l[k]:
                l[k] = l[min_index] + cost

print(int(l[end]))
