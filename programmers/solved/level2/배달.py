from collections import defaultdict
import heapq

# 한 정점으로부터 나머지 정점으로의 모든 최소 거리 -> 다익스트라 알고리즘
def dijkstra(N, graph, start):
    INF = 10**9
    dists = [INF] * (N + 1)
    hq = [[0, start]]
    dists[start] = 0

    if start in graph:
        while hq:
            current_dist, current_node = heapq.heappop(hq)

            if dists[current_node] < current_dist: # 확인할 필요도 없음
                continue

            for next, next_dist in graph[current_node].items():
                if dists[next] > current_dist + next_dist: # 다음으로 바로 가는거보다 현재 들렸다가 다음으로 갈때가더 가까우면
                    dists[next] = current_dist + next_dist
                    heapq.heappush(hq, [dists[next], next])

    return dists

def solution(N, road, K):
    graph = defaultdict(dict)

    for s, e, d in road:
        if e in graph[s]:
            d = min(d, graph[s][e])

        graph[s][e] = graph[e][s] = d

    dist = dijkstra(N, graph, 1)

    return len([d for d in dist if d <= K])

# 1번 마을에서 출발 N 개의 마을중에서 K 시간 이하로 배달이 가능한 마을의 수


N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

print(solution(N, road, K))
