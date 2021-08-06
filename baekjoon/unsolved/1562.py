N = int(input())


# 1 <= N < 100
dp = [[[0] * ((1<<10)) for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp[1][i][1<<i] = 1 # 맨 끝자리가 0 일때,
dp[1][0][1] = 0


for i in range(2, N+1): # 자리수가 2~N 인 놈까지 할거야
    for j in range(10): # 마지막 자리에 j를 붙여줄거야
        n = 1<<j
        for k in range(1, 1024):
            if j == 0: # 0을 붙이려면 맨 뒤가 1 만 존재
                dp[i][j][k|n] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][k|n] += dp[i-1][j-1][k]
            else:
                dp[i][j][k|n] += dp[i-1][j-1][k] + dp[i-1][j+1][k]

            dp[i][j][k|n] %= 1000000000

ans = 0
for i in range(10):
    ans += (dp[N][i][(1<<10)-1]) # 전체중에 비트가 모두 켜져 있는 놈들을 모두 더해본다링
    ans %= 1000000000
print(ans)