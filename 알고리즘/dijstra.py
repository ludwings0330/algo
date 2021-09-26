import sys
input = lambda:sys.stdin.readline().rstrip()
import heapq

INF = float('inf')
def dijkstra(start):
    dists = [INF] * N
    hq = [[0, start]]
    dists[start] = 0

    if start in graph:
        while hq:
            current_dist, current_node = heapq.heappop(hq)

            if dists[current_node] < current_dist: # 확인할 필요도 없음
                continue

            for next, next_dist in graph[current_node].items():
                if dists[next] > current_dist + next_dist: # 다음으로 바로 가는거보다 현재 들렸다가 다음으로 갈때가더 가까우면
                    dists[next] = current_dist + next_dist
                    heapq.heappush(hq, [dists[next], next])

    return dists

N, E = map(int, input().split())
graph = {}
for _ in range(E):
    a, b, c = map(int, input().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = {b:c}
    if b in graph:
        if a in graph[b]:
            graph[b][a] = min(graph[b][a], c)
        else:
            graph[b][a] = c
    else:
        graph[b] = {a:c}
