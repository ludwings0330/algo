#행렬 곱셈 순서
# 어떤 순서로 곱해야 곱셈 연산 횟수가 최소가 될까?
# 입력으로 주어진 행렬의 순서를 바꾸면 안된다
import sys
input = sys.stdin.readline

N = int(input())
# 1 <= N <= 500
matrices = []
MIN = sys.maxsize

for _ in range(N):
    r, c = map(int, input().split())
    # 1 <= r,c <= 500
    matrices.append([r, c])

dp = [[0] * N for _ in range(N)]
for s in range(N-1):
    dp[s][s+1] = matrices[s][0] * matrices[s][1] * matrices[s+1][1]

for n in range(2, N):
    for r in range(N-n):
        dp[r][r+n] = sys.maxsize
        for k in range(r, r+n):
            dp[r][r+n] = min(dp[r][r+n], dp[r][k] + dp[k+1][r+n] + matrices[r][0] * matrices[k][1] * matrices[r+n][1])
print(dp[0][-1])