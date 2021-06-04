import sys
input = sys.stdin.readline
dp = [0]*(1500002)
N = int(input())
T = [0]
P = [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i+T[i] <= N+1:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(max(dp[N], dp[N+1]))