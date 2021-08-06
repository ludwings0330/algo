import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {}
INF = 987654321

for _ in range(m):
    s, e, v = map(int, input().split())
    s -= 1
    e -= 1
    if s in graph:
        if e in graph[s]:
            graph[s][e] = min( graph[s][e], v)
        else:
            graph[s][e] = v
    else:
        graph[s] = {e:v}

f, t = map(int, input().split())
f -= 1
t -= 1

def dijstra(s, e):
    hq = []
    dist = [INF] * n
    dist[s] = 0
    heapq.heappush(hq, [dist[s], [s]])
    ret = [[s] for i in range(n)]
    while hq:
        nowdist, now = heapq.heappop(hq)

        if nowdist > dist[now[-1]]:
            continue
        if now[-1] in graph:
            for next, nextdist in graph[now[-1]].items():
                if dist[next] > nextdist + nowdist:
                    # 바로 가는거보다 돌아서 가는게 더 빠르다.
                    ret[next] = ret[now[-1]] + [next]
                    dist[next] = nextdist + nowdist
                    heapq.heappush(hq, [dist[next], now + [next]])

    return [dist[e], len(ret[e]), ret[e]]
ans = dijstra(f, t)
print(ans[0])
print(ans[1])
print(*(1+ans[2][i] for i in range(len(ans[2]))))
