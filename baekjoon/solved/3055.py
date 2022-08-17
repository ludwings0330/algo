from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

waters = []
start =()
for r in range(R):
    for c in range(C):
        if board[r][c] == '*':
            waters.append((r, c))
        elif board[r][c] == 'S':
            start = (r, c)

dq = deque()

for water in waters:
    # r, c, type, time
    dq.append((water[0], water[1], "*", 0))
# r, c, type, time
dq.append((start[0], start[1], "S", 0))

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[False] * C for _ in range(R)]

ans = 0
while dq:
    r, c, tp, time = dq.popleft()
    if board[r][c] == 'D':
        ans = time
        break
    board[r][c] = tp

    for dr, dc in move:
        nr = r + dr
        nc = c + dc

        # 범위를 벗어났다면
        if 0 <= nr < R and 0 <= nc < C:
            pass
        else:
            continue
        # 이미 방문했다면
        if visited[nr][nc]:
            continue
        # 벽이라면
        if board[nr][nc] == 'X':
            continue
        # 물채우는데 비버굴이라면
        if tp == '*' and board[nr][nc] == 'D':
            continue

        # 물이라면
        if board[nr][nc] == '*':
            continue

        visited[nr][nc] = True
        dq.append((nr, nc, tp, time + 1))


print(ans if ans != 0 else 'KAKTUS')