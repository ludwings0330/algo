# Title ; 팰린드롬 분할
# Tag ; 다이나믹 프로그래밍

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(987654321)
input_str = list(input())

N = len(input_str)
dp = [[False]*(N) for _ in range(N)]
ans = [-1] * 2501
for i in range(N):
    dp[i][i] = True
    if 0 > i-1:
        continue
    if input_str[i-1] == input_str[i]:
        dp[i][i-1] = True
        dp[i-1][i] = True

for i in range(2, N):
    for j in range(N-i):
        if input_str[j] == input_str[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True
            dp[j+i][j] = True

ans[0] = 0
ans[1] = 1
for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[j-1][i-1]:
            if ans[i] == -1 or ans[i] > ans[j-1] + 1:
                ans[i] = ans[j - 1] + 1
print(ans[N])