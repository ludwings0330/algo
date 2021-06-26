inputstr = input().upper()
dic = {}
MAX = 0
for ch in inputstr:
    if ch in dic:
        dic[ch] += 1
        MAX = max(MAX, dic[ch])
    else:
        dic[ch] = 1
        MAX = max(MAX, dic[ch])

ans = []
for ch in dic:
    if dic[ch] == MAX:
        ans.append(ch)
if len(ans) >1:
    print('?')
else:
    print(ans[0])