import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().rstrip().split())
chees = {}
for r in range(N):
    line = list(map(int, input().rstrip().split()))
    for c in range(M):
        if line[c] == 1:
            chees[(r, c)] = 0

move = ((0, 1), (0, -1), (1, 0), (-1, 0))

time = 0
while chees:
    dq = deque()
    dq.append([0, 0])
    visit = set()
    visit.add((0, 0))

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            tr = r + move[i][0]
            tc = c + move[i][1]
            if 0 <= tr < N and 0 <= tc < M and (tr, tc) not in visit:
                if (tr, tc) in chees:
                    chees[(tr, tc)] += 1
                    continue
                dq.append([tr, tc])
                visit.add((tr, tc))
    tchees = {}
    for (r, c), cnt in chees.items():
        if cnt < 2:
            tchees[(r, c)] = 0
    chees = tchees
    time += 1

print(time)