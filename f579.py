line1 = input().split()
A = int(line1[0])
B = int(line1[1])

N = int(input())

# 同時買了A 和 B 
total_buyers = 0

for i in range(N):
    record = list(map(int, input().split()))
    
    countA = 0
    countB = 0
    
    for x in record:
        if x == 0: 
            break
        
        # 商品 A
        if x == A:
            countA = countA + 1
        elif x == -A:
            countA = countA - 1
            
        # 商品 B
        if x == B:
            countB = countB + 1
        elif x == -B:
            countB = countB - 1
            
    # 2合一大於 0，代表他有買
    if countA > 0 and countB > 0:
        total_buyers = total_buyers + 1

print(total_buyers)
