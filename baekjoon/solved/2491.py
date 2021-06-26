N = int(input())
numList = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]


MAX = 1

for i in range(1, N):
    if numList[i] > numList[i-1]:
        dp[i][0] = dp[i-1][0] + 1
        MAX = max(MAX, dp[i][0])
    elif numList[i] < numList[i-1]:
        dp[i][1] = dp[i-1][1] + 1
        MAX = max(MAX, dp[i][1])
    else:
        dp[i][1] = dp[i - 1][1] + 1
        dp[i][0] = dp[i - 1][0] + 1
        MAX = max(MAX, dp[i][1])
        MAX = max(MAX, dp[i][0])
print(MAX)