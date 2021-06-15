# ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1

    N, K = map(int, input().split())
    buildTime = [0] + list(map(int, input().split()))
    edge = [0] * (N+1)
    dp = [0] * (N+1)
    graph = {}

    for _ in range(K):
        s, e = map(int, input().split())
        edge[e] += 1
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]
    W = int(input())

    dq = deque()
    for i in range(1, N+1):
        if edge[i] == 0:
            dq.append(i)
            dp[i] = buildTime[i]
    while dq:
        node = dq.popleft()

        if node in graph:
            for next in graph[node]:
                edge[next] -= 1
                dp[next] = max(dp[next], dp[node] + buildTime[next])
                if edge[next] == 0:
                    dq.append(next)
    print(dp[W])