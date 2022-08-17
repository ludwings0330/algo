import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))


def bfs(cr, cc, h):
    dq = deque()
    isPeak = True

    dq.append([cr, cc])
    while dq:
        tr, tc = dq.popleft()
        for dr, dc in move:
            nr = tr + dr
            nc = tc + dc

            if 0 <= nr < R and 0 <= nc < C:
                pass
            else:
                continue

            if board[nr][nc] > h:
                isPeak = False
            if board[nr][nc] != h:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = True
            dq.append([nr, nc])

    return isPeak


cnt = 0
for r in range(R):
    for c in range(C):
        if visited[r][c]:
            continue
        visited[r][c] = True
        if board[r][c] != 0 and bfs(r, c, board[r][c]):
            cnt += 1
print(cnt)