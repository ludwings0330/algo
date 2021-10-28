N = int(input())

dp = [0] * 81
dp[0] = dp[1] = 1
for i in range(2, 81):
    dp[i] = dp[i-1] + dp[i-2]

ans = 0
if N == 1:
    ans = 4
elif N == 2:
    ans = 6
else:
    ans = (dp[N-1] + dp[N-2] + dp[N-1])*2
print(ans)