# 최소 스패닝 트리
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
graph = {}
visit = [False]*(V+1)

for _ in range(E):
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

answer = 0

def prims(i):
    hq = []
    ret = 0
    for next in graph[i]:
        e = next
        v = graph[i][next]
        heapq.heappush(hq, [v, i, e])
    visit[i] = True

    while hq:
        v, s, e = heapq.heappop(hq)

        if visit[e]:
            continue

        #print(e)
        visit[e] = True
        ret += v
        if e in graph:
            for next in graph[e]:
                if not visit[next]:
                    v = graph[e][next]
                    heapq.heappush(hq, [v, e, next])
    print(ret)
prims(1)