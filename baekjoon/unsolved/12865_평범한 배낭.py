import sys
input = sys.stdin.readline

v = [0]
w = [0]
N, K = map(int, input().split())
# N : 물건 개수,  K : 최대 무게

for i in range(N):
    W, V = map(int, input().split())
    # W : 무게 , V : 가치
    w.append(W)
    v.append(V)

dp = [[0]*(K+1) for _ in range(N+1)]
MAX = 0
for i in range(1, N+1):
    for j in range(0, K+1):
        if w[i-1] <= j:
            dp[i][j] = max(v[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j]
        MAX = max(dp[i][j], MAX)

print(MAX)