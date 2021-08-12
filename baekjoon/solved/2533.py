# Title ; 사회망 서비스(SNS)
# Tag ; 트리

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
N = int(input())
# 2 <= N <= 1,000,000
dp = [[0, 0] for _ in range(N+1)]
# 나 빼고 모든 친구들이 얼리 아답터면 새로운 아이디어를 받아들인다.
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

vis = [False] *(N+1)
def recursiveSolve(node):
    vis[node] = True
    dp[node][0] = 1 # idx 0 은 얼리어답터
    for next in graph[node]:
        if not vis[next]: # 아직 next를 방문하지 않았을 때
            recursiveSolve(next)
            # 맨 아래부터 채워지기 때문에, bottom-up 시작
            # 내가 얼리어답터면 내 다음애들은 얼리어답터 거나, 얼리어답터가 아니다.
            dp[node][0] += min(dp[next][0], dp[next][1])

            # 내가 얼리어답터가 아니라면 내 다음애들은 얼리어답터
            dp[node][1] += dp[next][0]

recursiveSolve(1)
print(min(dp[1][0], dp[1][1]))

