import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
graph = defaultdict(lambda: defaultdict(int))

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = max(graph[A][B] if graph[A][B] else C, C)
    graph[B][A] = max(graph[B][A] if graph[B][A] else C, C)

factory_a, factory_b = map(int, input().split())

dq = deque()
visit = [False] * (N+1)
for next in graph[factory_a]:
    dq.append([next, graph[factory_a][next]])

ans = 0
while dq:
    current, weight = dq.popleft()
    visit[current] = True

    if current == factory_b:
        ans = max(ans, weight)
        continue
    for next in graph[current]:
        if not visit[next]:
            dq.append([next, min(weight, graph[current][next])])

print(ans)
