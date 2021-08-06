#  NxN 도시 M 개의 치킨집
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
house = []
chicken = []
for y in range(N):
    line = list(map(int, input().split()))

    for x, n in enumerate(line):
        if n == 1:
            house.append([x, y])
        elif n == 2:
            chicken.append([x, y])

INF = sys.maxsize
numOfHouse = len(house)
numOfChic = len(chicken)

DIST = [[INF]*numOfChic for _ in range(numOfHouse)]


for h, [hx, hy] in enumerate(house):
    for c, [cx, cy] in enumerate(chicken):
         DIST[h][c] = abs(hx - cx) + abs(hy - cy)

def getShortest(arr):
    shortDist = [INF]*numOfHouse

    for h in range(len(shortDist)):
        for c in arr:
            shortDist[h] = min(shortDist[h], DIST[h][c])


    return sum(shortDist)

def choice(i, arr, toPick):
    if toPick == 0:
        # 골랐으니까 여기서 각자 최소 거리로 방문해야지 집들이.
        global sDist
        sDist = min(sDist, getShortest(arr))
        return sDist # m 개 뽑을 때 최소 거리

    for j in range(i+1, numOfChic):
        arr.append(j)
        choice(j, arr, toPick - 1)
        arr.pop()

sDist = INF
for m in range(1, M+1):
    #최대 M개를 선택
    # 1 개 에서 M개를 뽑는 경우의 수.
    choice(-1, [], m) # d = m개 뽑을때 최소 거리

print(sDist)
