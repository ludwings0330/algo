import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
edge = [0] * (N + 1)
graph = {}
buildtime = [0] * (N + 1)
dp = [0] * (N+1)
for i in range(1, N+1):
    line = list(map(int,input().split()))
    time = line[0]
    K = line[1]

    if i == 1:
        buildtime[i] = time
        continue

    buildtime[i] = time

    for j in range(K):
        s, e = line[j+2], i
        # line[j] -> 선행 작업, i -> 후행 작업
        edge[e] += 1
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]

dq = deque()

for i in range(1, N+1):
    if edge[i] == 0:
        dq.append(i)
        dp[i] = buildtime[i]

while dq:
    node = dq.popleft()
    if node in graph:
        for next in graph[node]:
            edge[next] -= 1
            dp[next] = max(dp[next], dp[node] + buildtime[next])
            if edge[next] == 0:
                dq.append(next)

print(max(dp))
