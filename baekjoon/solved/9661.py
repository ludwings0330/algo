import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())


# 상근 -> 0, SK
# 창영 -> 1, CY

def solve(n, cnt, player):
    if n == 0:
        return player
    if n == 1:
        return solve(n-1, 0, (player+1) % 2)

    tmp = 1
    k = 0
    while tmp < n:
        tmp *= 4
        k += 1

    if cnt % 2 == 1:
        tmp //= 4
        return solve(n - tmp, cnt-1, (player+1)%2)
    else: # 짝수라면?
        if n%4 == 0:
            return solve(n-1, cnt+2, (player+1)%2)
        else:
            return player
encode = []
tmp = N
while tmp > 0:
    encode.append(tmp % 4)
    tmp //= 4

ans = solve(N, sum(encode), 0)

print('SK' if ans == 1 else 'CY')
