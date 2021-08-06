import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
MAP = []
VISIT = [[[False]*N for _ in range(N)] for __ in range(2)]

for _ in range(N):
    MAP.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def isRange(x, y, i):
    if 0 <= x < N and 0 <= y < N and not VISIT[i][y][x]:
        return True
    else:
        return False

def solve(x, y, type):
    dq = deque()
    dq.append([x, y, MAP[y][x]])
    VISIT[type][y][x] = True

    while dq:
        x, y, c = dq.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if isRange(tx, ty, type):
                if type == 0 and MAP[ty][tx] == c:
                    VISIT[type][ty][tx] = True
                    dq.append([tx, ty, MAP[ty][tx]])
                if type == 1:
                    if MAP[ty][tx] == c or (c == 'R' and MAP[ty][tx] == 'G') or (c == 'G' and MAP[ty][tx] == 'R'):
                        VISIT[type][ty][tx] = True
                        dq.append([tx, ty, MAP[ty][tx]])

cnt = 0
cnt2 = 0
for y in range(N):
    for x in range(N):
        if not VISIT[0][y][x]:
            solve(x, y, 0)
            cnt += 1
        if not VISIT[1][y][x]:
            solve(x, y, 1)
            cnt2 += 1
print(cnt, cnt2, sep=' ')