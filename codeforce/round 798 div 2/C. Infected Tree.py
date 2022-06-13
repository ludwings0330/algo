import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict


def cut(root):
    pass


def count_child(root, visited):
    visited[root] = True
    flag = True
    for child in graph[root]:
        if not visited[child]:
            flag = False
            childs[root] += count_child(child,visited)

    return childs[root]



t = int(input())
while t:
    t -= 1
    n = int(input())

    graph = defaultdict(lambda: defaultdict(int))

    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1

    childs = [1] * (n+1)
    count_child(1, [False] * (n + 1))

