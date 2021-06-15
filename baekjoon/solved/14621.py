import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

gender = [0]
gender += input().split()

graph = {}

for _ in range(M):
    s, e, v = map(int, input().split())
    if s in graph:
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], v)
        else:
            graph[s][e] = v
    else:
        graph[s] = {e:v}

    if e in graph:
        if s in graph[e]:
            graph[e][s] = min(graph[e][s], v)
        else:
            graph[e][s] = v
    else:
        graph[e] = {s:v}


hq = []
NOW = gender[1]
VISIT = [False] * (N+1)
for next in graph[1]:
    if gender[next] != NOW:
        heapq.heappush(hq, [graph[1][next], 1, next])
VISIT[1] = True

ret = 0

while hq:
    v, s, e = heapq.heappop(hq)
    if VISIT[e]:
        continue
    VISIT[e] = True
    NOW = gender[e]
    ret += v

    for next in graph[e]:
        if not VISIT[next] and NOW != gender[next]:
            heapq.heappush(hq, [graph[e][next], e, next])

for i in range(1, N+1):
    if not VISIT[i]:
        ret = -1
        break
print(ret)