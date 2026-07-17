while True:
    try:
        r, c = map(int,input().split()) 
        x = [] 
        for i in range(r):
            row = list(map(int,input().split()))
            x.append(row)
            
        for j in range(c):
            for i in range(r):
                print(x[i][j],end=" ")
            print()
    except:
        break
