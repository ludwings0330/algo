#문제집
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
edge = [0] * (N + 1)
graph = {}

for _ in range(M):
    A, B = map(int, input().split())
    # A -> B
    edge[B] += 1
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]

hq = []
for i in range(1, N+1):
    if edge[i] == 0:
        heapq.heappush(hq, i)
ret = []
while hq:
    node = heapq.heappop(hq)
    ret.append(node)
    if node in graph:
        for next in graph[node]:
            edge[next] -= 1
            if edge[next] == 0:
                heapq.heappush(hq, next)

print(*ret)