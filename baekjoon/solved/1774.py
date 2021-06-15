# 우주신과의 교감
# 정신적인 통로의 길이의 합이 최소가 되도록.

import sys
import heapq
import math
input = sys.stdin.readline

N, M = map(int, input().split())
# N ? 우주신들의 갯수
# M ? 이미 연결된 통로
ufos = [[0, 0]]
con = []
graph = {}
for _ in range(N):
    x, y = map(int, input().split())
    ufos.append([x, y])

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a, b
    con.append([a, b]) # a하고 b는 연결 되어 있다.


for a in range(1, N+1):
    for b in range(a+1, N+1):
        x1, y1 = ufos[a]
        x2, y2 = ufos[b]
        l = math.sqrt(((x2-x1)**2 + (y2-y1)**2))
        if a in graph:
            graph[a][b] = l
        else:
            graph[a] = {b:l}
        if b in graph:
            graph[b][a] = l
        else:
            graph[b] = {a:l}

for a, b in con:
    graph[a][b] = graph[b][a] = 0
visit = [False]*(N+1)

def prim():
    hq = []
    if M == 0:
        a = 1
    else:
        a = con[0][0]
    for next in graph[a]: # a하고 b는 연결되어 있음.
        # a 와 b에 연결된 모든 노선들을 heapq에 넣어준다.
        heapq.heappush(hq, [graph[a][next], a, next])

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

    print(format(ret,'.2f'))
prim()