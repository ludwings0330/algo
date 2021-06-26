import sys
import heapq

def dijkstra(graph, start):
    distances = [float('inf')] * (D+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        currentDistance, currentDestination = heapq.heappop(q)

        if distances[currentDestination] < currentDistance or not currentDestination < D:
            continue

        for newDestination, newDistance in graph[currentDestination].items():
            distance = currentDistance + newDistance
d
            if distance < distances[newDestination]:
                distances[newDestination] = distance
                heapq.heappush(q, [distance, newDestination])

    return distances

input = sys.stdin.readline

N, D = map(int, input().split())
graph = dict()

for i in range(D):
    S, E, T = i, i+1, 1
    graph[S] = {E:T}

for i in range(N):
    S, E, T = map(int, input().split())
    if E > D:
        continue
    if S in graph:
        if E in graph[S]:
            if T < graph[S][E] :
                graph[S][E] = T
        else:
            graph[S][E] = T
    else:
        graph[S] = {E:T}

answer = dijkstra(graph, 0)
print(answer[-1])
