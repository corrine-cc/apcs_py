#k517. P5.波動 (Wave)
p=int(input())
a=[]    #存每一個波的tupple
for i in range(p):
    q=list(input().split())
    c=q[0]
    d=int(q[1])
    v=int(q[2])
    x=d/v
    if c=="W":
        y=0
    elif c=="S":
        y=1
    elif c=="E":
        y=2
    else:
        y=3
    a.append((x,y))
a.sort()
for i in a:
    if i[1]==0:
        print("W",end="")
    elif i[1]==1:
        print("S",end="")
    elif i[1]==2:
        print("E",end="")
    else:
        print("N",end="")
