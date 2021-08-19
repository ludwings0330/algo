# Title : Strongly Connected Component (SCC)
# Tag : SCC

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
V, E = map(int, input().split())
# V : 정점의 개수
# E : 간선의 개수

graph = dict()
node_id = [0] * (V + 1)
ID = 1
finished = [False] * (V + 1)
visited = [False] * (V + 1)
SCC_list = []

for _ in range(E):
    s, e = map(int, input().split())
    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e:1}

stack = []
def SCC(idx):
    # DFS 를 이용한다.
    # finished, visited가 필요하다
    visited[idx] = True
    global ID
    node_id[idx] = ID
    ID += 1
    stack.append(idx)

    parent = node_id[idx]
    if idx in graph:
        for next in graph[idx]:
            if not visited[next]:
                parent = min(parent, SCC(next))
            elif not finished[next]:
                parent = min(parent, node_id[next])

    # 부모 노드가 자기 자신인 경우
    if parent == node_id[idx]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == idx:
                break
        SCC_list.append(sorted(scc))

    return parent


def solve():
    # 1. SCC 구하기
    for i in range(1, V+1):
        if not visited[i]:
            SCC(i)
    # 2. 각 SCC node 출력하기
    print(len(SCC_list))
    for scc in sorted(SCC_list):
        scc = scc + [-1]
        print(*scc)

solve()
