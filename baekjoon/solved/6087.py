import sys
from collections import deque

input = sys.stdin.readline

W, H = map(int, input().split())
MOVE = [(1, 0), (0, -1), (-1 ,0), (0, 1)]

MAP = []
VISIT = [[10000] * W for _ in range(H)]

start = []
end = []

for y in range(H):
    line = list(input().rstrip())
    MAP.append(line)
    for x, c in enumerate(line):
        if c == 'C':
            if not start:
                start = [x, y]
            else:
                end = [x, y]
def canMove(x, y):
    if 0<= x < W and 0 <= y< H and MAP[y][x] != '*':
        return True
    else:
        return False

def BFS():
    dq = deque()
    x, y = start
    for i in range(4):
        dq.append([x, y, i, 0])
    VISIT[y][x] = 0

    while dq:
        x, y, type, c = dq.popleft()
        # 원래 type 방향으로 가려고 했음.
        # if [x, y] == end:
        #     print(c)
        #     break
        for i in range(4):
            dx, dy = MOVE[i]
            tx, ty = x + dx, y + dy
            if canMove(tx, ty):
                if type == i:
                    if VISIT[ty][tx] >= c:
                        dq.append([tx, ty, i, c])
                        VISIT[ty][tx] = c
                else:
                    if VISIT[ty][tx] >= c+1:
                        dq.append([tx, ty, i, c+1])
                        VISIT[ty][tx] = c+1
BFS()
print(VISIT[end[1]][end[0]])
