a=list(input())

if a[0]=="W":
    x=32
elif a[0]=="X":
    x=30
elif a[0]=="Y":
    x=31
elif a[0]=="Z":
    x=33
elif a[0]=="I":
    x=34
elif a[0]=="O":
    x=35
elif ord(a[0])<ord("I"):
    x=ord(a[0])-55
elif ord(a[0])<ord("O"):
    x=ord(a[0])-56
else:
    x=ord(a[0])-57
s=x//10+(x%10)*9
for i in range(1,9):
    s+=int(a[i])*(9-i)

    
s+=int(a[9])
if s%10==0:
    print("real")
else:
    print("fake")
