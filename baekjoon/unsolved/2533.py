# title ; 사회망 서비스(SNS)
# tag ; 그래프 이론, 다이나믹 프로그래밍

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
# 1 <= N <= 1,000,000
# M = N-1
graph = {}

for _ in range(N):
    u, v = map(int, input().split())

    if u in graph:
        graph[u][v] = 1
    else:
        graph[u] = {v:1}

    if v in graph:
        graph[v][u] = 1
    else:
        graph[v] = {u:1}
