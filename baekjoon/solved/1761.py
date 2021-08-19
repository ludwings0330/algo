# title : 정점들의 거리
# Tag : LCA 최소 공통 조상

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

def init():
    dfs_init(1, 0, 1)

    for i in range(1, LOG):
        for j in range(1, N+1):
            parents[j][i] = parents[parents[j][i-1]][i-1]

def dfs_init(current, parent, depth):
    parents[current][0] = parent
    depths[current] = depth
    if parent != 0:
        dists[current] = dists[parent] + graph[current][parent]
    if current in graph:
        for next in graph[current]:
            if depths[next] == 0: # 아직 방문하지 않았다면
                dfs_init(next, current, depth + 1)
def LCA(node_a, node_b):
    # node_b의 깊이가 더 깊도록
    if depths[node_a] > depths[node_b]:
        node_a, node_b = node_b, node_a

    ret = 0
    # 깊이가 같도록 만든다
    for i in range(LOG-1, -1, -1):
        if depths[node_b] - depths[node_a] >= (1 << i):
            node_b = parents[node_b][i]


    # 조상을 찾아서 올라간다
    if node_a == node_b:
        return node_a

    for i in range(LOG - 1, -1, -1):
        if parents[node_a][i] != parents[node_b][i]:
            node_a = parents[node_a][i]
            node_b = parents[node_b][i]

    return parents[node_a][0]

N = int(input())
graph = {}
LOG = 17
parents = [[0] * LOG for _ in range(N+1)]
depths = [0 for _ in range(N+1)]
dists = [0] * (N + 1)
for _ in range(N - 1):
    s, e, d = map(int, input().split())

    if s in graph:
        graph[s][e] = d
    else:
        graph[s] = {e:d}
    if e in graph:
        graph[e][s] = d
    else:
        graph[e] = {s:d}

init()

M = int(input())
for _ in range(M):
    node_a, node_b = map(int, input().split())
    parent = LCA(node_a, node_b)
    print(dists[node_a] + dists[node_b] - (2 * dists[parent]))