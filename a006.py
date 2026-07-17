a,b,c=map(int,input().split())
x=b**2-(4*a*c)
n=(b*-1 + x**0.5)/(2*a) 
m=(b*-1 - x**0.5)/(2*a) 
y=(b*-1 + x**0.5)/(2*a)  
if x==0:  
  print('Two same roots x=%d'%y)
elif x>0:
  print('Two different roots x1=%d , x2=%d'%(n,m))
else:
  print('No real root')
