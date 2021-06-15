L = int(input())
inputstr = input()
dic = {}
for i, ch in enumerate(range(ord('a'), ord('z')+1)):
    ch = chr(ch)
    dic[ch] = i+1
HASH = 0
M = 1234567891
for i, ch in enumerate(inputstr):
    HASH = (HASH + dic[ch]*31**i)%M
   
print(HASH)