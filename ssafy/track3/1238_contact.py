from collections import defaultdict
from collections import deque


def dijkstra(start):
    dists = [float('inf')] * 101
    dists[start] = 0
    dq = deque()
    dq.append([start, 0])
    MAX = 0
    while dq:
        current, current_dist = dq.popleft()

        for next in store[current]:
            next_dist = current_dist + 1

            if dists[next] > next_dist:
                dists[next] = next_dist
                dq.append([next, dists[next]])
                MAX = max(MAX, next_dist)

    for i in range(100, 0, -1):
        if dists[i] == MAX:
            return i
    return -1


for tc in range(1, 11):
    ans = 0

    N, start = map(int, input().split())
    store = defaultdict(list)
    graph = list(map(int, input().split()))

    for i in range(0, N, 2):
        store[graph[i]].append(graph[i+1])
    N //= 2

    print(f'#{tc} {dijkstra(start)}')
