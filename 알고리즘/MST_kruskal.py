# 고속 도로를 건설하는 최소 비용
# 모든 도시를 잇는 고속도로를 건설하는 최소 비용
import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
T = int(input())

def find(x):
    if x == parent[x]:
        return x

    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: # 이미 같은 집합이라면?
        return False

    if rank[x] > rank[y]:
        rank[x] += rank[y] # 더 큰곳에 붙는다.
        parent[y] = x # y가 x에 붙었다.
    else:
        rank[y] += rank[x]
        parent[x] = y

    return True


for testCase in range(1, T+1):
    print("#%d" %testCase, end = ' ')

    N = int(input()) # N 도시의 수
    M = int(input()) # M 도로 후보의 수

    graph = {}

    for i in range(M):
        s, e, v = map(int, input().split())
        if s in graph:
            if e in graph[s]:
                graph[s][e] = min(graph[s][e], v)
            else:
                graph[s][e] = v
        else:
            graph[s] = {e:v}

        if e in graph:
            if s in graph[e]:
                graph[e][s] = min(v, graph[e][s])
            else:
                graph[e][s] = v
        else:
            graph[e] = {s:v}

    # -> 모든 도시를 잇도록 -> 최소 스패닝 트리

    hq = []
    for s in graph:
        for e in graph[s]:
            heapq.heappush(hq, [graph[s][e], s, e])

    parent = [i for i in range(N+1)]
    rank = [1 for i in range(N+1)]

    # 가장 작은 간선을 뽑고 두개 연결시도
    # 연결 시도 했을때 루프가 생기면 무시,
    # 루프가 생기지 않으면 계속
    ret = 0

    # 🌸 Kruskal 핵심
    while hq:
        c, s, e = heapq.heappop(hq)

        if not union(s, e):
            continue
        else:
            ret += c

    print(ret)