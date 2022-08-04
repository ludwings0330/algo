import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from collections import defaultdict
import heapq

N = int(input())
M = int(input())
graph = defaultdict(lambda:defaultdict(int))

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b] if graph[a][b] else c, c)
    graph[b][a] = min(graph[b][a] if graph[b][a] else c, c)

hq = []
visit = [False] * (N + 1)

heapq.heappush(hq, [0, 1, 1])
ret = 0

while hq:
    dist, s, e = heapq.heappop(hq)
    if not visit[e]:
        visit[e] = True
        if e in graph:
            for next in graph[e]:
                if not visit[next]:
                    heapq.heappush(hq, [graph[e][next], e, next])
            ret += dist

print(ret)
