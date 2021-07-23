import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
MAP = []
fish = {}

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for y in range(N):
    line = list(map(int, input().split()))
    for x, n in enumerate(line):
        if n != 0:
            if n in fish:
                fish[n].append([x, y])
            else:
                fish[n] = [[x, y]]

sharkPOS = fish[9]
sharkSize = 2
cnt = 0
time = 0

def sizeUp():
    global cnt, sharkSize
    cnt += 1
    if cnt == sharkSize:
        cnt = 0
        sharkSize += 1
def moveToTarget(sx, sy, ex, ey): # 시작 위치에서 target위치로 이동한다.
    dq = deque()
    VISIT = [[False] * N for _ in range(N)]

    dq.append([sx, sy, 0])
    VISIT[sx][sy] = True

    while dq:
        x, y, t = dq.popleft()

        if x == ex and y == ey:
            global time
            time += t
            MAP[sy][sx] = 0
            MAP[ey][ex] = 9
            return True

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < N and 0 <= ty < N and not VISIT[ty][tx] and MAP[ty][tx] <= sharkSize:
                dq.append([tx, ty, t+1])
                VISIT[ty][tx] = True
    return False

X = 0
Y = 1
VISIT = []
sortedFishSize = sorted(fish.keys())[:-1]

for i in sortedFishSize:
    VISIT.append([False]*len(fish[i]))

targetPOS = [-1, -1]
targetDist = sys.maxsize

for i, size in enumerate(sortedFishSize):
    if size >= sharkSize: # 먹을 수가 없음
        break
    # 여 아래는 먹을 수 있는거
    for j, fishPOS in enumerate(fish[size]):
        if not VISIT[i][j]:
            nextDist = abs(sharkPOS[X] - fishPOS[X]) + abs(sharkPOS[Y] - fishPOS[Y])
            if nextDist < targetDist: # 가까운 거리부터
                targetDist = nextDist
                targetPOS = fishPOS

            elif nextDist == targetDist:
                if targetPOS[Y] > fishPOS[Y]: # y가 작은 것부터
                    targetPOS = fishPOS

                elif targetPOS[Y] == fishPOS[Y]: # 높이가 같으면
                    if targetPOS[X] > fishPOS[X]: # 왼쪽에 있는놈 부터
                        targetPOS = fishPOS
# 먹을 수 있는 놈 중에 제일 가까이 있는 놈 골랐다.

moveToTarget(sharkPOS[X], sharkPOS[Y], targetPOS[X], targetPOS[Y])


print(time)