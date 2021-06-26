import sys
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = dict()

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    if A in graph:
        if B not in graph[A]:
            graph[A].append(B)
    else:
        graph[A] = [B]

def dijkstra(graph, start):
    distances =[float('inf')] * (N+1)

    distances[start] = 0

    for node in graph[start]:
        distances[node] = 1

    q = []

    for i in range(1, len(distances)):
        heapq.heappush(q, [distances[i], i])

    while q:
        node = heapq.heappop(q)[1]
        if node in graph:
            # 노드를 방문하지 않았으면
            for neighbor in graph[node]:
                if distances[neighbor] > distances[node] + 1:
                    distances[neighbor] = distances[node] + 1
                    heapq.heappush(q, [distances[neighbor], neighbor])
                    # 수정했으면 다시  최소 값을 넣어줘야지 어떻게 생각해보면 당연한거야??

    return distances

distances = dijkstra(graph, X)

n = -1
for i in range(len(distances)):
    if distances[i] == K:
        print(i)
        n += 1

if n == -1:
    print(n)
