# # 키 순서
# # 자신의 키가 정확히 몇번째인지 알 수 있는 사람이 모두 몇명인지 계산
import sys
input = sys.stdin.readline

INF = 987654321

N, M = map(int, input().split())
dp = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    dp[a][b] = 1

for k in range(1, N+1): # k를 거쳐서 간다.
    for s in range(1, N+1):
        for e in range(1, N+1):
            if dp[s][k] + dp[k][e] < dp[s][e]:
                dp[s][e] = dp[s][k] + dp[k][e]

cnt = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] != INF:
            cnt[i] += 1
            cnt[j] += 1
print(cnt.count(N-1))
