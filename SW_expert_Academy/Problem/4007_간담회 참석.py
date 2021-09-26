import heapq

T = int(input())

INF = float('inf')

def dijkstra(s, e):
    dists = [INF] * (N+1)
    dists[s] = 0

    hq = [[0, s]]

    if s in graph:
        while hq:
            current_dist, current_node = heapq.heappop(hq)

            if dists[current_node] < current_dist:
                continue

            for next, next_dist in graph[current_node].items():
                if dists[next] > current_dist + next_dist:
                    dists[next] = current_dist + next_dist
                    heapq.heappush(hq, [dists[next], next])

    return dists


for testCase in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = {}

    for _ in range(M):
        s, e, t = map(int, input().split())

        if s in graph:
            if e in graph[s]:
                graph[s][e] = min(graph[s][e], t)
            else:
                graph[s][e] = t
        else:
            graph[s] = {e:t}

    ans = 0
    distsX = dijkstra(X, 1)

    for s in range(1, N+1):
        if s == X:
            continue

        dist = dijkstra(s, X)[X] + distsX[s]
        ans = max(ans, dist)

    print("#%d %d" %(testCase, ans))