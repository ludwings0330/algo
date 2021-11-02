import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

ret = 0
VISIT = [[False]*M for _ in range(N)]
ex = [[[0, 0], [0, -1], [0, 1], [-1, 0]], [[0, 0], [0, 1], [-1, 0], [1, 0]],
      [[0, 0], [0, -1], [0, 1], [1, 0]], [[0, 0], [0, -1], [-1, 0], [1, 0]]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def inRange(x, y):
    if 0<=x<M and 0<=y<N:
        return True
    else:
        return False

def recursive(x, y, topick, SUM):
    if topick == 0:
        global ret
        ret = max(ret, SUM)
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if inRange(tx, ty) and not VISIT[ty][tx]:
            VISIT[ty][tx] = True
            recursive(tx, ty, topick-1, SUM+MAP[ty][tx])
            VISIT[ty][tx] = False

for y in range(N):
    for x in range(M):
        VISIT[y][x] = True
        recursive(x, y, 3, MAP[y][x])
        VISIT[y][x] = False

        for i in range(4):
            putUp = True
            SUM = 0
            for kx, ky in ex[i]:
                tx = x + kx
                ty = y + ky
                if not inRange(tx, ty):
                    putUp = False
                    break
                SUM += MAP[ty][tx]
            if putUp:
                ret = max(SUM, ret)
print(ret)
