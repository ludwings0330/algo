n = int(input())
wines = [0]*3
for _ in range(n):
    wines.append(int(input()))
dp = [0]*(n+3)

for i in range(3, n+3):
    dp[i] = wines[i] + max(dp[i-2], dp[i-3] + wines[i-1])
    dp[i] = max(dp[i], dp[i-1])
print(max(dp))
