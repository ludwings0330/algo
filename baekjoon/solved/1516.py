# 게임개발
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
buildTime = [0] * (N+1)
edge = [0] * (N + 1)
graph = {}
dp = [0] * (N + 1)

for i in range(1, N+1):
    line = list(map(int, input().split()))
    buildTime[i] = line[0]
    e = i
    for s in line[1:-1]:
        edge[e] += 1
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]
dq = deque()
for i in range(1,N+1):
    if edge[i] == 0:
        dq.append(i)
        dp[i] = buildTime[i]

while dq:
    node = dq.popleft()

    if node in graph:
        for next in graph[node]:
            dp[next] = max(dp[next], dp[node] + buildTime[next])
            edge[next] -= 1
            if edge[next] == 0:
                dq.append(next)
for t in dp[1:]:
    print(t)