F = int(input())
N = int(input())
y = list(map(int, input().split()))

bro = []
ans_round = -1
ans_text = ""

for i in range(N):
    # 哥哥出什麼
    if i == 0:
        move = F
    elif i >= 2 and y[i-1] == y[i-2]:
        if y[i-1] == 0: 
            move = 5
        elif y[i-1] == 2: 
            move = 0
        else: 
            move = 2
    else:
        move = y[i-1]
    
    bro.append(move)
    
    # 判斷勝負 (哥哥)
    if move == y[i]:
        pass # 平手
    elif (move == 0 and y[i] == 2) or (move == 2 and y[i] == 5) or (move == 5 and y[i] == 0):
        ans_round = i + 1
        ans_text = "Won"
        break 
    else:
        ans_round = i + 1
        ans_text = "Lost"
        break 


for i in range(len(bro)):
    print(bro[i], end=" ")

print(":", end=" ")

if ans_round == -1:
    print("Drew at round {}".format(N))
else:
    print("{} at round {}".format(ans_text, ans_round))
