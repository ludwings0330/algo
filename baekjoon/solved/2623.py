import sys
from collections import deque
# 위상정렬의 기본

input = sys.stdin.readline
N, M = map(int, input().split())
singer = [0] * (N+1)
graph = {}
for _ in range(M):
    l = list(map(int, input().split()))
    for i in range(1, l[0]):
        a = l[i]
        b = l[i+1]
        singer[b] += 1
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
dq = deque()
answer = []

for i in range(1,N+1):
    if singer[i] == 0:
        dq.append(i)

while dq:
    node = dq.popleft()
    answer.append(node)
    if node in graph:
        for next in graph[node]:
            singer[next] -= 1
            if singer[next] == 0:
                dq.append(next)
if len(answer) == N:
    for s in answer:
        print(s)
else:
    print(0)