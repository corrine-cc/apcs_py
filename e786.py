n = input()
a = len(n)
if a % 2 != 0:
    print("NO")
else:
    m = a // 2
    
    x = n[:m]
    y = n[m:]
    if y == x[::-1]:
        print("YES")
        print(x)
    else:
        print("NO")
    
