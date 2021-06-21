import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
visit = [[[False]*M for _ in range(N)] for _ in range(H)]
tomatos = []
numOfTomatos = 0
dq = deque()
for h in range(H):
    tomatos.append([])

    for _ in range(N):
        line = list(map(int, input().split()))
        tomatos[h].append(line)

        for m in range(len(line)):
            if line[m] != -1: # 빈칸이아니라면
                numOfTomatos += 1

                if line[m] == 1: # 익은 토마토라면
                    dq.append([h, _, m ,0])
                    visit[h][_][m] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dh = [-1, 1]
total = 0
while dq:
    h, y, x, t = dq.popleft()
    total += 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < M and 0 <= ty < N and not visit[h][ty][tx]:
            if tomatos[h][ty][tx] == 0:  # 익지 않은 토마토라면
                visit[h][ty][tx] = True  # 방문
                dq.append([h, ty, tx, t + 1])
    for i in range(2):
        th = h + dh[i]
        if 0 <= th < H and not visit[th][y][x]:
            if tomatos[th][y][x] == 0:  # 익지 않은 토마토라면
                visit[th][y][x] = True  # 방문
                dq.append([th, y, x, t + 1])

if total != numOfTomatos:
    print(-1)
else:
    print(t)