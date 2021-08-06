# Title : 사회망 서비스(SNS)
# Tag : 트리를 활용한 dp
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
graph = {}
for _ in range(N-1):
    s, e = map(int, input().split())
    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e : 1}

depth = [0] * (N+1)
depth[1] = 1
dq = deque()
vis = set()
dq.append([1, 1])
vis.add(1)

while dq:
    node, d = dq.popleft()
    depth[d] += 1

    if node in graph:
        for next in graph[node]:
            if next not in vis:
                dq.append([next, d+1])
                vis.add(next)

print(depth)