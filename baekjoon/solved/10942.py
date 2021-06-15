import sys
input = sys.stdin.readline

N = int(input())
line = [0]+list(map(int, input().split()))
dp = [[False]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][i] = True
    if line[i-1] == line[i]:
        dp[i][i-1] = True
        dp[i-1][i] = True

for i in range(2, N):
    for j in range(1, N+1-i):
        if line[j] == line[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True
            dp[j+i][j] = True

T = int(input())

while T:
    T -= 1
    s, e = map(int, input().split())
    if dp[s][e]:
        print(1)
    else:
        print(0)
