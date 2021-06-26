import sys

input = sys.stdin.readline

N = int(input())
INF = float('inf')
dp = [[INF] * N for _ in range(N)]
# graph = {}
# for i in range(N):
#     line = list(map(int, input().split()))
#
#     for j in range(len(line)):
#         if line[j] == 1:
#             if i in graph:
#                 graph[i][j] = 1
#             else:
#                 graph[i] = {j:1}
for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):
        if line[j] == 1:
            dp[i][j] = line[j]


def floydwarshall():
    for k in range(N):
        for s in range(N):
            for e in range(N):
                dp[s][e] = min(dp[s][e], dp[s][k] + dp[k][e])

floydwarshall(0)

for i in range(N):
    for j in range(N):
        if dp[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()