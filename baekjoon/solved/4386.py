#별자리 만들기
import sys
import heapq
import math

input = sys.stdin.readline

n = int(input())
visit = [False] * (n + 1)
POS = [(0, 0)]
graph = {}

for _ in range(n):
    x, y = map(float, input().split())

    POS.append((x, y))

for i in range(1, n + 1):
    for j in range(1, n+1):
        # i -> j
        l = math.sqrt((POS[i][0] - POS[j][0])**2 + (POS[i][1] - POS[j][1])**2)
        if i in graph:
            graph[i][j] = l
        else:
            graph[i] = {j:l}

hq = []
for next in graph[1]:
    heapq.heappush(hq, [graph[1][next], 1, next])

ret = 0

while hq:
    v, s, e = heapq.heappop(hq)
    if visit[e]:
        continue
    visit[e] = True
    ret += v
    for next in graph[e]:
        if not visit[next]:
            heapq.heappush(hq, [graph[e][next], e, next])

print("{:.2f}".format(ret))
