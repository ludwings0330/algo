import sys
input = sys.stdin.readline
import heapq

n, r, m = map(int, input().rstrip().split())
INF = 987654321
dist = [[INF] * n for _ in range(n)]

items = list(map(int, input().rstrip().split()))
path = {}

for _ in range(m):
    s, e, d = map(int, input().rstrip().split())
    s -= 1
    e -= 1
    dist[s][e] = min(dist[s][e], d)
    dist[e][s] = min(dist[e][s], d)

# 각 경로를 시작으로 각 정점으로의 최소 거리를 구한다.
# 플로이드 와샬

for k in range(n):
    dist[k][k] = 0
    for s in range(n):
        for e in range(n):
            dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

ans = 0
for k in range(n):
    tmp = 0
    for e in range(n):
        if dist[k][e] <= r:
            tmp+=items[e]
    ans = max(ans, tmp)

print(ans)