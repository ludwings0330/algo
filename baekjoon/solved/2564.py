import sys
input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())
MAP = [0] * (W+H) * 2
shops = []
for i in range(N+1):
    d, l = map(int, input().split())
    if d == 1:
        i = W - l
        pass
    elif d == 3:
        i = W + l
        pass
    elif d == 2:
        i = W + H + l
        pass
    elif d == 4:
        i = W + H + W + H - l
        pass
    shops.append(i)
    MAP[i] = 1
DG = shops[-1]
l, r = DG, DG
c = 0
while l >= 0 or r < len(MAP):
    if l>= 0:
        MAP[l] = c
    if r< len(MAP):
        MAP[r] = c
    c += 1
    l -= 1
    r += 1
answer = 0
for shop in shops[:-1]:
    MIN = min((W+H)*2-MAP[shop], MAP[shop])
    answer += MIN
print(answer)