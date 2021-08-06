# 2048 (EASY)
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [[[0]*N for _ in range(N)] for _ in range(1+4+4**2+4**3+4**4+4**5)]
tboard = []
MAX = 0
for _ in range(N):
    tboard.append(list(map(int, input().split())))
    tMAX = max(tboard[-1])
    MAX = max(tMAX, MAX)
board[0] = tboard

dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def left(s, e):
    visit = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if x == 0:
                board[e][y][x] = board[s][y][x]
                continue
            n = board[s][y][x]
            for t in range(x, 0, -1):
                # 이동할 수 있는 기준
                # 1. 숫자가 같다 + t-1위치가 아직 합쳐지지 않은 놈이다
                # 2. 숫자가 0 이다
                # 이동할 수 없는기준
                # 1. 전놈이랑 숫자가 다르다
                # 2. 이번놈이 이미 합쳐진 상태다.
                if board[e][y][t-1] == 0: # 0 인 경우 우선 움직일 수 있다.
                    board[e][y][t-1] = n
                    board[e][y][t] = 0
                    continue
                elif n != board[e][y][t-1] or visit[y][t-1]: # 다르면 이동할 수 없음.
                    board[e][y][t] = n
                    break
                elif n == board[e][y][t-1]: # 같은 숫자면 합쳐준다.
                    board[e][y][t] = 0
                    board[e][y][t-1] += n
                    global MAX
                    MAX = max(MAX, n*2)
                    visit[y][t-1] = True
                    break

def right(s, e):
    visit = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N-1, -1, -1):
            if x == N-1:
                board[e][y][x] = board[s][y][x]
                continue
            n = board[s][y][x]
            for t in range(x, N-1):
                if board[e][y][t+1] == 0:
                    board[e][y][t+1] = n
                    board[e][y][t] = 0
                    continue
                elif n != board[e][y][t+1] or visit[y][t+1]: # 다르면 이동할 수 없음.
                    board[e][y][t] = n
                    break
                elif n == board[e][y][t+1]: # 같은 숫자면 합쳐준다.
                    board[e][y][t+1] += n
                    board[e][y][t] = 0
                    global MAX
                    MAX = max(MAX, n*2)
                    visit[y][t+1] = True
                    break
    pass
def top(s, e):
    visit = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if y == 0:
                board[e][y][x] = board[s][y][x]
                continue
            n = board[s][y][x]
            for t in range(y, 0, -1):
                if board[e][t-1][x] == 0:
                    board[e][t-1][x] = n
                    board[e][t][x] = 0
                    continue
                elif n != board[e][t-1][x] or visit[t-1][x]: # 다르면 이동할 수 없음.
                    board[e][t][x] = n
                    break
                elif n == board[e][t-1][x]: # 같은 숫자면 합쳐준다.
                    board[e][t][x] = 0
                    board[e][t-1][x] += n
                    global MAX
                    MAX = max(MAX, n*2)
                    visit[t-1][x] = True
                    break
    pass
def bottom(s, e):
    visit = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N-1, -1, -1):
            if y == N-1:
                board[e][y][x] = board[s][y][x]
                continue
            n = board[s][y][x]
            for t in range(y, N-1):
                if board[e][t+1][x] == 0:
                    board[e][t+1][x] = n
                    board[e][t][x] = 0
                    continue
                elif n != board[e][t+1][x] or visit[t+1][x]: # 다르면 이동할 수 없음.
                    board[e][t][x] = n
                    break
                elif n == board[e][t+1][x]: # 같은 숫자면 합쳐준다.
                    board[e][t+1][x] += n
                    board[e][t][x] = 0
                    global MAX
                    MAX = max(MAX, n*2)
                    visit[t+1][x] = True
                    break
    pass

def move(s, e, type):
    if type == 1:
        left(s, e)
    elif type == 2:
        right(s, e)
    elif type == 3:
        top(s, e)
    elif type == 4:
        bottom(s, e)

dq = deque()

index = 0
dq.append([index, 0])

while dq:
    s, c = dq.popleft()

    if c == 5:
        continue

    for j in range(1, 5):
        index += 1
        move(s, index, j) # s 를 j 방향으로 움직였을때 index에 채워넣는다.
        dq.append([index, c+1])

print(MAX)