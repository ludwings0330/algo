import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
INF = 1e9
distance = [INF] * (N + 1)
def bellmanford(graph, start):
    distance[start] = 0

    for i in range(1, N+1):
        for j in range(M):
            c = graph[j][0]
            n = graph[j][1]
            w = graph[j][2]
            if distance[c] != INF and distance[n] > distance[c] + w:
                distance[n] = distance[c] + w
                if i == N:
                    return False
    return True



for _ in range(M):
    S, E, V = map(int, input().split())
    graph.append((S, E, V))

isPossible = bellmanford(graph, 1)

if isPossible:
    for i in range(2, N+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)