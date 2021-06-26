import sys
from collections import deque

input = sys.stdin.readline
RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, -1), (0, 1)
moveMonkey = [ RIGHT, LEFT, UP, DOWN ]
moveHorse = [ (2, -1), (2, 1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2) ]

K = int(input())
# 말 점프 가능한 횟수
W, H = map(int, input().split())
VISIT = [[[False] * W for _ in range(H)] for __ in range(K+1)]

MAP = []
for _ in range(H):
    MAP.append(list(map(int, input().split())))

def BFS():
    dq = deque()
    dq.append([0, 0, K, 0])
    VISIT[K][0][0] = True
    ret = -1
    while dq:
        x, y, k, c = dq.popleft()
        if x == W-1 and y == H-1:
            ret = c
            break

        if k > 0:
            for dx, dy in moveHorse:
                tx = x + dx
                ty = y + dy
                if 0 <= tx < W and 0 <= ty < H and MAP[ty][tx] == 0 and not VISIT[k-1][ty][tx]:
                    dq.append([tx, ty, k-1, c+1])
                    VISIT[k-1][ty][tx] = True

        for dx, dy in moveMonkey:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < W and 0 <= ty < H and MAP[ty][tx] == 0 and not VISIT[k][ty][tx]:
                dq.append([tx, ty, k, c + 1])
                VISIT[k][ty][tx] = True
    print(ret)

BFS()