import sys
input = sys.stdin.readline
from collections import deque

N, M, fuel = map(int, input().split())

board = [ list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
taxi = [r-1, c-1]
# [r, c]
passenger = {}

for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    passenger[(sr-1, sc-1)] = (er-1, ec-1)

move = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def findNearDist():
    dq = deque()
    visit = set()

    dq.append([taxi[0], taxi[1], 0])
    visit.add((taxi[0], taxi[1]))

    minDist = -1
    candidate = []
    while dq:
        r, c, d = dq.popleft()
        if d > fuel:
            return [-1, -1, -1]

        if minDist == -1 and (r, c) in passenger:
            minDist = d # 최초 실행시
            candidate.append([r, c])
            continue

        if d == minDist:
            if (r, c) in passenger:
                candidate.append([r, c])
            continue


        for dr, dc in move:
            tr = r + dr
            tc = c + dc
            if 0 <= tr < N and 0 <= tc < N and board[tr][tc] != 1 and (tr, tc) not in visit:
                dq.append([tr, tc, d+1])
                visit.add((tr, tc))

    if not candidate:
        return [-1, -1, -1]

    else:
        candidate = sorted(candidate, key=lambda x:(x[0], x[1]))
        return candidate[0] + [minDist]

def moveTo(dest):
    dq = deque()
    visit = set()

    dq.append([taxi[0], taxi[1], 0])
    visit.add((taxi[0], taxi[1]))

    while dq:
        r, c, d = dq.popleft()

        if d > fuel:
            return [-1, -1, -1]

        if (r, c) == dest:
            return [r, c, d]

        for dr, dc in move:
            tr = r + dr
            tc = c + dc
            if 0 <= tr < N and 0 <= tc < N and board[tr][tc] != 1 and (tr, tc) not in visit:
                dq.append([tr, tc, d+1])
                visit.add((tr, tc))
    return [-1, -1, -1]

ret = True
while passenger:
    sr, sc, d = findNearDist() # 가장 가까운 곳을 찾는다.

    if sr == -1 or d >= fuel:
        ret = False
        break
    else:
        taxi = [sr, sc]
        fuel -= d

        r, c, d = moveTo(passenger[(sr, sc)])
        taxi = [r, c]
        fuel -= d
        if r == -1 or fuel < 0:
            ret= False
            break
        fuel += d*2
        del passenger[(sr, sc)]
if ret:
    print(fuel)
else:
    print(-1)