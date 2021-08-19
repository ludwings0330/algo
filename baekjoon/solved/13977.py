# title ; 이항계수와 쿼리
# tag ; 페르마 소정리 a^p = a (mod p)
import sys
input = lambda: sys.stdin.readline().rstrip()

M = int(input())
factorial = [1]
MOD = 10**9+7

for i in range(1, 4000001):
    factorial.append((factorial[i-1] * i) % MOD)

def pow(a, p):
    if p == 0:
        return 1

    if p % 2 == 1:
        return (a * pow(a, p-1)) % MOD
    else:
        r = pow(a, p//2)
        return (r*r) % MOD

while M:
    M-= 1
    N, K = map(int, input().split())
    a = factorial[N]
    b = ( factorial[K] * factorial[N-K] ) % MOD
    c = pow(b, MOD - 2)
    ans = (a * c) % MOD
    print(ans)