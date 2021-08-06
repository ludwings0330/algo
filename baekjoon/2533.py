# Title ; 사회망 서비스(SNS)
# Tag ; 트리

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
# 2 <= N <= 1,000,000

# 나 빼고 모든 친구들이 얼리 아답터면 새로운 아이디어를 받아들인다.
graph = {}
for _ in range(N):
    s, e = map(int, input().split())

    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e : 1}

    if e in graph:
        graph[e][s] = 1
    else:
        graph[e] = {s : 1}
