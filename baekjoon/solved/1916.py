import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = dict()

for _ in range(M):
    s, e, v = map(int, input().split())
    if s in graph:
        if e in graph[s]:
            v = min(graph[s][e], v)
        graph[s][e] = v
    else:
        graph[s] = {e:v}

S, E = map(int, input().split())

def dijikstra(S, E):
    dp = [INF]*(N+1)

    dp[S] = 0
    hq = []
    heapq.heappush(hq, [dp[S], S])

    while hq:
        nowVal, now = heapq.heappop(hq)
        if now in graph:
            for next, distance in graph[now].items():
                if dp[next] > dp[now] + distance:
                    dp[next] = dp[now] + distance
                    heapq.heappush(hq, [dp[next], next])
    print(dp[E])
dijikstra(S, E)