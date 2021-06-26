import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = []

for i in range(N):
    dp.append(1)
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))