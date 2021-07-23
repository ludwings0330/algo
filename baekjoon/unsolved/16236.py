import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())
MAP = []
sharkSize = 2
time = 0
INF = sys.maxsize
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for y in range(N):
    line = list(map(int, input().split()))
    for x, s in enumerate(line):
        if s == 9:
            sharkPOS = [x, y]
    MAP.append(line)

def eat(sx, sy):
    VISIT = [[False]*N for _ in range(N)]
    dq = deque()
    dq.append([sx, sy, 0])
    VISIT[sy][sx] = True
    ret = [INF, INF]
    retTime = sys.maxsize
    isFinished = False
    while dq:
        x, y, t = dq.popleft()

        if MAP[y][x] != 0 and MAP[y][x] < sharkSize:
            if retTime >= t:
                retTime = t
                if y < ret[1]:
                    ret = [x, y]
                elif y == ret[1]:
                    if x < ret[0]:
                        ret = [x, y]
            isFinished = True
            continue

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not VISIT[ty][tx] and MAP[ty][tx] <= sharkSize and retTime >= t+1:
                dq.append([tx, ty, t+1])
                VISIT[ty][tx] = True
    if retTime != INF:
        global time
        time += retTime
    return ret

cnt = 0
while True:
    fishPOS = eat(sharkPOS[0], sharkPOS[1])
    if fishPOS == [INF, INF]:
        break
    else:
        cnt += 1
        if cnt == sharkSize:
            cnt = 0
            sharkSize += 1
        MAP[sharkPOS[1]][sharkPOS[0]] = 0
        sharkPOS = fishPOS[:]
        MAP[sharkPOS[1]][sharkPOS[0]] = 9
print(time)