import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(lambda: defaultdict(int))
cnt = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    # number of connect line
    cnt[u] += 1
    graph[u][v] += 1
    # graph[v].append(u)
INF = 10 ** 6
cache = [INF] * (n+1)


def dijkstra(i):
    cache[i] = 0
    hq = [[0, i]]

    while hq:
        current_dist, current_node = heapq.heappop(hq)

        if current_dist > cache[current_node]:
            continue

        for nxt_node in graph[current_node]:
            nxt_dist = current_dist + cnt[current_node] - graph[current_node][nxt_node] + 1

            if nxt_dist < cache[nxt_node]:
                cache[nxt_node] = nxt_dist
                heapq.heappush(hq, [nxt_dist, nxt_node])


dijkstra(1)
print(cache[n])
