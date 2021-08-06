import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(m):
    s, e, v = map(int, input().split())
    if dp[s][e] > v:
        dp[s][e] = v

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if i!=j:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in dp[1:]:
    for j in i[1:]:
        if j == float('inf'):
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()