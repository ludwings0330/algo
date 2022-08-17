import sys
sys.setrecursionlimit(10**5+1)
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [-1] * (N+1)
cut = 0

def dfs(current):
    for next in graph[current]:
        if visited[next] != -1:
            global cut
            cut += 1
            continue
        visited[next] = group
        dfs(next)


group = -1
for s in range(1, N+1):
    if visited[s] != -1:
        continue
    group += 1
    visited[s] = group
    dfs(s)

cut = max(0, M + group - (N-1))
print(group + cut)

