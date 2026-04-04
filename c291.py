n = int(input())

friends = list(map(int, input().split()))

visited = [False] * n
count = 0

for i in range(n):
    if not visited[i]:
        count += 1  
        current = i
        while not visited[current]:
            visited[current] = True    
            current = friends[current] 

print(count)
