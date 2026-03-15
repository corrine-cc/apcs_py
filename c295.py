#c295. APCS-2016-1029-2最大和
n, m = map(int,input().split())
total = []
s = 0
for i in range(n):
  x = list(map(int,input().split()))
  s += max(x)
  total.append(max(x))
print(s)

y = []
for j in total:
  if s % j == 0:
    y.append(j)
if len(y) == 0:
   print("-1")
else:
  print(" ".join(map(str,y)))
