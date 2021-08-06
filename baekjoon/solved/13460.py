import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
for y in range(N):
    MAP.append(list(input().rstrip()))

properties = [[-1, -1] for _ in range(3)]
# 0 : hole, 1 : Red ball, 2 : Blue ball

for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'B':
            MAP[y][x] = '.'
            properties[2] = [x, y]
        elif MAP[y][x] == 'R':
            MAP[y][x] = '.'
            properties[1] = [x, y]
        elif MAP[y][x] == 'O':
            properties[0] = [x, y]
dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 오른쪽 왼쪽 아래 위
# 파란구슬은 구멍에 빠지면 안되고
# 빨간구슬만 구멍에 넣어야한다.
def move(ball, direction, check = [0, 0]):
    x = ball[0]
    y = ball[1]
    ch = MAP[y][x]
    while True:
        tx = x + direction[0]
        ty = y + direction[1]

        if MAP[ty][tx] == 'O': # 공이 구멍에 들어간다면
            x, y = -1, -1
            break

        elif MAP[ty][tx] != '.' or (tx == check[0] and ty == check[1]): # 벽이 아니라면 혹은 이미 공이 위치해 있다면
            break

        x, y = tx, ty

    return [x, y]

def tilt(type, Red, Blue):
    # type == 0 오른쪽
    #         1 왼쪽
    #         2 아래
    #         3 위
    if type == 0:
        if Red[0] > Blue[0]: # 오른쪽으로 가야하는데 빨간공 먼저가야지 더 크니까
            Red = move(Red, dd[type])
            Blue = move(Blue, dd[type], Red)
        else:
            Blue = move(Blue, dd[type])
            Red = move(Red, dd[type], Blue)

    elif type == 1: # 왼쪽
        if Red[0] < Blue[0]: # 왼쪽으로 가야하는데 빨간공 먼저가야지 더 작으니까
            Red = move(Red, dd[type])
            Blue = move(Blue, dd[type], Red)
        else:
            Blue = move(Blue, dd[type])
            Red = move(Red, dd[type], Blue)

    elif type == 2: # 아래
        if Red[1] > Blue[1]: # 파란 공이 더 위에 있으니까 빨간공부터 움직여
            Red = move(Red, dd[type])
            Blue = move(Blue, dd[type], Red)
        else:
            Blue = move(Blue, dd[type])
            Red = move(Red, dd[type], Blue)

    elif type == 3: #위
        if Red[1] < Blue[1]: # 빨간공이 더 아래 있으니까 빨간공부터 움직여
            Red = move(Red, dd[type])
            Blue = move(Blue, dd[type], Red)
        else:
            Blue = move(Blue, dd[type])
            Red = move(Red, dd[type], Blue)

    return Red, Blue

ret = -1

dq = deque()
dq.append([0, properties[1], properties[2]])
            # 기울인 방향, 기울인 횟수, 빨간공, 파란공
VISIT = [[[[False] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]

while dq:
    c, redBallPOS, blueBallPOS = dq.popleft()

    if c > 10 : # 10회 이상이거나, 파란공이 구멍에 들어가면 안된다.
        break
    if blueBallPOS == [-1, -1]:
        continue

    if redBallPOS == [-1, -1]: # 파란공이 구멍에 안들어갔고, 10회 이하에, 빨간공이 들어가면 정답
        ret = c
        break

    for type in range(4):
        tRedBall, tBlueBall = tilt(type, redBallPOS, blueBallPOS)
        if tRedBall == [-1, -1] or tBlueBall == [-1, -1]:
            dq.append([c + 1, tRedBall, tBlueBall])
        elif not VISIT[tRedBall[1]][tRedBall[0]][tBlueBall[1]][tBlueBall[0]]:
            VISIT[tRedBall[1]][tRedBall[0]][tBlueBall[1]][tBlueBall[0]] = True
            dq.append([c+1, tRedBall, tBlueBall])


print(ret)