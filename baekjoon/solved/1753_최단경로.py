import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().rstrip().split())
K = int(input())
trunk = [[] for _ in range(V+1)]
d = [INF]*(V+1)
heap = []

for i in range(E):
    u, v, w = map(int, input().rstrip().split())
    trunk[u].append([v, w])

def dijkstra(node):
    d[node] = 0
    heapq.heappush(heap, [0, node])

    while heap:
        w, n = heapq.heappop(heap)
        for nn, ww in trunk[n]:
            nw = ww + w
            if nw < d[nn]:
                d[nn] = nw
                heapq.heappush(heap, [nw, nn])
    pass
dijkstra(K)

for i in d[1:]:
    print(i if i != INF else 'INF')