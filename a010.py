n=int(input())
a=2 #可能的因數
while n!=1:
  ac=0 #這個因數的次方
  while n%a==0:
    ac+=1
    n/=a
  if ac>=1: #表示a是因數
    if n==1:
      if ac>1:
        print('{}^{}'.format(a,ac))
      else:
        print('{}'.format(a))
    else:
      if ac>1:
        print('{}^{} * '.format(a,ac),end='')
      else:
        print('{} * '.format(a),end='')
  a+=1
