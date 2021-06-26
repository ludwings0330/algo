# 움직 이는 미로 탈출
# 8X8 체스판
# 사람먼저 인접, 대각 이동
# 벽이 내려옴
# 깔리면 끝
import sys
from collections import deque

input = sys.stdin.readline
#  start 0, 15
# end 7, 0
MAP = []
MOVE = [(0, 0), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, -1), (1, 1), (-1, 1)]

# MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

for i in range(8):
    line = list('........')
    MAP.append(line)

for i in range(8):
    line = list(input().rstrip())
    MAP.append(line)

def BFS():
    dq = deque()
    dq.append([0, 15, 0])
    ret = 0
    while dq:
        x, y, ay = dq.pop()
        if y == 0:
            ret = 1
            break

        for dx, dy in MOVE:
            tx = x + dx
            ty = y + dy
            tay = ay - dy
            if 0 <= tx < 8 and 0<= ty < 16 and MAP[ty][tx] != '#' and ty > 0 and MAP[ty -1][tx] != '#' and tay >= 0:
                dq.append([tx, ty - 1, tay])

    print(ret)

BFS()