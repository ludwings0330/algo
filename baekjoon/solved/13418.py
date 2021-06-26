import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}
VISIT = [False] * (N+1)

for _ in range(M+1):
    s, e, v = map(int, input().split())
    if s in graph:
        graph[s][e] = v
    else:
        graph[s] = {e:v}
    if e in graph:
        graph[e][s] = v
    else:
        graph[e] = {s:v}

hq = []

for next in graph[0]:
    heapq.heappush(hq, [graph[0][next], 0, next])
VISIT[0] = True
up = 0
down = 0

while hq:
    v, s, e = heapq.heappop(hq)

    if VISIT[e]:
        continue

    VISIT[e] = True
    if v == 0:
        up += 1
    else:
        down += 1

    for next in graph[e]:
        if not VISIT[next]:
            heapq.heappush(hq, [graph[e][next], e, next])

MAX = up**2

hq = []
VISIT = [False] * (N+1)
for next in graph[0]:
    heapq.heappush(hq, [-graph[0][next], 0, next])
VISIT[0] = True
up = 0
down = 0

while hq:
    v, s, e = heapq.heappop(hq)

    if VISIT[e]:
        continue

    VISIT[e] = True
    if v == 0:
        up += 1
    else:
        down += 1

    for next in graph[e]:
        if not VISIT[next]:
            heapq.heappush(hq, [-graph[e][next], e, next])
MIN = up**2
print(MAX - MIN)