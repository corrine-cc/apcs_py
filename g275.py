T = int(input())

for i in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = ""
    
    # 規則 A
    if not (a[1] != a[3] and a[1] == a[5] and
            b[1] != b[3] and b[1] == b[5]):
        ans += "A"
    
    # 規則 B
    if not (a[6] == 1 and b[6] == 0):
        ans += "B"
    
    # 規則 C
    if not (a[1] != b[1] and a[3] != b[3] and a[5] != b[5]):
        ans += "C"
    
    if ans == "":
        print("None")
    else:
        print(ans)


