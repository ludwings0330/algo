import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dictA = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        dictA[sum(A[i:j+1])] += 1

ans = 0
for i in range(m):
    for j in range(i, m):
        ans += dictA[T-sum(B[i:j+1])]
print(ans)
