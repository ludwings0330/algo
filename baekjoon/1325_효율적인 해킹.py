# 신뢰관계에 있으면 해킹 가능
# A가 B를 신뢰하는 경우에 B를 해킹하면 A도 해킹할 수 있다는 소리
# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 출력

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# N <= 10,000 M <= 100,000
graph = {}

for i in range(M):
    A, B = map(int, input().split())
    # A가 B를 신뢰한다.
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]

# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 오름차순으로 출력
# 너비 우선 탐색
answer = []
MAX = 0
for start in range(1, N+1):
    dq = deque()
    visit = [False] * (N+1)
    dq.append([start, 0])
    visit[start] = True
    count = 0
    while dq:
        current, count = dq.popleft()

        if current not in graph:
            continue

        for next in graph[current]:
            if not visit[next]:
                dq.append([next, count+1])
                visit[next] = True
    if MAX < count:
        answer = [start]
    elif MAX == count:
        answer.append(start)

answer.sort()
print(' '.join(map(str, answer)))