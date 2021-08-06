import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
visit = [[[False]*2 for _ in range(M)] for __ in range(N)]
trunk = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1] # 오 아 왼 위

for i in range(N):
    line = list(map(int, list(input().rstrip())))
    trunk.append(line)

dq = deque()
dq.append([0, 0, 1, 1])
answer = -1
visit[0][0][1] = True

while dq:
    x, y, b, count = dq.popleft()
    # b 벽을 부술수 있는 남은 횟수

    if x == M-1 and y == N-1:
        answer = count
        break

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < M and 0 <= ty < N and not visit[ty][tx][b]: # 범위 안에 있고 방문하지 않았으면
            if trunk[ty][tx] == 1 and b == 1: # 벽이지만 벽을 부술수 있을때,
                dq.append([tx, ty, b-1, count + 1])
                visit[ty][tx][b-1] = True
            elif trunk[ty][tx] == 0: # 벽이 없을때
                dq.append([tx, ty, b, count + 1])
                visit[ty][tx][b] = True


print(answer)