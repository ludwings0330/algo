import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))


def solve(r, c):
    if board[r][c] == 'W':
        return 0
    dq = deque()
    dq.append([r, c, 0])
    visit = [[False] * C for _ in range(R)]

    while dq:
        r, c, cnt = dq.popleft()

        if 0 <= r < R and 0 <= c < C:
            pass # 구간을 벗어났으면 continue
        else: continue

        if board[r][c] == 'W' or visit[r][c]:
            # 바다거나 이미 방문했으면 continue
            continue

        visit[r][c] = True
        for i in range(4):
            dr = r + move[i][0]
            dc = c + move[i][1]
            dq.append([dr, dc, cnt + 1])

    return cnt-1

MAX = 0
for r in range(R):
    for c in range(C):
       MAX = max(MAX, solve(r, c))
print(MAX)