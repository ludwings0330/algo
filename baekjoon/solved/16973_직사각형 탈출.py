from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visit = [[False] * M for _ in range(N)]
trunk = []
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
# 오 아 왼 위
walls = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
          walls.append([i, j])
    trunk.append(line)

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

def canMove(ty, tx, Type):

    for y, x in walls:
        if tx <= x < tx+W and ty <= y < ty + H:
            return False
    return True

def BFS():
    dq = deque()
    dq.append([Sr, Sc, 0])

    while dq:
        y, x, c = dq.popleft()
        if y == Fr and x == Fc:
            return c

        for type in range(4):
            ty = y + dy[type]
            tx = x + dx[type]

            if tx < 0 or ty < 0 or tx + W-1 >= M or ty + H-1 >= N or visit[ty][tx]:
                continue

            if canMove(ty, tx, type):
                visit[ty][tx] = True
                dq.append([ty, tx, c+1])
    return -1
print(BFS())