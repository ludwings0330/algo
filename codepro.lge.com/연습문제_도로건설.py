import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


N = int(input())
board = []

for _ in range(N):
    line = list(map(int, list(input())))
    board.append(line)

dq = deque()
INF = float('inf')
dp = [[INF] * N for _ in range(N)]

dq.append([0, 0, 0])

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dp[0][0] = 0
while dq:
    cr, cc, cv = dq.popleft()

    if cr == N-1 and cc == N-1:
        continue

    for i in range(len(move)):
        nr = cr + move[i][0]
        nc = cc + move[i][1]

        if 0 <= nr < N and 0 <= nc < N:
            nv = cv + board[nr][nc]

            if dp[nr][nc] > nv:
                dq.append([nr, nc, cv + board[nr][nc]])
                dp[nr][nc] = nv

print(dp[-1][-1])