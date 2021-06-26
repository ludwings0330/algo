# 줄 세우기
# N 명학생 줄세우기, 두학생의 키 비교 모든 학생들을 비교한것도 아님
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edge = [0] * (N+1)

ans = []
graph = {}
for _ in range(M):
    A, B = map(int, input().split())
    edge[B] += 1
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]
    # A < B 라는 뜻.
    # 이거그냥 위상 정렬 이네
dq = deque()
for i in range(1, N+1):
    if edge[i] == 0:
        dq.append(i)
while dq:
    node = dq.popleft()
    ans.append(node)

    if node in graph:
        for next in graph[node]:
            edge[next] -= 1
            if edge[next] == 0:
                dq.append(next)
print(*ans)