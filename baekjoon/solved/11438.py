# Title : LCA2
# Tag : LCA

import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)
def init():
    init_dfs(1, 0, 1)

    for i in range(1, LOG):
        for j in range(1, N+1):
            parents[j][i] = parents[parents[j][i-1]][i-1]

def init_dfs(current, parent, depth):
    parents[current][0] = parent
    depths[current] = depth

    for next in graph[current]:
        if depths[next] == 0: # 아직 깊이가 결정되지 않았다면
            init_dfs(next, current, depth + 1)

def LCA(node_a, node_b):
    if depths[node_a] > depths[node_b]:
        node_a, node_b = node_b, node_a

    # 깊이를 맞춰 준다.
    for i in range(LOG-1, -1, -1):
        if depths[node_b] - depths[node_a] >= (1<<i):
            node_b = parents[node_b][i]

    if node_a == node_b:
        return node_a
    # 아래서부터 올라오면서 조상을 찾는다.
    for i in range(LOG-1, -1, -1):
        if parents[node_a][i] != parents[node_b][i]:
            node_a = parents[node_a][i]
            node_b = parents[node_b][i]

    return parents[node_a][0]

N = int(input())
graph = [[] for _ in range(N+1)]
LOG = 18
depths = [0] * (N + 1)
parents = [[0] * LOG for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

init()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))