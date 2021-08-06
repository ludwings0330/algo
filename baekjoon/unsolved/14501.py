# 1 <= N <= 15
import sys
input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]

DP = [0]*(N+1)
# i 일이 마지막 상담일때 가치.

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

answer = 0
for i in range(1, N+1):
    if i + T[i] > N+1:
        continue
    DP[i] += P[i]
    answer = max(answer, DP[i])
    for j in range(i+T[i], N+1):
        DP[j] = max(DP[j], DP[i])
    # print(DP)
print(answer)