import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
sys.setrecursionlimit(10**5)
T = int(input())

def init(current, parent, depth):
    # 이미 초기화 되어있다면 그만 탐색
    if parents[current] != 0:
        return

    # current 의 부모와 깊이 설정
    parents[current] = parent
    depths[current] = depth

    for next in graph[current]:
        init(next, current, depth + 1)


def LCA(node_a, node_b):
    # node_b 의 깊이가 더 깊도록 설정
    if depths[node_a] > depths[node_b]:
        node_a, node_b = node_b, node_a

    while depths[node_b] > depths[node_a]:
        node_b = parents[node_b]

    while node_a != node_b:
        node_a = parents[node_a]
        node_b = parents[node_b]

    return node_a


while T:
    T -= 1
    N = int(input())
    parents = [0] * (N + 1)
    depths = [0] * (N + 1)
    graph = defaultdict(dict)
    childs = {}
    for _ in range(N-1):
        parent, child = map(int, input().split())
        graph[parent][child] = 1
        childs[child] = 1
    root = -1
    for i in range(1, N+1):
        if i not in childs:
            root = i
            break
    init(root, 0, 1)
    a, b = map(int, input().split())
    print(LCA(a, b))
