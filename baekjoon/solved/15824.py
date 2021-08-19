# title ; 너 봄에는 캡사이신이 맛있단다
# tag ; 정렬
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

K = n - 1
ans = 0
DIV = 10**9+7
def pow(a, k):
    if k == 0:
        S[0] = 1
        return 1
    if S[k] != -1:
        return S[k]
    if k%2 == 1:
        S[k] = (a*pow(a, k-1))%DIV
        return S[k]
    else:
        r = pow(a, k//2)
        S[k] = (r*r)%DIV
        return S[k]
S = [-1] * (n+1)
for i in range(n+1):
    pow(2, i)
for i in range(len(S)):
    S[i] -= 1
for i, num in enumerate(arr):
    ans += (num*(S[K] - S[n-K-1]))%DIV
    ans %= DIV
    K -= 1
print(ans)