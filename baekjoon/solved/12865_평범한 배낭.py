import sys
input = sys.stdin.readline

(N, K) = map(int, input().rstrip().split())
We = []
Va = []
dp = [0]*(K+1)
MAX = 0

for i in range(N):
    w, v = map(int, input().rstrip().split())
    We.append(w)
    Va.append(v)

for n in range(N):
    for w in range(K, -1, -1):
        if 0 <= w-We[n]:
            dp[w] = max(dp[w], dp[w-We[n]] + Va[n])

print(max(dp))

