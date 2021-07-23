import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def tsp(dists):
    N = len(dists)
    VISIT_ALL = (1 << N) - 1
    dp = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited): # visited bit가 켜진 놈들을 방문하면서 last로 향한다
        if visited == VISIT_ALL:
            return dists[last][0] or INF

        if dp[last][visited] is not None:
            return dp[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0: # city를 방문하지 않았고 거리가 존재하면
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])

        dp[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)

print(tsp(graph))