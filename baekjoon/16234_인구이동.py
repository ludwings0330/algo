import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
MAP = []
visit = [[False]*N for _ in range(N)]

for _ in range(N):
    line = list(map(int, input().split()))
    MAP.append(line)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def BFS(i, j):
    stack = []
    visit[i][j] = True
    stack.append([i, j, 0])

    while stack:
        x, y, c = stack.pop()
        visit[x][y] = True
        for i in range(4):
            tx = x + dxy[i][0]
            ty = y + dxy[i][1]

            if 0<=tx<N and 0<=ty<N and not visit[tx][ty] and L<= abs(MAP[tx][ty] - MAP[x][y])<=R:
                stack.append([tx, ty, c+1])


    if c == 0:
        return 0
    else:
        return 1
answer = 0

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
           answer += BFS(i, j)

print(answer)