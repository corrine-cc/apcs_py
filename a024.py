a,b=map(int,input().split())
d=a%b  #a除以b的餘數
#d=a%b
while d!=0:
  a=b
  b=d
  d=a%b
print(b)
