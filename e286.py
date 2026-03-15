#e286. 籃球比賽
h1 = list(map(int, input().split()))
a1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

home1 = sum(h1)
away1 = sum(a1)

home2 = sum(h2)
away2 = sum(a2)

print("{}:{}".format(home1,away1))
print("{}:{}".format(home2,away2))

win = 0
lose = 0

if home1 > away1:
    win += 1
else:
    lose += 1

if home2 > away2:
    win += 1
else:
    lose += 1

if win == 2:
    print("Win")
elif lose == 2:
    print("Lose")
else:
    print("Tie")
