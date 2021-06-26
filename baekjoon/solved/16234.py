import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
A = []
# while . 인구 변화가 없을 때 까지. 평균이 될때 까지.
# 1. 인구차이 L<= A[r][c] <= R 국경선을 하루 연다.
# 2. 국경선이 모두 열렸다면 인구 이동을 시작한다.
# 3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면 연합이라고 한다
# 4. 연합을 이루고 있는 각 칸의 인구수는 연합의인구수/연합을 이루고 있는 칸의 개수
# 5. 연합을 해체하고 모든 국경선을 닫는다.

for i in range(N):
    A.append(list(map(int, input().split())))

def MoveAble(x, y, Type, n):
    tx = x + dd[Type][0]
    ty = y + dd[Type][1]
    if 0 <= tx < N and 0 <= ty < N and not visit[ty][tx] and L <= abs(A[y][x] - A[ty][tx]) <= R:
        return True
    return False

def BFS(x, y, n):
    dq = deque()
    dq.append([x, y])
    visit[y][x] = n
    ret = 0
    count = 0
    Moved = False

    while dq:
        X, Y = dq.popleft()
        ret += A[Y][X]
        count += 1

        for Type in range(4):
            if MoveAble(X, Y, Type, n):
                tx = X + dd[Type][0]
                ty = Y + dd[Type][1]
                dq.append([tx, ty])
                visit[ty][tx] = n
                Moved = True

    return int(ret/count), Moved

def pMove(n, average):
    # x, y 와 연결된 국가들을 average로 채운다.
    for i in range(N):
        for j in range(N):
            if visit[i][j] == n:
                A[i][j] = average


answer = 0
isFinished = False
while True:
    visit = [[0]*N for _ in range(N)]
    n = 1
    isMoved = False
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                average, Moved = BFS(x, y, n)
                if Moved:
                    pMove(n, average)
                    isMoved = True
                n += 1
    if not isMoved:
        print(answer)
        break
    answer += 1

