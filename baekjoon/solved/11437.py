# Title : LCA
# Tag : LCA (최소 공통 조상)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

def LCA(node_a, node_b):
    while depths[node_a] != depths[node_b]:
        if depths[node_a] > depths[node_b]:
            node_a = parents[node_a]
        else:
            node_b = parents[node_b]

    while node_a != node_b:
        node_a = parents[node_a]
        node_b = parents[node_b]

    return node_a

def dfs(current, parent, depth):
    depths[current] = depth
    parents[current] = parent

    if current in graph:
        for next in graph[current]:
            if parents[next] == -1: # 아직 방문하지 않았으면 수행한다
                dfs(next, current, depth + 1)


N = int(input())
graph = {}
depths = [-1] * (N+1)
parents = [-1] * (N+1)
for _ in range(N-1):
    s, e = map(int, input().split())

    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e:1}

    if e in graph:
        graph[e][s] = 1
    else:
        graph[e] = {s:1}

dfs(1, 1, 1) # init values

M = int(input())
for _ in range(M):
    node_a, node_b = map(int, input().split())
    print(LCA(node_a, node_b))
