import sys
sys.setrecursionlimit(10**9)

T = int(input())
move = ((0, 1), (0, -1), (1, 0), (-1, 0))

cache = [[[-1] * (1001) for _ in range(3)] for _ in range(4)]
for r in range(4):
    for c in range(3):
        cache[r][c][1] = 1

# cache[r][c][n]

DIV = 1234567

def password(r, c, n):
    if 0 <= r < 4 and 0 <= c < 3:
        pass
    else:
        return 0

    if r == 3:
        if c != 0:
            return 0

    if cache[r][c][n] != -1:
        return cache[r][c][n]


    cache[r][c][n] = 0
    for (dr, dc) in move:
        tr = r + dr
        tc = c + dc

        cache[r][c][n] += password(tr, tc, n-1)
        cache[r][c][n] %= DIV

    return cache[r][c][n]

def solve(N):
    ret = 0
    for r in range(3):
        for c in range(3):
            ret += password(r, c, N)
            ret %= DIV

    ret += password(3, 0, N)
    ret %= DIV

    return ret

while T:
    T -= 1
    N = int(input())
    print(solve(N))
