# Title : 낚시왕
# Tag :

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
R, C, M = map(int, input().split())
sharks = {}
fishman = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = [s, d, z]

# [r:행, c:열, s: 속력, d:방향, z:크기]
# d == 1 위 d == 2 아래 d == 3 오른쪽 d == 4 왼쪽

# 1. 낚시왕이 오른쪽으로 한칸 이동
# 2. 낚시왕이 있는 열에 땅과 제일 가까운 상어를 잡음
# 3. 상어가 이동
move = {1:(-1, 0), 2:(1, 0), 3:(0,  1), 4:(0, -1)}
ans = 0
while fishman < C:
    # - 2 - 가장 가까운 놈을 잡음
    nextSharks = {}
    for r in range(R):
        if (r, fishman) in sharks:
            ans += sharks[(r, fishman)][2]
            del sharks[(r, fishman)]
            break
    # - 2 -

    # - 3 - 상어들이 이동한다
    for (r, c) in sharks:
        [s, d, z] = sharks[(r, c)]
        tr = r + move[d][0] * s

        while not (0 <= tr < R):
            if tr < 0:
                tr = abs(tr)
            elif tr >= R:
                tr = R-1 - (tr - (R-1))
            if d == 1 or d == 3:
                d += 1
            else:
                d -= 1

        tc = c + move[d][1] * s
        while not (0 <= tc < C):
            if tc < 0:
                tc = abs(tc)
            elif tc >= C:
                tc = C-1 - (tc - (C-1))
            if d == 1 or d == 3:
                d += 1
            else:
                d -= 1

        if (tr, tc) not in nextSharks:
            nextSharks[(tr, tc)] = [s, d, z]
        else:
            if nextSharks[(tr, tc)][2] < z:
               nextSharks[(tr, tc)] = [s, d, z]

    sharks = nextSharks
    # - 3 -
    fishman += 1
print(ans)