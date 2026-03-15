#k520. P8.幸運基數 (Base)
n = int(input())

for m in range(60, 1, -1):
    low = 2

    high = int(n**(1/(m-1))) + 1 if m > 2 else n - 1

    while low <= high:
        k = (low + high) // 2

        total = 0
        p = 1
        for i in range(m):
            total += p
            if total > n: 
                break # 超過了就不用再加了
            if i < m - 1:
                p *= k
        
        if total == n:
            print(k)
            exit() # 找到最小的 k 了，直接結束程式
        elif total < n:
            low = k + 1
        else:
            high = k - 1
