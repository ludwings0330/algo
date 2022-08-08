import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

C, R = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(R)]

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[float('inf')] * C for _ in range(R)]

visited[0][0] = 0

dq = deque()
dq.append([0, 0, 0])
ans = float('inf')

while dq:
    r, c, cnt = dq.popleft()
    if (r != 0 and c != 0) and visited[r][c] < cnt:
        continue

    if r == R-1 and c == C-1:
        ans = min(ans, cnt)

    for dr, dc in move:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < R and 0 <= nc < C:
            pass
        else:
            continue
        next_cnt = cnt + board[nr][nc]
        if visited[nr][nc] <= next_cnt:
            continue

        visited[nr][nc] = next_cnt
        dq.append([nr, nc, next_cnt])
print(ans)