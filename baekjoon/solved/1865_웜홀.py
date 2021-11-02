import sys
input = sys.stdin.readline

TC = int(input())

def bellmanford():
    global isPossible

    for i in range(1, N+1):
        for j in range(1, N+1):
            for w, v in graph[j]:
                if distance[v] > w + distance[j]:
                    distance[v] = w + distance[j]
                    if i == N:
                        isPossible = False
    return True

while TC:
    TC -= 1
    N, M, W = map(int, input().split())
    INF = float('inf')
    distance = [INF for _ in range(N + 1)]
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((T, E))
        graph[E].append((T, S))

    for i in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((-T, E))

    isPossible = True
    bellmanford()

    print("NO" if isPossible else "YES")

