import sys
import copy
from collections import deque

cp = copy.deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
viruses = []
MAP = []
RIGHT, DOWN, LEFT, UP = [1, 0], [0, 1], [-1, 0], [0, -1]
MOVE = [RIGHT, DOWN, LEFT, UP]


for i in range(N):
    line = list(map(int, input().split()))
    for j, n in enumerate(line):
        if n == 2:
            viruses.append([j, i])
    MAP.append(line)

emptyarea = 0
makewall = []
visit = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if MAP[i][j] != 1:
            emptyarea += 1
def make(walls, n, x, y):
    if n == 3:
        makewall.append(cp(walls))
        return
    for i in range(y, N):
        if n == 0:
            s = 0
        elif i == y:
            s = x + 1
        else:
            s = 0
        for j in range(s, M):
            if MAP[i][j] == 0:# and not visit[i][j]:
                #visit[i][j] = True
                walls.append([j, i])
                make(walls, n+1, j, i)
                walls.pop()
                #visit[i][j] = False
make([], 0, 0, 0)
MAX = 0
emptyarea -= 3 # 벽3개로 가리자너 ㅋ
def BFS():
    visit = [[False]*M for _ in range(N)]
    numofvirus = 0
    for virus in viruses:
        x, y = virus
        dq = deque()
        if not visit[y][x]:
            dq.append([x, y])
            visit[y][x] = True
            numofvirus += 1
        while dq:
            x, y = dq.pop()
            for i in range(4):
                tx = x + MOVE[i][0]
                ty = y + MOVE[i][1]

                if 0 <= tx < M and 0 <= ty < N and MAP[ty][tx] != 1 and not visit[ty][tx]:
                    dq.append([tx, ty])
                    visit[ty][tx] = True
                    numofvirus += 1
    global MAX
    if MAX < emptyarea - numofvirus :
        MAX = emptyarea - numofvirus


for wallPOS in makewall:
    for POS in wallPOS:
        MAP[POS[1]][POS[0]] = 1
    BFS()
    for POS in wallPOS:
        MAP[POS[1]][POS[0]] = 0
print(MAX)