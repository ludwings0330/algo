# title ; 경찰차
# tag ; 다이나믹 프로그래밍

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
N = int(input())
M = int(input())

events = [[-1, -1]]

for _ in range(M):
    r, c = map(int, input().split())
    events.append([r, c])

dp = [[-1] * (M+1) for _ in range(M+1)]
def getDist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def recursiveSolve(police_1, police_2, next):
    if dp[police_1][police_2] != -1:
        return dp[police_1][police_2]

    if police_1 == M or police_2 == M:
        return 0
    # base case

    if police_1 == 0:
        dist1 = getDist(1, 1, events[next][0], events[next][1])
    else:
        dist1 = getDist(events[police_1][0], events[police_1][1], events[next][0], events[next][1])

    if police_2 == 0:
        dist2 = getDist(N, N, events[next][0], events[next][1])
    else:
        dist2 = getDist(events[police_2][0], events[police_2][1], events[next][0], events[next][1])

    ret1 = dist1 + recursiveSolve(next, police_2, next+1) # 1번이 next로 이동 + 다음 차수 진행( 1번이동, 2번 이동)
    ret2 = dist2 + recursiveSolve(police_1, next, next+1) # 2번이 next로 이동 + 다음 차수 진행

    dp[police_1][police_2] = min(ret1, ret2)
    return dp[police_1][police_2]

def getPath(police_1, police_2, next):
    if police_1 == M or police_2 == M:
        return

    if police_1 == 0:
        dist1 = getDist(1, 1, events[next][0], events[next][1])
    else:
        dist1 = getDist(events[police_1][0], events[police_1][1], events[next][0], events[next][1])

    if police_2 == 0:
        dist2 = getDist(N, N, events[next][0], events[next][1])
    else:
        dist2 = getDist(events[police_2][0], events[police_2][1], events[next][0], events[next][1])
    # 1번이 next로 이동 +
    if dp[next][police_2] + dist1 < dp[police_1][next] + dist2:
        print(1)
        getPath(next, police_2, next+1)
    else:
        print(2)
        getPath(police_1, next, next+1)

print(recursiveSolve(0, 0, 1))
getPath(0, 0, 1)