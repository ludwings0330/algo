# title ; N 포커
# tag ; 포함 배제의 원리
import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 10**4+7
nCk = [[1] * 53 for _ in range(53)]
for n in range(53):
    for k in range(1, n):
        nCk[n][k] = nCk[n-1][k-1] + nCk[n-1][k]
        nCk[n][k] %= MOD
        nCk[n][n-k] = nCk[n][k]

ans = 0
N = int(input())
for i in range(1, N//4+1):
    if i % 2 == 1:
        ans += nCk[13][i] * nCk[52-i*4][N - i*4]
    else:
        ans -= nCk[13][i] * nCk[52-i*4][N - i*4]
ans %= MOD
print(ans)