import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().rstrip().split())
INF = 987654321

graph = {}
for _ in range(E):
    s, e, d = map(int, input().rstrip().split())
    s -= 1
    e -= 1
    if s in graph:
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], d)
        else:
            graph[s][e] = d
    else:
        graph[s] = {e:d}
    if e in graph:
        if s in graph[e]:
            graph[e][s] = min(graph[e][s], d)
        else:
            graph[e][s] = d
    else:
        graph[e] = {s:d}

v1, v2 = map(int, input().rstrip().split())

v1 -= 1
v2 -= 1
# 0번 정점에서 N-1번 정점으로 이동할 건데, 반드시 v1, v2를 지
# 0에서 N-1로 도착할 수 없을 때에는 -1 출력
# 최단 경로의 길이를 출력
def dijkstra(s, e):
    hq = [[0, s]]
    dist = [INF] * N
    dist[s] = 0
    if s in graph:
        while hq:
            nowdist, node = heapq.heappop(hq)

            if dist[node] < nowdist: #기존 거리보다  더 길면 확인 X
                continue

            for next, nextdist in graph[node].items():
                if dist[next] > nowdist + nextdist:
                    dist[next] = nowdist + nextdist
                    heapq.heappush(hq, [dist[next], next])

    return dist[e]

path1 = dijkstra(0, v1) + dijkstra(v1, v2) + dijkstra(v2, N-1)
path2 = dijkstra(0, v2) + dijkstra(v2, v1) + dijkstra(v1, N-1)
ans = min(path1, path2)

print(-1 if ans >= INF else ans)