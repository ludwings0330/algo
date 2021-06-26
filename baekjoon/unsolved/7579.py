#앱
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 실행중인 앱 N 개, M 바이트 추가 필요.
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
lenC = sum(c)
# 1 <= N <= 100
dp = [[0] * (lenC+1) for _ in range(N+1)]
MIN = sys.maxsize
for i in range(N+1):
    for C in range(lenC+1):
        if i == 0 or C == 0:
            # dp[i][C] = 0
            continue
        if C < c[i]:
            dp[i][C] = dp[i-1][C]
        else:
            dp[i][C] = max(dp[i-1][C-c[i]] + m[i], dp[i-1][C])
            if dp[i][C] >= M:
                MIN = min(MIN, C)
print(MIN)


