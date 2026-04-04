def solve():

    line = input().split()
    r1, c1, R, C, r_limit = map(int, line)

    A = []
    sum_a = 0
    for i in range(r1):
        row = list(map(int, input().split()))
        A.append(row)
        sum_a += sum(row)

    B = []
    for i in range(R):
        B.append(list(map(int, input().split())))

    count = 0
    min_diff = -1

    for i in range(R - r1 + 1):
        for j in range(C - c1 + 1):
            
            dist = 0  
            current_sum = 0 

            for dr in range(r1):
                for dc in range(c1):
                    if A[dr][dc] != B[i+dr][j+dc]:
                        dist += 1
                    current_sum += B[i+dr][j+dc]
            
            if dist <= r_limit:
                count += 1
                diff = abs(current_sum - sum_a)
                
                if min_diff == -1 or diff < min_diff:
                    min_diff = diff

    print(count)
    if count == 0:
        print(-1)
    else:
        print(min_diff)

solve()
