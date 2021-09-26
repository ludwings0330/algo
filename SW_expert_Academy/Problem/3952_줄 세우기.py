import heapq
from collections import deque
TC = int(input())

# 위상정렬 알고리즘
def TS():
    dq = deque()
    visit = [False] * (N+1)

    for i in range(1, N+1):
        if degree[i] == 0:
            dq.append(i)
            visit[i] = True

    while dq:
        current = dq.popleft()
        print(current, end=' ')

        if current in graph:
            for next in graph[current]:
                if not visit[next]:
                    degree[next] -= 1
                    if degree[next] == 0:
                        dq.append(next)
                        visit[next] = True


for testCase in range(1, TC+1):
    N, M = map(int, input().split())

    graph = {}
    degree = [0] * (N+1)

    for i in range(M):
        s, e= map(int, input().split())
        if s in graph:
            graph[s][e] = 1
        else:
            graph[s] = {e:1}
        degree[e] += 1

    print("#%d" %(testCase), end=' ')
    TS()
    print()
