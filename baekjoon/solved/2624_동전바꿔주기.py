import sys
input = lambda: sys.stdin.readline().rstrip()


T = int(input())

k = int(input())

coins = [list(map(int, input().split())) for _ in range(k)]
# [p, n]
# 금액, 개수

cache = [[-1]*(10000+1) for _ in range(len(coins))]

def solve(t, p):
    if t < 0:
        return 0
    elif t == 0:
        return 1

    if p >= len(coins):
        return 0

    if cache[p][t] != -1:
        return cache[p][t]

    cache[p][t] = 0
    for i in range(coins[p][1] + 1):
        cache[p][t] += solve(t - i*coins[p][0], p + 1)

    return cache[p][t]

print(solve(T, 0))
