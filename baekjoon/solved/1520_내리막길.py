'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

3
'''


import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cache = [[-1] * C for _ in range(R)]

cache[R-1][C-1] = 1

move = ((1, 0), (-1, 0), (0, 1), (0, -1))

def solve(r, c):
    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = 0
    for i in range(len(move)):
        tr = r + move[i][0]
        tc = c + move[i][1]
        if 0 <= tr < R and 0 <= tc < C and board[r][c] > board[tr][tc]:
            cache[r][c] += solve(tr, tc)

    return cache[r][c]

print(solve(0, 0))