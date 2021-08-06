import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp_forward = [0] * N
dp_backward = [0] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_forward[i] = max(dp_forward[i], dp_forward[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp_backward[i] = max(dp_backward[i], dp_backward[j]+1)

ans = max([x+y for x,y in zip(dp_forward, dp_backward)]) + 1
print(ans)