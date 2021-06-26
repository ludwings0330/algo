dic = {}
inputStr = input()

for i, ch in enumerate(inputStr):
    if ch not in dic:
        dic[ch] = i
for ch in range(ord('a'), ord('z')+1):
    ch = chr(ch)
    if ch in dic:
        print(dic[ch], end = ' ')
    else:
        print(-1, end=' ')