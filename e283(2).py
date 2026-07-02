dsion = {
    "0101": "A",
    "0111": "B",
    "0010": "C",
    "1101": "D",
    "1000": "E",
    "1100": "F"
}

while True:
    try:
        n = input()
        if not n:
            continue
        ans = ""
        for i in range(int(n)):
            x = input().replace(" ", "")
            ans += dsion[x]
        print(ans)
    except:
        break
