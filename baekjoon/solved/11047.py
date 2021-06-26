import sys
input = sys.stdin.readline

N, K = map(int, input().split())

s, e = 0, 0
coins = []
for _ in range(N):
    coins.append(int(input()))

ret = 0
for coin in reversed(coins):
    if K // coin < 1:
        continue
    else:
        ret += K//coin
        K %= coin

print(ret)