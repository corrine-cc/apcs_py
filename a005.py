x=int(input())
for i in range(x):
  a,b,c,d=map(int,input().split())
  if b/a==d/c:
    e=d*c/b
    e=int(e)
    print(a,b,c,d,e)
  else:
    e=d+c-b
    print(a,b,c,d,e)
