N = int(input())
# 1 <= N <= 100,000
DIV = 9901

dp = [[0, 0] for _ in range(N + 1)]

dp[1][1] = 2
dp[1][0] = 1

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][0]) % DIV
    dp[i][1] = (dp[i-1][1] + dp[i-1][0] * 2) % DIV

print(sum(dp[N]) % DIV)