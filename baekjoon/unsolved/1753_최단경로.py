import sys

V, E = map(int, input().split())
K = int(input())

visit = [False] * (V+1)
trunk = {}
dp = [0] * (V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u not in trunk:
        trunk[u] = [[v, w]]
    else:
        trunk[u].append([v,w])
    if v not in trunk:
        trunk[v] = [[u,w]]
    else:
        trunk[v].append([u,w])
# 정점 K에서 i번 정점으로 가는 최단 경로값. 자신은 0으로 출력, 경로가 존재하지 않는 경우 INF

MIN = float('inf')
index = 0
for i in range(V+1):
    if i == K:
        print(0)
    if dp[i] < min and not visit[i]:
        min = d[i]
        index = i

print(trunk)