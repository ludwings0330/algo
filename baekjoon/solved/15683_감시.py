import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cameras = []
MAP = []
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

d = [[],
     [UP, DOWN, RIGHT, LEFT],
     [(LEFT, RIGHT), (UP, DOWN)],
     [(UP, RIGHT), (RIGHT, DOWN), (DOWN, LEFT), (LEFT, UP)],
     [(LEFT, UP, RIGHT), (UP, RIGHT, DOWN), (RIGHT, DOWN, LEFT), (DOWN, LEFT, UP)],
     [(UP, RIGHT, DOWN, LEFT)]]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if 1 <= line[j] <= 5:
            cameras.append([j, i]) # x, y로 넣기
    MAP.append(line)

visit = [False]*len(cameras)

def getBlindSpot():
    ret = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                ret += 1
    return ret
MIN = 987654321
def setBlindSpot(x, y, dirs, f):
    for i in range(N):
        for t in dirs:
            tx = x + t[0]
            ty = y + t[1]
def solve(cameraNum):
    if cameraNum >= len(cameras):
        global MIN
        MIN = min(MIN, getBlindSpot())
        return

    x = cameras[cameraNum][0]
    y = cameras[cameraNum][1]
    cameraType = MAP[y][x]

    for direction in range(len(d[cameraType])):
        setBlindSpot(x, y, d[cameraType][direction], -1)
        solve(cameraNum+1)
        setBlindSpot(x, y, d[cameraType][direction], 1)
